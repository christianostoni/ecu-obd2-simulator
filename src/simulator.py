import can 
import random
import pidsModule

class obd2_simulator: 
    def __init__(self):
        #costrutture della funzione
        self.interface = "socketcan"
        self.channel = "can0"
        self.bus = can.Bus(interface = self.interface, channel = self.channel)
        self.pids = pidsModule.pids

    def requesting(self, message):
        if message.arbitration_id == 0x7DF: #si tratta di una richiesta
            nByte = message.data[0]
            mode = message.data[1]
            if mode == 0x01:
                print("ricevuta una richiesta mode 0x01")
                if nByte == 0x02 and message.data[2] in self.pids: #richiesta pid singolo con modalità dati in tempo reale
                    print("richiesta pid singolo")
                    pid = message.data[2]
                    dictionary = self.pids[pid]() #chiamo la funzione corrispondente che ritorna un dizionario
                    nbytes = dictionary['bytes'] #prendo il numero di byte ritornati dal pid
                    frame = dictionary['frame'] #prendo il frame
                    data = [0x02+nbytes, 0x41] #aggiungo i byte del frame e la modalita
                    for value in frame:
                        data.append(value) #aggiungo i dati al frame

                    print(f"nbytes: {nbytes}")
                    print(f"data: {data}")

                    response = can.Message(
                        arbitration_id = 0x7EF,
                        data = data,
                        is_extended_id = False
                    )
                    try:
                        self.bus.send(response)
                        print("risposta inviata correttamente")
                    except Exception as e:
                        print(f"errore: {e}")
                
                elif nByte >=0x02:
                    print("richiesta pid multiplo")
                    totBytes = 0
                    pidFrame = []
                    pidsRequested = []

                    for x in range(2,nByte+1): 
                        if message.data[x] in self.pids: #inserisco in un array i pid richiesti solo se sono supportati(sono nel dizionario)
                            pidsRequested.append(message.data[x])
                        else:
                            print(f"NO DATA for pid: {message.data[x]}")
                    
                    for pid in pidsRequested: 
                        dictionary = self.pids[pid]()
                        totBytes += dictionary['bytes']
                        for element in dictionary['frame']:
                            pidFrame.append(element)

                    data = [totBytes+len(pidsRequested)+1, 0x41] + pidFrame
                    response = can.Message(
                        arbitration_id = 0x7EF,
                        data = data,
                        is_extended_id = False
                    )
                    try:
                        self.bus.send(response)
                        print("risposta multi pid inviata correttamente")
                    except Exception as e:
                        print(f"errore: {e}")
                else:
                    print("NO DATA")
                    
            else:
                print("NO DATA")

            '''
            elif mode == 0x02:
                print("messaggio iniziale per il protocollo")
                #messaggio iniziale per riconoscere il protocollo
                data = self.pids[0x04]()
                response = can.Message(
                    arbitration_id = 0x7EF,
                    data = data,
                    is_extended_id = False
                )
                try:
                    self.bus.send(response)
                    print("risposta inviata correttamente")
                except Exception as e:
                    print(f"errore: {e}")
            '''
            

    def get_message(self):
        try:
            while True:
                try:
                    msg = self.bus.recv() #controllo se ci sono messaggi
                    if msg is not None:
                        self.requesting(msg)#se non è vuoto lo passo alla funzione che gestisce le richieste
                except Exception as e: #se c'è un eccezzione esco dal ciclo e chiudo il bus. 
                    print("error in get_message()")
                    print(e)
                    break
        finally:
            self.bus.shutdown()
            



                

