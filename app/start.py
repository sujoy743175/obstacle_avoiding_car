#from app.obstacleavoidance import avoid
#from app.blink import blink
#from app.ble import ble
#from app.ble_simple_peripheral import demo
#from app.ble_uart_repl import start_repl
from app.ble_uart_peripheral import demo

def start():
    #print('now its ble..')
    #blink()
    #avoid()
    #ble()
    demo()
    #start_repl()