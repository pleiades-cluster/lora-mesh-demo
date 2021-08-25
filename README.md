# loraMeshDemo
This repository is tracks the creation of a demonstration LoRa Mesh Network using hardware and software based on Adafruit's Feather M0 with the RFM95 radio modules operating at 915Mhz. This effort is currently led of engineers from CPP's Bronco Space group.

# Statement of Work

July 7, 2021

**Michael Pham**

_Bronco Space Lead Engineer_

**Megan Beck**

_Bronco Space SoW Leader_

1. **INTRODUCTION**

| General Details |
| --- |
| **Project Name** | Eta Tauri |
| **Project Lead** | Megan Beck (Bronco Space - mcbeck@cpp.edu) |
| **Period of Performance** | July 19th - August 19 2021 |
| **Overall Purpose** | Eta Tauri seeks to create a physical test bed for proposed satellite LoRa mesh networks, as a development project under the Pleiades CubeSat Cluster program.
The primary objective of Eta Tarui is to create a platform that shall enable terrestrial field testing of situational awareness and distributed sensing within a simulated spacecraft mesh network. |
| **Sponsor** | Michael Pham (Bronco Space - mlpham@cpp.edu) |
| **Budget Constraints** | Floor: | $ 500 |
| Target: | $ 1000 |
| Ceiling: | $ 5000 |

_ **Pleiades Cluster Background:** _

_The Pleiades CubeSat Cluster concept is a proposed investigation of methods to establish relative navigation and in space situational awareness for Small Satellite Swarms. As an extended concept, the methods tested by the Pleiades Cluster may also assist in the creation of space based collision avoidance and proximity operations systems to keep the orbits of Earth safe from runaway orbital debris. Additionally, as a multi-university collaboration using open source platforms, this mission acts as a wide scale opportunity to engage university students and establish pathways for student payloads to make their way to space._

_A demonstration mission has been formulated to test methods for a satellite to independently determine the size and shape of a swarm of satellites. Pleiades consists of eight spacecraft, and is intended to fill a standard 12U &quot;Quadpack&#39;&#39; CubeSat deployer. These eight spacecraft will consist of two 3U &quot;Seekers&quot; and six 1U &quot;Snitches.&quot; A combination of LoRa radio schemes, LED&#39;s, and optical cameras shall be used to establish the in space situational awareness of the satellite swarm._

1. **SCOPE OF WORK**

A mesh network demonstration system is a key milestone towards achieving the proposed Pleiades CubeSat Cluster mission. Eta Tauri seeks to produce a test bed that shall facilitate the terrestrial testing of mesh network software with engineering samples of the spacecraft architectures to be utilized for the Pleiades mission.

**Table 1: Minimum Success Criteria**

| **#** | **Criteria** |
| --- | --- |
| **M.1** | A stand alone system that can form and maintain a **mesh network** consisting of one or more **gateways** and three or more **remote nodes** |
| **M.2** | Gateways receive and log 1000 unique packets of data |
| **M.3** | Remote nodes transmit locally acquired state data (i.e. location, orientation, temperature, etc.) |
| **M.4** | 100 packets are successfully transmitted and received with an inter-node distance of 1km or more |

**Table 2: Extended Success Criteria**

| **#** | **Criteria** |
| --- | --- |
| **E.1** | System operates autonomously without significant failure for 24 hours with no human intervention |
| **E.2** | System operates as power positive without external electrical hookups |
| **E.3** | 10 or more data packets are received from a remote note mounted to a moving vehicle |
| **E.4** | Gateway estimates range to remote nodes with an accuracy of + 1% |
| **E.4** | 100 packets are successfully transmitted and received with an inter-node distance of 10km or more |

Creation of functioning protoflight or flight hardware is not within the scope of Eta Tauri, but the selection of demonstration hardware that may be retrofitted for protoflight purposes is strongly preferred.

It is anticipated that the demonstration system shall use or approximate the hardware architectures selected for the Pleiades CubeSat Cluster. Specifically that the **remote nodes** shall be a PyCubed based or comparable platform (microcontroller using Circuit Python or similar embedded programming language), and that the **gateways** shall be OreSat or comparable platform (i.e. Beaglebone, Jetson, Raspberry Pi, or other Linux embedded system).

Work may be completed at the Cal Poly Pomona campus within the Bronco Space Space Systems Lab (at the convenience of the Head Analyst of the Laboratory) or at any other location arranged by the project lead. Consistent with access to the Space Systems Lab is access to lab assets such as the mini lathe, reflow oven, 3D printers, etc. The project lead may also create new agreements for access and / or usage of commercial or community facilities at their own discretion so long as there is no direct quid pro quo between an external entity and Bronco Space as an entity. New agreements with entities at Cal Poly Pomona must be managed through the Head Analyst of the Laboratory.

**Node:** A node is defined as a single point within the communications network that may send or receive data.

**Gateway:** A gateway is defined as a node within the communications network that not only sends and receives data within the network, but also sends and receives data to an external network such as the internet.

**Mesh Network:** A mesh network is defined as a wireless network that is able to connect nodes dynamically and non-hierarchically to optimize the relay of information as efficiently as possible. Within the scope of Eta Tauri it is presumed the mesh network architecture shall use LoRaWAN or a similar protocol.