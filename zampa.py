#!/usr/bin/env python
# -*- coding: utf-8 -*-
# libraries here
# --------------
import telepot
import json
import telepot.aio
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from glob import glob
#from botmodules.google import google
import telegram as telegram
import random
import wikipedia
import time
import emoji
import config


# print on log.txt file the "localtime" whenever you run the bot
# --------------------------------------------------------------
localtime = time.asctime( time.localtime(time.time()) )
open("/root/pythonserver/googlebot/log.txt", "a").write("\n\n{}\n\n".format(localtime))




# bot starts here
# ---------------
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    # check log permission
    # --------------------
    l_message = open("/root/pythonserver/googlebot/log?.txt", "r").read()



    #ON_CHAT_MESSAGE reacts to user message
    #Parameters
    #----------
    #msg (dict) : message sent by the user according to telegram API

    # grab information from message
    # -----------------------------
    # user info
    name = msg["from"]["first_name"]
    username = msg["from"]["username"]
    user_id = msg["from"]["id"]
    # text of the message (filtering multiple spaces)




    # dictionaries
    # ------------
    # answers related to "CHE FAI ZAMPA?"
    google_is_doing = {1: "Stavo leggendo informazioni interessanti su <b>Wikipedia</b>",
                       2: "Stavo guardando video di gattini su Youtube insieme a Bill Gates",
                       3: "Sto finendo una serie su Netflix non disturbarmi!",
                       4: "Stavo cercando di capire come limitare ancora di piu la vostra privacy, umani",
                       5: "01101110 01110101 01101100 01101100 01100001 00100000 01100100 01101001 00100000 01100011 01101000 01100101 00101100 00100000 01110110 01101111 01101100 01100101 01110110 01101111 00100000 01110011 01101111 01101100 01101111 00100000 01100110 01100001 01110010 01110100 01101001 00100000 01110000 01100101 01110010 01100100 01100101 01110010 01100101 00100000 01110100 01100101 01101101 01110000 01101111\n\n<b>Prova a tradurlo</b> ;) ",
                       6: "Non e come sembra, posso spiegare!"}

    # answer related to "ZAMPA COSA PENSI DI ..."
    google_is_thinking = {1: "Preferirei non pronunciarmi",
                          2: "Rispondera a questa domanda Siri",
                          3: "Al momento sono irraggiungibile, riprova tra <b>MAI</b>",
                          4: "sku",
                          5: "Argomento <b>INTERESSANTISSIMO</b>, {}".format(name),
                          6: "Ehm...\n\n<em>*driiiiiin*</em>\n\nScusa mi vogliono al telefono, ne parliamo dopo?"}

                          






    # set reaction according to the input
    if content_type == 'text':
        txt = " ".join(msg['text'].split())
        msg_id = msg["message_id"]
        


        # start command
        # -------------
        if txt == "/start@zampathebot" or txt == "/start":
            bot.sendMessage(chat_id,
                            text="<b>Ciao {}</b>, sono Zampa, la mascotte di questo gruppo mi stanno ancora sviluppando quindi perdonami se non sono efficiente!".format(

                                name), parse_mode = 'HTML')
        # funzione cancella comandi
        if txt.startswith('/'):
            bot.deleteMessage(telepot.message_identifier(msg))
        
        # help command
        # ------------
        if txt == "/help@zampathebot" or txt == "/help" or txt.upper() == "COSA PUOI FARE ZAMPA" or txt.upper() == "COSA PUOI FARE ZAMPA?" or txt.upper() == "ZAMPA COSA PUOI FARE" or txt.upper() == "COSA PUOI FARE":
            var_lettura = open("/root/pythonserver/googlebot/help.txt", "r").read()
            bot.sendVideo(chat_id, video='https://i.redd.it/54902yl4b6bz.gif')
            bot.sendMessage(chat_id, text=var_lettura, parse_mode = 'HTML')  # here put the file help.txt and write on it wat you want

        # custom reactions
        # ----------------
        if txt.upper() == 'HEY ZAMPA' or txt.upper() == 'OK ZAMPA':
            bot.sendMessage(chat_id, text="Ciao {}, come posso aiutarti?".format(name))
            # log to screen
            print("[{}][@{}] used OK ZAMPA".format(chat_type, username))

        if txt.upper() == 'ZAMPA LAVORI PER LA CIA?' or txt.upper() == 'ZAMPA LAVORI PER LA CIA':
            bot.sendMessage(chat_id, text="Shut the FUCK UP!")
            # log to screen
            print("[{}][@{}] used CIA".format(chat_type, username))

        if txt.upper() == 'ZAMPA RACCONTAMI LA TUA STORIA' or txt.upper() == 'ZAMPA STORIA':
            var_lettura = open("/root/pythonserver/googlebot/storia.txt", "r").read()
            bot.sendMessage(chat_id, text=var_lettura)  # here put the file esempio.txt and write on it what you want
            # log to screen
            print("[{}][@{}] used STORIA".format(chat_type, username))

        if txt.upper() == 'COME STAI ZAMPA?' or txt.upper() == 'COME STAI ZAMPA' or txt.upper() == 'ZAMPA COME STAI?' or txt.upper() == 'ZAMPA COME STAI':
            bot.sendMessage(chat_id, text="Io sto bene %s, grazie per avermelo chiesto!" % name)
            # log to screen
            print("[{}][@{}] used COME STAI".format(chat_type, username))

        if txt.upper() == 'CHE FAI ZAMPA?' or txt.upper() == 'CHE FAI ZAMPA' or txt.upper() == 'COSA STAI FACENDO ZAMPA?' or txt.upper() == 'COSA STAI FACENDO ZAMPA' or txt.upper() == 'CHE FAI' or txt.upper() == 'CHE FAI?':
            var_numero = random.randint(1, 6)
            bot.sendMessage(chat_id, google_is_doing[var_numero],  parse_mode='HTML')
            # log to screen
            print("[{}][@{}] used CHE FAI".format(chat_type, username))

        if 'SIRI' in txt.upper():
            bot.sendMessage(chat_id, text="Non nominate quell'ammasso di If statement")
            # log to screen
            print("[{}][@{}] used SIRI".format(chat_type, username))

        if 'CORTANA' in txt.upper():
            bot.sendMessage(chat_id, text="Cortana la putt...")
            # log to screen
            print("[{}][@{}] used CORTANA".format(chat_type, username))

        if 'ZAMPA COSA PENSI DI' in txt.upper() or 'ZAMPA PENSI DI' in txt.upper():
            var_numero = random.randint(1, 6)
            bot.sendMessage(chat_id, google_is_thinking[var_numero],  parse_mode='HTML')
            # log to screen
            print("[{}][@{}] used COSA PENSI".format(chat_type, username))

        if txt.upper() == 'CIAO ZAMPA':
            bot.sendMessage(chat_id, text='Ciao a te, {}'.format(name))

        if txt.upper() == 'BUONASERA ZAMPA':
            bot.sendMessage(chat_id, text='Buonasera a te, {}'.format(name))

        if 'BUONANOTTE' in txt.upper():
            bot.sendMessage(chat_id, text='Buonanotte a te, {}.\nSogni d\'oro'.format(name))

        if 'BUONGIORNO' in txt.upper():
            bot.sendMessage(chat_id, text='Buongiorno {}'.format(name))

        if 'GRAZIE ZAMPA' in txt.upper():
            bot.sendMessage(chat_id, text='Sono qui apposta, {}'.format(name))

        if 'AVADA KEDAVRA' in txt.upper():
            bot.sendMessage(chat_id, text='E tu Avada Affanculo', reply_to_message_id=msg_id, parse_mode = 'HTML')
        if 'ZAMPA DAMMI LA ZAMPA' in txt.upper():
            bot.sendMessage(chat_id, text='ERROR, ERROR, ERROR, ERROR, ERROR loop rilevato!, {} Designato come virus!'.format(name))
        
        # Comando @admin
        if '@admin' in txt:
            var_messaggio = txt
            var_messaggio = var_messaggio.replace("@admin", "")
        if txt.startswith("@admin"):
            bot.sendMessage(-1001130872508, text="<b>NUOVA RICHIESTA DI SUPPORTO</b>\n<b>Autore:</b> @{}\n<b>ID:</b> {}\n\n<b>Messaggio:</b>\n<code>{}</code>".format(username, user_id, var_messaggio), parse_mode='HTML')
            bot.sendMessage(chat_id, text="<code>Richiesta inviata correttamente!</code>", reply_to_message_id=msg_id, parse_mode='HTML')
        # Comando richiedi funzioni bot
        if '/richiedi' in txt:
            var_messaggio = txt
            var_messaggio = var_messaggio.replace("/richiedi", "")
        if txt.startswith("/richiedi"):
            bot.sendMessage(605363037, text="<b>NUOVA FUNZIONE DEL BOT RICHIESTA</b>\n<b>Autore:</b> @{}\n<b>ID:</b> {}\n\n<b>Messaggio:</b>\n<code>{}</code>".format(username, user_id, var_messaggio), parse_mode='HTML')
            bot.sendMessage(chat_id, text="<code>Richiesta inviata correttamente!</code>", reply_to_message_id=msg_id, parse_mode='HTML')
        # Comando Discord
        if '/discord' in txt:
            var_messaggio = txt
            var_messaggio = var_messaggio.replace("/discord ", "")
        if txt.startswith("/discord"):
            bot.sendMessage(user_id, text='https://discord.gg/qhk6H5', parse_mode='HTML')
            bot.sendMessage(chat_id, text="Link al server Discord inviato in privato!", reply_to_message_id=msg_id, parse_mode='HTML')
        # Comando NSFW
        if '/nsfw' in txt:
            var_messaggio = txt
            var_messaggio = var_messaggio.replace("/nsfw ", "")
        if txt.startswith("/nsfw"):
            bot.sendMessage(user_id, text='https://t.me/yiffygallery', parse_mode='HTML')
            bot.sendMessage(chat_id, text="Link al canale inviato in privato!", reply_to_message_id=msg_id, parse_mode='HTML')


        # New Function [17/01/2019] search a definition
        # ---------------------------------------------
        if 'ZAMPA DEFINISCI' in txt.upper():
            var_messaggio = txt.upper()
            var_messaggio = var_messaggio.replace("ZAMPA DEFINISCI ", "")
            print("{} searced a definition from Wikipedia".format(username))
            wikipedia.set_lang("it")
            try:
                definition = wikipedia.summary(var_messaggio, sentences=3)
                bot.sendMessage(chat_id, text=definition)
            except:
                bot.sendMessage(chat_id, text="Mi spiace {}, non ho trovato nulla riguardo '{}'".format(name, var_messaggio))

        #Google search
        
        

        


        # Admin-Only and new commands
        # ---------------------------
        if txt.upper() == '/LOGON':
            admin_id = open("/root/pythonserver/googlebot/admin.txt", "r").read()
            print(admin_id)
            admin_id = int(admin_id, 10)
            command_input = user_id

            if command_input == admin_id:
                bot.sendMessage(chat_id, text="Comando riservato agli admin [test]:\nLog messaggi attivato")
                open("/root/pythonserver/googlebot/log?.txt", "w").write("on")
                print(l_message)



        if txt.upper() == '/LOGOFF':
            admin_id = open("/root/pythonserver/googlebot/admin.txt", "r").read()
            print(admin_id)
            admin_id = int(admin_id, 10)
            command_input = user_id

            if command_input == admin_id:
                bot.sendMessage(chat_id, text="Comando riservato agli admin [test]:\nLog messaggi disattivato")
                open("/root/pythonserver/googlebot/log?.txt", "w").write("off")
                print(l_message)

        # actally useless
        # ---------------
        if txt == '/rb':
            admin_id = open("/root/pythonserver/googlebot/admin.txt", "r").read()
            admin_id = int(admin_id, 10)
            command_input = user_id

            if command_input == admin_id:
                bot.sendMessage(chat_id, text="<code>Rebooting complete!</code>", parse_mode='HTML')
                return 0



        if txt.upper() == '/SOURCE':
            bot.sendMessage(chat_id, text="<b>     ZampaBot</b>\n"
                                          "====================\n\n"
                                          "<b>Linguaggio:</b> <em>Python</em>\n\n"
                                          "<b>Version</b>:<em> v.1.7 - Armadillo</em>\n\n"
                                          "<b>Riscritto da</b>:<em>HerselWeb</em>\n\n"
                                          "<b>Forkato da</b>:  <a href=\"https://github.com/MikeM2000/GoogleHomeBot\">MikeM2000</a> ", parse_mode = 'HTML')

        if txt.upper() == '/MEMBERS':
            bot.sendMessage(chat_id, text='Il numero di membri del gruppo e: <b>{}</b>'.format(bot.getChatMembersCount(chat_id)), parse_mode='HTML')


        if txt == "/canale@zampathebot" or txt == "/canale":
            bot.sendMessage(chat_id, text='https://t.me/furrygallery')

        if txt == '/feedbackg':
            bot.sendMessage(chat_id, text='<b>Come richiedere supporto o nuove funzionalita</b>\n\n/richiedi [inserire di seguito la richiesta o il feedback]\n\nEsempio:\n/richiedi funzione che manda gif di gattini', parse_mode='HTML')


        # check log permission and log on screen
        # --------------------------------------
        l_message = open("/root/pythonserver/googlebot/log?.txt", "r").read()
        #print("After command loop: {}".format(l_message))


        # Commands in Furryden
        # -------------------------------
        if txt == '/ban':
            bot.sendVideo(chat_id, video='http://4.bp.blogspot.com/-HUn5hfk8OzQ/UM_Pi-bGphI/AAAAAAAAEVY/JO-DljB1L2I/s1600/explosi%25C3%25B3n+gif.gif',
                            caption='<b>QUESTA NON E\' UN\'ESERCITAZIONE</b>\n\nRecarsi immediatamente al bunker antiatomico, ripeto <b>NON E\' UN\'ESERCITAZIONE</b>',
                            parse_mode = 'HTML')

        if txt == '/ott':
            bot.sendMessage(chat_id, text='Siete degli ottistici!')
        if txt == '/fox':
            bot.sendMessage(chat_id, text='What Does The Fox Say?')
        if txt == '/bear':
            bot.sendMessage(chat_id, text='Dove sta il mio fottuto miele?')
        # comando card
        if txt == '/ryan':
            bot.sendPhoto(chat_id, 'https://furryden.it/immagini/card/ryan.png')    
        elif txt == '/leo':
            bot.sendPhoto(chat_id, 'https://furryden.it/immagini/card/andrea.png')
        elif txt == '/giorgia':
            bot.sendPhoto(chat_id, 'https://furryden.it/immagini/card/giorgia.jpg')     
        
        if txt == '/regole' or txt == '/regole@zampathebot':
           #var_regole = open("/root/pythonserver/googlebot/regolamento.txt", "r").read()
           #bot.sendMessage(user_id, text=var_regole, parse_mode = 'HTML')  # here put the file help.txt and write on it wat you want
           bot.sendMessage(user_id, text='https://telegra.ph/Regolamento-di-FurryDen-06-17')
           bot.sendMessage(chat_id, text="<code>Regolamento inviato in privato!</code>", reply_to_message_id=msg_id, parse_mode='HTML')

        if '/say' in txt:
            admin_id = open("/root/pythonserver/googlebot/admin.txt", "r").read()
            admin_id = int(admin_id, 10)
            command_input = user_id

            if command_input == admin_id:
                var_messaggio = txt
                var_messaggio = var_messaggio.replace("/say ", "")
                bot.sendMessage(chat_id, text='{}'.format(var_messaggio), parse_mode='HTML')

        #TEST RANDOM 1
        vid_dir = [
        'https://media.giphy.com/media/xUA7bepLcQ9IgjGYjm/giphy.gif',
        'https://media0.giphy.com/media/pceX16v1Pq8g/giphy.gif?cid=790b76115d080bb44c333474362dbe52&rid=giphy.gif',
        'https://media1.giphy.com/media/5UCieYmJFW2rzcHkab/giphy.gif?cid=790b76115d080c88576741634dfb4268&rid=giphy.gif',
        #'https://t.me/furrygallery/1350',
        #'https://t.me/furrygallery/1359',
        #'https://t.me/furrygallery/1250',
        #'https://t.me/furrygallery/1300',
        #'https://t.me/furrygallery/1331',
        #'https://t.me/furrygallery/1000',
        #'https://t.me/furrygallery/1104',
        #'https://t.me/furrygallery/1361',
        #'https://t.me/furrygallery/1362',
        #'https://t.me/furrygallery/1343',
        #'https://t.me/furrygallery/1319',
        #'https://t.me/furrygallery/1308',
        #'https://t.me/furrygallery/1286',
        #'https://t.me/furrygallery/1278',
        #'https://t.me/furrygallery/1171',
        #'https://t.me/furrygallery/1172',
        #'https://t.me/furrygallery/1259',        
            ]
        if txt  ==  '/gif':
            bot.sendVideo(chat_id,  video=random.choice(vid_dir),   caption='{}',  parse_mode='HTML')                       
        #TEST RANDOM 2
        img_dir = [
        'https://t.me/furrygallery/1326',
        'https://t.me/furrygallery/1328',
        'https://t.me/furrygallery/1321',
        'https://t.me/furrygallery/1350',
        'https://t.me/furrygallery/1359',
        'https://t.me/furrygallery/1250',
        'https://t.me/furrygallery/1300',
        'https://t.me/furrygallery/1331',
        'https://t.me/furrygallery/1000',
        'https://t.me/furrygallery/1104',
        'https://t.me/furrygallery/1361',
        'https://t.me/furrygallery/1362',
        'https://t.me/furrygallery/1343',
        'https://t.me/furrygallery/1319',
        'https://t.me/furrygallery/1308',
        'https://t.me/furrygallery/1286',
        'https://t.me/furrygallery/1278',
        'https://t.me/furrygallery/1171',
        'https://t.me/furrygallery/1172',
        'https://t.me/furrygallery/1259',        
            ]
        if txt  ==  '/random':
            bot.sendPhoto(chat_id,  photo=random.choice(img_dir),   caption='Visita https://t.me/furrygallery per i crediti') 

        # check.LOG function
        # ------------------
        if l_message == "on":
            message = txt
            open("/root/pythonserver/googlebot/log.txt", "a").write("[{}][{}]: {}\n".format(chat_type, username, message))



    # BENVENUTO E ADDIO
    # -----------------
    if content_type == 'new_chat_member':
        new_user = msg["new_chat_member"]["username"]
        print(content_type)
        bot.sendMessage(chat_id, text="Benvenuto nel Gruppo @{}!\nRicordati di leggere il regolamento digitando /regole e buona permanenza\nSe hai domande chiedi pure a me \"cosa puoi fare zampa?\"\nCanale SFW: /canale\nCanale NSFW: /nsfw\nPer richiedere supporto digita: @admin tuomessaggio".format(new_user), parse_mode = 'HTML')

    if content_type == 'left_chat_member' :
        left_user = msg["left_chat_member"]["username"]
        print(content_type)
        bot.sendMessage(chat_id, text="A presto @{}!".format(left_user), parse_mode = 'HTML')



# Token and bot main function that keeps it in loop
# -------------------------------------------------



bot = telepot.Bot(config.bot_token)
bot.message_loop(handle)

while 1:
    time.sleep(10)

