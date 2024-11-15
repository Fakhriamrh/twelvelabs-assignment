import pytest
import allure
from utils.api_client import ApiClient
from tests_data.tests_data import CREATE_TO_GET

@allure.feature('Get Index by ID')
@allure.story('Retrieve an index by a valid ID')
@pytest.mark.parametrize("index_data", [CREATE_TO_GET])
def test_get_index_by_id(index_data):
    # First create the index
    create_response = ApiClient.create_index(index_data)
    index_id = create_response.json().get("_id")
    response = ApiClient.get_index_by_id(index_id)
    assert response.status_code == 200  # Expecting 200 for successful retrieval
    allure.attach(response.text, name="Get Index by ID Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('Get Index by ID')
@allure.story('Attempt to retrieve an index with an invalid ID, should return 400')
def test_get_index_by_invalid_id():
    invalid_id = "invalid-id"
    response = ApiClient.get_index_by_id(invalid_id)
    assert response.status_code == 400  # Expecting 400 for not found
    allure.attach(response.text, name="Get Index by Invalid ID Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('Get Index by ID')
@allure.story('Attempt to retrieve an index by ID with a non-existent ID, should return 400')
def test_get_index_by_non_existent_id():
    non_existent_id = "non-existent-id"
    response = ApiClient.get_index_by_id(non_existent_id)
    assert response.status_code == 400  # Expecting 400 for not found
    allure.attach(response.text, name="Get Index by Non-existent ID Response", attachment_type=allure.attachment_type.JSON)
