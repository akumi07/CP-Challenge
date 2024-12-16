import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from encoder import BinaryEncoder
from decoder import BinaryDecoder
import threading
import queue


class EncoderDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Encoder/Decoder")
        self.create_widgets()

    def create_widgets(self):
        # Input Section
        tk.Label(self.root, text="Manual Input").grid(row=0, column=0, padx=10, pady=10)
        self.input_field = tk.Entry(self.root, width=40)
        self.input_field.grid(row=0, column=1, padx=10, pady=10)

        self.encode_button = tk.Button(self.root, text="Encode", command=self.encode_manual)
        self.encode_button.grid(row=0, column=2, padx=10, pady=10)

        # File Selection Section
        tk.Label(self.root, text="Select File").grid(row=1, column=0, padx=10, pady=10)
        self.file_button = tk.Button(self.root, text="Choose File to Encode", command=self.select_file)
        self.file_button.grid(row=1, column=1, padx=10, pady=10)

        # Decode Section
        self.decode_button = tk.Button(self.root, text="Choose File to Decode", command=self.decode_file)
        self.decode_button.grid(row=2, column=1, padx=10, pady=10)

        # Output Section
        tk.Label(self.root, text="Output").grid(row=3, column=0, padx=10, pady=10)
        self.output_text = tk.Text(self.root, height=10, width=60)
        self.output_text.grid(row=3, column=1, padx=10, pady=10)

        # Scrollbar for Output Section
        self.scrollbar = tk.Scrollbar(self.root, command=self.output_text.yview)
        self.scrollbar.grid(row=3, column=2, sticky="ns", padx=10, pady=10)
        self.output_text.config(yscrollcommand=self.scrollbar.set)

    def encode_manual(self):
        # Encode data from manual input
        encoder = BinaryEncoder()
        data = self.input_field.get()

        try:
            if data.isdigit():
                encoder.encode_int(int(data))
            elif self.is_float(data):
                encoder.encode_float(float(data))
            else:
                encoder.encode_string(data)

            # Save to file
            save_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary Files", "*.bin")])
            if save_path:
                encoder.save_to_file(save_path)

                # Show encoded binary in output
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, "Encoded Binary Data (Hex):\n")
                self.output_text.insert(tk.END, encoder.get_binary_as_hex())

                messagebox.showinfo("Success", "Data encoded and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encode data: {e}")

    def select_file(self):
        # Select a CSV or text file for encoding
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt")])
        if file_path:
            # Create a queue for communication between thread and main GUI thread
            self.queue = queue.Queue()

            # Start a background thread for CSV encoding to keep the GUI responsive
            threading.Thread(target=self.encode_file_in_background, args=(file_path,), daemon=True).start()

            # Show a "saving" message while the encoding is happening
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "Encoding... Please wait...\n")

    def encode_file_in_background(self, file_path):
        encoder = BinaryEncoder()

        try:
            if file_path.endswith(".csv"):
                df = pd.read_csv(file_path)
                for _, row in df.iterrows():
                    for value in row:
                        if isinstance(value, int):
                            encoder.encode_int(value)
                        elif isinstance(value, float):
                            encoder.encode_float(value)
                        else:
                            encoder.encode_string(str(value))
            else:
                with open(file_path, 'r') as file:
                    for line in file:
                        encoder.encode_string(line.strip())

            # Save encoded binary data to file
            save_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary Files", "*.bin")])
            if save_path:
                encoder.save_to_file(save_path)

                # Send data back to the main GUI thread
                self.queue.put(encoder.get_binary_as_hex())
                self.queue.put("File encoding completed successfully!")

        except Exception as e:
            self.queue.put(f"Failed to encode file: {e}")

        # Check the queue and update the GUI once encoding is complete
        self.update_output()

    def update_output(self):
        try:
            # Get the encoded binary data or error message from the queue
            message = self.queue.get_nowait()
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, message)
        except queue.Empty:
            self.output_text.after(100, self.update_output)

    def decode_file(self):
        # Select a binary file to decode
        file_path = filedialog.askopenfilename(filetypes=[("Binary Files", "*.bin")])
        if file_path:
            decoder = BinaryDecoder(file_path)
            try:
                decoded_data = decoder.decode()  # This will decode based on type info
                # Display the decoded data in the output section
                if decoded_data:
                    self.output_text.delete(1.0, tk.END)
                    self.output_text.insert(tk.END, "\n".join(map(str, decoded_data)))
                else:
                    messagebox.showinfo("Result", "No valid data found in the file.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to decode file: {e}")

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    root = tk.Tk()
    app = EncoderDecoderApp(root)
    root.mainloop()
