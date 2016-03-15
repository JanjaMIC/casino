pozdravni_tekst = "Dobrodosel v Casino Clubu! Registriraj se in zmagaj Audija Q8"
pozdrav_ime = "Dobrodosla "
print pozdravni_tekst

registracija = raw_input("Prosimo vpisite svoje ime in priimek: ")

mail = raw_input("Prosimo zaupajte nam vas e-mail: ")

print pozdrav_ime + registracija

napoved_igre = "Uganite skrito petmestno stevilko in podarimo vam 100 evrov bonusa za igre na nasih slotih!"

print napoved_igre

vpis_stevilke = raw_input("Zmagovalna stevilka je: ")

zmagovalna_stevilka = "12345"

while vpis_stevilke != zmagovalna_stevilka:
    print("Zal, ne!  Poizkusite ponovno!")
    vpis_stevilke = raw_input("Zmagovalna stevilka je: ")

else:
    print ("Cestitamo. Imate pa res sreco! Uganili ste.Na kartici vas caka 100 eur, ki jih lahko porabite na nasih slotih do konca meseca.")







