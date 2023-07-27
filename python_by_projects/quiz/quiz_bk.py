# quiz.py
from string import ascii_lowercase
import random
NUM_PREGUNTAS_QUIZ = 5
PREGUNTAS = {
    'Que tipo de dominio separa una VLAN': ['broadcast', 'colision' , 'multicast', 'unicast'],
    'Que direccionamiento es utilizado en la capa 3 del modelo OSI': ['ip','mac-address', 'netbios', 'serial'],
    'Que dispositivo communta tramas y separa dominios de colision': ['switch', 'router', 'hub', 'firewall'],
    'Que tipo de direccionamiento es utilizado la capa 2': ['mac-address', 'ip', 'ipx', 'tcp']

}

num_preguntas = min(NUM_PREGUNTAS_QUIZ, len(PREGUNTAS))
preguntas = random.sample(list(PREGUNTAS.items()), k=num_preguntas)
cantidad_correctas = 0 
for n, (pregunta, opciones) in enumerate(preguntas, start=1):
    
    print(f'\nPregunta {n}:')
    print(f'¿{pregunta}?')
    respuesta_correcta = opciones[0]
    opciones_etiquetadas = dict(zip(ascii_lowercase,random.sample(opciones, k=len(opciones))))

    for etiqueta, opcion in opciones_etiquetadas.items():
        print(f'  {etiqueta})  {opcion}')


    while (respuesta_etiqueta := input(f'\nrespuesta? ')) not in opciones_etiquetadas:
        print(f'Por seleccione una de las respuestas de {", ".join(opciones_etiquetadas)}')

    respuesta = opciones_etiquetadas[respuesta_etiqueta]
    if respuesta == respuesta_correcta:
        cantidad_correctas += 1
        print('⭐ Correcto! ⭐')
    else:
        print(f'{respuesta} no es la repuesta, la respuesta es {respuesta_correcta}')

print(f'\nObtiviste {cantidad_correctas} correctas de {n} preguntas')
