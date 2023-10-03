
import requests
import logging

# from bot.config import BASE_API


def get_external_data():
    try:
        response = requests.get("http://127.0.0.1:8000/api")
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        logging.error(f"Error fetching external data: {str(e)}")
        return None

