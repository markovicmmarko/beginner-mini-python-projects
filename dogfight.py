import random

class Airplane:
    def __init__(self,name,health,ammo):
        self.name   = name
        self.health = health
        self.ammo   = ammo

    def shoot(self,airplane2):
        x = random.randint(1,10)
        self.ammo -= x
        airplane2.health -= x*2
        return self.ammo < 0 or self.health < 0   
        

su = Airplane("Sukhoi",100,100)
f_16 = Airplane("Fighting Falcon",100,100)
airplanes = [su,f_16]

print(f"round\tname      \thealth/ammo\t:\tname      \thealth/ammo")
print(f"***************************************************************************")

round = 0
while True:
    round += 1
    su.shoot(f_16)
    f_16.shoot(su)
    print(f"{round}\t{su.name}\t{su.health}/{su.ammo}\t\t\t\t{f_16.name}\t\t{f_16.health}/{f_16.ammo}")
    if su.shoot(f_16) or f_16.shoot(su):
        break
    else:
        continue
    
