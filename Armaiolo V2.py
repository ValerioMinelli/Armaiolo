'''
Python

Nome Script: Armaiolo
Descrizione: Questo script gestisce un negozio che permette di acquistare armi e modificarle. 

Autori: [Valerio]
Versione: 2.0
Data: [26 - 11 - 2025]
Copyright: © [Valerio] [2025]
Licenza: [Open Source]
'''

def menu():
    print('DIGITA:')
    print('1 per acquistare delle armi. ')
    print('2 per vedere che armi vende il tuo armaiolo. ')
    print('3 per vedere la tua armeria. ')
    print('4 per personalizzare un arma. ')
    print('5 per vedere il tuo budget. ')
    print('6 per aumentare il tuo budget. ')
    print('"e" per uscire. ')
    print('')


negozio = []


class Arma:
    def __init__(self, modello, calibro, colpi, paese, prezzo, tipo):
        self.modello = modello
        self.calibro = calibro
        self.colpi = colpi
        self.paese = paese
        self.prezzo = prezzo
        self.tipo = tipo

        self.arma = {'Nome':modello, 'Prezzo':prezzo, 'Tipo':tipo, 'Calibro':calibro, 'Caricatore':colpi, 'Paese di origine':paese}

        negozio.append(self.arma)


def printArmeria(armeria, nomeArmeria):
    if len(armeria) > 0:
        n = 0
        print(nomeArmeria, 'ha queste armi:')
        for i in armeria:
            n += 1
            print(n, ')', i)
    else:
        print(nomeArmeria, 'è vuota!')


def trovaArma(armeria, arma):
    for i in armeria:
        for x, y in i.items():
            if x == 'Nome' and y == arma:
                return i
            
class nuovaArma():
    def __init__(self, dettagli, quant, soldi):
        self.dettagli = dettagli
        self.quant = quant
        self.soldi = soldi

    def aggiungiArma(self):
        self.x = isinstance(self.dettagli, dict)
        if self.x == False:
            print(self.dettagli)
        else:
            if self.soldi >= self.dettagli['Prezzo'] * self.quant:
                self.soldi -= self.dettagli['Prezzo'] * self.quant
                miaArmeria.append({'Quantità':self.quant, 'Dettagli':self.dettagli})
                print(quantità, arma1['Nome'], "sono stati aggiunti alla tua armeria al costo di", arma1['Prezzo'] * quantità, '$!')
                print('Il tuo budget ora è di', self.soldi, '$!')
                return self.soldi
            else:
                print('Non hai abbastanza soldi per comprare tutte queste armi!')


# definisci le armi qui:
M4 = Arma(prezzo = 700, modello = 'M4', tipo = 'Fucile automatico', calibro = 5.56, colpi = 30, paese = 'U.S.A.')
SPAS12 = Arma(prezzo = 1000, modello = 'Spas 12', tipo = 'Fucile a pompa', calibro = 12, colpi = 8, paese = 'Italia')
# ------------------------------------------------------------------------------------


budget = 10

budget *= 1000

miaArmeria = []


print('BEVENTUO!')
print('')
print('Questo è un programma che gestisce un armaiolo digitale, dove puoi comprare e modificare delle armi custom. ')
print('')
print('')


repeat = True

while repeat == True:
    menu()

    azione = input('Cosa vuoi fare; ')
    print('')

    if azione == 'e':
        print('ARRIVEDERCI!')
        print('')
        print('')
        repeat = False
        break
    elif azione == '2':
        printArmeria(negozio, 'Il negozio')
        print('')
    elif azione == '3':
        printArmeria(miaArmeria, 'La tua armeria')
        print('')
    elif azione == '5':
        print('Il tuo budget è;', budget, '$')
        print('')
    elif azione == '6':
        addBudget = float(input('Quanti soldi vuoi aggiungere al tuo budget; '))
        x = isinstance(addBudget, float)
        if x == True:
            budget += addBudget
            print('Il tuo budget ora è;', budget, '$')
        else:
            print('Devi inserire un numero per aggiungere dei soldi al tuo budget!')
        print('')
    elif azione == '1':
        # METTERE QUI IL CODICE PER COMPRARE UN ARMA! 
        armaVoluta = str(input("Digita il nome dell'arma che desideri acquistare; "))
        print('')
        quantità = int(input('Quante di queste armi vuoi; '))
        print('')
        arma1 = trovaArma(armeria = negozio, arma = armaVoluta)
        addArma = nuovaArma(dettagli = arma1, soldi = budget, quant = quantità)
        budget = addArma.aggiungiArma()
        print('')
    elif azione == '4':
        # METTERE QUI IL CODICE PER MODIFICARE UN ARMA! 
        print('')
    else:
        print('Non ho riconosciuto il comando, RITENTA!')
        print('')

