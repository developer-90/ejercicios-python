#La nota del trimestre está basada en
#Nota hito individual = 30 %
#Nota hito grupal = 20 %
#Nota examen = 50 %

#datos de entrada
notaIndividual = float(input('Nota hito invidual: '))
notaGrupal = float(input('Nota hito grupal: '))
notaExamen = float(input('Nota examen: '))

#procedimiento
totalIndividual = notaIndividual * 0.3
totalGrupal = notaGrupal * 0.2
totalExamen = notaExamen * 0.5
totalTrimestre = totalIndividual + totalGrupal + totalExamen

#salida
print(f'Tu nota es {totalTrimestre}')
