import subprocess

def menu_cupp():

    print("[*] Executando Cupp [*]")

    comando = ["cupp", "-i"]

    try:
        subprocess.run(comando, check= True)
    except KeyboardInterrupt:
        print("[!] Erro, Ação interrompida pelo usuário [!]")

    input("[*] Aperte enter para voltar [*]")
        






def menu_crunch():
    print("[*] Executando Crunch [*]")
    print("[!] AVISO, Cuidado ao escolher o tamanho das wordlist e as opções, a ferramenta pode gerar wordlist de centenas de gigas [!]")
    print("[!] EXEMPLO: crunch 8 8  pode gerar 208.827.064.576 de senhas. Cada caractere a mais multiplica o tamanho por 26 [!]")
    print("[*] Escolha uma opção [*]")
    print("1 - Opção Normal (Só numeros)")
    print("2 - Opção com palavras e números (EX: Empresa@0000)")

    opcao_input = input("[?] Opção [?]\n")
    tamanho_min = input("[?] Tamanho Min [?]\n").strip()
    tamanho_max = input("[?] Tamanho Max [?]\n").strip()

    wordlist_input = input("Digite o caminho e o nome do arquivo (ex: Wordlists/lista.txt)\n").strip()

    if not wordlist_input:
        print("[!] É preciso do nome da wordlist para ser gerada [!]")
        return

    comando = ["crunch", tamanho_min, tamanho_max]

    if opcao_input == "1":
        comando.append("0123456789")

    elif opcao_input == "2":
        print("[*] Símbolos curingas: @ = letras minúsculas, % = números.")
        print("[*] Exemplo: Empresa@%%%% gerará Empresa@0000 até Empresa@9999")
        print("[*] Exemplo 2: Admin@@%% gerará Adminaa00 até Adminzz99")

        padrao_input = input("Digite o padrãon\n").strip()

        if not padrao_input:
            print("[!] É preciso de um padrão [!]")
            return
    comando.extend(["-o", wordlist_input])

    try:
            subprocess.run(comando, check=True)

    except KeyboardInterrupt:
            print("[!] Ação interrompida pelo usuário [!]")

    except subprocess.CalledProcessError:
            print("[!] Erro ao executar o crinch, verifique os parâmetros [!]")

    input("[*] Aperte enter para voltar [*]")
         










def menu_wordlists():
    while True:
          
        subprocess.run(["clear"])
        print("[*] Menu Wordlists [*]")
        print("1 - cupp (Geração de wordlists comuns)")
        print("2 - Crunch (Geração de wordlist padrão)")
        print("0 - Voltar")

        escolha = input("[?] Opção [?]\n")

        if escolha == "1":
            menu_cupp()

        elif escolha == "2":
            menu_crunch()

        elif escolha == "0":
            return