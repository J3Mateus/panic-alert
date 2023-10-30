DTO_ME_SUCCESS = {
    "id": "ID_do_usuário",
    "first_name": "primeiro_nome_do_usuario",
    "last_name": "ultimo_nome_do_usuario",
    "email": "seu_email",
    "is_active": "usuario_ativo",
    "is_admin":"usuario_é_admin",
    "is_superuser":"usuario_è_super_usuario"
}

DTO_VALIDATION_ERRO_ME = {
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
