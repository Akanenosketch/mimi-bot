import random 

def handle_Response(message, username) -> str:
    p_message = message.lower()

    if message == 'snipe':
        return 'not implemented, so your `mom`'
    
    if p_message == 'tu madre':
        return 'La tuya por si acaso'
     
    if p_message == 'fuck you':
        return 'when, where and how hard '+ username + ' ~'
    
    if p_message == 'sleep':
        return 'what\'s sleep, is that edible?'
    
    if p_message == 'notas al':
        rnd = random.randrange(3)
        if rnd == 0:
            return 'Stop trolling you fucking dingbat'
        if rnd == 1:
            return 'oh god no, I see a collective fail'
        if rnd == 2:
            return 'I would like this to end, thank you!!'
    
    if p_message[0:5] == '8ball':
        rnd = random.randrange(8)
        if rnd  == 0:
            toret = p_message[5:], '\n I can\'t say no, but also can\'t say yes'
            return toret
        if rnd == 1:
            toret = p_message[5:], '\n I agree'
            return toret
        if rnd == 2:
            toret = p_message[5:], '\n Ask someone else, will you?'
            return toret
        if rnd == 3:
            toret = p_message[5:], '\n Not sure why are you asking that, but ok boomer'
            return toret
        if rnd == 4:
            toret = p_message[5:], '\n Yes'
            return toret
        if rnd == 5:
            toret  = p_message[5:], '\n Not sure'
            return toret
        if rnd == 6:
            toret = p_message[5:], '\n I don\'t know? Fucking weirdo'
            return toret
        if rnd == 7:
            toret = p_message[5:], '\n I\'M NOT GOD IDK ALL THE ANSWERS, ASK YOUR GOD IDFK'
            return toret
        
    
    if p_message == 'future':
        rnd = random. randrange(6)
        msg = ' '
        if rnd == 0:
            msg = 'You have a "future" I guess'
        if rnd == 1:
            msg = 'A bright future awaits for you'
        if rnd == 2:
            msg = 'Your future seems good, don\'t sleep it up'
        if rnd == 3:
            msg = 'You\'re useless my guy'
        if rnd == 4:
            if username == 'ZeChurro#7826':
                msg = 'Hun you\'re mine so no suggar mommy for you'
            else:  
                msg = 'You might need a sugar daddy/mommy to survive'
        if rnd == 5:
            msg = 'Are you sure you don\'t want to jump out or something?'
        return msg
    else:
        return False
        

