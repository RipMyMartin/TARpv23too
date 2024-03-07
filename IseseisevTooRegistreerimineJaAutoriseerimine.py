from MyModul import *

kasutajad = []
paroolid = []

while True:
    print("\n0 - Registreerimine\n1 - Autoriseerimine\n2 - Nime või parooli muutmine\n3 - Unustatud parooli taastamine\n4 - Lõpetamine")
    valik = input("Sisestage number: ")
    
    if valik == "4":
        break

    kasutajanimi = input("Sisestage kasutajanimi: ")

    if valik == "0":
        valik_parool = input("Kas soovite sisestada oma parooli (s) või lasta süsteemil genereerida parool (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            parool = salasona(12)
        registreeri_kasutaja(kasutajanimi, parool, kasutajad, paroolid)

    elif valik == "1":
        valik_parool = input("Kas soovite sisestada oma parooli (s) või lasta süsteemil genereerida parool (g)? ")
        if valik_parool.lower() == "s":
            parool = input("Sisestage parool: ")
        elif valik_parool.lower() == "g":
            sisselogimine(kasutajanimi, None, kasutajad, paroolid)

    elif valik == "2":
        vana_parool = input("Sisestage vana parool: ")
        uus_parool = input("Sisestage uus parool: ")
        muuda_parool(kasutajanimi, vana_parool, uus_parool, kasutajad, paroolid)

    elif valik == "3":
        uus_parool = input("Sisestage uus parool: ")
        unustatud_parool(kasutajanimi, uus_parool, kasutajad, paroolid)
