import pytest
import allure
from utils.api_client import ApiClient
from tests_data.tests_data import CREATE_FOR_DELETE

@allure.feature('Delete Index')
@allure.story('Delete an index successfully')
@pytest.mark.parametrize("index_data", [CREATE_FOR_DELETE])
def test_delete_index(index_data):
    # Create an index first
    create_response = ApiClient.create_index(index_data)
    index_id = create_response.json().get("_id")
    response = ApiClient.delete_index(index_id)
    assert response.status_code == 204  # Expecting 204 for successful deletion
    allure.attach(response.text, name="Delete Index Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('Delete Index')
@allure.story('Attempt to delete an index that does not exist, should return 400')
def test_delete_non_existing_index():
    response = ApiClient.delete_index("non-existing-id")
    assert response.status_code == 400  # Expecting 400 for not found
    allure.attach(response.text, name="Delete Non-existing Index Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('Delete Index')
@allure.story('Attempt to delete an index with an invalid ID format, should return 400')
def test_delete_index_invalid_id_format():
    invalid_id = "invalid-format-id"
    response = ApiClient.delete_index(invalid_id)
    assert response.status_code == 400  # Expecting 400 for bad request
    allure.attach(response.text, name="Delete Index Invalid ID Format Response", attachment_type=allure.attachment_type.JSON)
