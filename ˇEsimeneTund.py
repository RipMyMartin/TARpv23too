print("Tere maailm")
#1
#nimi=input("Mis on sinu nimi?") #comment
#vanus=int(input("kui vana sa oled?")) #float()->2.5
#print("Tere tulemast!" +nimi+". Sa oled"+str(vanus)+" aastat vana")
#print("Tere tulemast!" ,nimi,". Sa oled",vanus,"aastat vana")
#print("Tere tulemast! {0} Sa oled {1} aastat vana".format(nimi, vanus))
#print("muutuja vanus=",vanus,",t��p on",type(vanus))
#2
#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_k�ib_koolis = True
#print("muutuja vanus=",vanus,",t��p on",type(vanus))
#print("muutuja vanus=",eesnimi,",t��p on",type(eesnimi))
#print("muutuja vanus=",pikkus,",t��p on",type(pikkus))
#print("muutuja vanus=",kas_k�ib_koolis,",t��p on",type(kas_k�ib_koolis))

#3
from random import *
kokku=randint(10,100)
print("kokku",kokku)
mitu=int(input("Mitu kommi tahad v�tta?"))
kokku-=mitu
print("N��d laua peal on",kokku,"kommi")
#4
�mberm��t = float(input("kirjutage puu umberm��t: "))
diameeter = �mberm��t / 3.14159
print("Puu diameeter:", diameeter)
#5
N = float(input("Sisestage ristk�liku pikkus N meetrites: "))
M = float(input("Sisestage ristk�liku laius M meetrites: "))
diagonaali_pikkus = (N ** 2 + M ** 2) ** 0.5
print("Ristk�liku diagonaali pikkus on:", diagonaali_pikkus , "meetrit")
#6
try:
    aeg = float(input("Mitu tundi kulus s�iduks? "))
    teepikkus = float(input("Mitu kilomeetrit s�itsid? "))
    kiirus = teepikkus / aeg
    print("sinu kiirus oli" + str(kiirus) + " km/h")
    except:
        print("viga andmet��b")

print("The average is:", average)
#8
#   @..@
#  (----)
#  ( \__/ )
# ^^ "" ^^
#9
a=float(input("Sisestage numbrit: "))
b = float(input("Sisestage numbrit: "))
c = float(input("Sisestage numbrit: "))
P = a + b + c
print(P)
#10
hinnang = 12.90
jootraha_protsent = 10
kokku = hinnang + (hinnang * (jootraha_protsent / 100))
iga�ks_makseb = kokku / 2
print("Iga�ks peab maksma:", iga�ks_makseb, "eurot")













try:
   aeg = float(input("Mitu tundi kulus s�iduks? "))
   teepikkus = float(input("Mitu kilomeetrit s�itsid? kiirus")
   kiirus = teepikkus/aeg
   print("sinu kiirus oli" + str(kiirus) + " km/h")

except :
    print("viga andmet��biga")


    print()
