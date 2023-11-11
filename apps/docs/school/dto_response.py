
DTO_RESPONSE_GET_ALL_SCHOOL = {
  "limit": 20,
  "offset": 0,
  "count": 2,
  "next": None,
  "previous": None,
  "results": [
    {
      "id": "33e23f70-ed0c-471a-9d6b-f1ad44440a42",
      "responsible": {
        "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
        "full_name": "José Mateus Rian das Chagas",
        "email": "admin@admin.com",
        "phone": "82 9913-3059",
        "is_active": True
      },
      "name": "Escola jany camelo çlima",
      "address": "Adalto",
      "geolocation": "848",
      "countie": {
        "id": "eab6c3fe-3ea4-4047-8c2b-de452a90cdf9",
        "name": "Água Branca",
        "code": "91f2cb89"
      },
      "is_deleted": True
    },
    {
      "id": "ecf0ec46-f9bf-45d1-855d-58f42e236f6b",
      "responsible": {
        "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
        "full_name": "José Mateus Rian das Chagas",
        "email": "admin@admin.com",
        "phone": "82 9913-3059",
        "is_active": True
      },
      "name": "Escola jany camelo çlima",
      "address": "Adalto",
      "geolocation": "848",
      "countie": {
        "id": "50dfb2bf-4600-48e7-b7e2-3abaa9f55135",
        "name": "Arapiraca",
        "code": "d1709518"
      },
      "is_deleted": True
    }
  ]
}

DTO_RESPONSE_DETAIL_SCHOOL = {
  "id": "ecf0ec46-f9bf-45d1-855d-58f42e236f6b",
  "responsible": {
    "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
    "full_name": "José Mateus Rian das Chagas",
    "email": "admin@admin.com",
    "phone": "82 9913-3059",
    "is_active": True
  },
  "name": "Escola jany camelo çlima",
  "address": "Adalto",
  "geolocation": "848",
  "countie": {
    "id": "50dfb2bf-4600-48e7-b7e2-3abaa9f55135",
    "name": "Arapiraca",
    "code": "d1709518"
  },
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
  "id": "33e23f70-ed0c-471a-9d6b-f1ad44440a42",
  "responsible": {
    "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
    "full_name": "José Mateus Rian das Chagas",
    "email": "admin@admin.com",
    "phone": "82 9913-3059",
    "is_active": True
  },
  "name": "Escola jany camelo çlima",
  "address": "Adalto",
  "geolocation": "848",
  "countie": {
    "id": "eab6c3fe-3ea4-4047-8c2b-de452a90cdf9",
    "name": "Água Branca",
    "code": "91f2cb89"
  },
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
  "id": "ecf0ec46-f9bf-45d1-855d-58f42e236f6b",
  "responsible": {
    "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
    "full_name": "José Mateus Rian das Chagas",
    "email": "admin@admin.com",
    "phone": "82 9913-3059",
    "is_active": True
  },
  "name": "Escola jany camelo çlima",
  "address": "Adalto",
  "geolocation": "848",
  "countie": {
    "id": "50dfb2bf-4600-48e7-b7e2-3abaa9f55135",
    "name": "Arapiraca",
    "code": "d1709518"
  },
  "is_deleted": False
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