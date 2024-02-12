
import requests
import logging

# from bot.config import BASE_API


def get_group_data():
    try:
        response = requests.get("http://127.0.0.1:8000/api/groups/")
        response.raise_for_status()
        data = response.json()

        groups = data.get("title")
        return groups
    except Exception as e:
        logging.error(f"Error fetching external data: {str(e)}")
        return None

