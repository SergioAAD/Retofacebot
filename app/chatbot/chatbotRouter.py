from app import api
from os import getenv
from json import dumps
from requests import post as post_request, delete as delete_request
from flask_restx import Resource, Namespace
from app.chatbot.chatbotRequest import ChatbotRequest
from app.chatbot.chatbotFlow import initial_message, random_messages, tipo_message


chatbot_ns = Namespace('chatbot', description='Webhooks Messenger Facebook')

@chatbot_ns.route('/webhook')
class webhook(Resource):
    @chatbot_ns.doc('webhook_connect')
    @chatbot_ns.expect(ChatbotRequest.webhook())
    def get(self):
        '''Webhook Facebook'''
        parser = ChatbotRequest.webhook().parse_args()
        mode = parser['hub.mode']
        challenge = parser['hub.challenge']
        verify_token = parser['hub.verify_token']

        if mode and verify_token and mode == 'subscribe' and verify_token == getenv('FB_HOOK_TOKEN'):
            return int(challenge), 200
        return 'Token errado', 403

    @chatbot_ns.doc('webhook_messages')
    def post(self):
        payload = self.api.payload
        for event in payload['entry']:
            messaging = event['messaging']
            for message in messaging:
                recipient_id = message['sender']['id']
                if message.get('postback') \
                    and message['postback'] \
                    and message['postback'].get('payload'):

                    postback = message['postback'].get('payload')
                    if postback == 'GET_STARTED_PAYLOAD':
                        initial_message(recipient_id=recipient_id)

                if message.get('message') and message['message']:
                    if message['message'].get('quick_reply'):
                        quick_reply = message['message'].get('quick_reply')
                        if quick_reply['payload'] == 'balada_payload':
                            tipo_message(recipient_id=recipient_id, genero='balada')
                            
                        if quick_reply['payload'] == 'rock_payload':
                            tipo_message(recipient_id=recipient_id, genero='rock')
                           
                        if quick_reply['payload'] == 'metal_payload':
                            tipo_message(recipient_id=recipient_id, genero='metal')
                           
                        if quick_reply['payload'] == 'clasica_payload':
                            tipo_message(recipient_id=recipient_id, genero='clasica')
                            
                        if quick_reply['payload'] == 'reggaeton_payload':
                            tipo_message(recipient_id=recipient_id, genero='reggaeton')

                        if quick_reply['payload'] == 'salsa_payload':
                            tipo_message(recipient_id=recipient_id, genero='salsa')
                            
                        if quick_reply['payload'] == 'cumbia_payload':
                            tipo_message(recipient_id=recipient_id, genero='cumbia')
                           
                        if quick_reply['payload'] == 'electronica_payload':
                            tipo_message(recipient_id=recipient_id, genero='electronica')
                           
                        if quick_reply['payload'] == 'rap_payload':
                            tipo_message(recipient_id=recipient_id, genero='rap')
                            
                        if quick_reply['payload'] == 'folklorica_payload':
                            tipo_message(recipient_id=recipient_id, genero='folklorica')  

                        random_messages(recipient_id=recipient_id)
                        #template_message(recipient_id=recipient_id)
                        initial_message(recipient_id=recipient_id)
        return 'Mensaje recibido', 200

@chatbot_ns.route('/setup')
class bot_setup(Resource):
    @chatbot_ns.doc('chatbot_setup')
    def get(self):
        '''Setup Get Started'''
        post_request('https://graph.facebook.com/v11.0/me/messenger_profile', 
            params={
                'access_token': getenv('FB_PAGE_TOKEN')
            },
            headers={
                'Content-Type': 'application/json'
            },
            data=dumps({
                'get_started': {
                    'payload': 'GET_STARTED_PAYLOAD'
                },
                'greeting': [
                    {
                        'locale': 'default',
                        'text': 'Hola {{user_full_name}} !'
                    }
                ]
            }))

        return 'Success Setup', 200

@chatbot_ns.route('/setup/remove')
class bot_setup_remove(Resource):
    @chatbot_ns.doc('chatbot_remove_setup')
    def delete(self):
        '''Remove Get Started and Greeting'''
        delete_request('https://graph.facebook.com/v11.0/me/messenger_profile', 
            params={
                'access_token': getenv('FB_PAGE_TOKEN')
            },
            headers={
                'Content-Type': 'application/json'
            },
            data=dumps({
                'fields': ['get_started', 'greeting']
            }))

        return 'Success Deleted', 200

api.add_namespace(chatbot_ns)
