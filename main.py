import requests


def main():
    print('####################')
    print('### consulta cep ###')
    print('####################')

    cep_input = input('digite o CEP para a consulta: ')

    if len(cep_input) != 8:
        print('quantidade de digitos invalido')
        exit()

    request = requests.get(
        'https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('===> CEP ENCONTRADO <==')

        print('CEP: {}'.format(address_data['cep']))
        print('LOGRADOURO: {}'.format(address_data['logradouro']))
        print('COMPLEMENTO: {}'.format(address_data['complemento']))
        print('BAIRRO: {}'.format(address_data['bairro']))
        print('LOCALIDADE: {}'.format(address_data['localidade']))
        print('UF: {}'.format(address_data['uf']))
        print('IBGE: {}'.format(address_data['ibge']))
        print('DDD: {}'.format(address_data['ddd']))
        # print(request.json())
    else:
        print('{}: CEP invalido.'.format(cep_input))

    option = int(
        input('deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()


if __name__ == '__main__':
    main()
