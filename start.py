import game
import time
import serial





port = "/dev/ttyACM0"
connection = serial.Serial(port, 9600)
print(f"Serial {port} is working well")

def wistangle(a1,a2):


    theata=180-a2
    xtheata=a1+theata
    xtheata1=xtheata-90
    wtheata=180-xtheata1

    return wtheata


"""
y
||
||
||
||
||
||
=================x

"""


def pickup(base,x,y):
    base=base+5
    x=x-8
    a1,a2=game.sim_inverse_k(x,y)
    print("=============")
    print(a1,a2)
    print("=============")
    
    x,a2=-a1,a2
    connection.write(f"s{120}".encode())
    time.sleep(0.5)
    connection.write(f"g{grup}".encode())
    time.sleep(0.5)
    connection.write(f"w{180}".encode())
    time.sleep(0.5)
    connection.write(f"e{a2}".encode())
    time.sleep(0.5)
    connection.write(f"b{base}".encode())
    time.sleep(0.5)
    connection.write(f"s{x}".encode())
    wang=wistangle(x,a2)
    print(wang)
    time.sleep(1)
    connection.write(f"w{wang}".encode())
    time.sleep(0.5)
    connection.write(f"g{grdow}".encode())
    time.sleep(0.5)
    connection.write(f"s{120}".encode())

base=90
length = 23
y=3
grup= 60
grdow=10
if 19>length or 33<length:
    print("""
   ___  _   _ _____    ___  _____   ____      _    _   _  ____ _____         _
  / _ \| | | |_   _|  / _ \|  ___| |  _ \    / \  | \ | |/ ___| ____|      /( )\    
 | | | | | | | | |   | | | | |_    | |_) |  / _ \ |  \| | |  _|  _|       / / \ \    __
 | |_| | |_| | | |   | |_| |  _|   |  _ <  / ___ \| |\  | |_| | |___     / /   \ \_ / _\ 
  \___/ \___/  |_|    \___/|_|     |_| \_\/_/   \_\_| \_|\____|_____|   / /     \__O (__
                                                                       / /___       \__/
                                                                      |___ARM|            """)                                                                                                                          
    exit()


pickup(base,length,y)
"""
# for up and down
pickup(base,length,y-2)
pickup(base,length,y-3)
pickup(base,length,y-4)
pickup(base,length,y-5)
pickup(base,length,y-6)
pickup(base,length,y-7)
pickup(base,length,y-8)
pickup(base,length,y-9)
pickup(base,length,y-10)
pickup(base,length,y-11)
pickup(base,length,y-12)
pickup(base,length,y-13)
pickup(base,length,y-14)
pickup(base,length,y-15)
pickup(base,length,y-16)
pickup(base,length,y-17)

"""

##########################
#  PLACE A OBJECT        #
##########################

def place(base,x,y):
    base=base+5
    x=x-8

    a1,a2=game.sim_inverse_k(x,y)
    print("=============")
    print(a1,a2)
    print("=============")
    
    x,a2=-a1,a2
    connection.write(f"s{120}".encode())
    time.sleep(0.5)
   


    time.sleep(0.5)
    connection.write(f"e{a2}".encode())
    time.sleep(0.5)
    connection.write(f"b{base}".encode())
    time.sleep(0.5)
    connection.write(f"s{x}".encode())
    wang=wistangle(x,a2)
    print(wang)
    time.sleep(1)
    connection.write(f"w{wang}".encode())
    time.sleep(0.5)
    connection.write(f"g{grup}".encode())
    time.sleep(0.5)
    connection.write(f"s{120}".encode())    

#place(45,23,-5) 

def openup():
    connection.write(f"g{grup}".encode())

def closedown():
    connection.write(f"g{grdow}".encode())

