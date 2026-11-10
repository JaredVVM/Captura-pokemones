class pokemon():
    def __init__(self, nombre, tipo, estadisticas):
        self.nombre = nombre
        self.tipo = tipo
        self.estadisticas = estadisticas

    def __str__(self):
        return f"Nombre: {self.nombre} | Tipo: {self.tipo} | Stats: {self.estadisticas}"

import random

def capturar_pokemon():
    pokemon_random = random.choice(pokedex)
    capturados.append(pokemon_random)
    print("Pokemon capturado")
    print(pokemon_random)

def mostrar_capturados():
    if not capturados:
        print("No hay pokemones capturados: ")
    else:
        print("Pokemon capturados: ")
        for i, p in enumerate(capturados, start=1):
            print(f"{i}. {p}")

capturados = []

pokedex = [
        pokemon("Squirtl", "Agua", "3ps 3atq 4dfs"),
        pokemon("Bulbasaur", "Planta", "3ps 3atq 3dfs"),
        pokemon("Tangela", "Planta", "4ps 3atq 4dfs"),
        pokemon("Charmander", "Fuego", "3ps 4atq 2dfs"),
        pokemon("Vulpix", "Fuego", "3ps 3atq 3dfs"),
        pokemon("Ponyta", "Fuego", "4ps 4atq 3dfs"),
        pokemon("Poliwag", "Agua", "3ps 3atq 3dfs"),
        pokemon("Caterpie", "Bicho", "2ps 2atq 2dfs"),
        pokemon("Weedle", "Bicho", "2ps 3atq 2dfs"),
        pokemon("Pidgey", "Normal/Volador", "3ps 3atq 3dfs"),
        pokemon("Rattata", "Normal", "3ps 4atq 2dfs"),
        pokemon("Doduo", "Normal/Volador", "3ps 4atq 2dfs"),
        pokemon("Pikachu", "Electrico", "3ps 4atq 3dfs"),
        pokemon("Magnemite", "Electrico/Acero", "3ps 3atq 4dfs"),
        pokemon("Voltorb", "Electrico", "3ps 3atq 3dfs"),
        pokemon("Sandshrew", "Tierra", "4ps 3atq 4dfs"),
        pokemon("Diglett", "Tierra", "2ps 4atq 2dfs"),
        pokemon("Nidoran♂", "Veneno", "3ps 3atq 3dfs"),
        pokemon("Koffing", "Veneno", "4ps 3atq 4dfs"),
        pokemon("Abra", "Psiquico", "2ps 4atq 2dfs"),
        pokemon("Drowzee", "Psiquico", "3ps 3atq 4dfs"),
        pokemon("Machop", "Lucha", "4ps 4atq 3dfs"),
        pokemon("Gastly", "Fantasma/Veneno", "2ps 4atq 2dfs"),
        pokemon("Onix", "Roca/Tierra", "4ps 2atq 5dfs")

]





while True:
     print("MENU")
     print("1. Mostrar pokedex")
     print("2. Capturar pokemon")
     print("3. Mostrar pokemones capturados")
     opcion = input("Seleccionar opcion")

     if opcion == "1":
        for p in pokedex:
                print(p)
    
     elif opcion == "2":
            capturar_pokemon()

     elif opcion == "3":
            mostrar_capturados()

     else:
         print("Opcion no valida")



