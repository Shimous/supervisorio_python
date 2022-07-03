from pyModbusTCP.client import ModbusClient
from time import sleep

client = ModbusClient('localhost', 502, auto_open=True)

while True:
    Pecas206 = client.read_holding_registers(0,1)
    print(Pecas206)  

    Pecas256 = client.read_holding_registers(1,1)
    print(Pecas256)

    PecasNEDS = client.read_holding_registers(2,1)
    print(PecasNEDS)

    with open ("apontamento_prod.txt", "w") as arquivo:
        arquivo.write(str(Pecas206))
        arquivo.write(",")
        arquivo.write(str(Pecas256))
        arquivo.write(",")
        arquivo.write(str(PecasNEDS)) 

    sleep(1)
