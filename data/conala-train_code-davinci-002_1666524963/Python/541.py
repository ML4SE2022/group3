import hashlib

# Create a hash object
h = hashlib.md5()

# Update the hash with the string "Hello World"
h.update("Hello World")

# Get the digest of the hash
digest = h.digest()

# Create a new key with the digest as the key name
key = Key(bucket, digest)

# Set the contents of the key to "Hello World"
key.set_contents_from_string("Hello World")