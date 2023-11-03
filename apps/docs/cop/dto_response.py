DTO_RESPONSE_GET_ALL_COP = {
	"limit": 20,
	"offset": 0,
	"count": 1,
	"next": None,
	"previous": None,
	"results": [
		{
			"id": "fa2fa213-c63e-47e1-8637-3311d97d7e01",
			"responsible": {
				"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
				"full_name": "José Mateus",
				"email": "admin@admin.com",
				"phone": "82 9913-2309",
				"is_active": True
			},
			"name": "4ª Delegacia Regional de Polícia",
			"address": "Rua Miguel Correia de Amorim, 936 - Baixão, Arapiraca - AL, 57305     495",
			"geolocation": "-892 , -896",
			"is_deleted": False
		}
	]
}

DTO_RESPONSE_DETAIL_COP = {
	"id": "fa2fa213-c63e-47e1-8637-3311d97d7e01",
	"responsible": {
		"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"phone": "82 9913-2309",
		"is_active": True
	},
	"name": "4ª Delegacia Regional de Polícia",
	"address": "Rua Miguel Correia de Amorim, 936 - Baixão, Arapiraca - AL, 57305     495",
	"geolocation": "-892 , -896",
	"is_deleted": False
}

DTO_RESPONSE_DETAIL_BAD_REQUEST = {
	"message": "Validation error",
	"extra": {
		"fields": {
			"non_field_errors": [
				"O valor “31d362c-fb03-4a04-be91-c34d13647cd9” não é um UUID válido"
			]
		}
	}
}

DTO_RESPONSE_DENIED = {
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

DTO_RESPONSE_COP_CREATED = {
	"id": "fa2fa213-c63e-47e1-8637-3311d97d7e01",
	"responsible": {
		"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"phone": "82 9913-2309",
		"is_active": True
	},
	"name": "4ª Delegacia Regional de Polícia",
	"address": "Rua Miguel Correia de Amorim, 936 - Baixão, Arapiraca - AL, 57305     495",
	"geolocation": "-892 , -896",
	"is_deleted": False
}

DTO_RESPONSE_CREATE_BAD_REQUEST = {
	"message": "Validation error",
	"extra": {
		"fields": {
			"responsible": [
				"Este campo é obrigatório."
			]
		}
	}
}

DTO_RESPONSE_UPDATE_SUCESS = {
	"id": "fa2fa213-c63e-47e1-8637-3311d97d7e01",
	"responsible": {
		"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"phone": "82 9913-2309",
		"is_active": True
	},
	"name": "5º Delegacia Regional de Polícia",
	"address": "Rua Miguel Correia de Amorim, 936 - Baixão, Arapiraca - AL, 57305     495",
	"geolocation": "-892 , -896",
	"is_deleted": True
}

DTO_RESPONSE_DELETE_SUCESS = {
	"id": "fa2fa213-c63e-47e1-8637-3311d97d7e01",
	"responsible": {
		"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"phone": "82 9913-2309",
		"is_active": True
	},
	"name": "5º Delegacia Regional de Polícia",
	"address": "Rua Miguel Correia de Amorim, 936 - Baixão, Arapiraca - AL, 57305     495",
	"geolocation": "-892 , -896",
	"is_deleted": True
}

DTO_RESPONSE_NOT_AUTH = {
	"message": "As credenciais de autenticação não foram fornecidas.",
	"extra": {}
}