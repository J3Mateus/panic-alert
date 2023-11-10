
DTO_RESPONSE_GET_ALL_SCHOOL = {
	"limit": 20,
	"offset": 0,
	"count": 1,
	"next": None,
	"previous": None,
	"results": [
		{
			"id": "9e87f127-ccd9-4b0f-a11f-4775b32b13ec",
			"responsible": {
				"id": "cf0e1803-0718-46ff-b68e-4ccfdb2ee4bb",
				"full_name": "José Mateus",
				"email": "josematheus12@outlook.com",
				"phone": "(82) 9.9913-3059",
				"is_active": True
			},
			"name": "Escola Estadual de Educação Básica Professor José Quintela",
			"address": "Av. Ventura de Farias - Baixão, Arapiraca - AL, 57300-590",
			"geolocation": "-892 , -896",
			"is_deleted": False
		}
	]
}


DTO_RESPONSE_DETAIL_SCHOOL = {
	"id": "1f1d362c-fb03-4a04-be91-c34d13647cd9",
	"responsible": {
		"id": "2fb35ca3-5128-4026-aedb-578c32231aa1",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"is_admin": True
	},
	"name": "Escola Estadual de Educação Básica Professor José Quintela",
	"address": "Av. Ventura de Farias - Baixão, Arapiraca - AL, 57300-590",
	"geolocation": "-892 , -896",
	"is_deleted": False,
	"created_by": {
		"id": "2fb35ca3-5128-4026-aedb-578c32231aa1",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"is_admin": True
	},
	"created_at": "2023-10-29T17:37:35.007104-03:00",
	"updated_at": "2023-10-29T17:37:35.007201-03:00"
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

DTO_RESPONSE_CREATE_ACCESS_DENIED = {
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

DTO_RESPONSE_SCHOOL_CREATED = {
	"id": "916f44e8-b937-499f-a619-b2388efa789e",
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

DTO_RESPONSE_CREATE_BAD_REQUEST ={
	"message": "Validation error",
	"extra": {
		"fields": {
			"responsible": [
				"Este campo não pode ser nulo."
			]
		}
	}
}

DTO_RESPONSE_UPDATE_SUCESS = {
	"id": "916f44e8-b937-499f-a619-b2388efa789e",
	"responsible": {
		"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"phone": "82 9913-2309",
		"is_active": True
	},
	"name": "FERNANDO DE COLO DE MELO",
	"address": "Av. Ventura de Farias - Baixão, Arapiraca - AL, 57300-590",
	"geolocation": "-892 , -896",
	"is_deleted": True
}

DTO_RESPONSE_UPDATE_ACCESS_DENIED = {
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

DTO_RESPONSE_DELETE_SUCESS = {
	"id": "916f44e8-b937-499f-a619-b2388efa789e",
	"responsible": {
		"id": "762ffa0d-da4d-4baf-bbf2-51bd4bb0e17a",
		"full_name": "José Mateus",
		"email": "admin@admin.com",
		"phone": "82 9913-2309",
		"is_active": True
	},
	"name": "FERNANDO DE COLO DE MELO",
	"address": "Av. Ventura de Farias - Baixão, Arapiraca - AL, 57300-590",
	"geolocation": "-892 , -896",
	"is_deleted": True
}

DTO_RESPONSE_DELETE_ACCESS_DENIED = {
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