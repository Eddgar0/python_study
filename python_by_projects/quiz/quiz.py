# quiz.py Refactored
from string import ascii_lowercase
import random
import pathlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


NUM_PREGUNTAS_QUIZ = 5
PREGUNTAS_PATH = pathlib.Path(__file__).parent / 'questions.toml'
PREGUNTAS = tomllib.loads(PREGUNTAS_PATH.read_text())

def prepara_preguntas(path, num_preguntas):
    preguntas = tomllib.loads(path.read_text())['questions']
    num_preguntas = min(num_preguntas, len(preguntas))
    return random.sample(list(preguntas), k=num_preguntas)


def obten_respuesta(pregunta, opciones):
    print(f'¿{pregunta}?')

    opciones_etiquetadas = dict(zip(ascii_lowercase, opciones))
    for etiqueta, opcion in opciones_etiquetadas.items():
        print(f'  {etiqueta})  {opcion}')
    
    while (respuesta_etiqueta := input(f'\nrespuesta? ')) not in opciones_etiquetadas:
        print(f'Por seleccione una de las respuestas de {", ".join(opciones_etiquetadas)}')
        
    return opciones_etiquetadas[respuesta_etiqueta]


def haz_pregunta(pregunta):
    respuesta_correcta = pregunta['respuesta']
    opciones = [pregunta['respuesta']] + pregunta['opciones']
    opciones_ordenadas = random.sample(opciones, k=len(opciones))
    respuesta = obten_respuesta(pregunta['pregunta'], opciones_ordenadas)

    if respuesta == respuesta_correcta:
        print('⭐ Correcto! ⭐')
        return 1
    else:
        print(f'{respuesta} no es la repuesta, la respuesta es {respuesta_correcta}')
        return 0


def run_quiz():
    preguntas = prepara_preguntas(PREGUNTAS_PATH, num_preguntas=NUM_PREGUNTAS_QUIZ)
    
    cantidad_correctas = 0 
    for n, pregunta in enumerate(preguntas, start=1):
         print(f'\nPregunta {n}:')
         cantidad_correctas += haz_pregunta(pregunta)

    print(f'\nObtuviste {cantidad_correctas} correctas de {n} preguntas')

if __name__ == '__main__':
    run_quiz()