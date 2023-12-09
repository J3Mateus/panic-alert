DTO_RESPONSE_GET_ALL= {
  "limit": 20,
  "offset": 0,
  "count": 5,
  "next": None,
  "previous": None,
  "results": [
    {
      "id": "d83f7d54-c3dd-4644-9bf2-d84362c5904f",
      "full_name": "José Mateus Rian Das Chagas",
      "roles": [],
      "email": "admin@admin.com",
      "phone": "82 9913-3059",
      "schools": [],
      "cops": [],
      "whatsapp": "82 9913-3059",
      "is_deleted": False
    },
    {
      "id": "2fdd040e-ddc3-4878-8900-03e93e00b238",
      "full_name": "TIAGO JOSÉ DAS CHAGAS",
      "roles": [
        {
          "id": "b83c5977-0dea-4a16-bede-cdc621778d22",
          "name": "PROFESSOR",
          "code": "TEACHER"
        }
      ],
      "email": "jmrc1@aluno.ifal.edu.br",
      "phone": "82 9.9913-3059",
      "schools": [],
      "cops": [],
      "whatsapp": "82 9.9913-3059",
      "is_deleted": False
    },
    {
      "id": "7dd68209-cf5b-4bd7-ae63-6f5000eb18f6",
      "full_name": "JOSÉ CICERO DAS CHAGAS",
      "roles": [
        {
          "id": "b83c5977-0dea-4a16-bede-cdc621778d22",
          "name": "PROFESSOR",
          "code": "TEACHER"
        }
      ],
      "email": "jmrc2@aluno.ifal.edu.br",
      "phone": "82 9.9913-3059",
      "schools": [
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
      ],
      "cops": [],
      "whatsapp": "82 9.9913-3059",
      "is_deleted": False
    },
    {
      "id": "208edd18-7dfb-4d1b-aa49-7b8b524aaab4",
      "full_name": "ARTUR DAS CHAGAS",
      "roles": [
        {
          "id": "a5ea0534-fd55-4374-8d62-e4b682c2adb0",
          "name": "AGENTE",
          "code": "AGENT"
        }
      ],
      "email": "jmrc3@aluno.ifal.edu.br",
      "phone": "82 9.9913-3059",
      "schools": [],
      "cops": [],
      "whatsapp": "82 9.9913-3059",
      "is_deleted": False
    },
    {
      "id": "70b545b0-2776-46a8-bc7c-7f70e937695f",
      "full_name": "agente",
      "roles": [
        {
          "id": "a5ea0534-fd55-4374-8d62-e4b682c2adb0",
          "name": "AGENTE",
          "code": "AGENT"
        }
      ],
      "email": "jrmc5@admin.com",
      "phone": "82 9913.03049",
      "schools": [],
      "cops": [
        {
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
      ],
      "whatsapp": "82 92020",
      "is_deleted": False
    }
  ]
}

DTO_RESPONSE_CREATE = {
  "id": "1de23a8f-79cd-4fb3-aa30-b775e1570c76",
  "full_name": "JOSÉ MATEUS RIAN DAS CHAGAS",
  "roles": [
    {
      "id": "b83c5977-0dea-4a16-bede-cdc621778d22",
      "name": "PROFESSOR",
      "code": "TEACHER"
    }
  ],
  "email": "josematheus@gmail.com",
  "phone": "82 9913-3059",
  "schools": [
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
  ],
  "cops": [],
  "whatsapp": "82 9913-3059",
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
  "id": "70b545b0-2776-46a8-bc7c-7f70e937695f",
  "full_name": "agente",
  "roles": [
    {
      "id": "a5ea0534-fd55-4374-8d62-e4b682c2adb0",
      "name": "AGENTE",
      "code": "AGENT"
    }
  ],
  "email": "jrmc5@admin.com",
  "phone": "82 9913.03049",
  "schools": [],
  "cops": [
    {
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
  ],
  "whatsapp": "82 92020",
  "is_deleted": True
}

DTO_RESPONSE_UPDATE_SUCESS = {
  "id": "d83f7d54-c3dd-4644-9bf2-d84362c5904f",
  "full_name": "José Mateus Rian Das Chagas",
  "roles": [
    {
      "id": "b83c5977-0dea-4a16-bede-cdc621778d22",
      "name": "PROFESSOR",
      "code": "TEACHER"
    }
  ],
  "email": "admin@admin.com",
  "phone": "82 9913-3059",
  "schools": [],
  "cops": [],
  "whatsapp": "82 9913-3059",
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