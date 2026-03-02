
import webbrowser

def abrir_site(url: str):
    
    try:
        # Abre em uma nova aba do navegador padrão
        webbrowser.open_new_tab(url)
        print(f"Consegui acessar o site do Pudim")
    except:
        print("O site Pudin não está acesivel no momento")

if __name__ == "__main__":
    site = input('https://pudim.com.br/').strip()
    abrir_site(site)


