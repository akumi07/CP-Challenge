import struct

class BinaryEncoder:
    def __init__(self):
        self.buffer = bytearray()

    def encode(self, data):
        if data is None:
            self.buffer.extend([0x04])  # 'null' type indicator
            self.buffer.extend([0x00])  # Empty sequence for None
        elif isinstance(data, bytes):
            self.buffer.extend([0x06])  # 'octets' type indicator
            self.buffer.extend(struct.pack("I", len(data)))  # Length of byte array
            self.buffer.extend(data)  # Byte data
        elif isinstance(data, int):
            self.buffer.extend([0x07])  # 'integer' type indicator
            self.buffer.extend(struct.pack("<I", data))  # Integer in little-endian
        elif isinstance(data, dict):
            self.buffer.extend([0x03])  # Dictionary type indicator
            self.buffer.extend(struct.pack("I", len(data)))  # Number of items in dictionary
            for key, value in data.items():
                self.encode_string(key)
                self.encode(value)
        elif isinstance(data, list):
            self.buffer.extend([0x05])  # List type indicator
            self.buffer.extend(struct.pack("I", len(data)))  # Length of list
            for item in data:
                self.encode(item)

    def encode_string(self, value):
        encoded_string = value.encode('utf-8')  # Encode string to bytes
        self.buffer.extend(struct.pack("I", len(encoded_string)))  # Add length as 4 bytes
        self.buffer.extend(encoded_string)  # Add the string bytes

    def save_to_file(self, file_path):
        with open(file_path, "wb") as f:
            f.write(self.buffer)

    def get_binary_as_hex(self):
        return " ".join(f"{byte:02x}" for byte in self.buffer)

