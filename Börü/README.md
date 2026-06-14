# 🐺 BÖRÜ - Gelişmiş Dizin Tarama Aracı (Directory Brute-Forcer)

Börü, web sitelerindeki gizli dizinleri ve dosyaları tespit etmek için Python3 ile geliştirilmiş, hızlı, esnek ve akıllı bir siber güvenlik aracıdır. Sızma testlerinizde (Pentest) hedef üzerinde bilgi toplama aşamasını kolaylaştırmak amacıyla tasarlanmıştır.

Proje, gelişim sürecini ve farklı kullanım alışkanlıklarını desteklemek adına iki farklı sürüm (`v1.0` ve `v1.1`) olarak sunulmuştur.

---

## 🔀 Sürümler ve Aralarındaki Farklar

Proje klasöründe ihtiyacınıza uygun sürümü seçip çalıştırabilirsiniz:

### 🔹 Börü v1.0 (Klasik / Detaylı Mod)
* **Çalışma Mantığı:** Tarama esnasında `200` dönen başarılı sonuçları kalıcı olarak yazar. Eğer `-v` (verbose) modu aktifse, tüm istekleri (404, 500 vb.) sırasıyla alt alta ekrana döker.
* **Kullanım Amacı:** Tarama akışını tamamen canlı ve satır satır log şeklinde takip etmek isteyenler için idealdir.

### 🔹 Börü v1.1 (Canlı Göstergeli / Dirb Tarzı Mod) - *Önerilen*
* **Çalışma Mantığı:** Terminal kirliliğini önlemek için en alt satırda **Canlı Gösterge (Progress Indicator)** barındırır. Anlık denenen kelimeler tek bir satırda fır fır dönerken ekranı kaplamaz.
* **Akıllı Filtreleme:** Sadece `200`, `3xx` veya `5xx` gibi kritik bir durum kodu yakaladığında o satırı kalıcı listeye fırlatır ve alt satırdan canlı göstergeye devam eder.
* **Kullanım Amacı:** Tıpkı **Dirb** veya **Gobuster** gibi modern araçların arayüz dinamizmini ve temizliğini terminalinde görmek isteyenler için birebirdir.

---

## 🔥 Ortak Özellikler

* ⚡ **Çift Tarama Modu (`--attackmode`):**
  * `Attack`: Agresif, en yüksek hızda tarama.
  * `Peace`: İstekler arası gecikmeli, sızma tespit sistemlerine (IDS/WAF) yakalanmamak için sakin tarama.
* 🛡️ **Ctrl+C ile Akıllı Sıralama:** Tarama herhangi bir anda yarım bırakılırsa (ve `-v` modu aktifse), o ana kadar toplanan tüm sonuçları önem sırasına göre (`200`'ler en üstte, `404`'ler en altta) otomatik olarak dizer.
* 🕵️ **User-Agent Kamuflajı:** Basit bot engelleme mekanizmalarını aşmak için özel başlıklar (headers) kullanır.

---

## 🚀 Kurulum

Aracın çalışması için sisteminizde Python3 ve `requests` kütüphanesinin kurulu olması yeterlidir.

```bash
# Depoyu klonlayın
git clone [https://github.com/efekaanakkar/Boru.git](https://github.com/efekaanakkar/Boru.git)

# Proje dizinine girin
cd Boru

# Gerekli kütüphaneyi yükleyin
pip3 install requests

# Araçlara çalıştırma izni verin
chmod +x Börü_v1.0.py Börü_v1.1.py
