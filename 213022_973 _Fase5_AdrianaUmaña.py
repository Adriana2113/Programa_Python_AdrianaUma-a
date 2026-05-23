# ===========================================
# Clasificacion del compromiso de clientes
# ===========================================


# Matriz con los datos de los clientes
# [ID Cliente, Duracion en segundos, Eventos clics]

clientes = [
    ["C001", 250, 10],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 190, 4],
    ["C005", 300, 12]
]

# Mostrar datos almacenados
print("Datos de las sesiones")
print("-----------------------------------------")

for cliente in clientes:
    print("ID:", cliente[0],
          "| Duracion:", cliente[1],"seg",
          "| Clics:", cliente[2])
    
print("\n")


# Funcion para clasificar el compromiso

def clasificar_compromiso(duracion, clics):
    
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    # Si no cumple ninguna de las funciones anterioes, se dalsifica como "Medio"   
    else:
        return "Medio"
    
# Informe final

print("Informe Final De Clientes")
print("--------------------------------------")

# Motrar lista final con resultados

for cliente in clientes:
    
    id_cliente = cliente[0]
    duracion = cliente[1]
    clics = cliente[2]
    
    clasificacion = clasificar_compromiso(duracion, clics)
    
    print("Cliente:", id_cliente,
         "| Clasificacion:", clasificacion)
    