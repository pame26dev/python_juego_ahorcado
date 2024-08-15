
import random


def obtener_palabra_secreta() -> str:
    palabras = [ 'python', 'javascript','java','angular', 'django', 'tensorflow', 'react', 'typescript','git', 'flask']
    return random.choice(palabras)

def mostrar_avance(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += '_'
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_avance(palabra_secreta, letras_adivinadas), "La palabra secreta tiene: ", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduce una letra válida (sólo escribir una letra)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Excelente, has acertado!, la letra '{adivinanza}' se encuentra en la palabra secreta")
            else:
                intentos -= 1
                print(f"Lo siento, la letra '{adivinanza}' no se encuentra en la palabra secreta")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Felicitaciones!¡Has ganado! La palabra secreta era: '{palabra_secreta.capitalize()}'")

    if intentos == 0:
        print(f"Lo sentimos mucho, se han acabo los intentos que tenias disponible, la palabra secreta era: '{palabra_secreta.capitalize()}'")
        
juego_ahorcado()
