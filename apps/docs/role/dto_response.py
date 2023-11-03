DTO_RESPONSE_GET_ALL= {
	"limit": 20,
	"offset": 0,
	"count": 3,
	"next": None,
	"previous": None,
	"results": [
		{
			"id": "8344a3af-29ef-435e-ada0-861c304c365b",
			"code": "ADMIN",
			"name": "ADMINISTRADOR",
			"is_deleted": False
		},
		{
			"id": "f6da1624-ba36-4142-ac93-2d075079a701",
			"code": "AGENT",
			"name": "AGENTE",
			"is_deleted": False
		},
		{
			"id": "6bda03c7-53b2-4c0f-9742-5dcd95563475",
			"code": "TEACHER",
			"name": "PROFESSOR",
			"is_deleted": False
		}
	]
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