from genz_bloom_filter.integrations.hashing.base import Hashing

class HashStrategy:
    
    def __init__(self, hash: Hashing):
        self.hash = hash

    def get_hashes(self, item:str, array_size:int, no_of_hashes:int):
        return self.hash.get_hashes(item, array_size, no_of_hashes)

        