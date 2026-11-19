import subprocess

def menu_torbrowser():
    print("[*] Abrindo Tor browser [*] \n")
    try:
        subprocess.Popen(["torbrowser-launcher"])
    except Exception as e:
        print("[!] Falha ao Abrir o Tor [!]")
    input("\n[*] Pressione enter para voltar [*]\n")
        



def menu_curl():
    print("\n CURL Requisições web")
    url = input("Digite a URL:\n").strip()

    if not url:
        print("[!] URL inválida [!]")
        return

    print("Escolha uma ação\n")
    print("1 - Baixar HTML da página")
    print("2 - Ver apenas cabeçalhos (Headers)")
    print("3 - Fingir ser um navegador (User Agent)")

    opcao = input("Escolha uma opção\n")

    if opcao == "1":
        comando = ["curl", "-s", url]
    elif opcao == "2":
        comando = ["curl", "-s", "-I", url]
    elif opcao == "3":
       
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        comando = ["curl", "-s", "-A", user_agent, url]
    else:
        print("[!] Opção inválida [!]")
        return
    print(f"\n[*] Executando {' '.join(comando)} [*]")

    try:
        subprocess.run(comando)
    except subprocess.CalledProcessError:
        print("[!] Erro verifique a URL [!]")
    except KeyboardInterrupt:
        print("[!] Ação interrompida pelo usuário [!]")
    input("\nAperte enter para voltar")


def menu_fuzz():
    print("\n --- WFuzz (Web Fuzzer) --- ")
    print("[*] Coloque FUZZ na URL ainde você quer testar EX:(https://site.com/FUZZ) [*]")

    url = input("\n Digite a URL com FUZZ no final \n")

    if not url:
        print("[!] Digite uma URL [*]")
        return

    
    wordlist_padrao = "Wordlists/Web/common.wordlist"
    
    wordlist = input("Digite o caminho da wordlist ou aperte enter para a padrão \n").strip()

    if not wordlist:
        wordlist = wordlist_padrao

    print("[*] Escolha um filtro [*]")
    print("1 - Ocultar os 404 (Diretório não encontrado)")
    print("2 - Mostrar todas as respostas")
    opcao = input("\n[*] Opção [*]\n").strip()

    comando = ["wfuzz", "-w", wordlist, "-u", url]

    print(f"[*] Executando {' '.join(comando)} [*]")

    if opcao == "1":
        comando.extend(["--hc", "404"])
        

    elif opcao == "2":
        pass

    else:
        print("[!] ERRO, opção inválida [!]")
        return

    try:
        subprocess.run(comando, check=True)

    except KeyboardInterrupt:
        print("[!] Ação interrompida pelo usuário [!]")
    except subprocess.CalledProcessError:
        print("[!] Erro ao executar o Wfuzz  [!]")

    input("[*] Pressione enter para voltar [*]")


    

def menu_gobuster():
    print("[*] Gobuster [*]")
    url = input("Digite a url \n").strip()

    if not url:
        print("[!] URL inválida [!]")
        return

    wordlist_padrao = "Wordlists/Web/common.wordlist"

    wordlist = input("Digite o caminho da wordlist ou aperte enter para a padrão \n").strip()

    if not wordlist:
        wordlist = wordlist_padrao

    extensoes = input("Digite uma extensão (EX: .PHP .CSS ETC...) ou aperte enter para pular\n")

    threads_input = input("Digite o numero de threads, ou enter para escolher o padrão(10)\n").strip()

    if not threads_input or not threads_input.isdigit():
        threads = "10"

    else:
        threads = threads_input

    comando = ["gobuster", "dir", "-u", url, "-w", wordlist, "-t", threads]

    if extensoes:
        comando.extend(["-x", extensoes])
    print(f"[*] Executando {' '.join(comando)} [*]")

    try:
        subprocess.run(comando, check=True)

    except KeyboardInterrupt:
        print("[!] Comando interrompido pelo usuário [!]")

    except subprocess.CalledProcessError:
        print("[!] ERRO, verifique a URL [*]")

    input("[*] Pressione enter para voltar [*]")

    

def menu_sql():
    print("[*] SQLMAP (Injeção de sql) [*]")
    print("\n [*] Dica: A URL deve conter um parametro (ex: http://site.com/index.php?id=1) [*] \n")

    url = input("Digite a URL \n").strip()

    if not url:
        print("[!] Digite uma URL válida")
        return
    comando = ["sqlmap", "-u", url]

    risco_input = input("[?] Digite o nivel de risco (1 - 3, padrão = 1)[?]\n").strip()

    if risco_input in["1", "2", "3"]: # <-- Se risco inpute for 1 2 ou 3
        risco = risco_input # <-- risco recebe o input do usuario
    else: #<-- se não ele é 1
        risco = "1"


    level_input = input("[?] Digite o level desejado (1 -5, padrão = 1) [?]\n").strip()

    if level_input in ["1", "2", "3", "4", "5"]:
        level = level_input
    else:
        level = "1"

    print("[?] Oque deseja fazer [?]")
    print("1 - Testar se é vulneravel")
    print("2 - Listar os bancos de dados (--dbs)")
    print("3 - Listar as tabelas dos bancos de dados (--tables)")

    opcao = input("[?] Qual opção desejada [?]").strip()

    comando = ["sqlmap", "-u", url, f"--risk={risco}", f"--level={level}"]

    if opcao == "1":
        pass

    elif opcao == "2":
        comando.append("--dbs")

    elif opcao == "3":
        banco = input("Digite o nome do banco de dados \n").strip()
        if not banco:
            print("[!] É necessário o nome do banco de dados [!]")
            return
        comando.extend(["--D", banco, "--tables"])

    else:
        print("[!] Opção inválida [!]")
        return

    print(f"[*] Executando {' '.join(comando)} [*]")

    try:
        subprocess.run(comando)

    except KeyboardInterrupt:
        print("[!] Ação interrompida pelo usuário")

    except subprocess.CalledProcessError:
        print("[!] Erro, Verefique a URL")

    input("[*] Pressione enter para voltar [*]")








def menu_web():
    while True:
        subprocess.run(["clear"])
        print("\n=== Módulo de WEB ===")
        print("1 - Tor browser (Navegador para privacidade)")
        print("2 - CURL (Ferramenta para coleta de HTML)")
        print("3 - Fuzz (Teste de diretórios WEB)")
        print("4 - Gobuster (Teste de diretórios WEB com extensões)")
        print("5 - SqlMap (Injeção de SQL)")
        print("0 - Para voltar")



        escolha = input("Escolha uma opção \n")

        if escolha == "1":
            menu_torbrowser()

        elif escolha == "2":
            menu_curl()

        elif escolha == "3":
            menu_fuzz()

        elif escolha == "4":
            menu_gobuster()

        elif escolha == "5":
            menu_sql()

        elif escolha == "0":
            return
        else:
            print("[!] Opção inválida [!]")
            return

