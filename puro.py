import random
import os
os.system("clear")
i = 0
seggip = 0
seggis = 0
seggid = 0
prop = 0
pros = 0
prod = 0
totp = 0
totd = 0
tots = 0
while i < 24: #Dunque 40 seggi, 16 dh
	print("Tornata %d"%(i+1))
	votp = random.randint(100,333)
	vots = random.randint(100,333)
	votd = random.randint(100,333)
	totp = totp + votp
	tots = vots + tots
	totd = totd + votd
	print("Voti popolari: ",votp)
	print("Voti socialisti: ",vots)
	print("Voti democristiani: ",votd)
	if votp > votd and votp > vots:
		seggip = seggip +1
		if votd > vots:
			prod = prod + votd
		else:
			pros = pros + vots
	if vots > votp and vots > votd:
		seggis = seggis +1
		if votd > votp:
			prod = prod + votd
		else:
			prop = prop + votp
	if votd > vots and votd > votp:
		seggid = seggid +1
		if votp > vots:
			prop = prop + votp
		else:
			pros = pros + vots
	i = i + 1
print("RISULTATO FINALE")
print "*"*35
print("Seggi popolari: ",seggip)
print("Seggi socialisti: ",seggis)
print("Seggi democristiani: ",seggid)
print "*"*35
print("Proporzionali popolari: ",prop)
print("Proporzionali socialisti: ",pros)
print("Proporzionali democristiani: ",prod)
print "*"*35
print("Voti popolari: ",totp)
print("Voti socialisti: ",tots)
print("Voti democristiani: ",totd)
totel = totp + tots + totd
print("TOTALE VOTI: ",totel)
