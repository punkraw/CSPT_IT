#importiamo librerie essenziali 
#random dara' la possibilta di randomizzare al complilatore stesso
#string in modo da avere tutti i caratteri disponibili per ascii etc
import random       
import string
#compiliamo le definizioni
def pwd_generator():
    print ("il programma consente di scegliere password semplici o complesse")
    ascii_chars= string.digits + string.ascii_letters + string.punctuation
    alphanum_chars= string.digits + string.ascii_letters
    #questo due piccole "librerie " fatte dalla somma delle librerie
    #dei caratteri andranno a definire i due livelli di password
    #semplice o complessa che l'utente andra' a scegliere
    if input("Desideri una password semplice o complessa? S/C ") == 'C':
       lunghezza = 20
       tipo = ascii_chars
    else:
        lunghezza = 8   
        tipo = alphanum_chars
    #abbiamo definito una scelta in base alla lettera C con un if e un else
    psw = ""
    counter = 0
    #creato una stringa vuota per la password e una variabile di controllo
    while counter < lunghezza :
        char = random.choice (tipo)
        psw += char
        counter += 1
    print (f"la password generata e': {psw}")
    #avviamo la funzione 
pwd_generator()