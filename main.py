import game
import time
import serial



base=90+5
length = 25-8
grup= 60
grdow=10

port = "/dev/ttyACM0"
connection = serial.Serial(port, 9600)
print(f"Serial {port} is working well")


a1,a2=game.sim_inverse_k(length,3)

def wistangle(a1,a2):


    theata=180-a2
    xtheata=a1+theata
    xtheata1=xtheata-90
    wtheata=180-xtheata1

    return wtheata


print(a1, a2)
#correction
x=-a1
#x=78-y
print(x,a2)

connection.write(f"s{120}".encode())
time.sleep(0.7)
connection.write(f"g{grup}".encode())
time.sleep(0.5)
connection.write(f"w{180}".encode())
#as2.send_data(conection,f"s{x}")
connection.write(f"e{a2}".encode())
time.sleep(3)
connection.write(f"b{base}".encode())
time.sleep(1)
#connection.write(f"w{120}".encode())
time.sleep(0.5)
connection.write(f"s{x}".encode())
time.sleep(3.5)
wang=wistangle(x,a2)
print(wang)
connection.write(f"w{wang}".encode())
time.sleep(1.9)
connection.write(f"g{grdow}".encode())
time.sleep(1.5)
connection.write(f"s{120}".encode())
time.sleep(0.9)
connection.write(f"b{0}".encode())
time.sleep(0.9)
connection.write(f"s{x}".encode())
connection.write(f"g{grup}".encode())
#as2.send_data(conection,f"e{a2}")

