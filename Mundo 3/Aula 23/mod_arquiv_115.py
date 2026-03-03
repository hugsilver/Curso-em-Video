import os

def cv_arq(base_dir: str, nome_arquivo="dados_clientes.txt"):
    os.system("cls")
    pasta = os.path.dirname(os.path.abspath(base_dir))
    caminho = os.path.join(pasta, nome_arquivo)

    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            #f.write('')
            pass
        #print(f"✅ Criado em: {caminho}")
        return caminho
    else:
        try:
            os.system("cls")
            with open(caminho, "r", encoding="utf-8", errors="ignore") as f:
                conteudo = f.read().strip()
            if conteudo:
                print('Dados: ')
                print(conteudo)
            else:
                print('Base sem dados!!!')
                return caminho
        except FileNotFoundError:
            print('Arquivo não existente!!!')
    return caminho  
  

