import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from encoder import BinaryEncoder
from decoder import BinaryDecoder


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
        self.file_button = tk.Button(self.root, text="Choose File", command=self.select_file)
        self.file_button.grid(row=1, column=1, padx=10, pady=10)

        # Decode Section
        self.decode_button = tk.Button(self.root, text="Decode Binary File", command=self.decode_file)
        self.decode_button.grid(row=2, column=1, padx=10, pady=10)

        # Output Section
        tk.Label(self.root, text="Output").grid(row=3, column=0, padx=10, pady=10)
        self.output_text = tk.Text(self.root, height=10, width=60)
        self.output_text.grid(row=3, column=1, padx=10, pady=10)

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
                encoder.encode_string(data)  # Handle strings correctly

            save_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary Files", "*.bin")])
            if save_path:
                encoder.save_to_file(save_path)
                messagebox.showinfo("Success", "Data encoded and saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encode data: {e}")

    def select_file(self):
        # Select a CSV or text file for encoding
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Text Files", "*.txt")])
        if file_path:
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
                save_path = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary Files", "*.bin")])
                if save_path:
                    encoder.save_to_file(save_path)
                    messagebox.showinfo("Success", "File encoded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to encode file: {e}")

    def decode_file(self):
        # Decode a binary file
        file_path = filedialog.askopenfilename(filetypes=[("Binary Files", "*.bin")])
        if file_path:
            decoder = BinaryDecoder(file_path)
            try:
                decoded_data = []
                while decoder.pointer < len(decoder.data):
                    # Safely decode data based on type
                    if decoder.pointer + 4 <= len(decoder.data):  # Check for enough bytes for a length-prefixed string
                        try:
                            decoded_data.append(f"String: {decoder.decode_string()}")
                        except ValueError:
                            break
                    else:
                        # End of file or invalid format
                        break

                # Display the decoded data
                if decoded_data:
                    self.output_text.delete(1.0, tk.END)
                    self.output_text.insert(tk.END, "\n".join(decoded_data))
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
