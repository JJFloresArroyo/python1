
#Crear e imprimir un diccionario:

Diccionario = {
  "Marca": "Ford",
  "ModelO": "Mustang",
  "Año": 1964
}
print(Diccionario)

'''
#Imprime el valor de "marca" del diccionario:

Diccionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
}
print(Diccionario["Marca"])

#Los valores duplicados sobrescribirán los valores existentes:siendo el
#ultimo el que sustituya a sus anteriores

Diccionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964,
  "Año": 2020
}
print(Diccionario)

'''
'''
#Longitud del diccionario
#Para determinar cuántos elementos tiene un diccionario, use la función len():

#Ejemplo
#Imprime el número de elementos en el diccionario:


print(len(Diccionario))
'''
'''
#[11:47 a. m., 1/7/2022] Marco Programación: Tipos de datos de cadena, int, booleanos y de lista:

Diccionario = {
  "Marca": "Ford",
  "Electrico": False,
  "Año": 1964,
  "Color": ["Rojo", "Blanco", "Azul"]
}
#[11:48 a. m., 1/7/2022] Marco Programación: Imprime el tipo de datos de un diccionario:

Diccionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
}
print(type(Diccionario))
''''''
Acceso a elementos
Puede acceder a los elementos de un diccionario haciendo referencia a su nombre clave, entre corchetes:

Ejemplo
Obtenga el valor de la clave "modelo":

Diccionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
}
#x = Diccionario["Modelo"]
#x = Diccionario.get("Modelo")
x = Diccionario.values()
print(x)

Adición de elementos
La adición de un elemento al diccionario se realiza utilizando una nueva clave de índice y asignándole un valor:

Ejemplo
'''
'''
Diccionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
}
Diccionario["Color"] = "Rojo"
print(Diccionario)
'''
#El pop()método elimina el elemento con el nombre de clave especificado:

Diccionario = {
  "Marca": "Ford",
  "Modelo": "Mustang",
  "Año": 1964
}
Diccionario.pop("Modelo")
print(Diccionario)







