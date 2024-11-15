import requests
from config import Config

class ApiClient:
    @staticmethod
    def create_index(index_data):
        url = f"{Config.BASE_URL}indexes"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": Config.API_KEY
        }
        response = requests.post(url, json=index_data, headers=headers)
        return response

    @staticmethod
    def list_indexes(page=1, page_limit=10, sort_by="created_at", sort_option="desc"):
        url = f"{Config.BASE_URL}indexes?page={page}&page_limit={page_limit}&sort_by={sort_by}&sort_option={sort_option}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": Config.API_KEY
        }
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def get_index_by_id(index_id):
        url = f"{Config.BASE_URL}indexes/{index_id}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": Config.API_KEY
        }
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def delete_index(index_id):
        url = f"{Config.BASE_URL}indexes/{index_id}"
        headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "x-api-key": Config.API_KEY
        }
        response = requests.delete(url, headers=headers)
        return response
