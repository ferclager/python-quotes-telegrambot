
# Python Quotes Telegram Bot

This repository contains the code for building a Quote Telegram Bot using Python. The bot fetches quotes from the They Said So® API and sends them to a specified Telegram chat.

## Prerequisites

Before you begin, make sure you have the following:

* **Telegram Bot**: Create a Telegram bot by following the instructions [here](https://core.telegram.org/bots).

* **Telegram Chat ID**: Obtain the chat ID from your bot. Refer to [this guide](https://core.telegram.org/bots#3-how-do-i-create-a-bot) for more information.

* **Quotes API from They Said So®**: Sign up for the They Said So® API to get access to the quotes. You can make 10 free calls per hour. Visit [here](https://theysaidso.com/api/) to get your API key.

* **Dependencies**: Check the `requirements.txt` file for the required libraries: [requests](https://pypi.org/project/requests/), [urllib](https://pypi.org/project/urllib3/), and [python-dotenv](https://pypi.org/project/python-dotenv/). Install these libraries before running the code.

* **Configuration**: Configure your environment by creating a `.env` file and adding the following environment variables:
```.env
	API_KEY_THEYSAIDSO=YOUR_API_KEY_FROM_THEYSAIDSO
	TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN
	TELEGRAM_CHAT_ID=YOUR_CHAT_ID
```

## Usage
To use the Quote Telegram Bot, follow these steps:

* Clone the repository:

```bash
	git clone https://github.com/your-username/python-quotes-telegrambot.git
```

* Navigate to the project directory:
```bash
	cd python-quotes-telegrambot 
```

* Run the quotes.py script 
``` bash
	python3 quotes.py
```

That's it! The bot will fetch quotes from the They Said So® API and send them to the specified Telegram chat.

Feel free to modify the code according to your requirements and enhance the functionality of the bot.

## License

This project is licensed under the MIT License.
