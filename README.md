# ECU-OBD2 Simulator

## Overview
This ECU simulator uses an MCP2515 CAN transceiver to handle OBD2 requests and send responses. 

## Supported Modes and PIDs
Currently, the simulator supports only mode `01` and the following PIDs:
1. `00` - Supported PIDs
2. `04` - Calculated Engine Load
3. `05` - Engine Coolant Temperature
4. `0A` - Fuel Pressure
5. `0B` - Intake Manifold Pressure
6. `0C` - Engine RPM
7. `0D` - Vehicle Speed
8. `0E` - Timing Advance
9. `0F` - Intake Air Temperature
10. `10` - Mass Air Flow Rate

(*Refer to the `pid00` request in the code to get supported PIDs*)

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
    ```
    git clone https://github.com/christianostoni/ecu-obd2-simulator
    ```
2. Navigate to the project directory:
    ```
    cd ecu-obd2-simulator
    ```
3. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

### Running the Simulator
1. Ensure your Raspberry Pi is set up to use the MCP2515 CAN transceiver.
2. Run the simulator script:
    ```
    python3 main.py
    ```