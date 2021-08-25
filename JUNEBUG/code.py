# SPDX-FileCopyrightText: 2021 ladyada  Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of sending and recieving data with the RFM95 LoRa radio.
# Author: Tony DiCola and Megan
import board
import time
import adafruit_rfm9x
import busio
import digitalio


# set the time interval (seconds) for sending packets
transmit_interval = 10

# Define radio parameters.
RADIO_FREQ_MHZ = 915.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip, use these if wiring up the breakout according to the guide:
# CS = digitalio.DigitalInOut(board.D5)
# RESET = digitalio.DigitalInOut(board.D6)
# Or uncomment and instead use these if using a Feather M0 RFM9x board and the appropriate
# CircuitPython build:
CS = digitalio.DigitalInOut(board.RFM9X_CS)
RESET = digitalio.DigitalInOut(board.RFM9X_RST)

# Define the onboard LED
LED = digitalio.DigitalInOut(board.D13)
LED.direction = digitalio.Direction.OUTPUT

# Initialize SPI bus.
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# Note that the radio is configured in LoRa mode so you can't control sync
# word, encryption, frequency deviation, or other settings!

# You can however adjust the transmit power (in dB).  The default is 13 dB but
# high power radios like the RFM95 can go up to 23 dB:
rfm9x.tx_power = 23

# enable CRC checking
rfm9x.enable_crc = True
# ask and set node addresses
fromid = 2
print("This feather is Node", fromid)
fromid = int(fromid)
rfm9x.node = fromid
toid = input("Please enter the node id of the desired receiving node:\n")
print("This feather is sending to Node", toid)
toid = int(toid)
rfm9x.destination = toid
# initialize counter
counter = 0
# send a broadcast message from my_node with ID = counter
rfm9x.send(bytes("startup message from node {} ".format(rfm9x.node), "UTF-8"))

# Send a packet.  Note you can only send a packet up to 252 bytes in length.
# This is a limitation of the radio packet size, so if you need to send larger
# amounts of data you will need to break it into smaller send calls.  Each send
# call will wait  the previous one to finish before continuing.
rfm9x.send(bytes("Startup message from node {}".format(rfm9x.node), "utf-8"))
print("Sent initial message!")

# Wait to receive packets.  Note that this library can't receive data at a fast
# rate, in fact it can only receive and process one 252 byte packet at a time.
# This means you should only use this  low bandwidth scenarios, like sending
# and receiving a single message at a time.
print("Waiting  packets...")
# initialize flad and timer
while True:
 #   packet = rfm9x.receive()
    # Look  a new packet: only accept if addresses to my_node
    packet = rfm9x.receive(with_header=True)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header):", [hex(x) for x in packet[0:4]])
        print("Received (raw payload): {0}".format(packet[4:]))
        print("Received RSSI: {0}".format(rfm9x.last_rssi))
        counter = counter + 1
        time.sleep(1)
        # send a  mesage to destination_node from my_node
        rfm9x.send(
            bytes(
                "message number {} from node {}".format(counter, rfm9x.node), "UTF-8"
            ),
            keep_listening=True,
        )
        print("sent message", counter)