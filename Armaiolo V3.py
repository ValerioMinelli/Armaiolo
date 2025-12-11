'''
Python

Nome Script: Armaiolo
Descrizione: Questo script gestisce un negozio che permette di acquistare armi e modificarle. 

Autori: [Valerio]
Versione: Alpha 3.0
Data: [11 - 12 - 2025]
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
    print('7 per testare un arma. ')
    print('"e" per uscire. ')
    print('')


negozio = []


class Arma:
    def __init__(self, modello, calibro, colpi, paese, prezzo, tipo, precisione):
        self.modello = modello
        self.calibro = calibro
        self.colpi = colpi
        self.paese = paese
        self.prezzo = prezzo
        self.tipo = tipo
        self.precisione = precisione

        self.arma = {'Nome':modello, 'Prezzo':prezzo, 'Precisione':precisione, 'Tipo':tipo, 'Calibro':calibro, 'Caricatore':colpi, 'Paese':paese}

        negozio.append(self.arma)


def printArmeria(armeria, nomeArmeria):
    if len(armeria) > 0:
        n = 0
        print(nomeArmeria, 'contiene queste armi:')
        for i in armeria:
            n += 1
            if "Quantità" in i:
                print(n, ')', i['Quantità'], 'x', i['Dettagli'])
            else:
                print(n, ')', i)
    else:
        print(nomeArmeria, 'non contiene armi!')


def trovaArma(armeria, arma, cerca_in_dettagli = False):
    for i in armeria:
        if 'Dettagli' in i and cerca_in_dettagli == True:
            if i['Dettagli']['Nome'] == arma:
                return i 
        else:
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
                print(self.quant, self.dettagli['Nome'], "sono stati aggiunti alla tua armeria al costo di", self.dettagli['Prezzo'] * self.quant, '$!')
                print('Il tuo budget ora è di', self.soldi, '$!')
                return self.soldi
            else:
                print('Non hai abbastanza soldi per comprare tutte queste armi!')


# definisci le armi qui:
M4 = Arma(prezzo = 700, modello = 'M4', precisione = 10, tipo = 'fucile automatico', calibro = 5.56, colpi = 30, paese = 'U.S.A.')
SPAS12 = Arma(prezzo = 1000, modello = 'Spas 12', precisione = 5, tipo = 'fucile a pompa', calibro = 12, colpi = 8, paese = 'Italia')
# ------------------------------------------------------------------------------------


budget = 10

budget *= 1000

miaArmeria = []


modifiche = {'Silenziatore':10, 'Mirino':30, 'Mirino Ottico':60, 'Caricatore Esteso':20}


print('BENVENUTO!')
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
        risultato = addArma.aggiungiArma()
        if risultato is not None:
            budget = risultato
        print('')
    elif azione == '4':
        # METTERE QUI IL CODICE PER MODIFICARE UN ARMA! 
        arma2 = input('Quale delle tue armi vuoi modificare; ')
        armaMod = trovaArma(armeria = miaArmeria, arma = arma2, cerca_in_dettagli=True)
        
        if armaMod is None:
            print("Arma non trovata nella tua armeria!")
        elif armaMod['Quantità'] < 1:
            print("Non hai questa arma in magazzino!")
        else:
            armaMod['Quantità'] -= 1  # Scala la quantità
            print(f"Hai prelevato 1 {arma2} dalla tua armeria. Ne restano {armaMod['Quantità']}.")
            print('')
            print('Lista delle modifiche disponibili:')
            for x, y in modifiche.items():
                print('La modifica', x, 'alza la precisione della tua arma del', y, '%!')
            print('')
            mod = input('Che modifica vuoi fare alla tua arma; ')
            print('')
            trovato = False
            for x, y in modifiche.items():
                if x == mod:
                    armaMod['Dettagli']['Precisione'] += y
                    if 'Modifiche' not in armaMod:
                        armaMod['Modifiche'] = []
                    armaMod['Modifiche'].append(mod)
                    print(f"Modifica '{mod}' applicata con successo!")
                    trovato = True
                    break
            if not trovato:
                print("Modifica non trovata!")
        print('')
    else:
        print('Non ho riconosciuto il comando, RITENTA!')
        print('')

