import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType


class Bot:
    def __init__(self,vk_session,vk,longpoll):
        self.vk = vk
        self.vk_session = vk_session
        self.longpoll = longpoll
    def start_bot(self,name ='',years_old = '',time_for_play = '',youtube= '',streams = '',becose = ''):
        j1 = -1
        for event in self.longpoll.listen():

            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                j1 += 1
                msg1 = event.text
                msg = msg1.lower()

                if msg == "пока":

                    break

                if msg == "регистрация":

                    if event.from_user:


                        self.vk.messages.send(

                            user_id=event.user_id,

                            message='для того чтобы зарегестрироваться на бета тест\nнапишите вашу фамилию имя отчество\nпосле этого мы зададим вам пару вопросов',

                            random_id=random.random()

                        )
                if event.from_user and j1 == 1:
                    self.name = msg


                    self.vk.messages.send(

                        user_id=event.user_id,

                        message='первый вопрос:\nсколько тебе лет?',

                        random_id=random.random()

                    )
                if event.from_user and j1 == 2:
                    self.years_old = msg
                    self.vk.messages.send(

                        user_id=event.user_id,

                        message='второй вопрос:\nкак много времени в день ты уделяешь игре',

                        random_id=random.random()

                    )
                if event.from_user and j1 == 3:
                    self.time_for_play = msg
                    self.vk.messages.send(

                        user_id=event.user_id,

                        message='третий вопрос:\nесть ли у тебя ютуб-канал если да напиши количество подписчеков иначе напиши "нет"',

                        random_id=random.random()

                    )
                if event.from_user and j1 == 4:
                    self.youtube = msg
                    self.vk.messages.send(

                        user_id=event.user_id,

                        message='четвертый вопрос:\nбудеш ли ты делать стримы по игре',

                        random_id=random.random()

                    )
                if event.from_user and j1 == 5:
                    self.streams = msg
                    self.vk.messages.send(

                        user_id=event.user_id,

                        message='пятый вопрос:\nпочему мы',

                        random_id=random.random()

                    )

                if event.from_user and j1 == 6:
                    self.becose = msg
                    break
    def get(self):
        return self.name,self.years_old,self.time_for_play,self.youtube,self.streams,self.becose



