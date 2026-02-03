#Scrivi una funzione che data in ingresso una 
#lista A contenente n parole, restituisca 
#in output una lista B di interi che rappresentano
#la lunghezza delle parole contenute in 
#SOLUZIONE in pyhton la funzione len()andremo a calcolare 
#quelli che sono i carattari contenuti all'interno delle liste ,stringhe etc.

def char_counter (lista_a):
    lista_b = []
    for parola in lista_a:
        lista_b.append(len(parola))
    return lista_b
#il codice dato non rappresenta una giusta risoluzione in quanto fa le operazioni richieste 
#ma non mostra ne in input ne in output le lunghezze delle parole in quanto non siamo andati
#a inserire nessun input.
#andiamo ad inserire l'input
x = input("Inserisci le parole: ")
#andiamo a trasformare x in una lista o stringa
lista_c = x.split()
#richiamiamo la funzione e stampiamo il risultato
risultato = char_counter(lista_c)
print("numero totali caratteri parole: ", risultato)
 






