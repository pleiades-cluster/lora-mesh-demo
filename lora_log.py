# Packet Logger for Radio Bonnet
import time
import busio
from digitalio import DigitalInOut, Direction, Pull
import board
# Import the SSD1306 module.
import adafruit_ssd1306
# Import the RFM9x radio module.
import adafruit_rfm9x


# Configure RFM9x LoRa Radio
CS = DigitalInOut(board.CE1)
RESET = DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)


# Attempt to set up the RFM9x Module
try:
    rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, 915.0)
except RuntimeError as error:
    # Thrown on version mismatch
    print('RFM9x Error: ', error)
rfm9x.node = 69
file=open("packetstorage.csv","w")
# initialize counter
counter = 0
print("Waiting  packets...")




while counter < 1000:
    file=open("packetstorage.csv","a")
    # Look  a new packet: only accept if addresses to my_node
    packet = rfm9x.receive(with_header=True)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header):", str([hex(x) for x in packet[0:4]]))
        print("Received (raw payload): {0}".format(packet[4:]))
        print("Received RSSI: {0}".format(rfm9x.last_rssi))
        print(packet[4:].decode("utf-8"))
        packet_str = str(packet[4:].decode("utf-8"))
        print(packet_str, ",", counter)

        file.write(packet_str + "," + str(counter) + ",\n")

        #file.write("Received (raw header):" + str([hex(x) for x in packet[0:4]]))
        #file.write('\n')
        #file.write("Received (raw payload): {0}".format(packet[4:]))
        #file.write('\n')
        #file.write("Received RSSI: {0}".format(rfm9x.last_rssi))
        #file.write('\n')
        #file.write("Received Counter:" + counter)
        #file.write('\n')
        
        counter = counter + 1
        file.close()
