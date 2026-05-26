import pytest
from unittest.mock import patch, MagicMock
import quotes


class TestGetQuote:
    """Tests for the getQuote function."""

    @patch('quotes.requests.get')
    def test_get_quote_success(self, mock_get):
        """Test successful quote retrieval."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'contents': {
                'quotes': [{
                    'quote': 'Test quote',
                    'author': 'Test Author',
                    'permalink': 'https://example.com/quote'
                }]
            }
        }
        mock_get.return_value = mock_response

        result = quotes.getQuote()

        assert result == '"Test quote"\n- Test Author'
        mock_get.assert_called_once()

    @patch('quotes.requests.get')
    def test_get_quote_api_error(self, mock_get):
        """Test handling of API error response."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'error': {
                'message': 'Rate limit exceeded'
            }
        }
        mock_get.return_value = mock_response

        result = quotes.getQuote()

        assert result == ''

    @patch('quotes.requests.get')
    def test_get_quote_message_error(self, mock_get):
        """Test handling of message error response."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'message': 'Unauthorized'
        }
        mock_get.return_value = mock_response

        result = quotes.getQuote()

        assert result == ''


class TestSendMessage:
    """Tests for the sendMessage function."""

    @patch('quotes.requests.get')
    def test_send_message_called(self, mock_get):
        """Test that send_message makes a request to Telegram API."""
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        quotes.sendMessage("Hello World")

        mock_get.assert_called_once()
        call_url = mock_get.call_args[1]['url']
        assert 'api.telegram.org' in call_url
        assert 'sendMessage' in call_url

    @patch('quotes.requests.get')
    def test_send_message_encodes_special_chars(self, mock_get):
        """Test that special characters are URL encoded."""
        mock_response = MagicMock()
        mock_get.return_value = mock_response

        quotes.sendMessage("Hello & World")

        call_url = mock_get.call_args[1]['url']
        assert 'Hello%20%26%20World' in call_url or 'Hello+%26+World' in call_url


class TestMain:
    """Tests for the main function."""

    @patch('quotes.sendMessage')
    @patch('quotes.getQuote')
    def test_main_sends_quote_when_available(self, mock_get_quote, mock_send):
        """Test that main sends a message when quote is available."""
        mock_get_quote.return_value = '"Test quote"\n- Author'

        quotes.main()

        mock_send.assert_called_once_with('"Test quote"\n- Author')

    @patch('quotes.sendMessage')
    @patch('quotes.getQuote')
    def test_main_does_not_send_empty_quote(self, mock_get_quote, mock_send):
        """Test that main does not send a message when quote is empty."""
        mock_get_quote.return_value = ''

        quotes.main()

        mock_send.assert_not_called()
