#!/usr/bin/env python2
from hermes_python.hermes import Hermes
from datetime import datetime
from pytz import timezone

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))


def verbalise_hour(i):
	if i == 0:
		return "media noche"
	elif i == 1:
		return "una"
	else:
		return "{0} horas".format(str(i)) 

def verbalise_minute(i):
	if i == 0:
		return ""
	else:
		return "{0}".format(str(i)) 


def intent_received(hermes, intent_message):

	print()
	print(intent_message.intent.intent_name)
	print ()

	if intent_message.intent.intent_name == 'gplaza:askTime':


		print(intent_message.intent.intent_name)
		now = datetime.now(timezone('America/Santiago'))
		
		if now.hour == 0:
			sentence = 'Es la '
		elif now.hour == 1:
			sentence = 'Es la '
		else:
			sentence = 'Son las '
		
		sentence += verbalise_hour(now.hour) + " " + verbalise_minute(now.minute)
		print(sentence)

		hermes.publish_end_session(intent_message.session_id, sentence)

	elif intent_message.intent.intent_name == 'gplaza:greetings':

		hermes.publish_end_session(intent_message.session_id, "De nada!")


with Hermes(MQTT_ADDR) as h:
	h.subscribe_intents(intent_received).start()
