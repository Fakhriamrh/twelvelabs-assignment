import pytest
import allure
from utils.api_client import ApiClient
from tests_data.tests_data import INDEX_DATA, INVALID_INDEX_DATA, MINIMAL_INDEX_DATA, MISSING_REQUIRED_FIELD

@allure.feature('Create Index')
@allure.story('Successfully create an index using all configuration')
@pytest.mark.parametrize("index_data", [INDEX_DATA])
def test_create_index(index_data):
    create_response = ApiClient.create_index(index_data)
    assert create_response.status_code == 201
    allure.attach(create_response.text, name="Create Index Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('Create Index')
@allure.story('Successfully create an index with minimal data')
@pytest.mark.parametrize("index_data", [MINIMAL_INDEX_DATA])
def test_create_minimal_index(index_data):
    create_response = ApiClient.create_index(index_data)
    assert create_response.status_code == 201
    allure.attach(create_response.text, name="Create Minimal Index Response", attachment_type=allure.attachment_type.JSON)


@allure.feature('Create Index')
@allure.story('Attempt to create an index with invalid data, should return 400')
@pytest.mark.parametrize("index_data", [INVALID_INDEX_DATA])
def test_create_invalid_index(index_data):
    create_response = ApiClient.create_index(index_data)
    assert create_response.status_code == 400  # should return 400
    allure.attach(create_response.text, name="Create Invalid Index Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('Create Index')
@allure.story('Attempt to create an index missing required fields, should return 400')
@pytest.mark.parametrize("index_data", [MISSING_REQUIRED_FIELD])
def test_create_index_missing_required_fields(index_data):
    # Minimal data missing required fields should fail
    create_response = ApiClient.create_index(index_data)
    assert create_response.status_code == 400  # Missing required fields should return 400
    allure.attach(create_response.text, name="Create Index Missing Required Fields", attachment_type=allure.attachment_type.JSON)

@allure.feature('Create Index')
@allure.story('Attempt to create an index with invalid format, should return 400')
@pytest.mark.parametrize("index_data", [INVALID_INDEX_DATA])
def test_create_index_with_invalid_format(index_data):
    # Sending invalid formatted data (e.g., wrong data types) should fail
    create_response = ApiClient.create_index(index_data)
    assert create_response.status_code == 400  # should return 400
    allure.attach(create_response.text, name="Create Index Invalid Format", attachment_type=allure.attachment_type.JSON)
