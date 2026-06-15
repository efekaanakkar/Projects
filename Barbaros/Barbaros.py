import re

def Parola_Gücü(password):
    score = 0

    # Uzunluk Kontrolü
    if len(password) >= 8:
        score += 2
    if len(password) >= 10:
        score += 3

    # Küçük Harf Kontrolü
    if re.search(r"[a-z]", password):
        score += 1

    # Büyük Harf Kontrolü
    if re.search(r"[A-Z]", password):
        score += 2

    # Rakam Kontrolü
    if re.search(r"[0-9]", password):
        score += 2

    # Özel Karakter Kontrolü
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2

    # Sonuçlar
    if score <= 4:
        return "🔴 Zayıf", score
    elif score <= 7:
        return "🟡 Orta", score
    else:
        return "🟢 Güçlü", score



password = input("Şifreni gir: ")

result, score = Parola_Gücü(password)

print("\nSonuç:", result)
print("Skor:", score, "/ 10")
