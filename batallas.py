# Función para simular una batalla entre dos personajes
def batalla(personaje1, personaje2):
    print(f"¡Comienza la batalla entre {personaje1['nombre']} y {personaje2['nombre']}!")
    print("-" * 30)

    while personaje1["vida"] > 0 and personaje2["vida"] > 0:
        # Turno del personaje 1
        daño1 = max(personaje1["ataque"] - personaje2["defensa"], 0)
        personaje2["vida"] -= daño1
        print(f"{personaje1['nombre']} ataca a {personaje2['nombre']} causando {daño1} de daño.")
        print(f"Vida restante de {personaje2['nombre']}: {max(personaje2['vida'], 0)}")

        if personaje2["vida"] <= 0:
            print(f"¡{personaje2['nombre']} ha sido derrotado!")
            break

        # Turno del personaje 2
        daño2 = max(personaje2["ataque"] - personaje1["defensa"], 0)
        personaje1["vida"] -= daño2
        print(f"{personaje2['nombre']} ataca a {personaje1['nombre']} causando {daño2} de daño.")
        print(f"Vida restante de {personaje1['nombre']}: {max(personaje1['vida'], 0)}")

        if personaje1["vida"] <= 0:
            print(f"¡{personaje1['nombre']} ha sido derrotado!")
            break

        print("-" * 30)

# Ejemplo de batalla
personaje1 = personajes[0]  # Guerrero
personaje2 = personajes[1]  # Mago

# Clonar los personajes para no modificar los originales
import copy
personaje1 = copy.deepcopy(personaje1)
personaje2 = copy.deepcopy(personaje2)

batalla(personaje1, personaje2)