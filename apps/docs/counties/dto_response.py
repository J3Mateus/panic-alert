DTO_RESPONSE_GET_ALL= {
  "limit": 20,
  "offset": 0,
  "count": 102,
  "next": "http://127.0.0.1:8000/api/counties/get/list/all?limit=20&offset=20",
  "previous": None,
  "results": [
    {
      "id": "eab6c3fe-3ea4-4047-8c2b-de452a90cdf9",
      "name": "Água Branca",
      "code": "91f2cb89"
    },
    {
      "id": "2727b537-f3b1-422b-98dc-b66586491b8c",
      "name": "Anadia",
      "code": "97eb3f5a"
    },
    {
      "id": "50dfb2bf-4600-48e7-b7e2-3abaa9f55135",
      "name": "Arapiraca",
      "code": "d1709518"
    },
    {
      "id": "5e1cf440-faf4-448e-a0f9-39736d4c6fa3",
      "name": "Atalaia",
      "code": "2b36ef23"
    },
    {
      "id": "58a0b7ec-1cf7-46ec-8971-2723c3ed8402",
      "name": "Barra de Santo Antônio",
      "code": "375aace9"
    },
    {
      "id": "a0919462-70ac-4435-bba9-3df3848ca0e0",
      "name": "Barra de São Miguel",
      "code": "1a456f08"
    },
    {
      "id": "685d9d23-de56-4a6a-9989-05d00aecf576",
      "name": "Batalha",
      "code": "2ee88b05"
    },
    {
      "id": "81c0db50-7f1c-4358-8bdb-5140feeca5af",
      "name": "Belém",
      "code": "d8dcce76"
    },
    {
      "id": "d4450eb0-4e42-45a9-b046-b3a62515f592",
      "name": "Belo Monte",
      "code": "446dddae"
    },
    {
      "id": "e27f9f4a-99bf-4f56-bd1d-da221d0026a3",
      "name": "Boca da Mata",
      "code": "3aa61850"
    },
    {
      "id": "69461f52-e7b0-4c5c-9cbd-2028be5aff8d",
      "name": "Branquinha",
      "code": "963cfd5f"
    },
    {
      "id": "b91935cc-ff41-4e5f-a963-1c0e56e304d7",
      "name": "Cacimbinhas",
      "code": "78c2860c"
    },
    {
      "id": "24e4360d-d848-469a-9e81-fa90ec6a3444",
      "name": "Cajueiro",
      "code": "3db95dcb"
    },
    {
      "id": "51e2f2b7-c6de-4f6b-9ecc-f06b8e0f969b",
      "name": "Campestre",
      "code": "89bc0a51"
    },
    {
      "id": "56ed1541-ae43-402a-8a79-f0cbb80e2817",
      "name": "Campo Alegre",
      "code": "3d677f8e"
    },
    {
      "id": "43ae10da-3438-4d73-8286-4c6710631138",
      "name": "Campo Grande",
      "code": "d8c0105b"
    },
    {
      "id": "26892361-3ce2-4175-9691-90441c7c3029",
      "name": "Canapi",
      "code": "eccbdc67"
    },
    {
      "id": "9942f7b3-1a73-4936-9b47-0e67a6c6d2a7",
      "name": "Capela",
      "code": "9a0a9229"
    },
    {
      "id": "5fff9dfa-0de8-4385-a36d-d7af63306218",
      "name": "Carneiros",
      "code": "6de70eca"
    },
    {
      "id": "fa53aaf8-e826-460c-8919-553e2b92d115",
      "name": "Chã Preta",
      "code": "0053cb93"
    }
  ]
}

DTO_RESPONSE_GET_BY_ID = {
  "id": "5e1cf440-faf4-448e-a0f9-39736d4c6fa3",
  "name": "Atalaia",
  "code": "2b36ef23"
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