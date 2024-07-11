# ECU-OBD2 Simulator

## Overview
This ECU simulator uses an MCP2515 CAN transceiver to handle OBD2 requests and send responses. 

## Supported Modes and PIDs

1. `00` - Supported PIDs
2. `20` - Supported PIDs (21-40)
3. `40` - Supported PIDs (41-60)
4. `04` - Calculated Engine Load
5. `05` - Engine Coolant Temperature
6. `0A` - Fuel Pressure
7. `0B` - Intake Manifold Pressure
8. `0C` - Engine RPM
9. `0D` - Vehicle Speed
10. `0E` - Timing Advance
11. `0F` - Intake Air Temperature
12. `10` - Mass Air Flow Rate
13. `11` - Absolute Throttle Position
14. `12` - Secondary Air Status
15. `13` - Location of Oxygen Sensor
16. `14` - Bank 1, Sensor 1 Oxygen Sensor
17. `15` - Bank 1, Sensor 2 Oxygen Sensor
18. `16` - Bank 1, Sensor 3 Oxygen Sensor
19. `17` - Bank 1, Sensor 4 Oxygen Sensor
20. `18` - Bank 2, Sensor 1 Oxygen Sensor
21. `19` - Bank 2, Sensor 2 Oxygen Sensor
22. `1A` - Bank 2, Sensor 3 Oxygen Sensor
23. `1B` - Bank 2, Sensor 4 Oxygen Sensor
24. `1F` - Time Since Engine Start
25. `21` - Distance Travelled with MIL Activated
26. `2E` - Commanded Evaporative Purge
27. `2F` - Fuel Level Input
28. `31` - Distance Since DTC Cleared
29. `33` - Barometric Pressure
30. `3C` - Catalyst Temperature Bank 1, Sensor 1
31. `3D` - Catalyst Temperature Bank 2, Sensor 1
32. `3E` - Catalyst Temperature Bank 1, Sensor 2
33. `3F` - Catalyst Temperature Bank 2, Sensor 2
34. `42` - Control Module Voltage
35. `43` - Absolute Load Value
36. `44` - Commanded Equivalence Ratio
37. `45` - Relative Throttle Position
38. `46` - Ambient Air Temperature
39. `47` - Absolute Throttle Position B
40. `48` - Absolute Throttle Position C
41. `49` - Accelerator Pedal Position D
42. `4A` - Accelerator Pedal Position E
43. `4B` - Accelerator Pedal Position F
44. `4C` - Commanded Throttle Actuator
45. `4D` - Time Run with MIL On
46. `4E` - Time Since Trouble Codes Cleared

(*Refer to the `pid00`, `pid20`, and `pid40` requests in the code to get supported PIDs*)

## Hardware Requirements
- Raspberry Pi
- MCP2515 CAN transceiver

## Software Requirements
Please refer to the `requirements.txt` file for the necessary software dependencies.

## Getting Started

### Hardware Setup
1. Connect the MCP2515 CAN transceiver to your Raspberry Pi.
2. Ensure proper power supply and CAN bus connections.

### Software Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/christianostoni/ecu-obd2-simulator
    ```
2. Navigate to the project directory:
    ```bash
    cd ecu-obd2-simulator
    ```
3. Assign execution rights to the start script:
    ```bash
    chmod u+x start.sh
    ```
4. Start the simulator:
    ```bash
    ./start.sh
    ```
