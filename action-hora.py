#!/usr/bin/env python3

from hermes_python.hermes import Hermes
from hermes_python.ffi.utils import MqttOptions
from hermes_python.ontology import *
import config

from datetime import datetime
from pytz import timezone


class actionHour:
    '''
    '''

    def __init__(self):
        self.load_config()
        if (self.mqtt_user is not None and
            self.mqtt_pass is not None and
                self.mqtt_pass is not None):
            mqtt_opts = MqttOptions(username=self.mqtt_user,
                                    password=self.mqtt_pass,
                                    broker_address=self.mqtt_host)
        else:
            mqtt_opts = MqttOptions(broker_address=self.mqtt_host)

        with Hermes(mqtt_options=mqtt_opts) as h:
            h.subscribe_intents(self.intent_received).start()

    def load_config(self):
        print("Cargando información... ")

        # Load MQTT credentials
        mqtt_config = config.get_mqtt_config()
        if mqtt_config is None:
            exit(1)

        self.mqtt_user = None
        self.mqtt_pass = None
        self.mqtt_host = None

        if 'mqtt_username' in mqtt_config:
            self.mqtt_user = mqtt_config['mqtt_username']
        if 'mqtt_password' in mqtt_config:
            self.mqtt_pass = mqtt_config['mqtt_password']
        if 'mqtt' in mqtt_config:
            self.mqtt_host = mqtt_config['mqtt']

        # Load Skill configuration
        config_needed = [{'group': 'global',
                          'items': ['timezone',
                                    'intent_name'
                                    ],
                          }
                         ]
        skill_config = config.get_skill_config(config_needed)
        if skill_config is None:
            exit(1)

        self.intent_name = skill_config['intent_name']
        self.timezone = skill_config['timezone']

    def intent_received(self, hermes, intent_message):
        '''
            Recibimos el Intent
        '''
        print("INTENT: {0}".format(intent_message.intent.intent_name))

        if intent_message.intent.intent_name == self.intent_name:
            print(intent_message.intent.intent_name)
            now = datetime.now(timezone(self.timezone))

            if now.hour == 1:
                sentence = 'Es la '
            else:
                sentence = 'Son las '

            sentence += self.verbalize_hour(now.hour) + " " + \
                self.verbalize_minute(now.minute)
            sentence = sentence.strip()

            print("ANSWER: {}".format(sentence))
            hermes.publish_end_session(intent_message.session_id, sentence)

    def verbalize_hour(self, i):
        '''
           Convertimos hora a texto
        '''
        if i == 0:
            return "media noche"
        elif i == 1:
            return "una"
        else:
            return "{0}".format(str(i))

    def verbalize_minute(self, i):
        '''
            Convertimos minutos a texto
        '''
        if i == 0:
            return ""
        else:
            return "{0}".format(str(i))


if __name__ == "__main__":
    action_hour = actionHour()
