import struct

class BinaryDecoder:
    def __init__(self, file_name):
        with open(file_name, 'rb') as file:
            self.data = file.read()
        self.pointer = 0

    def decode(self):
        result = []
        while self.pointer < len(self.data):
            item_type = self.data[self.pointer]
            self.pointer += 1
            if item_type == 0x04:  # 'null'
                result.append(None)
                self.pointer += 1  # Skip empty sequence
            elif item_type == 0x06:  # 'octets'
                length = struct.unpack("I", self.data[self.pointer:self.pointer + 4])[0]
                self.pointer += 4
                result.append(self.data[self.pointer:self.pointer + length])
                self.pointer += length
            elif item_type == 0x07:  # 'integer'
                result.append(struct.unpack("<I", self.data[self.pointer:self.pointer + 4])[0])
                self.pointer += 4
            elif item_type == 0x03:  # Dictionary
                num_items = struct.unpack("I", self.data[self.pointer:self.pointer + 4])[0]
                self.pointer += 4
                dictionary = {}
                for _ in range(num_items):
                    key = self.decode_string()
                    value = self.decode_value()
                    dictionary[key] = value
                result.append(dictionary)
            elif item_type == 0x05:  # List
                length = struct.unpack("I", self.data[self.pointer:self.pointer + 4])[0]
                self.pointer += 4
                array = []
                for _ in range(length):
                    array.append(self.decode_value())
                result.append(array)
        return result

    def decode_string(self):
        length = struct.unpack("I", self.data[self.pointer:self.pointer + 4])[0]
        self.pointer += 4
        return self.data[self.pointer:self.pointer + length].decode('utf-8')

    def decode_value(self):
        item_type = self.data[self.pointer]
        self.pointer += 1
        if item_type == 0x04:  # 'null'
            return None
        elif item_type == 0x06:  # 'octets'
            length = struct.unpack("I", self.data[self.pointer:self.pointer + 4])[0]
            self.pointer += 4
            return self.data[self.pointer:self.pointer + length]
        elif item_type == 0x07:  # 'integer'
            return struct.unpack("<I", self.data[self.pointer:self.pointer + 4])[0]
        elif item_type == 0x03:  # Dictionary
            num_items = struct.unpack("I", self.data[self.pointer:self.pointer + 4])[0]
            self.pointer += 4
            dictionary = {}
            for _ in range(num_items):
                key = self.decode_string()
                value = self.decode_value()
                dictionary[key] = value
            return dictionary
        elif item_type == 0x05:  # List
            length = struct.unpack("I", self.data[self.pointer:self.pointer + 4])[0]
            self.pointer += 4
            array = []
            for _ in range(length):
                array.append(self.decode_value())
            return array
