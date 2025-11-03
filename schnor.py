import create_keypair as ckp
import schnorr_lib as sl



n_keys = int(input("Insert the number of keys to be generated:"))

ckp.create_keypair(n_keys)["users"]

user = ckp.create_keypair(1)["users"]

M = input("Insert the message to sign:")
M = sl.sha256(M.encode())

sig = sl.schnorr_sign(M, user[0]["privateKey"])

print("PublicKey =",user[0]["publicKey"])
print("Signature =",sig.hex())
n_keys = int(input("Insert the number of keys to be generated:"))
users = ckp.create_keypair(n_keys)["users"]

M = input("Insert the message to sign:")
M = sl.sha256(M.encode())

sig, X = sl.schnorr_musig_sign(M, users)

print("Aggregated key =",X.hex())
print("Signature =",sig.hex())
M = input("Insert the message to verify:")
M = sl.sha256(M.encode())

pubkey = input("Insert the public key (or the aggregated key if MuSig was used):")
pubkey_bytes = bytes.fromhex(pubkey)

sig = input("Insert the generated sign:")
sig_bytes = bytes.fromhex(sig)

result = sl.schnorr_verify(M, pubkey_bytes, sig_bytes)

if result:
    print("The signature is VALID for this message and this public key")
else:
    print("The signature is NOT VALID for this message and this public key")
