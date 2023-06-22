from Professional import Professional
from Visit import Visit
from Visitor import Visitor
from datetime import datetime
import json

professionals = []
visitors = []
visits = {}

def menu():
    while True:
        choice = str(input("""
======================
        MENU
======================
1- Cadastrar Profissional
2- Cadastrar Visitante
3- Localizar Profissional
4- Registrar Visita
5- Relatório de Conferência
6- Gerar arquivo de Registros do dia
7- Ler arquivos profissionais / visitantes
Escolha: """))
        if choice == "1":
            choiceOne()
        elif choice == "2":
            choiceTwo()
        elif choice == "3":
            choiceThree()
        elif choice == "4":
            choiceFour()
        elif choice == "5":
            choiceFive()
        elif choice == "6":
            choiveSix()
        elif choice == "7":
            choiceSeven()
        else:
            break


def choiceOne():
    professional = Professional()
    professional.name = str(input("Qual o nome do profissional? ")).strip()
    professional.specialty = str(input(f"Qual a especialidade de {professional.name}? ")).strip()
    professional.office = str(input("Qual o número da sala? "))
    professionals.append(professional)
    print("Profissional salvo com sucesso")


def choiceTwo():
    visitor = Visitor()
    visitor.name = str(input("Qual o nome do visitante? "))
    visitor.document = str(input(f"Qual o documento de {visitor.name}? "))
    visitors.append(visitor)
    print("Visitante salvo com sucesso")


def choiceThree():
    choice = str(input("Deseja localizar o profissional por seu nome ou sua profissão? 1 profissão e 2 para nome: "))
    if choice == "1":
        searchProfessionalBySpecialty()
    else:
        searchProfessionalByName()


def choiceFour():
    professional = chooseProfessionalByIndex()
    visitor = chooseVisitorByIndex()
    time = getDate()
    if professional is not None and visitor is not None:
        visits[visitor] = {
            "professionalName": professional.name,
            "time": time,
            "office": professional.office
        }


def choiceFive():
    professionalVisitors = []
    professional = chooseProfessionalByIndex()
    if professional is not None:
        for key, value in visits.items():
            if value["office"] == professional.office:
                visit = Visit()
                visit.time = value["time"]
                visit.professional = professional
                visit.visitor = key
                professionalVisitors.append(visit)
        print(f"Visitantes de {professional.name}:")
    for professionalVisitor in professionalVisitors:
        print(str(professionalVisitor))


def choiveSix():
    saveFile()

def choiceSeven():
    readProfessionalsFile()
    readVisitorsFile()
    print("Profissionais:")
    for professional in professionals:
        print(str(professional))
    print("Visitantes:")
    for visitor in visitors:
        print(str(visitor))

def searchProfessionalByName():
    typedName = str(input("Digite o nome do profissional: ")).strip()
    professionalFound = "Profissional não encontrado"
    for professional in professionals:
        if professional.name == typedName:
            professionalFound = professional
    print(str(professionalFound))


def searchProfessionalBySpecialty():
    typedSpecialty = str(input("Digite a especialidade do profissional: ")).strip()
    professionalsFound = []
    for professional in professionals:
        if professional.specialty == typedSpecialty:
            professionalsFound.append(professional)
    for professionalFound in professionalsFound:
        print(str(professionalFound))


def chooseProfessionalByIndex():
    chosenProfessional = None
    for index, professional in enumerate(professionals):
        numberList = index + 1
        print(f"{str(numberList)} - {professional.name}")
    choice = int(input("Escolha o profissional (digite apenas o número): "))
    maximumIndex = len(professionals)-1
    newIndex = choice-1
    if newIndex <= maximumIndex:
        chosenProfessional = professionals[newIndex]
    return chosenProfessional


def chooseVisitorByIndex():
    chosenVisitor = None
    for index, visitor in enumerate(visitors):
        numberList = index + 1
        print(f"{str(numberList)} - {visitor.name}")
    choice = int(input("Escolha o visitante (digite apenas o número): "))
    maximumIndex = len(visitors)-1
    newIndex = choice-1
    if newIndex <= maximumIndex:
        chosenVisitor = visitors[newIndex]
    return chosenVisitor


def getDate():
    return datetime.now().strftime('%H:%M')


def saveFile():
    fileName = "visits.json"
    dict = convertDictionary()
    with open(fileName, 'w') as file:
        json.dump(dict, file, indent=4, separators=(", ", ": "))
    print("Arquivo criado com sucesso!")

def convertDictionary():
    dict = {}
    for visitor, value in visits.items():
        dict[visitor.document] = {
            'professional': value["professionalName"],
            'time': value["time"],
            'office': value["office"]
        }
    return dict

def readProfessionalsFile():
    with open("professionals.txt", encoding="utf-8") as file:
        for line in file:
            lineList = line.split(":")
            professional = Professional()
            professional.name = lineList[0]
            professional.specialty = lineList[1]
            professional.office = lineList[2]
            professionals.append(professional)

def readVisitorsFile():
     with open("visitors.txt", encoding="utf-8") as file:
        for line in file:
            lineList = line.split(":")
            visitor = Visitor()
            visitor.name = lineList[0]
            visitor.document = lineList[1]
            visitors.append(visitor)


menu()
