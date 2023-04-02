import requests
import json

cep = input("Digite o CEP desejado: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.content)
    print("CEP: ", data["cep"])
    print("Logradouro: ", data["logradouro"])
    print("Complemento: ", data["complemento"])
    print("Bairro: ", data["bairro"])
    print("Cidade: ", data["localidade"])
    print("Estado: ", data["uf"])
else:
    print("Não foi possível obter informações para o CEP informado.")
