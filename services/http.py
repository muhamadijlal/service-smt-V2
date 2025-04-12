import json
import requests

from config.logger import setup_logger

logger = setup_logger(__name__)

def http_post(url: str, data: dict):
    try:
        json_data = json.dumps(data, default=str)  # Pastikan datetime bisa di-serialize
        headers = {
            'Content-Type': 'application/json',
            'Content-Length': str(len(json_data))  # Panjang string JSON, bukan dict
        }

        response = requests.post(url, data=json_data, headers=headers)
        response.raise_for_status()

        return response.json()
    except requests.RequestException as e:
        logger.error(f"Request failed: {e}")
        return None
