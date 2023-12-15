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
      "problem_solving": "",
      "created_at": "2023-12-15T09:04:54.837843-03:00"
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
  "problem_solving": "",
  "created_at": "2023-12-15T09:04:54.837843-03:00"
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
  "id": "f988beb8-cda2-450b-8a5a-0c9bac4e0742",
  "type_incident": {
    "id": "228996cd-aef9-42e9-b1ef-08b89132a37d",
    "name": "nao_informado",
    "code": "Não informado"
  },
  "teacher": {
    "id": "cb1659a1-20db-486f-bcd6-f9157ab828fa",
    "full_name": "TIAGO JOSÉ CHAGAS",
    "email": "jmrc1@aluno.ifal.edu.br",
    "phone": "82 9.9913-3059",
    "is_active": True
  },
  "school": {
    "id": "ad11b416-d611-4ce4-b444-9f4d21646328",
    "responsible": {
      "id": "cb1659a1-20db-486f-bcd6-f9157ab828fa",
      "full_name": "TIAGO JOSÉ CHAGAS",
      "email": "jmrc1@aluno.ifal.edu.br",
      "phone": "82 9.9913-3059",
      "is_active": True
    },
    "name": "E.Q.C - Escola Estadual de Educação Básica Professor José Quintela Cavalcanti",
    "geolocation": "82,93",
    "address": {
      "zipCode": "57300-590",
      "district": "Centro",
      "uf": "AL",
      "location": "Arapiraca",
      "publicArea": "Rua Expedicionários Brasileiros"
    },
    "countie": {
      "id": "fc9c4231-ba94-446c-86cd-30eb51cf2cf6",
      "name": "Arapiraca",
      "code": "a508281d"
    },
    "is_deleted": False
  },
  "cop": {
    "id": "ad06e011-2f78-4eff-8fc2-6a9b7f5a724d",
    "name": "Delegacia Geral de Polícia Civil",
    "address": {
      "zipCode": "57300-590",
      "district": "Centro",
      "uf": "AL",
      "location": "Arapiraca",
      "publicArea": "Rua Expedicionários Brasileiros"
    },
    "responsible": {
      "id": "ca424b55-c18b-4d44-a4ce-b84b1156ebea",
      "full_name": "JOSÉ MATEUS RIAN DAS CHAGAS",
      "email": "admin@admin.com",
      "phone": "82 9.9913-3059",
      "is_active": True
    },
    "geolocation": "82 ,-28",
    "countie": {
      "id": "fc9c4231-ba94-446c-86cd-30eb51cf2cf6",
      "name": "Arapiraca",
      "code": "a508281d"
    },
    "is_deleted": False
  },
  "status": "ocorrencia_iniciada",
  "description": "",
  "responsible": None,
  "problem_solving": "",
  "created_at": "2023-12-15T09:04:54.837843-03:00"
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
  "problem_solving": "",
  "created_at": "2023-12-15T09:04:54.837843-03:00"
}

DTO_RESPONSE_DELETE_SUCESS = {}

DTO_RESPONSE_NOT_AUTH = {
	"message": "As credenciais de autenticação não foram fornecidas.",
	"extra": {}
}