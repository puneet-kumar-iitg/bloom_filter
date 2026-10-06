from bitarray import bitarray

class FileOperations:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_file(self, bit_array: bitarray):
        with open(self.file_path, "wb") as fp:
            bit_array.tofile(fp)
    
    def load_file(self, array_size: int):
        bit_array = bitarray()
        with open(self.file_path, 'rb') as fp:
            bit_array.fromfile(fp)
        
        # Handle potential padding (files store whole bytes, so it might read up to 7 extra 0 bits)
        if len(bit_array) > array_size:
            bit_array = bit_array[:array_size]
        
        return bit_array
