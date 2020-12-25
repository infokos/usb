# sudo apt-get install python-pip
# sudo pip2 install base58

# importing binascii to be able to convert hexadecimal strings to binary data
import binascii
import hashlib
import base58
import sys

# Step 1: here we have the private key
private_key_static = sys.argv[1]
# Step 2: let's add 80 in front of it
extended_key = "80"+private_key_static
# Step 3: first SHA-256
first_sha256 = hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
# Step 4: second SHA-256
second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
# Step 5-6: add checksum to end of extended key
final_key = extended_key+second_sha256[:8]
# Step 7: finally the Wallet Import Format is the base 58 encode of final_key
WIF = base58.b58encode(binascii.unhexlify(final_key))

print (WIF)
print ("_________________________________")
print ("Donations for BTC: 1QELWathdM9BNUNG9afmgHmMc5L49V6FMo")