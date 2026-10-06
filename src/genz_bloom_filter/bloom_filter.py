import math
import bitarray
from genz_bloom_filter.integrations.hashing.built_in import BuiltInHash
from genz_bloom_filter.persistence import FileOperations
from pathlib import Path

class BloomFilter:

    def __init__(self, array_size: int, no_of_existing_items: int, file_operations: FileOperations, supported_hash: str = "hashlib",):
        self.array_size = array_size
        self.no_of_existing_items = no_of_existing_items
        self.no_of_required_hash_functions = self._get_hash_function_count()
        self.bit_array = bitarray.bitarray(self.array_size)
        self.bit_array.setall(0)
        self.supported_hashes = {"hashlib": BuiltInHash()}
        self.supported_hash = supported_hash
        self.file_operations = file_operations

    def __str__(self):
        return f"hash function count : {self.no_of_required_hash_functions}"

    def _get_hash_function_count(self):
        return round((self.array_size/self.no_of_existing_items)*round(math.log(2), 5))
    
    def exists(self, item: str) -> bool:
        # run all hash functions for the name and find it's value
        supplied_hash = self.supported_hashes.get(self.supported_hash)
        hash_indices = supplied_hash.get_hashes(item, self.array_size, no_of_hashes=self.no_of_required_hash_functions)
        bit_array = self.file_operations.load_file(self.array_size)
        for idx in hash_indices:
            if bit_array[idx] == 0:
                return False
        return True
    
    def set(self, item: str) -> None:
        supplied_hash = self.supported_hashes.get(self.supported_hash)
        hash_indices = supplied_hash.get_hashes(item, self.array_size, no_of_hashes=self.no_of_required_hash_functions)
        for idx in hash_indices:
            self.bit_array[idx] = 1
        self.file_operations.save_file(self.bit_array)


if __name__ == "__main__":
    array_size = 20
    no_of_existing_items = 1
    supported_hash = "hashlib"
    ROOT_PATH = Path(__file__).resolve().parent.parent
    file_path = f"{ROOT_PATH}/storage/bloom_filter_data.bin"
    file_operations = FileOperations(file_path=file_path)
    bf = BloomFilter(array_size, no_of_existing_items, file_operations, supported_hash)
    username = "apple00"
    print(f"before : {bf}")
    # bf.set(username)
    print(f"After : {bf}")
    print(f"username : {username} exists -> {bf.exists(username)}")


