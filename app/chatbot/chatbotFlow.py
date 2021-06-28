from app.helpers import sender_graph
from random import choice

def initial_message(**kwargs):
    # https://developers.facebook.com/docs/messenger-platform/send-messages/quick-replies
    return sender_graph(recipient_id=kwargs['recipient_id'], 
            message={
                "text": "Escoge un tipo de música:",
                "quick_replies":[
                    {
                        "content_type":"text",
                        "title":"Baladas",
                        "payload":"balada_payload"
                        #"image_url":"https://upload.wikimedia.org/wikipedia/commons/b/b9/Solid_red.png"
                    },{
                        "content_type":"text",
                        "title":"Rock",
                        "payload":"rock_payload"
                        #"image_url":"https://upload.wikimedia.org/wikipedia/commons/c/c7/Solid_green.png"
                    },{
                        "content_type":"text",
                        "title":"Metal",
                        "payload":"metal_payload"
                        #"image_url":"https://upload.wikimedia.org/wikipedia/commons/c/c7/Solid_green.png"
                    },{
                        "content_type":"text",
                        "title":"Clásica",
                        "payload":"clasica_payload"
                        #"image_url":"https://upload.wikimedia.org/wikipedia/commons/c/c7/Solid_green.png"  
                    },{
                        "content_type":"text",
                        "title":"Reggaetón",
                        "payload":"reggaeton_payload"
                        #"image_url":"https://upload.wikimedia.org/wikipedia/commons/c/c7/Solid_green.png"
                    } 
                ]
            }
    )



def tipo_message(**kwargs):
    palabra = ['Buena elección', 'Mala elección', 'Lo mejor de lo mejor', 'Excelsior', 'Mejor no me hables']
    return sender_graph(recipient_id=kwargs['recipient_id'], message={
        'text': f'Escogiste el color {kwargs["genero"]}, {choice(palabra)}'
    })

# def template_message(**kwargs):
#     # https://developers.facebook.com/docs/messenger-platform/send-messages/template/generic
#     return sender_graph(recipient_id=kwargs['recipient_id'], message={
#         "attachment":{
#             "type":"template",
#             "payload":{
#                 "template_type":"generic",
#                 "elements":[
#                     {
#                         "title":"Google",
#                         "image_url":"https://www.google.com.pe/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
#                         "subtitle":"We have the right hat for everyone.",
#                         "buttons":[
#                             {
#                                 "type":"web_url",
#                                 "url":"https://www.google.com.pe",
#                                 "title":"View Website"
#                             }         
#                         ]      
#                     },
#                     {
#                         "title":"Amazon",
#                         "image_url":"http://pngimg.com/uploads/amazon/amazon_PNG13.png",
#                         "subtitle":"We have the right hat for everyone.",
#                         "buttons":[
#                             {
#                                 "type":"web_url",
#                                 "url":"https://www.amazon.com",
#                                 "title":"View Website"
#                             }         
#                         ]      
#                     },
#                     {
#                         "title":"Youtube",
#                         "image_url":"https://logodownload.org/wp-content/uploads/2014/10/youtube-logo-5-2.png",
#                         "subtitle":"We have the right hat for everyone.",
#                         "buttons":[
#                             {
#                                 "type":"web_url",
#                                 "url":"https://www.youtube.com",
#                                 "title":"View Website"
#                             }         
#                         ]      
#                     }
#                 ]
#             }
#         }
#     })

def random_messages(**kwargs):
    palabras = ['Buena elección', 'Mala elección', 'Lo mejor de lo mejor', 'Excelsior', 'Mejor no me hables']
    return sender_graph(recipient_id=kwargs['recipient_id'], message=choice(palabras))
