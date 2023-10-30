
DTO_RESPONSE_GET_ALL_SCHOOL = {
	"limit": 20,
	"offset": 0,
	"count": 1,
	"next": None,
	"previous": None,
	"results": [
		{
			"id": "39194952-bf63-4851-b312-3ef3674dff08",
			"responsible": {
				"id": "2fb35ca3-5128-4026-aedb-578c32231aa1",
				"first_name": "José",
				"last_name": "Mateus",
				"email": "admin@admin.com",
				"is_admin": True
			},
			"name": "ESCOLA DE ENSINO FUNDAMENTAL GOVERNADOR FERNANDO COLLOR DE MELLO",
			"address": "POVOADO CANAA, S/N ZONA RURAL. 57300-970 Arapiraca - AL.",
			"geolocation": "-892 , -896",
			"is_deleted": True,
			"created_by": {
				"id": "2fb35ca3-5128-4026-aedb-578c32231aa1",
				"first_name": "José",
				"last_name": "Mateus",
				"email": "admin@admin.com",
				"is_admin": True
			},
			"created_at": "2023-10-29T17:35:50.998725-03:00",
			"updated_at": "2023-10-29T19:15:05.791175-03:00"
		}
	]
}


DTO_RESPONSE_DETAIL_SCHOOL = {
	"id": "1f1d362c-fb03-4a04-be91-c34d13647cd9",
	"responsible": {
		"id": "2fb35ca3-5128-4026-aedb-578c32231aa1",
		"first_name": "José",
		"last_name": "Mateus",
		"email": "admin@admin.com",
		"is_admin": True
	},
	"name": "Escola Estadual de Educação Básica Professor José Quintela",
	"address": "Av. Ventura de Farias - Baixão, Arapiraca - AL, 57300-590",
	"geolocation": "-892 , -896",
	"is_deleted": False,
	"created_by": {
		"id": "2fb35ca3-5128-4026-aedb-578c32231aa1",
		"first_name": "José",
		"last_name": "Mateus",
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