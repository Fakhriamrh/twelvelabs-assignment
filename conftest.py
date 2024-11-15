import pytest
from config import Config
import requests
from utils.api_client import ApiClient


@pytest.fixture(scope="session")
def api_client():
    
    return requests.Session()

@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown(api_client):
    cleanup_indexes(api_client)
    yield api_client
    cleanup_indexes(api_client)
    

def cleanup_indexes(api_client):
    response = ApiClient.list_indexes()
    
    if response.status_code != 200:
        print(f"Failed to list indexes: {response.text}")
        return  # Exit if the API request failed

    # Parse the response
    indexes = response.json()

    # If no indexes or empty response
    if not indexes:  # If the response is empty or None
        print("No indexes found to clean up.")
        return  # Exit the function as there is nothing to clean up

    if isinstance(indexes, dict) and "data" in indexes:
        data = indexes["data"]
        if not data:  # If no data under "data"
            print("No indexes found to clean up.")
            return  # Exit the function as there is nothing to clean up

        for index in data:
            if index.get("index_name", "").startswith("Test"):
                index_name = index["index_name"]
                index_id = index.get("_id")
                print(f"Cleaning up index: {index_name}")
                delete_response = ApiClient.delete_index(index_id)
                assert delete_response.status_code in (200, 204), (
                    f"Failed to delete index {index_name}: {delete_response.text}"
                )