import serial
import inverse_k as IK
import time
# Configure the serial port

ser = serial.Serial('/dev/ttyACM0', 9600)  # Change 'COM3' to match your Arduino's serial port
sen= serial.Serial('/dev/ttyACM1', 9600)
#start point
dist=10
yaxis=4
base=90
i=0
try:
    while True:
        # Read a line of data from the serial port
        line = ser.readline().decode().strip()
        i=i+1
        print(i)
        # Print the received data
        print(line)
        if line=="Up":
            dist=dist+0.5
        elif line=="Down":
            dist=dist-0.5
        elif line=="Right":
            base=base+5
        elif line=="Left":
            base=base-5

        poss,a1,a2=IK.inverse_k2dof(dist,y=yaxis,l1=12.5,l2=12.5)
        #print(dist)
        #print(a1,a2)
        #time.sleep(0.10)
        
        print("===================")
        print(f"BASE:  {base} || DIST:  {dist} || Angles:  {a1,a2} || LINE:  {line} || ")
        print("===================")
        sen.write(f"b{base}".encode())
       # time.sleep(0.10)
     #   sen.write(f"s{a1}".encode())
       # time.sleep(0.10)
     #   sen.write(f"e{a2}".encode())
       # time.sleep(0.10)
        print(i)


except KeyboardInterrupt:
    # Close the serial port when the program is terminated
    ser.close()
    print("Serial port closed")
