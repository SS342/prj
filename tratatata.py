import bot
import time
from bot import Bot
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import create
from create import DataBase
import sqlite3
from admin import APP
conn = sqlite3.connect('user_info.db')
cursor1 = conn.cursor()
vk_session = vk_api.VkApi(token='ab775457b8fb03e786de6d52cfa744442d25e47c5d53e0dbc2198b5673adb6403d79def9b927d95837433')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


q = input('ENTER')
if q =='admin':
    print(1)
    app = APP(conn=conn, cursor1=cursor1)
    app.start_app()
else:
    pass
bot = Bot(vk_session = vk_session, vk = vk_session.get_api(),longpoll = longpoll)
bot.start_bot()
name = bot.get()[0]
years_old = bot.get()[1]
time_for_play = bot.get()[2]
youtube = bot.get()[3]
streams = bot.get()[4]
becose = bot.get()[5]
print(name,years_old,time_for_play,youtube,streams,becose)
name_list = name.split(' ')
print(name_list)
name = name_list[0]
surname = name_list[1]
middle_name = name_list[2]

db = DataBase(conn = conn, cursor1 = cursor1)
db.do()
j2 = db.j2
print(j2)
time.sleep(3)
db.save(str(j2),name,surname,middle_name,years_old,time_for_play,youtube,streams,becose)
