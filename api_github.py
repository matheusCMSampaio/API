import requests

print('*-* GitHub Users *-*')

username = input('Usuario: ')

url= f'https://api.github.com/users/{username}'

response = requests.get(url)
data = response.json()


if response.status_code == 200:
    print(f'Nome: {data["name"]}')
    print(f'Empresa: {data["company"]}')
    print(f'Localização: {data["location"]}')
    print(f'Seguidores: {data["followers"]}')
    print(f'Seguindo: {data["following"]}')
    print(f'Repositórios: {data["public_repos"]}')

else:
    print('Usuário não encontrado.')


