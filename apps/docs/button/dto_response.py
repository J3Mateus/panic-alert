DTO_RESPONSE_GET_ALL = {
  "limit": 1,
  "offset": 0,
  "count": 1,
  "next": None,
  "previous": None,
  "results": [
    {
      "id": "a6f8cfe6-4655-47a5-b275-d695e67fd5e3",
      "teacher": {
        "id": "7dd68209-cf5b-4bd7-ae63-6f5000eb18f6",
        "full_name": "JOSÉ CICERO DAS CHAGAS",
        "email": "jmrc2@aluno.ifal.edu.br",
        "phone": "82 9.9913-3059",
        "is_active": True
      },
      "school": {
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
      },
      "cop": {
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
      },
      "status": "ocorrencia_iniciada",
      "description": "Homem armado invadiu a escola com uma faca",
      "responsible": {
        "id": "70b545b0-2776-46a8-bc7c-7f70e937695f",
        "full_name": "agente",
        "email": "jrmc5@admin.com",
        "phone": "82 9913.03049",
        "is_active": True
      },
      "problem_solving": ""
    }
  ]
}

DTO_RESPONSE_DETAIL = {
  "id": "a6f8cfe6-4655-47a5-b275-d695e67fd5e3",
  "teacher": {
    "id": "7dd68209-cf5b-4bd7-ae63-6f5000eb18f6",
    "full_name": "JOSÉ CICERO DAS CHAGAS",
    "email": "jmrc2@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "school": {
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
  },
  "cop": {
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
  },
  "status": "ocorrencia_iniciada",
  "description": "Homem armado invadiu a escola com uma faca",
  "responsible": {
    "id": "70b545b0-2776-46a8-bc7c-7f70e937695f",
    "full_name": "agente",
    "email": "jrmc5@admin.com",
    "phone": "82 9913.03049",
    "is_active": True
  },
  "problem_solving": ""
}

DTO_RESPONSE_BAD_REQUEST = {}

DTO_RESPONSE_DETAIL_BAD_REQUEST = {
  "message": "Validation error",
  "extra": {
    "fields": {
      "non_field_errors": [
        "O valor “a6f8cfe6-4655-47a5-b275-d695e67fd5e4\"” não é um UUID válido"
      ]
    }
  }
}

DTO_RESPONSE_BAD_REQUEST_NOT_FIELD = {
  "message": "Validation error",
  "extra": {
    "fields": {
      "non_field_errors": [
        "O usuário não está associado a nenhuma escola."
      ]
    }
  }
}

DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_SCHOOL = {}

DTO_RESPONSE_CONFLICT = {}

DTO_RESPONSE_BAD_REQUEST_NOT_FOUND_ROLE = {}

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

DTO_RESPONSE_CREATED = {
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "teacher": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "full_name": "string",
    "email": "string",
    "phone": "string",
    "is_active": True
  },
  "school": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "responsible": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "full_name": "string",
      "email": "string",
      "phone": "string",
      "is_active": True
    },
    "name": "string",
    "geolocation": "string",
    "address": {
      "zipCode": "string",
      "district": "string",
      "uf": "string",
      "location": "string",
      "publicArea": "string"
    },
    "countie": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "string",
      "code": "string"
    },
    "is_deleted": False
  },
  "cop": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "string",
    "address": {
      "zipCode": "string",
      "district": "string",
      "uf": "string",
      "location": "string",
      "publicArea": "string"
    },
    "responsible": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "full_name": "string",
      "email": "string",
      "phone": "string",
      "is_active": True
    },
    "geolocation": "string",
    "countie": {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "string",
      "code": "string"
    },
    "is_deleted": False
  },
  "status": "string",
  "description": "string",
  "responsible": {
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "full_name": "string",
    "email": "string",
    "phone": "string",
    "is_active": True
  },
  "problem_solving": "string"
}

DTO_RESPONSE_UPDATE_SUCESS = {
  "id": "a6f8cfe6-4655-47a5-b275-d695e67fd5e3",
  "teacher": {
    "id": "7dd68209-cf5b-4bd7-ae63-6f5000eb18f6",
    "full_name": "JOSÉ CICERO DAS CHAGAS",
    "email": "jmrc2@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "school": {
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
  },
  "cop": {
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
  },
  "status": "ocorrencia_iniciada",
  "description": "Alguém está com arma na escola",
  "responsible": {
    "id": "70b545b0-2776-46a8-bc7c-7f70e937695f",
    "full_name": "agente",
    "email": "jrmc5@admin.com",
    "phone": "82 9913.03049",
    "is_active": True
  },
  "problem_solving": ""
}

DTO_RESPONSE_DELETE_SUCESS = {}

DTO_RESPONSE_NOT_AUTH = {
	"message": "As credenciais de autenticação não foram fornecidas.",
	"extra": {}
}