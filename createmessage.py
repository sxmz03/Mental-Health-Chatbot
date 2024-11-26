from chatbot import happy
from chatbot import angry
from chatbot import suprise
from chatbot import fear
from chatbot import sad
from phonenumber import number
from main import logusername
from twilio.rest import Client
class SMS:
    #initilisation
    def __init__(self, start = TRUE):
        self.start = start
    global logusername
    global happy
    global angry
    global suprise
    global fear
    global sad
    global message
    global feedback
    global number
    def diagnose(self):
        #compares emotions and forms a message to diagnose the user
        if happy > angry and suprise and fear and sad:
            message = "Hello this is Therabuddy.",logusername, "has made good progress in their session today and has shown signs of happiness"
        elif angry > happy and suprise and fear and sad:
            message = "Hello this is Therabuddy.",logusername,"has made good progress in their session today and has shown signs of anger. This could indicate early sings of anger issues.  "
        elif suprise > happy and angry and fear and sad:
            message = "Hello this is Therabuddy.",logusername,"has made good progress in their session today and has shown signs of shock. This could indicate early signs of anxiety."
        elif fear > happy and angry and suprise and sad:
            message = "Hello this is Therabuddy.",logusername,"has made good progress in their session today and has shown signs of fear. This could indicate early signs of paranoia."
        elif sad > happy and angry and suprise and fear:
            message = "Hello this is Therabuddy.",logusername,"has made good progress with in their session today and has shown signs of saddness. This could indicate early signs of depression."
        else:
            message = "Hello this is Therabuddy.", logusername, "has made good progress with in their session today, but it is unclear on a diagnoses yet, please allow them to keep up with their sessions."
        self.sendmessage()
    def feedback(self):
        feedback = "In order to keep up their progress", logusername, "should try keep a journal to write down their feelings and try meditation, to try and clear their head"
        self.sendfeedback()

    def sendmessage(self):
        #sends SMS message to user
        account_sid = 'AC431900a2c6316840e42d60f98a8c9ca6'
        auth_token = '16ecccfb4dba53741b8672241e3d7fef'
        client = Client(account_sid, auth_token)

        SMS1 = client.messages.create(

            messaging_service_sid='MG3b401935134331df4cc7336b466d0024',
            body=message,
            to=number
        )
    def sendfeedback(self):
        #sends SMS message to user
        account_sid = 'AC431900a2c6316840e42d60f98a8c9ca6'
        auth_token = '16ecccfb4dba53741b8672241e3d7fef'
        client = Client(account_sid, auth_token)

        SMS2 = client.messages.create(

            messaging_service_sid='MG3b401935134331df4cc7336b466d0024',
            body=feedback,
            to=number
        )
SMS(TRUE).diagnose()
SMS(TRUE).feedback()