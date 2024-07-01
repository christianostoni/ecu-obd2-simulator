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
            0x20:self.get_supported_pid2,
            0x04:self.calculated_engine_load,
            0x05:self.engine_coolant_temperature,
            0x0A:self.fuel_pressure,
            0x0B:self.manifold_absolute_pressure,
            0x0C:self.engine_speed,
            0x0D:self.veichle_speed_sensor,
            0x0E:self.ignition_time_advance,
            0x0F:self.intake_air_temperature,
            0x10:self.air_flow_rate,
            0x11:self.absolute_throttle_position,
            0x12:self.secondary_air_status,
            0x13:self.location_of_oxygen_sensor,
            0x14:self.bank1_sensor1,
            0x15:self.bank1_sensor2,
            0x16:self.bank1_sensor3,
            0x17:self.bank1_sensor4,
            0x18:self.bank2_sensor1,
            0x19:self.bank2_sensor2,
            0x1A:self.bank2_sensor3,
            0x1B:self.bank2_sensor4,
            0x1F:self.time_since_engine_start,

        }

    def get_supported_pid1(self):
        #ritorno i bit supportati:
        #04 05 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1F
        return [0x06, 0x41, 0x00, 0x18, 0x7f, 0xFF, 0xE3, 0x00]

    def get_supported_pid2(self):#pid 20
        #ritorno i bit supportati: 
        #
        return [0x06, 0x41, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00]    
    
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
    
    def veichle_speed_sensor(self): #pid 0D
        value = random.randint(0,255)
        return [0x03, 0x41, 0x0D, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]
    
    def ignition_time_advance(self): #pid 0E
        value = random.radint(0,255)
        return [0x03, 0x41, 0x0E, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]
    
    def intake_air_temperature(self): #pid 0F
        value = random.radint(0,175)
        return [0x03, 0x41, 0x0F, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]
    
    def air_flow_rate(self): #pid 10
        value = random.radint(0,255)
        return [0x03, 0x41, 0x10, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

    def absolute_throttle_position(self): #pid 11
        value = random.radint(0,255)
        return [0x03, 0x41, 0x11, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

    def secondary_air_status(self): #pid 12
        #ritorno i seguenti bit
        #n.0 = upstream of first catalytic converter = 1
        #n.1 = downstream of first catalytic converter inlet = 1
        #n.2 = atmosphere / off  = 1
        return [0x03, 0x41, 0x12, 0x07, 0x00, 0x00, 0x00, 0x00]

    def location_of_oxygen_sensor(self): #pid 13
        #ci sono i seguenti sensori di ossigeno: 
        #bank1 sensor1, sensor2, sensor3, sensor4
        #bank2 sensor1, sensor2, sensor3, sensor4
        return [0x03, 0x41, 0x13, 0xFF, 0x00, 0x00, 0x00, 0x00]
    
    def bank1_sensor1(self): #pid 14
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x14, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]
    
    def bank1_sensor2(self): #pid 15
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x15, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]

    def bank1_sensor3(self): #pid 16
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x16, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]
    
    def bank1_sensor4(self): #pid 17
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x17, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]

    def bank2_sensor1(self): #pid 18
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x18, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]
    
    def bank2_sensor2(self): #pid 19
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x19, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]
    
    def bank2_sensor3(self): #pid 1A
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x1A, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]
    
    def bank2_sensor4(self): #pid 1B
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x1B, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]
    
    def time_since_engine_start(self): #pid 1F
        byteA = random.randint(0,255)
        byteB = random.randint(0,255)
        return [0x04, 0x41, 0x1F, int(hex(byteA)[2:], 16), int(hex(byteA)[2:], 16), 0x00, 0x00, 0x00]


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



                

