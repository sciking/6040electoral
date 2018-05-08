import random
import os
os.system("clear")
def proporzionale(a,b,c,d,e):
	global seggip, seggis, seggid
	seggi = a
	votitotali = b
	quoziente = int(votitotali/seggi)
	votia = c
	votib = d
	votic = e
	seggia = 0
	seggib = 0
	seggic = 0
	while votia >= quoziente:
		votia=votia-quoziente
		seggia = seggia+1
	while votib >= quoziente:
		votib=votib-quoziente
		seggib = seggib+1
	while votic >= quoziente:
		votic=votic-quoziente
		seggic = seggic+1

	resto = seggi-(seggia+seggib+seggic)
	while resto > 0:
		if votia > votib and votia > votic:
			votia = 0
			seggia = seggia+1
		if votib > votia and votib > votic:
			votib = 0
			seggib = seggib+1
		if votic > votia and votic > votib:
			votic = 0
			seggic = seggic+1
		resto = resto -1
	seggip = seggip+seggia
	seggis = seggis+seggib
	seggid = seggid+seggic
	

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
	votd = random.randint(50,250)
	totp = totp + votp
	tots = vots + tots
	totd = totd + votd
	print("Voti popolari: "+str(votp))
	print("Voti socialisti: "+str(vots))
	print("Voti democristiani: "+str(votd))
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
print "*"*35
print("RISULTATO FINALE")
print "*"*35
print("Uninominali popolari: "+str(seggip))
print("Uninominali socialisti: "+str(seggis))
print("Uninominali democristiani: "+str(seggid))
print "*"*35
print("Proporzionali popolari: "+str(prop))
print("Proporzionali socialisti: "+str(pros))
print("Proporzionali democristiani: "+str(prod))
print("Voti DISPERSI: "+str(disp))
print "*"*35
print("Voti popolari: "+str(totp))
print("Voti socialisti: "+str(tots))
print("Voti democristiani: "+str(totd))
totel = totp + tots + totd
propel = prop + pros + prod
print("TOTALE VOTI: "+str(totel))
proporzionale(16,propel,prop,pros,prod)
print "*"*35
print("TOTALE SEGGI:")
print("Seggi popolari: "+str(seggip))
print("Seggi socialisti: "+str(seggis))
print("Seggi democristiani: "+str(seggid))
print "*"*35
print("CON SISTEMA MERAMENTE PROPORZIONALE:")
seggip,seggis,seggis = 0,0,0
proporzionale(40,totel,totp,tots,totd)
print("Ipotetici popolari: "+str(seggip))
print("Ipotetici socialisti: "+str(seggis))
print("Ipotetici democristiani: "+str(seggid))
