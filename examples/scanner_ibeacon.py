import time
from beacontools import BeaconScanner, IBeaconFilter

lrssi1=[]
lrssi2=[]
lrssi3=[]

def caldis1(rssi):
    tx_power=-59
    ratio = rssi*1.0/tx_power
    if rssi==0:
        return -1.0
    elif ratio<1.0:
        return (ratio)**10
    else:
        return (0.89976)*(ratio)**7.7095+0.111

def caldis2(rssi):
    return 10**((-59-rssi)/(40))


def callback1(bt_addr, rssi, packet, additional_info):
    #print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    lrssi1.append(rssi)
    if len(lrssi1)==10:
        avg = sum(lrssi1)/float(len(lrssi1))
        print("Beacon 1: %f" %caldis1(avg))
        lrssi1.clear()

def callback2(bt_addr, rssi, packet, additional_info):
    #print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    lrssi2.append(rssi)
    if len(lrssi2)==10:
        avg = sum(lrssi2)/float(len(lrssi2))
        print("Beacon 2: %f" %caldis1(avg))
        lrssi2.clear()

def callback3(bt_addr, rssi, packet, additional_info):
    #print("<%s, %d> %s %s" % (bt_addr, rssi, packet, additional_info))
    lrssi3.append(rssi)
    if len(lrssi3)==10:
        avg = sum(lrssi3)/float(len(lrssi3))
        print("Beacon 3: %f\n" %caldis1(avg))
        lrssi3.clear()

# scan for all iBeacon advertisements from beacons with the specified uuid 
scanner1 = BeaconScanner(callback1, 
    device_filter=IBeaconFilter(uuid="c401da18-6d38-4b61-9b3e-ff3790f0eeb2")
)
scanner2 = BeaconScanner(callback2, 
    device_filter=IBeaconFilter(uuid="2f234454-cf6d-4a0f-adf2-f4911ba9ffa6")

)
scanner3 = BeaconScanner(callback3, 
    device_filter=IBeaconFilter(uuid="2f4168bf-06f0-4832-8803-a8f8472d2479")
)
scanner1.start()
scanner2.start()
scanner3.start()
while(1):
    time.sleep(5)
scanner1.stop()
scanner2.stop()
scanner3.stop()

