import json

def verificar_valores_unicos(json_data):
    # Convertir JSON a diccionario
    dict_data = json.loads(json_data)
    print(dict_data)
    # Crear un conjunto para almacenar valores únicos
    valores_unicos = set()
    otros_valores = set([1,2,3])
    # print(otros_valores)
    # Función auxiliar para verificar valores
    def verificar_valores(data):
        # Si es un diccionario, iterar por sus valores
        if isinstance(data, dict):
            for value in data.values():
                verificar_valores(value)
        # Si es una lista, iterar por sus elementos
        elif isinstance(data, list):
            for item in data:
                verificar_valores(item)
        # Si es un valor simple, verificar si está en el conjunto de valores únicos
        else:
            if data in valores_unicos:
                print(f"Valor repetido encontrado: {data}")
                # raise ValueError(f"Valor repetido encontrado: {data}")
            valores_unicos.add(data)
    
    # Verificar los valores del diccionario principal
    verificar_valores(dict_data)
    
    return dict_data

# Ejemplo de uso
json_data = '''
{
    "nombre": ["leer", "futbol", "ajedrez"],
    "edad": 30,
    "edad": 32,
    "empleado": true,
    "apellido":["leer", "futbol", "ajedrez"],
    "direccion": {
        "calle": "123 Calle Falsa",
        "ciudad": "Springfield"
    },
    "hobbies": ["leer", "futbol", "ajedrez"]
}
'''

# try:
dict_resultante = verificar_valores_unicos(json_data)
print("No hay valores repetidos.")
print(dict_resultante)
# except ValueError as e:
    # print("ERROR")
