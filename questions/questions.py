import random
import sys
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
# 2do Inciso puntaje
puntaje = 0
# El usuario deberá contestar 3 preguntas
for x in range(3):
# Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)
# Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
# Verificacion si respondio un numero
        if user_answer.isdigit():
            user_answer = int(user_answer)
# Verifica si el numero esta dentro del rango de posibles respuestas
            match user_answer:
                case 1|2|3|4:
# Se verifica si la respuesta es correcta
                    user_answer = user_answer - 1
                    if user_answer == correct_answers_index[question_index]:
                        puntaje += 1
                        print("\n¡Correcto!")
                        break
                    else:
# Sino tiene otro intento
                        print("\nIncorrecto. Intente nuevamente\n")
                        puntaje -= 0.5
                        if (intento==1):
                            print(f"\nLa respuesta correcta era: {answers[question_index][correct_answers_index[question_index]]}")
                case _:
                    print("Respuesta no válida")
                    sys.exit(1)        
        else:
            print("Respuesta no válida")
            sys.exit(1)
# Si el usuario no responde correctamente después de 2 intentos, se muestra la respuesta correcta
# Se imprime un blanco al final de la pregunta
    print()
# Final de la partida
print(f"El puntaje obtenido por el jugador/a fue de: {puntaje} puntos, sobre un total de 3 puntos posibles")
