import urllib.request
import requests
import time
import serial
import datetime
import threading
import random
import yagmail
import matplotlib.pyplot as plt
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()
month=0
po=0
p=0
flag=0
ebill=[0]
ebillm=ebill[-1]
start=time.perf_counter()

def mailing(ebillm):
    password=""
    with open("/home/pi/.local/share/.email_password", "r") as f:
        password=f.read()

    yag = yagmail.SMTP('tcharan241@gmail.com', password)
    ebillm=str(ebillm)
    yag.send(to='tcharan241@gmail.com',
             subject="your electrity bill",
             contents="your electricity bill is: "+ str(ebillm),
             attachments="/home/pi/Desktop/output.jpg")
    print("email sent")

while(True):
    d = datetime.datetime.now()
    d=int(d.strftime("%m"))
    data4=requests.get('https://api.thingspeak.com/channels/1340012/fields/4/last.json').json()
    data5=requests.get('https://api.thingspeak.com/channels/1340012/fields/5/last.json').json()
    data6=requests.get('https://api.thingspeak.com/channels/1340012/fields/6/last.json').json()
    data7=requests.get('https://api.thingspeak.com/channels/1340012/fields/7/last.json').json()
    data8=requests.get('https://api.thingspeak.com/channels/1340012/fields/8/last.json').json()
    switch11=data4['field4']
    switch12=data5['field5']
    temp1=data6['field6']
    intensity1=data7['field7']
    main_sw=data8['field8']
    val1=random.randint(1,30)
    val2=random.randint(1,30)
    val3=random.randint(1,10)
    print('data')
    print(switch11)
    print(switch12)
    print(temp1)
    print(intensity1)
    print(main_sw)
    if d!=month:
        message=1
        plt.plot(ebill)
        plt.savefig("output.jpg")
        mailing(ebillm)
        ebill=[0]
        p=0
        message=0

    value_list = [str(switch11),str(switch12),str(temp1),str(intensity1),str(main_sw),str(message),str(ebillm)]
    send_string = ','.join(value_list)
    send_string += "\n"
    ser.write(send_string.encode('utf-8'))
    receive_string = ser.readline().decode('utf-8')
    receive_string = receive_string.split(',')
    receive_string =[x.rstrip() for x in receive_string]
    print(receive_string)
    if len(receive_string)<4:
        pn=0
    else:
        pn=abs(float(receive_string[5]))
    end = time.perf_counter()
    gap=end-start
    print(gap)
    start = time.perf_counter()
    p=((pn+po)/2)*gap+p
    po=pn

    if p<50:
        cost=p*1
        ebill.append(cost)
    elif p<100:
        cost=p*2
        ebill.append(cost)
    elif p<1000:
        cost=p*3
        ebill.append(cost)
    else :
        cost=p*4
        ebill.append(cost)
    month=d
    print(ebill)
    print(ebillm)
    print(p)
    val4=p
    URL='https://api.thingspeak.com/update?api_key=6T19KVDAHUDUHPUR&field1=0'
    KEY="6T19KVDAHUDUHPUR"
    conn=urllib.request.urlopen(URL+"&field1=%d" %(val1)+"&field2=%d" %(val2)+"&field3=%d" %(val3)+"&field8=%d" %(val4))
    ebillm=ebill[-1]
    print(' ')
