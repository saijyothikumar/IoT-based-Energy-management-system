
import urllib.request
import time
import requests
import threading
import random
def thingspeak_post2():
	threading.Timer(30,thingspeak_post2).start()
	val1=random.randint(1,30)
	val2=random.randint(1,30)
	val3=random.randint(1,10)
	val4=random.randint(1,500)
	print("room 2 data:")
	print( val1 )
	print( val2 )
	print( val3 )
	print(val4)
	print( " ")
	URL='https://api.thingspeak.com/update?api_key=6T19KVDAHUDUHPUR&field1=0'
	KEY="6T19KVDAHUDUHPUR"
	conn=urllib.request.urlopen(URL+"&field1=%d" %(val1)+"&field2=%d" %(val2)+"&field3=%d" %(val3)+"&field8=%d" %(val4))

def thingspeak_post1():
	threading.Timer(30,thingspeak_post1).start()
	val1=random.randint(1,30)
	val2=random.randint(1,30)
	val3=random.randint(1,10)
	print("room 1 data")
	print( val1 )
	print( val2 )
	print( val3 )
	URL='https://api.thingspeak.com/update?api_key=LTVVJSU9MSN5WD4F&field1=0'
	KEY="LTVVJSU9MSN5WD4F"
	conn=urllib.request.urlopen(URL+"&field1=%d" %(val1)+"&field2=%d" %(val2)+"&field3=%d" %(val3))

if __name__=='__main__':
	thingspeak_post1()
	thingspeak_post2()
