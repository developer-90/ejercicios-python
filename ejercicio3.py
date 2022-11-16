#Se pide calcular la nota de tu examen tipo test.
#Serán 20 preguntas
#Las preguntas correctas sumarán 0,5
#Las preguntas incorrectas restarán 0,25
#Las preguntas sin contestar tendrán 0

#datos entrada
preguntasAcertada = 13
preguntasFalladas = 5
preguntasSinContestar = 2

# procedimiento
totalAcertadas = preguntasAcertada*0.5
totalFalladas = preguntasFalladas*0.25
total = totalAcertadas-totalFalladas

# datos salida
print(f'La nota es {total}')