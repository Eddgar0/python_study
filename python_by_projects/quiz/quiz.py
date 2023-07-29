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
    topic_info = tomllib.loads(path.read_text())
    print(topic_info.values())
    topics = {topic['label']: topic['questions'] for topic in topic_info.values()}

    topic_label = obten_respuesta(
        pregunta = 'Que tema quiere el Quiz',
        opciones = sorted(topics),
    )[0]
    
    preguntas = topics[topic_label]
    num_preguntas = min(num_preguntas, len(preguntas))
    return random.sample(preguntas, k=num_preguntas)


def obten_respuesta(pregunta, opciones, num_opciones=1, pista=None):
    print(f'¿{pregunta}?')

    opciones_etiquetadas = dict(zip(ascii_lowercase, opciones))
    if pista:
        opciones_etiquetadas['?'] = 'pista'

    for etiqueta, opcion in opciones_etiquetadas.items():
        print(f'  {etiqueta})  {opcion}')
    
    while True:
        plural_s = '' if num_opciones == 1 else f's (selecciona {num_opciones})'
        respuesta = input(f'\nrespuesta{plural_s}: ')
        respuestas = set(respuesta.replace(',', ' ').split())

        # Maneja las pistas
        if pista and '?' in respuestas:
            print(f'\nPista: {pista}')
            continue

        # Maneja las respuestas invalidas
        if len(respuestas) != num_opciones:
            plural_s = "" if num_opciones == 1 else 's, separados por coma'
            print(f'Por favor responda {num_opciones} alternativa{plural_s}')
            continue
        
        if any((invalid := respuesta) not in opciones_etiquetadas for respuesta in respuestas):
            print(f'{invalid!r} no es una seleccion valida. ', f'Por favor utilice {", ".join(opciones_etiquetadas)}')
            continue
        
        return [opciones_etiquetadas[respuesta] for respuesta in respuestas]

def haz_pregunta(pregunta):
    respuestas_correctas = pregunta['respuestas']
    opciones = pregunta['respuestas'] + pregunta['opciones']
    opciones_ordenadas = random.sample(opciones, k=len(opciones))
    respuestas = obten_respuesta(pregunta['pregunta'],
                                 opciones_ordenadas, 
                                 num_opciones=len(respuestas_correctas),
                                 pista = pregunta.get('pista')
                                 )

    if correcto := (set(respuestas) == set(respuestas_correctas)):
        print('⭐ Correcto! ⭐')
    else:
        is_or_are = ' es' if len(respuestas_correctas) == 1 else 's son'
        print(f'\n- '.join([f'No, la respuesta{is_or_are}:'] + respuestas_correctas))
    
    if 'explicacion' in pregunta:
        print(f'\nEXPLICACION:\n{pregunta["explicacion"]}')

    return 1 if correcto else 0 

def run_quiz():
    preguntas = prepara_preguntas(PREGUNTAS_PATH, num_preguntas=NUM_PREGUNTAS_QUIZ)
    
    cantidad_correctas = 0 
    for n, pregunta in enumerate(preguntas, start=1):
         print(f'\nPregunta {n}:')
         cantidad_correctas += haz_pregunta(pregunta)

    print(f'\nObtuviste {cantidad_correctas} correctas de {n} preguntas')

if __name__ == '__main__':
    run_quiz()