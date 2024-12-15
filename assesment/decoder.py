import struct


class BinaryDecoder:
    def __init__(self, file_name):
        with open(file_name, 'rb') as file:
            self.data = file.read()
        self.pointer = 0

    def decode_int(self):
        value = struct.unpack('>i', self.data[self.pointer:self.pointer + 4])[0]
        self.pointer += 4
        return value

    def decode_float(self):
        value = struct.unpack('>f', self.data[self.pointer:self.pointer + 4])[0]
        self.pointer += 4
        return value

    def decode_string(self):
        length = self.decode_int()
        value = self.data[self.pointer:self.pointer + length].decode('utf-8')
        self.pointer += length
        return value
