import requests # Acessa a api
import textwrap # Edição de texto

def busca_cep(cep):
    formato = "json"
    # site: https://docs.awesomeapi.com.br/
    # API que faz a busca do endereço pelo cep
    link = (f"https://cep.awesomeapi.com.br/{formato}/{cep}")
    requisicao = requests.get(link)

    # Verificador - Se o retorno for True ou False
    if requisicao.status_code == 200: # 200 - é um código de requisições padrão da internet que retorna True
        endereco = (requisicao.json())
        return endereco
    else: # 400/404 - Código de Erro web padrão da internet que retorna False
        print("@@@ ERRO: CEP não aceito @@@")
        return False

def formata_endereco(endereco):
    # Formata o endereço de maneira legível
    linhas = [
        f"CEP: {endereco.get('cep', 'N/A')}",
        f"Tipo de Logradouro: {endereco.get('address_type', 'N/A')}",
        f"Nome do Logradouro: {endereco.get('address_name', 'N/A')}",
        f"="*25,
        f"Logradouro: {endereco.get('address', 'N/A')}",
        f"Bairro: {endereco.get('district', 'N/A')}",
        f"Cidade: {endereco.get('city', 'N/A')}",
        f"Estado: {endereco.get('state', 'N/A')}",
        f"="*25,
        f"Latitude: {endereco.get('lat', 'N/A')}",
        f"Longitude: {endereco.get('lng', 'N/A')}",
        f"DDD: {endereco.get('ddd', 'N/A')}",
        f"="*40,
    ]

    # Use textwrap para garantir que as linhas não fiquem muito longas
    texto_formatado = '\n'.join(textwrap.fill(linha, width=70) for linha in linhas)
    return texto_formatado

def main():
    while True:
        cep = input("Digite um CEP para buscar o endereço (0 para sair): ")
        if cep == "0":
            print("Saindo do Programa!")
            break
        endereco_final = busca_cep(cep)
        if endereco_final:
            print("Procurando Endereço....")
            print(formata_endereco(endereco_final))

main()