import os
import requests
import urllib
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
API_KEY_THEYSAIDSO = os.getenv("API_KEY_THEYSAIDSO")

print("DELETEME '" + TELEGRAM_CHAT_ID + "'")

URL_QUOTE = "https://quotes.rest/qod"
HEADERS = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-TheySaidSo-Api-Secret': API_KEY_THEYSAIDSO
}

def getQuote():
  r = requests.get(url = URL_QUOTE, headers = HEADERS)
  data = r.json()
  message = ''
  if 'contents' in data:
    quote = data['contents']['quotes'][0]['quote']
    author = data['contents']['quotes'][0]['author']
    permalink = data['contents']['quotes'][0]['permalink']
    message = f"\"{quote}\"\n- {author}"
  elif 'error' in data:
    print("Error: " + data['error']['message'])
  elif 'message' in data:
    print("Error: " + data['message'])
  return message

def sendMessage(query):
    r = requests.get(url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={urllib.parse.quote(query)}", headers = HEADERS)

def main():
  quote = getQuote()
  if (quote != ''):
    sendMessage(quote)

if __name__ == "__main__":
  main()
