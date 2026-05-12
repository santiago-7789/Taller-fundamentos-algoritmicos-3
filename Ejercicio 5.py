# Se pone la lista del ejercicio 1
nombres = ["Juan", "Santiago", "Alex", "Edwin", "David"] 
print("Vector original de nombres:", nombres)
# Para eliminar el tercer nombre se utliza len y if para establecer una condicion 
if len(nombres) >= 3:
    # Se elimina el tercer nombre
    del nombres[2] 
    # Se imprime el resultado
    print("Vector resultante:", nombres)



