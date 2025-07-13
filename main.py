from machine import Pin
import time

INT1 = Pin(12, Pin.OUT)
INT2 = Pin(13, Pin.OUT)
INT3 = Pin(14, Pin.OUT)
INT4 = Pin(15, Pin.OUT)

build_in_led = Pin(2, Pin.OUT)

def mode():
    mode_select = input("front (1) back (2) left (3) right (4) ")
    if mode_select == "1":
        build_in_led.on()
        INT1.on()
        INT2.off()
        INT3.on()
        INT4.off()
        print("frente")
        if input("quit? (q)")== "q":
            stop()
        else:
            mode()
    elif mode_select == "2":
        build_in_led.on()
        INT1.off()
        INT2.on()
        INT3.off()
        INT4.on()
        print("tras") 
        if input("quit? (q)") == "q":
            stop()
        else:
            mode()
    elif mode_select == "3":
        build_in_led.on()
        INT1.off()
        INT2.on()
        INT3.on()
        INT4.off()
        print("esquerda")
        if input("quit? (q)") == "q":
            stop()
        else:
            mode()
    elif mode_select == "4":
        build_in_led.on()
        INT1.on()
        INT2.off()
        INT3.off()
        INT4.on()
        print("direita")
        if input("quit? (q)") == "q":
            stop()
        else:
            mode()
    else:
        mode()
        time.sleep(3)
    time.sleep(1)

def stop():
    INT1.off()
    INT2.off()
    INT3.off()
    INT4.off()
    build_in_led.off()
    time.sleep(1)
    mode()

mode()