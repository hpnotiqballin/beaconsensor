# test BLE Scanning software
# jcs 6/8/2014
# det 12/29/2019, added functionality to send presence events to hub via HTTP GET


import blescan
import sys
import requests


import bluetooth._bluetooth as bluez


dev_id = 0
try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"


except:
        print "error accessing bluetooth device..."
        sys.exit(1)


blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

count = 0

while True:
        returnedList = blescan.parse_events(sock, 10)
        for beacon in returnedList:
                  value = beacon.find("")
                  if value > -1:
                      requests.get('arrived')
                      count = 0
                  elif value <= -1:
                      count += 1
                  if count == 300:
                      requests.get('departed')             
