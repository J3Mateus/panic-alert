
DTO_RESPONSE_GET_ALL_SCHOOL = {
  "limit": 20,
  "offset": 0,
  "count": 1,
  "next": None,
  "previous": None,
  "results": [
    {
      "id": "9fa8cf00-64b3-4338-9f46-7a2c8abe7858",
      "responsible": {
        "id": "2fdd040e-ddc3-4878-8900-03e93e00b238",
        "full_name": "TIAGO JOSÉ DAS CHAGAS",
        "email": "jmrc1@aluno.ifal.edu.br",
        "phone": "82 9.9913-3059",
        "is_active": True
      },
      "name": "E.Q.C - Escola Estadual de Educação Básica Professor José Quintela Cavalcanti",
      "geolocation": "82,96",
      "address": {
        "zipCode": "57020-970",
        "district": "Centro",
        "uf": "AL",
        "location": "Maceió",
        "publicArea": "Rua do Sol 57"
      },
      "countie": {
        "id": "0468676f-f994-4b9d-9a65-93e81e879ece",
        "name": "Arapiraca",
        "code": "63965742"
      },
      "is_deleted": False
    }
  ]
}

DTO_RESPONSE_DETAIL_SCHOOL = {
  "id": "9fa8cf00-64b3-4338-9f46-7a2c8abe7858",
  "responsible": {
    "id": "2fdd040e-ddc3-4878-8900-03e93e00b238",
    "full_name": "TIAGO JOSÉ DAS CHAGAS",
    "email": "jmrc1@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "name": "E.Q.C - Escola Estadual de Educação Básica Professor José Quintela Cavalcanti",
  "geolocation": "82,96",
  "address": {
    "zipCode": "57020-970",
    "district": "Centro",
    "uf": "AL",
    "location": "Maceió",
    "publicArea": "Rua do Sol 57"
  },
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
  "id": "f3ce33a4-30de-4539-860c-bfbea5ef3c65",
  "responsible": {
    "id": "2fdd040e-ddc3-4878-8900-03e93e00b238",
    "full_name": "TIAGO JOSÉ DAS CHAGAS",
    "email": "jmrc1@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "name": "Escola",
  "geolocation": "-82,95",
  "address": {
    "zipCode": "cep",
    "district": "distrito",
    "uf": "AL",
    "location": "arapiraca",
    "publicArea": "arapiraca"
  },
  "countie": {
    "id": "eeedf433-41a3-4bc9-a5bf-f3c03626152f",
    "name": "Belém",
    "code": "78dd9c48"
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
  "id": "f3ce33a4-30de-4539-860c-bfbea5ef3c65",
  "responsible": {
    "id": "2fdd040e-ddc3-4878-8900-03e93e00b238",
    "full_name": "TIAGO JOSÉ DAS CHAGAS",
    "email": "jmrc1@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "name": "escola nova",
  "geolocation": "-82,95",
  "address": {
    "zipCode": "cep",
    "district": "distrito",
    "uf": "AL",
    "location": "arapiraca",
    "publicArea": "arapiraca"
  },
  "countie": {
    "id": "eeedf433-41a3-4bc9-a5bf-f3c03626152f",
    "name": "Belém",
    "code": "78dd9c48"
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
  "id": "f3ce33a4-30de-4539-860c-bfbea5ef3c65",
  "responsible": {
    "id": "2fdd040e-ddc3-4878-8900-03e93e00b238",
    "full_name": "TIAGO JOSÉ DAS CHAGAS",
    "email": "jmrc1@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "name": "escola nova",
  "geolocation": "-82,95",
  "address": {
    "zipCode": "cep",
    "district": "distrito",
    "uf": "AL",
    "location": "arapiraca",
    "publicArea": "arapiraca"
  },
  "countie": {
    "id": "eeedf433-41a3-4bc9-a5bf-f3c03626152f",
    "name": "Belém",
    "code": "78dd9c48"
  },
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