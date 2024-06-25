import datetime
import calendar
import os

hoje = datetime.datetime.today() #usa o datetime para atribuir today a hoje.
ano_atual = hoje.year  #usa o novo 'hoje' para pegar o year e o month atribuir ao ano atual e mes atual
mes_atual = hoje.month


def exibirHoras():
    hora_atual = datetime.datetime.now()
    print (f"Horário: {hora_atual.hour:02}:{hora_atual.minute:02}") #hora atual com format 2 digitos

def exibirCalendario(ano, mes):
    print(calendar.month(ano, mes))

def proximoMes(ano, mes):
    if mes == 12:
        return ano + 1, 1
    else:
        return ano, mes + 1

def mesAnterior(ano, mes):
    if mes == 1:
        return ano - 1, 12
    else:
        return ano, mes - 1
    
def limpaMes(): 
    os.system('cls')
    
    
while True:
    exibirCalendario(ano_atual, mes_atual)
    exibirHoras()
    comando = str(input("\nDigite 'a' para ver o mês anterior, e 'd' para o próximo mês, ou 's' para sair:\n\n"))

    if comando == 'a':
        ano_atual, mes_atual = mesAnterior(ano_atual, mes_atual)
        limpaMes() #limpa o console para exibir o proximo mes
        
    elif comando == 'd':
        ano_atual, mes_atual = proximoMes(ano_atual, mes_atual)
        limpaMes()
        
    elif comando == 's':
        break
        limpaMes()
    else:
        limpaMes()
        print('comando inválido.')
        
        