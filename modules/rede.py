import subprocess

def menu_nmap():
    print("\nNmap escaneamento de rede")
    alvo = input("Digite o IP do Alvo\n").strip()
    if not alvo:
        print("[!] Alvo inválido [!]")
        return

    print("\n Escolha o tipo de scan")
    print("1 - Scan rápido")
    print("2 - Scan de versão -sV")
    print("3 - Scan de ping (-sn descobrir hosts vivos)")
    print("4 - Scan furtivo -sS")

    tipo = input("[?] Opção [?]")

    if tipo == "1":
        comando = ["nmap", alvo]
    elif tipo == "2":
        comando = ["nmap", "-sV", alvo]
    elif tipo == "3":
        comando = ["nmap", "-sn", alvo]
    elif tipo == "4":
        comando = ["nmap", "-sS", alvo]
    else:
        print("[!] Opção inválida [!]")

    print("[*] Configuração de velocidade -T [*]\n")
    print("[*] 0 = Lento/Silencioso | 3 = Padrão | 5 = Rápido/Barulhento [*]")
    tempo_input = input("[?] Digite a velocidade [?]\n").strip()
    if not tempo_input:
        tempo = "3"
    elif tempo_input.isdigit() and int(tempo_input) <= 5:
        tempo = tempo_input
    else:
        print("[!] Valor inválido use de 0 a 5 [!]")
        return
    comando.extend([f"-T{tempo}"])

    print("\n[?] Deseja tentar detectar o Sistema Operacional? (-O) [?]\n")
    os_input = input("[?] Adcionar -O [?] \n").strip().lower()
    if os_input == "s":
        comando.append("-O")


    print(f"[*] Executando NMAP em {alvo} e tempo {tempo} [*]")
    subprocess.run(comando)
    input("Pressione enter para voltar")


def menu_dump():
    print("\n TCPDUMP Sniffing de pacotes")
    interface = input("\n Digite a interface (ex: eth0, wlan0, ou 'any' para todas)\n").strip()

    if not interface:
        interface = "any"

    filtro = input("\n Digite o filtro desejado \n").strip()

    comando = ["sudo", "tcpdump", "-i", interface, "-n"]
    if filtro:
        comando.extend(filtro.split()) # <-- comando.extend (Joga oque o usuario esqueveu pro final do comando),
        #filtro.split (insere dados no filtro porém com split ele conta o espaço do usuario ou seja corta em pedaço o port 80 vira ["port", "80"])
    print(f"\n[*] Iniciando captura em {interface} [*]")
    try:
        subprocess.run(comando, check=True)
    
    except KeyboardInterrupt:
        print("[!] Captura interrompida pelo usuário [!]")

    except subprocess.CalledProcessError:
        print("[!] ERRO, verifique se a interface está correta [!]")
    
    input("[*] Aperte enter para voltar ao menu [*]")


def menu_wireshark():
    print("[*] Abrindo Wireshark [*]")


    try:
        subprocess.Popen(["sudo", "wireshark"])

    except Exception as e:
        print("[!] Falha ao abrir o Wireshark [!]")

    input("[*] Pressione enter para voltar [*]\n")


def menu_zenmap():
    print("[*] Abrindo o Zenmap [*]")

    try:
        subprocess.Popen(["sudo", "zenmap"])
    except Exception as e:
        print("[!] Erro ao abrir o Zenmap [!]")
    input("[*] Pressione enter para voltar [*]\n")


def menu_netcat():
    print("[*] Netcat (Canivete suíço de rede)[*]")
    print("\n [*] Escolha uma opção [*] \n")
    print("1 - Verificar se uma porta está aberta (-z)")
    print("2 - Modo verboso (-v)")
    print("3 - Abrir um listener (Modo de escuta)")

    opcao = input("[?] Opcao [?]\n").strip()

    if opcao == "1" or opcao == "2":
        alvo = input("Digite o IP/DOMÍNIO do alvo \n").strip()
        porta = input("Digite a porta do alvo \n").strip()

        if not alvo or not porta:
            print("[!] Alvo ou Porta incorreto [!]")
            return

        if opcao == "1":
            comando = ["nc", "-zv", alvo, porta]

        else:
            comando = ["nc", "-v", alvo, porta]


    elif opcao == "3":
        escuta_input = input("\n Digite uma porta para escutar \n")

        if not escuta_input.isdigit():
            print("[!] Porta inválida [!]")
            return
        comando = ["nc", "-lvp", escuta_input]
    else:
        print("[!] Opção inválida [!]")
        return
    print(f"\n[*] Escutando {' '.join(comando)} [*]") #< -- ' ' (Para dar espaço), o.join vai colocar o espaço entre cada item da lista que e o (comando)

    try:
        subprocess.run(comando, check=True)

    except KeyboardInterrupt:
        print("[!] Ação interrompida pelo usuário [!]")
    except Exception as e:
        print(f"[!] Erro ao executar o Netcat {e}[!]")
        
    input("[*] Pressione enter para voltar ao menu [*]")


        

def menu_rede():
    while True:
        subprocess.run(["clear"])
        print("=== MODULO DE REDE E SNIFFING ===")
        print("1 - Nmap (Scanner de portas e rede)")
        print("2 - Tcpdump (Sniffing de pacotes)")
        print("3 - Wireshark (Escaneamento de pacotes)")
        print("4 - Zenmap (Scanner de Portas e rede via interface gráfica (GUI))")
        print("5 - Netcat (Conexoes TCP/UDP)")
        print("0 - Voltar ao menu principal")

        escolha = input("\n Escolha uma ferramenta\n")

        if escolha == "1":
            menu_nmap()

        elif escolha == "2":
            menu_dump()

        elif escolha == "3":
            menu_wireshark()

        elif escolha == "4":
            menu_zenmap()

        elif escolha == "5":
            menu_netcat()
        
        elif escolha == "0":
            return
        else:
            print("[!] Opção inválida [!]")
            return
            


