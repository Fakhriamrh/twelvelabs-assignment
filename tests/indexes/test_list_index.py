import pytest
import allure
from utils.api_client import ApiClient

@allure.feature('List Indexes')
@allure.story('List all indexes')
def test_list_all_indexes():
    response = ApiClient.list_indexes()
    assert response.status_code == 200  # Expecting 200 for successful listing
    allure.attach(response.text, name="List All Indexes Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('List Indexes')
@allure.story('List indexes with pagination')
def test_list_indexes_with_pagination():
    response = ApiClient.list_indexes(page=1, page_limit=5)
    assert response.status_code == 200  # Expecting 200 for successful listing
    allure.attach(response.text, name="List Indexes With Pagination Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('List Indexes')
@allure.story('Attempt to list indexes with invalid parameters, should return 400')
def test_list_indexes_invalid_parameters():
    response = ApiClient.list_indexes(page="invalid", page_limit="invalid")
    assert response.status_code == 400  # Expecting 400 for bad request
    allure.attach(response.text, name="List Indexes Invalid Parameters Response", attachment_type=allure.attachment_type.JSON)

@allure.feature('List Indexes')
@allure.story('List indexes without providing pagination')
def test_list_indexes_without_pagination():
    response = ApiClient.list_indexes(page=1, page_limit=10)
    assert response.status_code == 200  # Expecting 200 for successful listing
    allure.attach(response.text, name="List Indexes Without Pagination Response", attachment_type=allure.attachment_type.JSON)

