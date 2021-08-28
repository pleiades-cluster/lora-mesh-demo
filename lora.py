import board
import time
import adafruit_rfm9x
import busio
import digitalio

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0
CS = digitalio.DigitalInOut(board.RFM9X_CS)
RESET = digitalio.DigitalInOut(board.RFM9X_RST)
# Define the onboard LED
LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT
# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
# Initialze RFM radio
radio = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)
radio.tx_power = 18
radio.enable_crc = True
print("Radio Initizalied")


print("Sending startup broadcast to all nodes")
radio.send(bytes("startup message", "UTF-8"))


def setNode(node):
    radio.node = node
    print("This feather is Node", radio.node)

def setPower(tx_power):
    radio.tx_power = tx_power


def send(message,destination = 255):
    print("This feather is sending to Node", destination)
    radio.send(
        bytes(
            message, "UTF-8"
        ),
        keep_listening=True,
        destination = destination,
    )

def listen():
    # initialize counter
    counter = 0
    print("Waiting  packets...")
    while True:
        # Look  a new packet: only accept if addresses to my_node
        packet = radio.receive(with_header=True)
        # If no packet was received during the timeout then None is returned.
        if packet is not None:
            # Received a packet!
            # Print out the raw bytes of the packet:
            print("Received (raw header):", [hex(x) for x in packet[0:4]])
            print("Received (raw payload): {0}".format(packet[4:]))
            print("Received RSSI: {0}".format(radio.last_rssi))
            counter = counter + 1