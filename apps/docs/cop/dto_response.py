DTO_RESPONSE_GET_ALL_COP = {
  "limit": 20,
  "offset": 0,
  "count": 1,
  "next": None,
  "previous": None,
  "results": [
    {
      "id": "9992a240-f76e-49f8-be49-11809f490b8b",
      "name": "Delegacia",
      "address": {
        "zipCode": "57020-970",
        "district": "Centro",
        "uf": "AL",
        "location": "Maceió",
        "publicArea": "Rua do Sol 57"
      },
      "responsible": {
        "id": "208edd18-7dfb-4d1b-aa49-7b8b524aaab4",
        "full_name": "ARTUR DAS CHAGAS",
        "email": "jmrc3@aluno.ifal.edu.br",
        "phone": "82 9.9913-3059",
        "is_active": True
      },
      "geolocation": "-85,96",
      "countie": {
        "id": "0468676f-f994-4b9d-9a65-93e81e879ece",
        "name": "Arapiraca",
        "code": "63965742"
      },
      "is_deleted": False
    }
  ]
}

DTO_RESPONSE_DETAIL_COP = {
  "id": "9992a240-f76e-49f8-be49-11809f490b8b",
  "name": "Delegacia",
  "address": {
    "zipCode": "57020-970",
    "district": "Centro",
    "uf": "AL",
    "location": "Maceió",
    "publicArea": "Rua do Sol 57"
  },
  "responsible": {
    "id": "208edd18-7dfb-4d1b-aa49-7b8b524aaab4",
    "full_name": "ARTUR DAS CHAGAS",
    "email": "jmrc3@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "geolocation": "-85,96",
  "countie": {
    "id": "0468676f-f994-4b9d-9a65-93e81e879ece",
    "name": "Arapiraca",
    "code": "63965742"
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
  "id": "9992a240-f76e-49f8-be49-11809f490b8b",
  "name": "Delegacia",
  "address": {
    "zipCode": "57020-970",
    "district": "Centro",
    "uf": "AL",
    "location": "Maceió",
    "publicArea": "Rua do Sol 57"
  },
  "responsible": {
    "id": "208edd18-7dfb-4d1b-aa49-7b8b524aaab4",
    "full_name": "ARTUR DAS CHAGAS",
    "email": "jmrc3@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "geolocation": "-85,96",
  "countie": {
    "id": "0468676f-f994-4b9d-9a65-93e81e879ece",
    "name": "Arapiraca",
    "code": "63965742"
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
  "id": "6d9ead92-059a-4368-bbc0-4001e42bbcb0",
  "name": "string",
  "address": {
    "zipCode": "57300-030",
    "district": "Centro",
    "uf": "AL",
    "location": "Arapiraca",
    "publicArea": "Rua Boa Vista"
  },
  "responsible": {
    "id": "208edd18-7dfb-4d1b-aa49-7b8b524aaab4",
    "full_name": "ARTUR DAS CHAGAS",
    "email": "jmrc3@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "geolocation": "string",
  "countie": {
    "id": "0468676f-f994-4b9d-9a65-93e81e879ece",
    "name": "Arapiraca",
    "code": "63965742"
  },
  "is_deleted": True
}

DTO_RESPONSE_DELETE_SUCESS = {
  "id": "6d9ead92-059a-4368-bbc0-4001e42bbcb0",
  "name": "string",
  "address": {
    "zipCode": "57300-030",
    "district": "Centro",
    "uf": "AL",
    "location": "Arapiraca",
    "publicArea": "Rua Boa Vista"
  },
  "responsible": {
    "id": "208edd18-7dfb-4d1b-aa49-7b8b524aaab4",
    "full_name": "ARTUR DAS CHAGAS",
    "email": "jmrc3@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "geolocation": "string",
  "countie": {
    "id": "0468676f-f994-4b9d-9a65-93e81e879ece",
    "name": "Arapiraca",
    "code": "63965742"
  },
  "is_deleted": True
}

DTO_RESPONSE_NOT_AUTH = {
	"message": "As credenciais de autenticação não foram fornecidas.",
	"extra": {}
}