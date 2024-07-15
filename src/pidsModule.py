import random

def get_supported_pid1():
    #ritorno i bit supportati:
    #04 05 0A 0B 0C 0D 0E 0F 10 11 12 13 14 15 16 17 18 19 1A 1B 1F
    return {'bytes':0x04,
            'frame':[0x00, 0x18, 0x7f, 0xFF, 0xE3]}
    #return [0x06, 0x41, 0x00, 0x18, 0x7f, 0xFF, 0xE3, 0x00]

def get_supported_pid2():#pid 20
    #ritorno i bit supportati: 
    return {'bytes':0x04,
            'frame':[0x20, 0x80, 0x06, 0xA0, 0x1F]}
    #return [0x06, 0x41, 0x20, 0x80, 0x06, 0xA0, 0x1F, 0x00]    

def get_supported_pid3(): #pid 40
    return {'bytes':0x04,
            'frame':[0x40,0x7F,0xFC]}
    #return [0x06, 0x41, 0x40, 0x7F, 0xFC, 0x00, 0x00, 0x00]

def calculated_engine_load(): #pid 04
    value = random.randint(0,255)
    return {'bytes':0x01,
            'frame':[0x04, int(hex(value)[2:], 16)]}
    #return [0x03, 0x41, 0x04, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

def engine_coolant_temperature(): #pid 05
    value = random.randint(0,175) #genero un numero tra 0 e 175 per avere un valore piu reale
    return {'bytes':0x01,
            'frame':[0x05, int(hex(value)[2:], 16)]}
    #return [0x03, 0x41, 0x05, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00] 

def fuel_pressure(): #pid 0A
    value = random.randint(0,255)
    return {
        'bytes': 0x01, 
        'frame': [0x0A, int(hex(value)[2:], 16)]
        }
    #return [0x03, 0x41, 0x0A, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

def manifold_absolute_pressure(): #pid 0B
    value = random.randint(0,255)
    return {'bytes': 0x01, 
            'frame': [0x0B, int(hex(value)[2:], 16)]}
    #return [0x03, 0x41, 0x0B, int(hex(value)[2:], 16), 0x00, 0x00, 0x00, 0x00]

def engine_speed(): #pid 0C
    byteA = random.randint(0,255)
    byteB = random.randint(0,255)
    return {'bytes': 0x02, 'frame': [0x0C, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}
    #return [0x04, 0x41, 0x0C, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16), 0x00, 0x00, 0x00]

def veichle_speed_sensor():  # pid 0D
    value = random.randint(0, 255)
    return {'bytes': 0x01, 'frame': [0x0D, int(hex(value)[2:], 16)]}

def ignition_time_advance():  # pid 0E
    value = random.randint(0, 255)
    return {'bytes': 0x01, 'frame': [0x0E, int(hex(value)[2:], 16)]}

def intake_air_temperature():  # pid 0F
    value = random.randint(0, 175)
    return {'bytes': 0x01, 'frame': [0x0F, int(hex(value)[2:], 16)]}

def air_flow_rate():  # pid 10
    value = random.randint(0, 255)
    return {'bytes': 0x01, 'frame': [0x10, int(hex(value)[2:], 16)]}

def absolute_throttle_position():  # pid 11
    value = random.randint(0, 255)
    return {'bytes': 0x01, 'frame': [0x11, int(hex(value)[2:], 16)]}

def secondary_air_status():  # pid 12
    return {'bytes': 0x01, 'frame': [0x12, 0x07]}

def location_of_oxygen_sensor():  # pid 13
    return {'bytes': 0x01, 'frame': [0x13, 0xFF]}

def bank1_sensor1():  # pid 14
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x14, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def bank1_sensor2():  # pid 15
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x15, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def bank1_sensor3():  # pid 16
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x16, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def bank1_sensor4():  # pid 17
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x17, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def bank2_sensor1():  # pid 18
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x18, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def bank2_sensor2():  # pid 19
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x19, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def bank2_sensor3():  # pid 1A
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x1A, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def bank2_sensor4():  # pid 1B
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x1B, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def time_since_engine_start():  # pid 1F
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x1F, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def distance_travelled_mil_activated():  # pid 21
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x21, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def commanded_evaporative_purge():  # pid 2E
    value = random.randint(0, 255)
    return {'bytes': 0x01, 'frame': [0x2E, int(hex(value)[2:], 16)]}

def fuel_level_input():  # pid 2F
    value = random.randint(0, 255)
    return {'bytes': 0x01, 'frame': [0x2F, int(hex(value)[2:], 16)]}

def distance_since_dtc_cleared():  # pid 31
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x31, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def barometric_pressure():  # pid 33
    value = random.randint(0, 255)
    return {'bytes': 0x01, 'frame': [0x33, int(hex(value)[2:], 16)]}

def catalyst_temp_bank1_sens1():  # pid 3C
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x3C, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def catalyst_temp_bank2_sens1():  # pid 3D
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x3D, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def catalyst_temp_bank1_sens2():  # pid 3E
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x3E, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def catalyst_temp_bank2_sens2():  # pid 3F
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {'bytes': 0x02, 'frame': [0x3F, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]}

def control_module_voltage(): # 0x42
    byteA = random.randint(0,255)
    byteB = random.randint(0,255)
    return {
        'bytes': 0x02,
        'frame': [0x42, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]
    }

def absolute_load_value(): # 0x43
    byteA = random.randint(0,255)
    byteB = random.randint(0,255)
    return {
        'bytes': 0x02,
        'frame': [0x43, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]
    }

def commanded_equivalence_ratio(): # 0x44
    byteA = random.randint(0,255)
    byteB = random.randint(0,255)
    return {
        'bytes': 0x02,
        'frame': [0x44, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]
    }

def relative_throttle_position(): # 0x45
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x45, int(hex(value)[2:], 16)]
    }

def ambient_air_temperature(): # 0x46
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x46, int(hex(value)[2:], 16)]
    }

def absolute_throttle_position_b(): # 0x47
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x47, int(hex(value)[2:], 16)]
    }

def absolute_throttle_position_c(): # 0x48
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x48, int(hex(value)[2:], 16)]
    }

def accelerator_pedal_position_d(): # 0x49
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x49, int(hex(value)[2:], 16)]
    }

def accelerator_pedal_position_e(): # 0x4A
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x4A, int(hex(value)[2:], 16)]
    }

def accelerator_pedal_position_f(): # 0x4B
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x4B, int(hex(value)[2:], 16)]
    }

def commanded_throttle_actuator(): # 0x4C
    value = random.randint(0, 255)
    return {
        'bytes': 0x01,
        'frame': [0x4C, int(hex(value)[2:], 16)]
    }

def time_run_with_mil_on(): # 0x4D
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {
        'bytes': 0x02,
        'frame': [0x4D, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]
    }

def time_since_trouble_codes_cleared(): # 0x4E
    byteA = random.randint(0, 255)
    byteB = random.randint(0, 255)
    return {
        'bytes': 0x02,
        'frame': [0x4E, int(hex(byteA)[2:], 16), int(hex(byteB)[2:], 16)]
    }


pids = {
    0x00:get_supported_pid1,
    0x20:get_supported_pid2,
    0x40:get_supported_pid3,
    0x04:calculated_engine_load,
    0x05:engine_coolant_temperature,
    0x0A:fuel_pressure,
    0x0B:manifold_absolute_pressure,
    0x0C:engine_speed,
    0x0D:veichle_speed_sensor,
    0x0E:ignition_time_advance,
    0x0F:intake_air_temperature,
    0x10:air_flow_rate,
    0x11:absolute_throttle_position,
    0x12:secondary_air_status,
    0x13:location_of_oxygen_sensor,
    0x14:bank1_sensor1,
    0x15:bank1_sensor2,
    0x16:bank1_sensor3,
    0x17:bank1_sensor4,
    0x18:bank2_sensor1,
    0x19:bank2_sensor2,
    0x1A:bank2_sensor3,
    0x1B:bank2_sensor4,
    0x1F:time_since_engine_start,
    0x21:distance_travelled_mil_activated,
    0x2E:commanded_evaporative_purge,
    0x2F:fuel_level_input,
    0x31:distance_since_dtc_cleared,
    0x33:barometric_pressure,
    0x3C:catalyst_temp_bank1_sens1,
    0x3D:catalyst_temp_bank2_sens1,
    0x3E:catalyst_temp_bank1_sens2,
    0x3F:catalyst_temp_bank2_sens2,
    0x42:control_module_voltage,
    0x43:absolute_load_value,
    0x44: commanded_equivalence_ratio,
    0x45: relative_throttle_position,
    0x46: ambient_air_temperature,
    0x47: absolute_throttle_position_b,
    0x48: absolute_throttle_position_c,
    0x49: accelerator_pedal_position_d,
    0x4A: accelerator_pedal_position_e,
    0x4B: accelerator_pedal_position_f,
    0x4C: commanded_throttle_actuator,
    0x4D: time_run_with_mil_on,
    0x4E: time_since_trouble_codes_cleared,
    }
