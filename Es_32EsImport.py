import random

alice = random.randint(1,6)
bob = random.randint(1,6)

print(alice, bob)
if(alice > bob):
    print(f"Ha vinto Alice")
else:
    print(f"Ha vinto Bob")



