import struct

class MACDecoder:
    def __init__(self):
        pass

    def decode_packet(self, packet):
        # Example packet decoding (this will need to be expanded)
        frame_control = struct.unpack('<H', packet[:2])[0]
        sequence_number = packet[2]
        address_info = packet[3:13]
        
        # Decode frame control
        frame_type = (frame_control >> 0) & 0x7
        security_enabled = (frame_control >> 3) & 0x1
        frame_pending = (frame_control >> 4) & 0x1
        ack_request = (frame_control >> 5) & 0x1
        intra_pan = (frame_control >> 6) & 0x1

        decoded_info = {
            'Frame Type': frame_type,
            'Security Enabled': security_enabled,
            'Frame Pending': frame_pending,
            'ACK Request': ack_request,
            'Intra-PAN': intra_pan,
            'Sequence Number': sequence_number,
            'Address Info': address_info.hex(),
        }
        return decoded_info

# Example usage
packet = b'\x61\x88\x01\x23\x45\x67\x89\xab\xcd\xef\x12\x34'
decoder = MACDecoder()
decoded_packet = decoder.decode_packet(packet)
print(decoded_packet)
import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MACDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("802.15.4 MAC Layer Decoder")

        self.decoder = MACDecoder()

        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.load_button = ttk.Button(self.frame, text="Load Packet", command=self.load_packet)
        self.load_button.grid(row=0, column=0, padx=5, pady=5)

        self.decode_button = ttk.Button(self.frame, text="Decode", command=self.decode_packet)
        self.decode_button.grid(row=0, column=1, padx=5, pady=5)

        self.result_text = tk.Text(self.frame, width=80, height=20)
        self.result_text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.pulse_button = ttk.Button(self.frame, text="Pulse Inspector", command=self.show_pulse_inspector)
        self.pulse_button.grid(row=2, column=0, padx=5, pady=5)

        self.iq_osc_button = ttk.Button(self.frame, text="IQ Oscilloscope", command=self.show_iq_oscilloscope)
        self.iq_osc_button.grid(row=2, column=1, padx=5, pady=5)

        self.iq_class_button = ttk.Button(self.frame, text="IQ Signal Classifier", command=self.show_iq_classifier)
        self.iq_class_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def load_packet(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'rb') as f:
                self.packet = f.read()
                self.result_text.insert(tk.END, f"Loaded packet: {self.packet.hex()}\n")

    def decode_packet(self):
        if hasattr(self, 'packet'):
            decoded_info = self.decoder.decode_packet(self.packet)
            self.result_text.insert(tk.END, f"Decoded packet: {decoded_info}\n")
        else:
            self.result_text.insert(tk.END, "No packet loaded.\n")

    def show_pulse_inspector(self):
        if hasattr(self, 'packet'):
            pulse_data = self.simulate_pulse_data()
            fig, ax = plt.subplots()
            ax.plot(pulse_data)
            ax.set_title('Pulse Inspector')
            ax.set_xlabel('Time')
            ax.set_ylabel('Amplitude')

            self.show_plot(fig)
        else:
            self.result_text.insert(tk.END, "No packet loaded.\n")

    def show_iq_oscilloscope(self):
        if hasattr(self, 'packet'):
            i_data, q_data = self.simulate_iq_data()
            fig, ax = plt.subplots()
            ax.plot(i_data, label='I Component')
            ax.plot(q_data, label='Q Component')
            ax.set_title('IQ Oscilloscope')
            ax.set_xlabel('Time')
            ax.set_ylabel('Amplitude')
            ax.legend()

            self.show_plot(fig)
        else:
            self.result_text.insert(tk.END, "No packet loaded.\n")

    def show_iq_classifier(self):
        if hasattr(self, 'packet'):
            classification = self.simulate_iq_classification()
            self.result_text.insert(tk.END, f"IQ Signal Classification: {classification}\n")
        else:
            self.result_text.insert(tk.END, "No packet loaded.\n")

    def simulate_pulse_data(self):
        # Simulate pulse data
        return np.sin(np.linspace(0, 20, 1000))

    def simulate_iq_data(self):
        # Simulate I and Q data
        t = np.linspace(0, 10, 1000)
        i_data = np.sin(t)
        q_data = np.cos(t)
        return i_data, q_data

    def simulate_iq_classification(self):
        # Simulate signal classification
        return 'Type A'

    def show_plot(self, fig):
        plot_window = tk.Toplevel(self.root)
        plot_canvas = FigureCanvasTkAgg(fig, master=plot_window)
        plot_canvas.draw()
        plot_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = MACDecoderApp(root)
    root.mainloop()
