import hashlib


def hash_calculation(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
        hash_hex = sha256_hash.hexdigest()
        return hash_hex
