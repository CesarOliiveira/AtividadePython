def crime(quest1, quest2, quest3, quest4, quest5):
    if quest1 == "1" and quest2 == "1":
        return "Suspeita"
    elif quest3 == "1" or quest4 == "1":
        return "Cúmplice"
    elif quest5 == "1":
        return "Assassino"
    else:
        return "Inocente"

print("Digite 0 para (Não) e 1 para (Sim)")
quest1 = input("Você telefonou para vítima?\n")
quest2 = input("Você esteve no local do crime?\n")
quest3 = input("Você mora perto da vítima?\n")
quest4 = input("Você tinha dívidas com a vítima?\n")
quest5 = input("Você Já trabalhou com a vítima?\n")


print(crime(quest1, quest2, quest3, quest4, quest5))

