#coding: utf-8
from evdev import InputDevice
from select import select
import pdb

def detectInputKey():
    dev = InputDevice('/dev/input/event4')
    # while True:
    try :
    	pdb.set_trace()
    	select([dev], [], [],1)
    except Exception ,e:
    	print e 
    for event in dev.read():
        if (event.value == 1 or event.value == 0) and event.code != 0:
            print "Key: %s Status: %s" % (event.code, "pressed" if event.value else "release")


if __name__ == '__main__':
    detectInputKey()