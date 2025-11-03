# Schnorr-digital-signatures-and-verification
Schnorr Digital Signature is a cryptographic scheme used to authenticate a message using public-key cryptography.
Key Concepts

p: A large prime number

q: A large prime factor of (p − 1)

g: A generator of order q in the group (i.e., 
g^q≡1modp)
x: The private key (randomly chosen in [1, q−1])

y: The public key 
y=g^−xmodp
Step 1: Key Generation

Choose large primes 
𝑝
p and 
𝑞
q, with 
𝑞
∣
(
𝑝
−
1
)
q∣(p−1)

Choose generator 
𝑔
g of order 
𝑞
q

Choose private key 
𝑥
∈
[
1
,
𝑞
−
1
]
x∈[1,q−1]

Compute public key:y=g−xmodp
or sometimes 
𝑦=𝑔𝑥mod𝑝
depending on the convention
