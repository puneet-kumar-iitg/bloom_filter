from genz_bloom_filter.integrations.hashing.base import Hashing
import hashlib

class BuiltInHash(Hashing):

    def get_hashes(self, item: str, array_size: int, no_of_hashes: int):

        item_str = str(item)
        hash_indices = []
        for i in range(no_of_hashes):
            salted_str = f"{item_str}:{i}"
            # ensure that no matter what machine our code runs on, the text is translated into the exact same sequence of bytes every time.
            byte_str = salted_str.encode('utf-8')
            # Generate a massive 256-bit hexadecimal hash string
            hash_hex = hashlib.sha256(byte_str).hexdigest()
            # Convert the hex string into a large integer
            hash_int = int(hash_hex, 16)

            index = hash_int % array_size
            hash_indices.append(index)
        return hash_indices


