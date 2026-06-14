import re

def password_strength(password):
    score = 0

    # Uzunluk
    if len(password) >= 8:
        score += 2
    if len(password) >= 12:
        score += 3

    # Küçük harf
    if re.search(r"[a-z]", password):
        score += 1

    # Büyük harf
    if re.search(r"[A-Z]", password):
        score += 1

    # Rakam
    if re.search(r"[0-9]", password):
        score += 1

    # Özel karakter
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2

    # Sonuç
    if score <= 4:
        return "🔴 Zayıf", score
    elif score <= 7:
        return "🟡 Orta", score
    else:
        return "🟢 Güçlü", score


# Kullanıcıdan şifre al
password = input("Şifreni gir: ")

result, score = password_strength(password)

print("\nSonuç:", result)
print("Skor:", score, "/ 6")
