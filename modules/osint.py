import subprocess
import os #<-- Para Criar pastas e etc...

def menu_whois():
    print("\n--- WHOIS: Consulta de Domínio ---")
    dominio = input("Digite o domínio (ex: google.com): ").strip() #<-- .strip e para remover espaço
    if not dominio:
        print("[!] Dominio invalido. [!]")
        return
    
    print("\n Escolha o tipo de consulta")
    print("1 - Basico")
    print("2 - Detalhado (-B: tentar expor e-mails)")

    tipo = input("Opção: ")
    if tipo == "1":
        comando = ["whois", dominio]
    elif tipo == "2":
        comando = ["whois", "-B", dominio]
    else:
        print("[!] Opção inválida [!]")
        return


    
    print(f"\n[*] Executando WHOIS em {dominio} [*]")
    subprocess.run(comando)
    input("\nPressione Enter para voltar...")


def menu_recon():
    print("\n--- DNSRECON: Enumeracao de DNS ---")
    dominio = input("Digite o Domínio (ex: google.com)\n").strip()
    if not dominio:
        print("[!] Domínio inválido [!]")
        return

    print("\n Escolha o seu tipo de scan: ")
    print("1 - Scan Padrão (A, NS, MX, etc)")
    print("2 - Transferência de Zona (AXFR)")
    print("[*] 3 - Scan Padrão (A, NS, MX, etc) COM UV [*]")
    print("[*] 4 - Transferência de Zona (AXFR) COM UV [*]")
    tipo = input("[?] Opcao [?]\n")
    if tipo == "1":
        comando = ["dnsrecon", "-d", dominio]
    elif tipo == "2":
        comando = ["dnsrecon", "-d", dominio, "-t", "axfr"]

    elif tipo == "3":
        comando = ["uv", "run", "dnsrecon", "-d", dominio]

    elif tipo == "4":
        comando = ["uv", "run", "dnsrecon", "-d", dominio, "-t", "axfr"]

    else:
        print("[!] Opção inválida [!]")
        return

    print("\n[*] Configuração de threads [*]")
    print("\n[*] Padrão é 10, quanto maior o valor, mais barulho faz [*] ")
    threads_input = input("Adcione um valor\n").strip()

    if not threads_input:
        threads = "10"
    elif threads_input.isdigit(): # <-- isdigit verefica se o valor inserido e de 0 a 9 em numeros inteiros
        threads = threads_input
    else:
        print("[!] Adcione um numero de valor inteiro [!]")
        return

    comando.extend(["--threads", threads])


    
    print(f"\n[*] Executando DNSRecon em {dominio} com {threads} threads [*]\n")
    
    pasta_dnsrecon = os.path.expanduser("~/Documents/dnsrecon")
    
    if tipo in ["3", "4"]:
        try:
            subprocess.run(comando, cwd=pasta_dnsrecon, check=True)
        except FileNotFoundError:
            print("\n[!] ERRO: O comando 'uv' ou a pasta do DNSRecon nao foi encontrado. [!]")
        except subprocess.CalledProcessError:
            print("\n[!] ERRO: O DNSRecon falhou ao executar. [!]")
        except KeyboardInterrupt:
            print("\n[!] Ação interrompida pelo User [!]")
            
    else:
        try:
            subprocess.run(comando, check=True)
        except FileNotFoundError:
            print("\n[!] ERRO: O comando 'dnsrecon' nao esta instalado no sistema (apt). [!]")
        except subprocess.CalledProcessError:
            print("\n[!] ERRO: O DNSRecon falhou ao executar. [!]")
        except KeyboardInterrupt:
            print("\n[!] Ação interrompida pelo User [!]")

    input("\nPressione Enter para voltar...")


    

def menu_osint():
    while True:
        subprocess.run(["clear"])
        print("\n=== MODULO OSINT (Reconhecimento Passivo) ===")
        print("1 - Whois (Dados de registro do dominio)")
        print("2 - DNS RECON (enumeração de dns)")
        print("0 - Voltar ao menu principal")
        
        escolha = input("\nEscolha uma ferramenta:\n ")

        if escolha == "1":
            menu_whois()
        elif escolha == "2":
            menu_recon() 

        elif escolha == "0":
            return # <-- Sai do loop e volta pro menu principal
        else:
            print("Opcao invalida.")