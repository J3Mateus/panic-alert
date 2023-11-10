DTO_VALIDATION_ERRO_EMAIL_AND_PASSWORD_SESSION = {
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

DTO_SUCCESS_SESSION = {
    "session": "sua_sessão_id",
    "data": {
        "id": "ID_do_usuário",
		"full_name": "Nome completo do usuário",
        "email": "seu_email",
        "is_active": "usuario_ativo",
        "is_admin":"usuario_é_admin",
        "is_superuser":"usuario_è_super_usuario"
    }
}
