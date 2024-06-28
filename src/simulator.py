import can 
import random

class obd2_simulator: 
    def __init__(self):
        #costrutture della funzione
        self.interface = "socketcan"
        self.channel = "can0"
        self.bus = can.Bus(interface = self.interface, channel = self.channel)
        self.pids = {
            0x00:self.get_supported_pid1,
            0x04:self.calculated_engine_load,
            0x05:self.engine_coolant_temperature,
            0x0A:self.fuel_pressure,
            0x0B:self.manifold_absolute_pressure,
            0x0C:self.engine_speed,
        }

    def get_supported_pid1(self):
        #ritorno i bit supportati:
        #04 05 0A 0B 0C 0D 0E 0F 10
        return [0x06, 0x41, 0x00, 0x18, 0x7f, 0x00, 0x00]
    

    def calculated_engine_load(self): #pid 04
        value = random.randint(0,255)
        #ritorno i dati: byte - mode - pid - dati(4byte, 1byte ciascuno)
        return [0x03, 0x41, 0x04, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

    def engine_coolant_temperature(self): #pid 05
        value = random.randint(0,175) #genero un numero tra 0 e 175 per avere un valore piu reale
        return [0x03, 0x41, 0x05, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00] 

    def fuel_pressure(self): #pid 0A
        value = random.randint(0,255)
        return [0x03, 0x41, 0x0A, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

    def manifold_absolute_pressure(self): #pid 0B
        value = random.randint(0,255)
        return [0x03, 0x41, 0x0B, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

    def engine_speed(self): #pid 0C
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x0C, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]

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
                    print(e)
                    break
        finally:
            self.bus.shutdown()



                

