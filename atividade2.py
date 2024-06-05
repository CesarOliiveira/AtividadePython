import math

teste = False

votos = {"Windows Server": 0,
         "Unix": 0,
         "Unbutu Server": 0,
         "Red Hat Enterprise Linux (RHEL)": 0,
         "Solaris": 0,
         "Outro": 0
         }

def calcularPorcentagem(sistema):
    totalDeVotos = votos["Windows Server"] + votos["Unix"] + votos["Unbutu Server"] + votos["Red Hat Enterprise Linux (RHEL)"] + votos["Solaris"] + votos["Outro"]

    if votos[sistema] == 0:
        return 0
    elif votos[sistema] >= 0:
        porcentagem = (votos[sistema] / totalDeVotos) * 100

        duasCasasDepoisVirgula = str(round(porcentagem, 2))

        numeroDepoisVirgula = duasCasasDepoisVirgula.split(".")

        if int(numeroDepoisVirgula[1]) >= 60:
            return math.ceil(porcentagem)
        else:
            return math.floor(porcentagem)

def maisVotado():
    maiorPorcentagem = 0
    sistema = ""

    for i in votos:
        if votos[i] > maiorPorcentagem:
            maiorPorcentagem = votos[i]
            sistema = i

    if maiorPorcentagem == 0:
        return "N/A"

    return sistema


def totalVotos():
    total = votos["Windows Server"] + votos["Unix"] + votos["Red Hat Enterprise Linux (RHEL)"] + votos["Solaris"] + votos["Unbutu Server"] + votos["Outro"]

    return total

while teste == False:

    print("Qual o melhor Sistema Operacional para uso em servidores?\n" 
          "0 - Sair\n" 
          "1 - Windows Server 2022\n"
          "2 - Unix\n"
          "3 - Red Hat Enterprise Linux (RHEL)\n"
          "4 - Solaris\n"
          "5 - Unbutu Server OS\n"
          "6 - Outro\n")
    sistema = int(input("Digite o número da sua escolha: "))

    match sistema:
        case 0:
            teste = True
        case 1:
            votos["Windows Server"] = votos["Windows Server"] + 1
            print("1 voto computado para Windows Server 2022")
        case 2:
            votos["Unix"] = votos["Unix"] + 1
            print("1 voto computado para Unix")
        case 3:
            votos["Unbutu Server"] = votos["Unbutu Server"] + 1
            print("1 voto computado para Unbuntu Server")
        case 4:
            votos["Red Hat Enterprise Linux (RHEL)"] = votos["Red Hat Enterprise Linux (RHEL)"] + 1
            print("1 voto computado para Red Hat Enterprise Linux (RHEL)")
        case 5:
            votos["Solaris"] = votos["Solaris"] + 1
            print("1 voto computado para Solaris")
        case 6:
            votos["Outro"] = votos["Outro"] + 1
            print("1 voto computado para Outro")


print("Sistema Operacionais - Votos % \n"
             f'Windows Server 2022 - {votos["Windows Server"]} {calcularPorcentagem("Windows Server")}% \n'
             f'Unix - {votos["Unix"]} {calcularPorcentagem("Unix")}%\n'
             f'Red Hat Enterprise Linux (RHEL) - {votos["Red Hat Enterprise Linux (RHEL)"]} {calcularPorcentagem("Red Hat Enterprise Linux (RHEL)")}%\n'
             f'Solaris - {votos["Solaris"]} {calcularPorcentagem("Solaris")}%\n'
             f'Unbutu Server OS - {votos["Unbutu Server"]} {calcularPorcentagem("Unbutu Server")}%\n'
             f'Outro - {votos["Outro"]} {calcularPorcentagem("Outro")}%\n'
             f'Total de {totalVotos()}\n'
             )

if maisVotado() == "N/A":
    print('Ninguem votou.')
else:
    print(f'O Sistema Operacional mais votado foi o {maisVotado()}, com {votos[maisVotado()]}, correspondendo a {calcularPorcentagem(maisVotado())}% dos votos\n')