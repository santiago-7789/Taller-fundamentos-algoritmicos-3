#   iniciamos el vector 
notas = []
print(" Ejercicio 2, notas ")
# ciclo for, con 7 elementos
for i in range(7):
    # Pedimos al usuario las notas
    nota = float(input( f"ingrese la nota {i+1}: "))
    # Se envian al final de la lista/vector
    notas.append(nota)

    
# declaramos la nota mayor y menor , mediante Max y min
nota_mayor = max(notas)
print (" La nota mayor es : ", nota_mayor)
nota_menor = min(notas)
print (" La nota menor es : ", nota_menor)

# Declaramos el promedio por medio de sum y len
prom = sum(notas)/len(notas)
print ("El promedio es igual a : ", prom)

