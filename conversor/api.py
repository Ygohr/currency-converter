import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://api.exchangerate.host/"
access_key = os.getenv("EXCHANGE_API_KEY")

def get_live_change_by_currency(currency: str) -> float:
    try:
        response = requests.api.get(f'{url}/live?access_key={access_key}&currencies={currency}')
        data = response.json()
        quotes = data["quotes"]

        response.close()

        return quotes[f'USD{currency}']
    except:
        print("An exception occurred")