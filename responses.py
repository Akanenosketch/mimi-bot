import random 

def handle_Response(message, username) -> str:
    p_message = message.lower()
    if p_message == 'tu madre':
        return 'La tuya por si acaso'
    
    if p_message == 'fuck you':
        return 'when, where and how hard '+ username + ' ~'
    
    if p_message == 'sleep':
        return 'what\'s sleep, is that edible?'
    
    if p_message == 'notas al':
        return 'Stop trolling you fucking dingbat'
    
    if p_message == 'Fabi':
        return 'Stop...changing...SHIT YOU FUCKING DICKHEAD'
    
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
            msg = 'You might need a sugar daddy/mommy to survive'
        if rnd == 5:
            msg = 'Are you sure you don\'t want to jump out or something?'
        return msg

