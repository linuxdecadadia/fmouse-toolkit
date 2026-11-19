import subprocess

def menu_photorec():
    print("[*] Abrindo o PHOTOREC [*]")

    try:
        subprocess.run("photorec", check=True)

    except KeyboardInterrupt:
        print("[!] Ação cancelada pelo usuário [!]")
    input("[*] Aperte enter para voltar [*]")




def menu_steghide():
    print("[*] Steghide (Esteganografia) [*]")
    print("Escolha uma opção")
    print("1 - Esconder arquivo em imagem/audio")
    print("2 - Extrair arquivo de imagem/audio")
    print("3 - Ver informação de imagem/audio ")

    opcao = input("[?] Opção [?]\n")

    if opcao == "1":
        arquivo_principal = input("Diretório do arquivo e o arquivo que voce vai esconder os arquivos nele\n").strip()

        if not arquivo_principal:
            print("[!] ERRO, é necessário um arquivo [!]")
            return

        esconder_arquivo = input("Digite o diretório com o arquivo que irá ser escondido\n").strip()

        if not esconder_arquivo:
            print("[!] ERRO, é necessário um arquivo [!]")
            return
        senha = input("Digite a senha\n")
        comando = ["steghide", "embed", "-cf", arquivo_principal, "-ef", esconder_arquivo, "-f"]

        if senha:
            comando.extend(["-p", senha])


    elif opcao == "2":
        arquivo_escondido = input("Difite o caminho do arquivo escondido\n").strip()

        if not arquivo_escondido:
            print("[!] ERRO, é necessário um arquivo")
            return

        senha = input("Digite a senha ou enter para arquivo sem senha\n")
        comando = ["steghide", "extract", "-sf", arquivo_escondido, "-f"]

        if senha:
            comando.extend(["-p", senha])


    elif opcao == "3":
        analisar_arquivo = input("Digite o diretório do arquivo a ser analisado\n").strip()

        if not analisar_arquivo:
            print("[!] ERRO, é necessário um arquivo")
            return

        comando = ["steghide", "info", analisar_arquivo]
    else:
        print("[!] ERRO, opção inválida [!]")
        return

    try:
        subprocess.run(comando, check=True)

    except KeyboardInterrupt:
        print("[!] Ação interrompida pelo usuário [!]")

    except subprocess.CalledProcessError:
        print("[!] ERRO, Verifique o caminho, senha ou o formato [!]")

    input("[*] Aperte enter para voltar [*]")

    

    






def menu_forense():
    while True:
        subprocess.run(["clear"])
        print("[*] Escolha uma opção [*]")
        print("1 - photorec (Recuperação de dados do armazenamento (HD / SSD))")
        print("2 - Steghide (Esconder arquivos em fotos e abrir fotos)")
        print("0 - Voltar ao início")

        escolha = input("[?] Opção [?]\n")

        if escolha == "1":
            menu_photorec()

        elif escolha == "2":
            menu_steghide()

        elif escolha == "0":
            return


        