DTO_VALIDATION_ERRO_EMAIL_AND_PASSWORD_JWT = {
	"message": "Validation error",
	"extra": {
		"fields": {
			"email": [
				"Este campo não pode ser em branco."
			],
			"password": [
				"Este campo não pode ser em branco."
			]
		}
	}
}

DTO_VALIDATION_INCORRECT_EMAIL_AND_PASSWORD_JWT = {
	"message": "Usuário e/ou senha incorreto(s)",
	"extra": {}
}

DTO_SUCCESS_JWT = {
	"refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5ODUyNjE4OSwiaWF0IjoxNjk4NTIyNTg5LCJqdGkiOiIwNTdjN2FjZTgzZDk0MzliOTVkMWQwYzgxYTM5ODgxOCIsInVzZXJfaWQiOiIzNzQ1OGU5Mi0wNDMzLTQ1OTMtOGE0Yy1mMmU3ODY0YmEzYzAifQ.kQ6DZAGFkpjMh6-I8h-dQPGID42qTLdAgSV_ITtrJs4",
	"access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk4NTI2MTg5LCJpYXQiOjE2OTg1MjI1ODksImp0aSI6IjIyZmVkY2NhMzczYjRlNDRiNDNhYmQ5NDNkMzRlNmQzIiwidXNlcl9pZCI6IjM3NDU4ZTkyLTA0MzMtNDU5My04YTRjLWYyZTc4NjRiYTNjMCJ9.ZVk7QWe_n-tIyySGOstonw4GNH0sCWaKLAjzdFLLmSk"
}

DTO_VALIDATION_ERRO_LOGOUT_JWT = {
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

DTO_VALIDATION_USER_DELETED_JWT = {
	"message": "Este usuário foi desativado.",
	"extra": {}
}
