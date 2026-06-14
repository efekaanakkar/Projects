# ⚓ BARBAROS - Şifre Güçlülük Analiz Aracı

Barbaros, kullanıcıların belirlediği şifrelerin güvenliğini siber güvenlik standartlarına göre test eden, Python3 ile yazılmış hafif ve etkili bir komut satırı aracıdır. Şifrenizin uzunluğunu, barındırdığı karakter çeşitliliğini (büyük/küçük harf, rakam, özel karakter) analiz ederek bir güç skoru çıkartır.

---

## 🧭 Analiz Kriterleri & Skor Tablosu

Barbaros, şifrenizi şu metriklere göre değerlendirir:

* 📏 **Uzunluk Kontrolü:** Şifre en az 8 karakter ise (+2 puan), 12 karakter veya üzerindeyse (+3 puan).
* 🔤 **Karakter Çeşitliliği:** * Küçük harf içeriyorsa (`[a-z]`) (+1 puan)
  * Büyük harf içeriyorsa (`[A-Z]`) (+1 puan)
  * Rakam içeriyorsa (`[0-9]`) (+1 puan)
  * Özel karakter içeriyorsa (`!@#$%^&*` vb.) (+2 puan)

### 📊 Güvenlik Seviyeleri

| Skor (Maks: 6) | Durum | Açıklama |
| :--- | :--- | :--- |
| **0 - 4 Puan** | 🔴 Zayıf | Kolayca brute-force edilebilecek veya tahmin edilebilecek şifre. |
| **5 - 7 Puan** | 🟡 Orta | Temel gereksinimleri karşılayan ancak daha güvenli olabilecek şifre. |
| **8+ Puan** | 🟢 Güçlü | Kırılması son derece zor, güvenli şifre. |

---

## 🚀 Kurulum & Çalıştırma

Herhangi bir harici kütüphaneye (third-party dependency) ihtiyaç duymaz, sadece Python3'ün yerleşik `re` modülünü kullanır.

```bash
# Depoyu klonlayın
git clone [https://github.com/kullaniciadi/Barbaros.git](https://github.com/kullaniciadi/Barbaros.git)

# Proje dizinine girin
cd Barbaros

# Araca çalıştırma izni verin
chmod +x Barbaros.py

# Aracı çalıştırın
python3 Barbaros.py
