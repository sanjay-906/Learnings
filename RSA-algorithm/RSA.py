# RSA Algorithm
import random
import math


def is_prime(a):
    b=2
    prime= True
    while(b!=a):
        if a%b ==0:
            prime= False
            break;
        b=b+1
    if prime:
        return True

    return False


def generate_prime(min_val, max_val):
    prime= random.randint(min_val, max_val)
    while not is_prime(prime):
        prime= random.randint(min_val, max_val)

    return prime


def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d*e)% phi ==1:
            return d
    raise ValueError("Can not calculate Inverse")


p, q= generate_prime(1000, 5000), generate_prime(1000, 5000)

while p==q:
    q= generate_prime(1000, 5000)
print('p:', p, 'q:',q)
n= p*q

phi= (p-1)*(q-1)


e= random.randint(3, phi-1)
while math.gcd(e, phi) !=1:
    e= random.randint(3, phi-1)

print('phi:',phi,'e:',e)
d= mod_inverse(e, phi)
print('d:', d)

#convert to ASCII
message= "Earth is Flat"
message_encoded= [ord(ch) for ch in message]

#(m^e)mod n= cipher

ciphertext= [pow(ch,e,n) for ch in message_encoded]

print("Cipher Text:",ciphertext)

message_encoded= [pow(ch, d, n) for ch in ciphertext]
message= "".join(chr(ch) for ch in message_encoded)

print("Original Message:",message)
