from Szamitogep import Szamitogep

peldany_1 = Szamitogep("win", 32)
peldany_2 = Szamitogep("mac", 16)
peldany_3 = Szamitogep("win", 16)
szamitogepek = []
szamitogepek.append(peldany_1)
szamitogepek.append(peldany_2)
szamitogepek.append(peldany_3)
for i in range(len(szamitogepek)):
    oprsz = szamitogepek[i].oprsz
    ram = szamitogepek[i].ram
    print(f"oprendszer:{oprsz} ram: ({ram})")
#összegzés tétele----------------------------------------------------------------
print("Átlag: ", end="")
gyujto = 0
for i in range(len(szamitogepek)):
    gyujto += szamitogepek[i].ram
print(f"{round(gyujto/len(szamitogepek),3)}")


#maximum kiválasztás tétele--------------------------------------------------------
print("Legtöbb ramot tartalmazó oprendszer: ", end="")
index = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > szamitogepek[index].ram:
        index = i
oprsz = szamitogepek[index].oprsz
print(f"{oprsz}")
#megszámlálás tétel-----------------------------------------------------------------

print("Hány  Windows gépünk van? ", end="")
ures = 0
for i in range(len(szamitogepek)):
    if szamitogepek[i].oprsz == "win":
        ures +=1

print(f"{ures} db Windowzos gépünk van")


#eldőntés tétel---------------------------------------------------------------------
vizsgalt_ram = 22
print(f"Van-e {vizsgalt_ram} GB-nal nagyobb Windows? ", end="")

ivh = False
for i in range(len(szamitogepek)):
    if szamitogepek[i].ram > vizsgalt_ram and szamitogepek[i].oprsz == "win":
        ivh = True


if ivh == True:
    print("Van ilyen gép")
else:
    print("Nincs ilyen gép")