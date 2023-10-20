import requests

cep = "05305030"
cep = cep.replace(".","").replace("-","")

print(cep)
if len(cep)== 8:
    url = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(url)

    dic_requisicao = requisicao.json()

    print(dic_requisicao)

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    ddd = dic_requisicao['ddd']
    print(f'Cidade {cidade}\nUF: {uf}\nDDD: {ddd}')
else:
    print('CEP inválido')

