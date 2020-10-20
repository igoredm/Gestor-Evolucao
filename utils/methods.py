from utils.vars import cooldown, playing
from settings import PREFIX
from threading import Timer
from datetime import datetime

# Class to check this related to Cooldown list
class Cooldown():
    def check_cooldown(id):
        if id in cooldown:
            return True
        return False

    def add_cooldown(id):
        cooldown.append(id)

        timer = Timer(180.0, Cooldown.remove_cooldown, [id])

        timer.start()

    def remove_cooldown(id):
        cooldown.remove(id)

# Class to check this related to Playing dict
class Playing():
    def check_playing(id):
        if id in playing:
            return True
        return False
    
    def add_playing(id):
        start_time = datetime.now()
        string_tempo = start_time.strftime("%H:%M:%S")
        print(f"    - Tempo de início: {string_tempo} \n")
        playing.update({id: start_time})
    
    def stop_playing(id):
        end_time = datetime.now()
        start_time = playing[id]
        delta = end_time - start_time

        del playing[id]

        minutes_played = int(delta.seconds / 60)

        return minutes_played


        

# Class to check basics validations
class BasicValidation():
    def check_message(message):
        if BasicValidation.check_bot(message.author) or message.content.startswith(PREFIX):
            return False
        return True

    def check_bot(member):
        if member.bot:
            return True
        return False
