import struct

class BinaryEncoder:
    def __init__(self):
        self.data = bytearray()

    def encode_int(self, value):
        self.data.extend(struct.pack('>i', value))

    def encode_float(self, value):
        self.data.extend(struct.pack('>f', value))

    def encode_string(self, value):
        encoded_str = value.encode('utf-8')
        self.data.extend(struct.pack('>i', len(encoded_str)))
        self.data.extend(encoded_str)

    def save_to_file(self, file_name):
        with open(file_name, 'wb') as file:
            file.write(self.data)
