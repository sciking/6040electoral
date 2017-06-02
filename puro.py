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
disp = 0
while i < 24: #Dunque 40 seggi, 16 dh
	print("Tornata %d"%(i+1))
	votp = random.randint(100,400)
	vots = random.randint(100,333)
	votd = random.randint(10,200)
	totp = totp + votp
	tots = vots + tots
	totd = totd + votd
	print("Voti popolari: ",votp)
	print("Voti socialisti: ",vots)
	print("Voti democristiani: ",votd)
	if votp > votd and votp > vots:
		seggip = seggip +1
		print("Seggio POPOLARE")
		if votd > vots:
			prod = prod + votd
			print("Proporzionale DEMOCRISTIANA")
			disp = disp + vots
		else:
			pros = pros + vots
			print("Proporzionale SOCIALISTA")
			disp = disp + votd
	if vots > votp and vots > votd:
		seggis = seggis +1
		print("Seggio SOCIALISTA")
		if votd > votp:
			prod = prod + votd
			print("Proporzionale DEMOCRISTIANA")
			disp = disp + votp
		else:
			prop = prop + votp
			print("Proporzionale POPOLARE")
			disp = disp + votd
	if votd > vots and votd > votp:
		seggid = seggid +1
		print("Seggio DEMOCRISTIANO")
		if votp > vots:
			prop = prop + votp
			print("Proporzionale POPOLARE")
			disp = disp + vots
		else:
			pros = pros + vots
			print("Proporzionale SOCIALISTA")
			disp = disp + votp
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
print("Voti DISPERSI: ",disp)
totel = totp + tots + totd
print("TOTALE VOTI: ",totel)
print "*"*35
sp = input("Inserire seggi proporzionali popolari:")
ss = input("Inserire seggi proporzionali socialisti:")
sd = input("Inserire seggi proporzionali democristiani:")
sp = sp+ seggip
sd = sd+ seggid
ss = ss+ seggis
print "*"*35
print("TOTALE SEGGI:")
print("Seggi popolari: ",sp)
print("Seggi socialisti: ",ss)
print("Seggi democristiani: ",sd)
