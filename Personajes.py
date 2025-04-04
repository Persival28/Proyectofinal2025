#Lista de personajes con sus habilidades
personajes = [
    {
        "nombre": "Guerrero",
        "vida": 100,
        "ataque": 20,
        "defensa": 15,
        "habilidades": ["Espadazo", "Bloqueo"]
    },
    {
        "nombre": "Mago",
        "vida": 80,
        "ataque": 25,
        "defensa": 10,
        "habilidades": ["Bola de Fuego", "Escudo Mágico"]
    },
    {
        "nombre": "Arquero",
        "vida": 90,
        "ataque": 18,
        "defensa": 12,
        "habilidades": ["Disparo Preciso", "Esquivar"]
    },
    {
        "nombre": "Asesino",
        "vida": 85,
        "ataque": 22,
        "defensa": 8,
        "habilidades": ["Ataque Sorpresa", "Invisibilidad"]
    },
    {
        "nombre": "Paladín",
        "vida": 110,
        "ataque": 15,
        "defensa": 20,
        "habilidades": ["Golpe Divino", "Curación"]
    },
    {
        "nombre": "Nigromante",
        "vida": 70,
        "ataque": 30,
        "defensa": 5,
        "habilidades": ["Invocar Esqueletos", "Drenar Vida"]
    }
]

# Ejemplo de cómo mostrar los personajes
for personaje in personajes:
    print(f"Nombre: {personaje['nombre']}")
    print(f"Vida: {personaje['vida']}")
    print(f"Ataque: {personaje['ataque']}")
    print(f"Defensa: {personaje['defensa']}")
    print(f"Habilidades: {', '.join(personaje['habilidades'])}")
    print("-" * 20)