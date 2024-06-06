# 802.15.4 MAC Layer Decoder

## Introduction

Welcome to the 802.15.4 MAC Layer Decoder! This application is designed to decode and visualize the MAC layer packets of the IEEE 802.15.4 standard, which is widely used in wireless communication protocols such as ZigBee and 6LoWPAN. The application also includes tools for inspecting pulse signals, visualizing I/Q components, and classifying signals.

## Features

- **MAC Layer Packet Decoding**: Parse and decode various fields in the 802.15.4 MAC layer packets.
- **Pulse Inspector**: Visualize pulse signals from the packets.
- **IQ Oscilloscope**: Visualize in-phase (I) and quadrature (Q) components of the signal.
- **IQ Signal Classifier**: Classify signals based on their characteristics.

## Installation

To run this application, you need to have Python installed on your system. The required Python version is 3.x. You also need to install Tkinter and Matplotlib.

### Steps to Install

1. **Clone the Repository**
2. Install Dependencies
Install the required Python packages using pip:pip install tk matplotlib
3. pip install tk matplotlib
4. run the app.

   Usage
Loading a Packet

    Launch the application.
    Click on the "Load Packet" button to load a packet file. This should be a binary file containing the packet data.

Decoding a Packet

    After loading a packet, click on the "Decode" button to parse and display the packet details in the text area.

Inspecting Pulse Signals

    Click on the "Pulse Inspector" button to visualize the pulse signals from the packet.
    A new window will open displaying the pulse signal plot.

Visualizing IQ Components

    Click on the "IQ Oscilloscope" button to visualize the in-phase (I) and quadrature (Q) components of the signal.
    A new window will open displaying the IQ component plot.

Classifying Signals

    Click on the "IQ Signal Classifier" button to classify the signal.
    The classification result will be displayed in the text area.

Code Structure

    mac_decoder.py: Contains the MACDecoder class responsible for decoding 802.15.4 MAC layer packets.
    mac_decoder_app.py: Contains the main application logic, including the Tkinter UI setup and event handling.
    README.md: This file, providing an extensive explanation of the application.

Example Packet

For demonstration purposes, you can use the following example packet data in hexadecimal:61 88 01 23 45 67 89 ab cd ef 12 34

Save this data in a binary file and load it using the "Load Packet" button in the application.

Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

