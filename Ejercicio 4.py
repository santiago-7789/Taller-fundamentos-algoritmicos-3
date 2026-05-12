# Inicializamos el vector vacio
edades = []
# utilizamos for en un rango de 5 edades
for i in range(5):
    # Le pedimos al usuario que ingrese las edades
    edad = int(input(f"ingresa la edad {i+1}: "))
    # Se envia cada edad al final de la lista/vector
    edades.append(edad)
    # Ciclo for y if para imrprimir edades mayores o iguales a 18
    for edad in edades:
        if edad>=18:
            print(edad)

