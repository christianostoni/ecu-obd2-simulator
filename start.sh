
USER="pi"
SCRIPT_FILE="/home/${USER}/ecu-obd2-simulator/src"
VENV_DIR="/home/${USER}/ecu-obd2-simulator/venv"
PROJECT_DIR="/home/${USER}/ecu-obd2-simulator"

if ! [ -d ${SCRIPT_FILE} ];
then
    echo "directory non esistente"
    exit
fi

pip3 install virtualenv --break-system-packages

if ! [ -d ${VENV_DIR} ];
then    
    echo "ambiente virtuale non trovato"
    echo "ambiente vituale in creazione...."
    cd ${PROJECT_DIR}
    python3 -m virtualenv venv
    source venv/bin/activate
    echo "ambiente virtuale attivato"
fi

cd ${PROJECT_DIR}
if ! [ -e requirements.txt ];
then   
    echo "requirement non trovato"
    exit
fi

pip install -r requirements.txt --break-system-packages

if ! [ -e /etc/systemd/system/obd2_simulator.service ];
then
    sudo cp obd2_simulator.service /etc/systemd/system/
else
    sudo rm /etc/systemd/system/obd2_simulator.service
    sudo cp obd2_simulator.service /etc/systemd/system/
fi

sudo systemctl enable obd2_simulator.service
sudo systemctl start obd2_simulator.service


