'''
Tempo de um Evento

No mês de maio você precisa precificar diversos casamentos. 
Como responsável contábil pela empresa de festas, 
cabe a você calcular a duração dos eventos de casamento para definir o valor a ser pago. 
É uma atividade de precisão, portanto é necessário estimar a duração 
considerando dias, horas, minutos e segundos.

Crie um programa que calcule a duração total de um evento sabendo o dia, hora, 
minutos e segundos para as datas inicial e final do mesmo.


Entrada
A primeira linha da entrada contém o dia que começa a festa de casamento, 
seguido de um espaço e do horário exato de início, 
composto por 3 valores inteiros separados por ':' no formato hh:mm:ss 
(horas, minutos e segundos, respectivamente). 
A linha seguinte apresenta, no mesmo formato, 
a informação da data e horários exatos do fim da festa.


Saída
A saída consiste na apresentação da duração do evento, em dias, horas, minutos, 
e segundos, nesta ordem, uma informação por linha. 
Para cada, indique também a unidade de tempo, conforme os exemplos.

Caso haja um erro e as informações fornecidas na entrada indiquem que o 
horário de término da festa não é após seu início, 
indique o erro com a mensagem " Data inválida!".

For example:

Input	
5 08:12:23
9 06:13:23

Result
3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)
'''

dateBegin, dateEnd = input(),input()

def unpack_dates(dateBegin,dateEnd):

    datesList = []

    for date in [dateBegin,dateEnd]:
        
        day,rest = date.split(' ')
        hours,minutes,seconds = rest.split(':')

        auxList = [day,hours,minutes,seconds]
        auxList = [int(x) for x in auxList]

        datesList.append(auxList)

    return datesList

def verify_unified():

    beginList,endList = unpack_dates(dateBegin,dateEnd)

    totalSecondsList = []

    for date in [beginList,endList]:

        for j in range(len(beginList)):

            if j == 0:
                totalSeconds = date[j]*24
            elif (j == 1) or (j == 2):
                totalSeconds = (totalSeconds + date[j])*60
            elif j == 3:
                totalSeconds += date[j]
            
        totalSecondsList.append(totalSeconds)

    totalDifference = totalSecondsList[1] - totalSecondsList[0]

    if totalDifference <= 0:
        print('Data inválida!')

    else:
        days,remainder = totalDifference//(24*60*60), totalDifference%(24*60*60) 
        hours,remainder = remainder//(60*60), remainder%(60*60)
        minutes,seconds = remainder//(60), remainder%(60)

        print(
        f'{days} dia(s)',
        f'{hours} hora(s)',
        f'{minutes} minuto(s)',
        f'{seconds} segundo(s)',
        sep="\n")

verify_unified()