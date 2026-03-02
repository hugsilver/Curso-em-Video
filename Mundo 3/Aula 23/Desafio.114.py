#Trabalhando
import webbrowser
import requests

def abrir_site(url):
    try:
        # Abre em uma nova aba do navegador padrão
        # webbrowser.open_new_tab(url)
        resposta = requests.head(url, timeout=5)  # HEAD é mais rápido que GET
        # return 200 <= resposta.status_code < 400
    except requests.RequestException:
        print("O site Pudin não está acesivel no momento")
    else:
        print(f"Consegui acessar o site do Pudim")
    finally:
        print('Obrigado por usar nossos serviços.')

abrir_site('https://pudim.com.br')




