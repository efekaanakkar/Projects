def Parola_Gücü(password):
    Güç_Puanı = 0

    if len(password) >= 10:
        Güç_Puanı += 3
    elif len(password) >= 8:
        Güç_Puanı += 2

    if any(harf.islower() for harf in password):
        Güç_Puanı += 1

    if any(harf.isupper() for harf in password):
        Güç_Puanı += 2

    if any(harf.isdigit() for harf in password):
        Güç_Puanı += 2

    Özel = "!@#$%^&*(),.?\":{}|<>"
    if any(harf in Özel for harf in password):
        Güç_Puanı += 2

    if Güç_Puanı <= 4:
        return " Zayıf", Güç_Puanı
    elif Güç_Puanı <= 7:
        return " Orta", Güç_Puanı
    else:
        return " Güçlü", Güç_Puanı



password = input("Şifreni gir: ")

result, Güç_Puanı = Parola_Gücü(password)

print("\nSonuç:", result)
print("Güç_Puanı:", Güç_Puanı, "/ 10")
