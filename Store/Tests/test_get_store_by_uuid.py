import pytest
from unittest.mock import Mock
from Application.UseCases.GetStoreByUuidUseCase import GetStoreByUuidUseCase


@pytest.fixture
def store_repository():
	return Mock()


@pytest.fixture
def get_store_by_uuid_use_case(store_repository):
	return GetStoreByUuidUseCase(store_repository)


def test_get_store_by_uuid(get_store_by_uuid_use_case, store_repository):
	# Datos simulados
	mock_store = {
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
	uuid = "123e4567-e89b-12d3-a456-426614174000"
	store_repository.getStore.return_value = mock_store

	# Ejecutar el caso de uso
	store = get_store_by_uuid_use_case.execute(uuid)

	# Verificar resultados
	assert store == mock_store
	store_repository.getStore.assert_called_once_with(uuid)
