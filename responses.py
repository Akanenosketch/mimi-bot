import random #For the rng based replies

#Note: some of the keywords are server restricted
def handle_Response(message) -> str:
    p_message = message.lower()
    if p_message == 'tu madre':
        return 'La tuya por si acaso'

    if p_message == "coc" or p_message == "clash" or p_message == "clash of clans":
        return "Lemme kill those mofos\nLEMME KILL THOSE MOFOS\n\n\nLEMME KILLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
    
    if p_message == 'notas al':
        rnd = random.randrange(7)
        match rnd:
            case 0:
                return 'Stop trolling you fucking dingbat'
            case 1:
                return 'Oh god no, I see a collective fail'
            case 2: 
                return 'I would like this to end, than you!!'
            case 3: 
                return 'July filled with angry students? Checked'
            case 4:
                return 'Quemen las chanclas'
            case 5:
                return 'https://cdn.discordapp.com/attachments/1092853240032395316/1115177151650598963/Video_sin_titulo.gif'
            case 6: 
                return "Quemen las chanclas ||~~y el pelo de Fabi, viva el bullying~~||"
    
    if p_message == 'notas aci':
        rnd = random.randrange(4)
        toret = ''
        match rnd:
            case 0: 
                toret = 'MS or 8085...? That\'s the question....'
            case 1: 
                toret = 'If everyone fails it\'s due to the teacher not knowing jackshit'
            case 2:
                toret = 'Notas ACI == Julio'
            case 3:
                toret = "El de ACI cuando ve a la gente sufrir\n https://cdn.discordapp.com/avatars/852614483326664786/a_ab188be8b19e42e06ed5ae41a907b0d5.gif?size=1024"
        return toret  
    
    if p_message == 'vibin':
        return 'https://tenor.com/view/dance-happy-anime-vr-gif-26404766'