import can 
import random

class obd2_simulator: 
    def __init__(self):
        #costrutture della funzione
        self.interface = "socketcan"
        self.channel = "can0"
        self.bus = can.Bus(interface = self.interface, channel = self.channel)
        

    def requesting(self, message):
        if message.arbitration_id == 0x7DF: #si tratta di una richiesta
            print("test1")
            mode = message.data[1]
            pid = message.data[2]
            if mode == 0x01 and pid in self.pids: #modalità dati in tempo reale
                print("test2")
                data = self.pids[pid]() #chiamo la funzione corrispondente
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
            
            else:
                print("NO DATA")

    def get_message(self):
        try:
            while True:
                try:
                    msg = self.bus.recv() #controllo se ci sono messaggi
                    print("messaggio ricevuto correttamente")
                    if msg is not None:
                        self.requesting(msg)#se non è vuoto lo passo alla funzione che gestisce le richieste
                except Exception as e: #se c'è un eccezzione esco dal ciclo e chiudo il bus. 
                    print("error in get_message()")
                    print(e)
                    break
        finally:
            self.bus.shutdown()



                

