arquivos = open("palavras.txt","r")
for linha in arquivos:
    print(linha)
arquivos.close()