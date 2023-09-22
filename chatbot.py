
import re
import random
import time

tiempo_limite = 5
inicio_conversacion = time.time()

def get_response(user_input):
  split_message=re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())

  response= check_all_messages(split_message)
  return response


def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
  message_certainty=0

  has_required_words=True


  for word in user_message:
    if word in recognized_words:
        message_certainty+=1

  percentage=float(message_certainty) / float(len(recognized_words))



  for word in required_word:
    if word not in user_message:
        has_required_words=False
        break


  if has_required_words or single_response:
    return int(percentage * 100)
  else:
    return 0


def check_all_messages(message):

    highest_prob={}

    def response(bot_response, list_of_words, single_response=False,required_words=[]):

      nonlocal highest_prob

      highest_prob[bot_response]=message_probability(message, list_of_words, single_response, required_words)


## definir saludos
    response('Hola, soy tu asistente virtual llamado Booti, ¿Realizaste tu tarea ?', ['Hola', 'hola','booti'], single_response=True)
    response('Buenos dias, soy tu asistente virtual llamado Booti, ¿Realizaste tu tarea?', ['Buenos','dias','buenos', 'noches', 'booti'], single_response=True)

## definir actividades
    response('Felicidades, sigue estudiando no te olvides que tienes actvidades para la proxima semana', ['Si','realice','mi','tarea','si'], single_response=True)
    response('Por favor realiza tu tarea que es para la proxima semana',['No','realice','mi','tarea','no'], single_response=True)

## definir recordatorio semanal
    response('\n Lunes: Examen, prototipado a las 10:00 am \n Martes: Tienes una cita con la señorita Kimberly a las 21:00, no olvides llevar protección \n Miercoles: No tienes nada programado para este dia \n Jueves: Reunion laboral con el Equipo de Software en horario matutino \n Viernes: Descanso \n Sabado: Entrega de primera parte de la tarea \n Domingo: No tienes mas que definir',['tengo','algo','para','la','proxima','semana'], single_response=True)

## definir recordatorios individuales
    response('Lunes: Examen, prototipado a las 10:00 am',['tengo','algo','para','el','lunes'], single_response=True)
    response('Martes: Tienes una cita con la señorita Kimberly a las 21:00, no olvides llevar protección',['tengo','algo''tengo','para','el','martes'], single_response=True)
    response('Miercoles: No tienes nada programado para este dia',['tengo','algo','para','el','miercoles'], single_response=True)
    response('Jueves: Reunion laboral con el Equipo de Software en horario matutino',['tengo','algo','para','el','jueves'], single_response=True)
    response('Viernes: Descanso',['tengo','algo','para','el','viernes'], single_response=True)
    response('Sabado: Entrega de primera parte de la tarea',['tengo','algo','para','el','sabado'], single_response=True)
    response('Domingo: No tienes mas que definir',['tengo','algo','para','el','domingo'], single_response=True)

## definir despedida
    response('Encantado de ayudar',['gracias', 'por', 'la','informacion'],single_response=True)
    response('Estoy aqui cuando quieras',['gracias','por' ,'ser', ' un', 'buen', 'asistente', 'amigo'],single_response=True)


## cuál es la respuesta que más encaja
    best_match=max(highest_prob, key=highest_prob.get)

## si la probabilidad es menor que 1 vamos a devolver que no coincide, de lo contrario vamos a devolver la que menor encaje
    return unknown() if highest_prob[best_match]<1 else best_match

## no entiende el bot lo que está preguntando
def unknown():
      response = ['Puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'Escribe bien, porfavor', 'No te logro entender'][random.randrange(4)]
      return response

## método get_response, va a recibir una entrada de parte del usuario.
while True:
    inicio_conversacion = time.time()

    print("Booti: " + get_response(input('Cliente:')))

    tiempo_transcurrido = time.time() - inicio_conversacion


    if tiempo_transcurrido > tiempo_limite:
            print("Conversación cerrada debido a inactividad.")
            break;
