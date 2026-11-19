import subprocess


def menu_medusa():
    print("[*] Medusa (Força Bruta) [*]")
    alvo = input("Digite o IP do alvo (ex: 192.168.1.10)\n").strip()


    if not alvo:
        print("[!] Erro, Alvo incorreto")
        return

    print("[?] Como você quer testar o usuário [?]")
    print("1 - Usuário específico")
    print("2 - Brute com wordlist padrão")
    print("3 - Brute com wordlist específica")

    opcao_usuario = input("[?] Opção [?] \n").strip()
    wordlist_padrao_User = "Wordlists/Username/Users.txt"
    wordlist_padrao_Password = "Wordlists/Username/Passwords.txt"


    if opcao_usuario == "1":
        usuario = input("Digite o nome de usuário\n")
        flag_usuario = "-u"

    elif opcao_usuario == "2":
        usuario = wordlist_padrao_User
        flag_usuario = "-U"

    elif opcao_usuario == "3":
        usuario = input("Digite o caminho da sua wordlist\n").strip()
        flag_usuario = "-U"

    else:
        print("[!] Opção inválida [!]")
        return

    print("[?] Como você quer testar a senha [?]")
    print("1 - Senha específica")
    print("2 - Brute com wordlist padrão")
    print("3 - Brute com wordlist específica")

    opcao_senha = input("[?] Opção [?]\n").strip()

    if opcao_senha == "1":
        senha = input("Digite a senha\n")
        flag_senha = "-p"

    elif opcao_senha == "2":
        senha = wordlist_padrao_Password
        flag_senha = "-P"

    elif opcao_senha == "3":
        senha = input("Digite o caminho da wordlist").strip()
        flag_senha = "-P"

    else:
            print("[!] Opção inválida [!]")
            return

    print("[*] Escolha um protocolo [*]")
    print("1 - SSH")
    print("2 - FTP")

    protocolo_input = input("[?] Opção [?]\n").strip()

    if protocolo_input == "1":
        protocolo = "ssh"

    elif protocolo_input == "2":
        protocolo = "ftp"

    else:
        print("[!] Opção inválida [!]")
        return

    comando = ["medusa", "-h", alvo, flag_usuario, usuario, flag_senha, senha, "-M", protocolo]

    print(f"[*] Rodando {' '.join(comando)} [*]")

    try:
        subprocess.run(comando, check=True)

    except KeyboardInterrupt:
        print("[!] Ação interrompida pelo usuário [!]")

    except subprocess.CalledProcessError:
        print("[!] ERRO, Verifique se digitou o alvo correto [!]")

    input("[*] Aperte enter para voltar [*]")
    
    

        
def menu_hydra():
    print("[*] Hydra (Brute Force ) [*]")
    wordlist_padrao_User = "Wordlists/Username/Users.txt"
    wordlist_padrao_Password = "Wordlists/Username/Passwords.txt"
    


    alvo = input("Digite a URL ou IP do alvo\n").strip()

    if not alvo:
        print("[!] Alvo inválido [!]")
        return

    print("[?] Como vai ser o teste em usuário [?]")
    print("1 - Usuario específico")
    print("2 - Wordlist específica")
    print("3 - Wordlist padrão")

    escolha_usuario = input("[?] Opção [?]\n")

    if escolha_usuario == "1":
        usuario = input("Digite o usuário\n")
        flag_usuario = "-l"

    elif escolha_usuario == "2":
        usuario = input("Digite o caminho da wordlist\n").strip()
        flag_usuario = "-L"

    elif escolha_usuario == "3":
        usuario = wordlist_padrao_User
        flag_usuario = "-L"

    else:
        print("[!] Opção inválida [!]")
        return

    print("[?] Como vai ser o teste em senha [?]")
    print("1 - Senha específica")
    print("2 - Wordlist específica")
    print("3 - Wordlist padrão")

    escolha_senha = input("[?] Opção [?]\n").strip()

    if escolha_senha == "1":
        senha = input("Digite a senha\n")
        flag_senha = "-p"

    elif escolha_senha == "2":
        senha = input("Digite o caminho da wordlist\n").strip()
        flag_senha = "-P"

    elif escolha_senha == "3":
        senha = wordlist_padrao_Password
        flag_senha = "-P"

    else:
        print("[!] Opção inválida [!]")
        return

    print("[*] Escolha o protocolo [*]")
    print("1 - FTP")
    print("2 -  SSH")
    print("3 - MYSQL/MARIADB")

    protocolo_opcao = input("[?] Opção [?]").strip()

    if protocolo_opcao == "1":
        protocolo = "ftp"

    elif protocolo_opcao == "2":
        protocolo = "ssh"

    elif protocolo_opcao == "3":
        protocolo = "mysql"

    else:
        print("[!] Opção inválida [!]")
        return

    comando = ["hydra", flag_usuario, usuario, flag_senha, senha, alvo, protocolo, "-f", "-V"]

    try:
        subprocess.run(comando, check=True)

    except KeyboardInterrupt:
        print("[!] Ação interrompida pelo usuário [!]")

    except subprocess.CalledProcessError:
        print("[!] Erro, Verifique a URL/IP [!]")
    input("Pressione enter para voltar")







    
def menu_hashcat():
    print("[*] Hashcat (Quebra de hashes) [*]")

    caminho_hash_padrao = "Hashes/teste.txt"

    wordlist_input = input("Digite o caminho wordlist ou enter para a padrão\n")
    
    if not wordlist_input:
            wordlist_input = "Wordlists/Username/Passwords.txt"

    print("[*] Escolha o caminho do hash [*]")
    print("1 - Caminho aonde esta o hash de teste (Hash padrão da ferramenta)")
    print("2 - Caminho específico")

    escolha_hash = input("[?] Opção [?]\n").strip()

    if escolha_hash == "1":
        caminho_hash = caminho_hash_padrao

    elif escolha_hash == "2":
        caminho_hash = input("Digite o caminho\n").strip()

    else:
        print("[!] Opção inválida [!]")
        return

    print("Escolha o tipo de hash")
    print("1 - MD5")
    print("2 - SHA1")
    print("3 - SHA256")
    print("4 - NTLM (Windows)")

    opcao_hash = input("[?] Opção [?]\n").strip()

    if opcao_hash == "1":
        tipo_hash = "0"

    elif opcao_hash == "2":
        tipo_hash = "100"

    elif opcao_hash == "3":
        tipo_hash = "1400"

    elif opcao_hash == "4":
        tipo_hash = "1000"

    else:
        print("[!] Opção inválida [!]")
        return

    comando = ["hashcat", "-a", "0", "-m", tipo_hash, caminho_hash, wordlist_input, "--potfile-disable", "-o", "senha_quebrada.txt"]

    try:
        subprocess.run(comando, check=True)

    except KeyboardInterrupt:
        print("[!] Erro, ação interrompida pelo usuário")

    except subprocess.CalledProcessError:
        print("[!] Erro, Senha não encontrada [!]")
    input("[*] Aperte enter para voltar [*]")









def menu_brute():
    while True:
        subprocess.run(["clear"])

        print("\n=== Módulo de senha e brute force ===\n")

        print("1 - Medusa (Forca bruta de senhas)")
        print("2 - Hydra (Força bruta)")
        print("3 - Hash cat (Quebra de Hashs)")
        print("0 - Voltar ao menu inicial")

        escolha = input("[?] Opção [?]\n")

        if escolha == "1":
            menu_medusa()

        elif escolha == "2":
            menu_hydra()
            
        
        elif escolha == "3":
            menu_hashcat()

        elif escolha == "0":
            return
        
        else:
            print("[!] Opção inválida [!]")
            return
        
        