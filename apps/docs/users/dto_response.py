DTO_RESPONSE_GET_ALL= {
	"limit": 20,
	"offset": 0,
	"count": 2,
	"next": None,
	"previous": None,
	"results": [
		{
			"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
			"full_name": "José Mateus",
			"role": [],
			"email": "admin@admin.com",
			"phone": "82 9913-2309",
			"school": [],
			"whatsapp": "82 9914-2959",
			"is_deleted": False
		},
		{
			"id": "0646d9c5-3e97-4293-9f7e-d89e4ea5fcbf",
			"full_name": "José Mateus",
			"role": [],
			"email": "professor@gmail.com",
			"phone": "(82) 9.9913-3059",
			"school": [],
			"whatsapp": "(82) 9.9913-3059",
			"is_deleted": False
		}
	]
}

DTO_RESPONSE_CREATE = {
	"id": "7f8ca468-f7dc-42e6-8941-4918ef021242",
	"full_name": "José Mateus",
	"role": [
		{
			"id": "8344a3af-29ef-435e-ada0-861c304c365b",
			"name": "ADMINISTRADOR",
			"code": "ADMIN"
		}
	],
	"email": "rian@gmail.com",
	"phone": "(82) 9.9913-3059",
	"school": [
		{
			"id": "d377c265-c11a-467c-b044-ddf792b428c3",
			"responsible": {
				"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
				"full_name": "José Mateus",
				"email": "admin@admin.com",
				"phone": "82 9913-2309",
				"is_active": True
			},
			"name": "Escola Estadual de Educação Básica Professor José Quintela",
			"address": "Av. Ventura de Farias - Baixão, Arapiraca - AL, 57300-590",
			"geolocation": "-892 , -896",
			"is_deleted": False
		}
	],
	"whatsapp": "(82) 9.9913-3059",
	"is_deleted": False
}

DTO_RESPONSE_CONFLICT = {
	"message": {
		"detail": "A chave única já existe no banco de dados."
	},
	"code": "Conflict",
	"messages": [
		{
			"field": "email",
			"message": "O email já está sendo usado por um usuario"
		}
	],
	"extra": {}
}

DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_SCHOOL = {
	"message": "Validation error",
	"extra": {
		"fields": {
			"non_field_errors": [
				"A escola com o UUID(9580fdd2-ec84-48b9-8871-93a9452f8e25) fornecido não existe no banco de dados."
			]
		}
	}
}

DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_ROLE = {
	"message": "Validation error",
	"extra": {
		"fields": {
			"non_field_errors": [
				"O papel com o UUID(9580fdd2-ec84-48b9-8871-93a9452f8e25)  fornecido não existe no banco de dados."
			]
		}
	}
}

DTO_RESPONSE_BAD_REQUEST_NOT_FIELD = {
	"message": "Validation error",
	"extra": {
		"fields": {
			"roles": [
				"Este campo é obrigatório."
			]
		}
	}
}

DTO_RESPONSE_DELETE_SUCESS = {
	"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
	"full_name": "José Mateus",
	"role": [],
	"email": "admin@admin.com",
	"phone": "82 9913-2309",
	"school": [],
	"whatsapp": "82 9914-2959",
	"is_deleted": True
}

DTO_RESPONSE_UPDATE_SUCESS = {
	"id": "7f8ca468-f7dc-42e6-8941-4918ef021242",
	"full_name": "José Mateus",
	"role": [
		{
			"id": "8344a3af-29ef-435e-ada0-861c304c365b",
			"name": "ADMINISTRADOR",
			"code": "ADMIN"
		}
	],
	"email": "rian@gmail.com",
	"phone": "(82) 9.9913-3059",
	"school": [
		{
			"id": "d377c265-c11a-467c-b044-ddf792b428c3",
			"responsible": {
				"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
				"full_name": "José Mateus",
				"email": "admin@admin.com",
				"phone": "82 9913-2309",
				"is_active": True
			},
			"name": "Escola Estadual de Educação Básica Professor José Quintela",
			"address": "Av. Ventura de Farias - Baixão, Arapiraca - AL, 57300-590",
			"geolocation": "-892 , -896",
			"is_deleted": False
		}
	],
	"whatsapp": "(82) 9.9913-3059",
	"is_deleted": False
}

DTO_RESPONSE_ACCESS_DENIED = {
	"message": {
		"detail": "O token informado não é válido para qualquer tipo de token",
		"code": "token_not_valid",
		"messages": [
			{
				"token_class": "AccessToken",
				"token_type": "access",
				"message": "O token é inválido ou expirado"
			}
		]
	},
	"extra": {}
}