DTO_RESPONSE_GET_ALL_COP = {
  "limit": 20,
  "offset": 0,
  "count": 1,
  "next": None,
  "previous": None,
  "results": [
    {
      "id": "fb9eb89e-dfda-40be-be53-f2f398a5c3ec",
      "responsible": {
        "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
        "full_name": "José Mateus Rian das Chagas",
        "email": "admin@admin.com",
        "phone": "82 9913-3059",
        "is_active": True
      },
      "name": "teste",
      "address": "teste",
      "geolocation": "teste",
      "countie": {
        "id": "50dfb2bf-4600-48e7-b7e2-3abaa9f55135",
        "name": "Arapiraca",
        "code": "d1709518"
      },
      "is_deleted": False
    }
  ]
}

DTO_RESPONSE_DETAIL_COP = {
  "id": "fb9eb89e-dfda-40be-be53-f2f398a5c3ec",
  "responsible": {
    "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
    "full_name": "José Mateus Rian das Chagas",
    "email": "admin@admin.com",
    "phone": "82 9913-3059",
    "is_active": True
  },
  "name": "teste",
  "address": "teste",
  "geolocation": "teste",
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
  "id": "fb9eb89e-dfda-40be-be53-f2f398a5c3ec",
  "responsible": {
    "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
    "full_name": "José Mateus Rian das Chagas",
    "email": "admin@admin.com",
    "phone": "82 9913-3059",
    "is_active": True
  },
  "name": "teste",
  "address": "teste",
  "geolocation": "teste",
  "countie": {
    "id": "50dfb2bf-4600-48e7-b7e2-3abaa9f55135",
    "name": "Arapiraca",
    "code": "d1709518"
  },
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
  "id": "fb9eb89e-dfda-40be-be53-f2f398a5c3ec",
  "responsible": {
    "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
    "full_name": "José Mateus Rian das Chagas",
    "email": "admin@admin.com",
    "phone": "82 9913-3059",
    "is_active": True
  },
  "name": "teste",
  "address": "teste",
  "geolocation": "teste",
  "countie": {
    "id": "6ee5db60-7377-4fe6-bad3-a21cc0e1c829",
    "name": "Coité do Nóia",
    "code": "d86a8032"
  },
  "is_deleted": False
}

DTO_RESPONSE_DELETE_SUCESS = {
  "id": "fb9eb89e-dfda-40be-be53-f2f398a5c3ec",
  "responsible": {
    "id": "908d314f-78de-4f5b-b528-6d5912f5eae2",
    "full_name": "José Mateus Rian das Chagas",
    "email": "admin@admin.com",
    "phone": "82 9913-3059",
    "is_active": True
  },
  "name": "teste",
  "address": "teste",
  "geolocation": "teste",
  "countie": {
    "id": "50dfb2bf-4600-48e7-b7e2-3abaa9f55135",
    "name": "Arapiraca",
    "code": "d1709518"
  },
  "is_deleted": True
}

DTO_RESPONSE_NOT_AUTH = {
	"message": "As credenciais de autenticação não foram fornecidas.",
	"extra": {}
}