import pytest
from unittest.mock import Mock
from Application.UseCases.GetStoresUseCase import GetStoresUseCase

@pytest.fixture
def store_repository():
	return Mock()


@pytest.fixture
def get_stores_use_case(store_repository):
	return GetStoresUseCase(store_repository)


def test_get_stores(get_stores_use_case, store_repository):
	# Datos simulados
	mock_stores = [
		{
			"name": "Cafe UP",
			"rfc": "rfc28",
			"street": "carretera villaflores",
			"number": "asdasd",
			"neighborhood": "edeadsd",
			"city": "TUXTLA",
			"reference": "asdasd",
			"phone_number": "28",
			"opening_hours": "asdasd",
			"closing_hours": "asdasdas",
			"url_image": "url procesada"
		}
	]
	store_repository.list_stores.return_value = mock_stores

	stores = get_stores_use_case.execute()

	assert stores == mock_stores
	store_repository.list_stores.assert_called_once()
