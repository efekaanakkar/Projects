# 🐆 PARS - Hızlı ve Multi-Threaded Port Tarama Aracı

Pars, hedef bir IP adresi veya alan adı (domain) üzerindeki belirli port aralıklarını ağ protokolleri üzerinden tarayarak açık olanları tespit eden, Python3 ile geliştirilmiş yüksek hızlı bir port tarayıcıdır. 

`socket` programlama temelleri üzerine kurulan araç, **ThreadPoolExecutor** kullanarak eşzamanlı (Multi-threaded) çalışır. Bu sayede yüzlerce portu saniyeler içinde tarayabilir.

---

## 🔥 Özellikler

* ⚡ **Yüksek Hız (Multi-Threading):** Aynı anda 100 farklı iş parçacığı (worker) kullanarak tarama süresini minimuma indirir.
* 🛠️ **Esnek Aralık Tanımlama:** Başlangıç ve bitiş portlarını tamamen kullanıcının kontrolüne bırakır.
* 🎯 **Hafif ve Bağımsız:** Herhangi bir harici kütüphaneye (Nmap, Scapy vb.) ihtiyaç duymadan, tamamen Python'ın yerleşik kütüphaneleriyle çalışır.
* 🔍 **Hata Yönetimi:** Tarama esnasında oluşabilecek zaman aşımı (timeout) ve bağlantı kopmalarını akıllıca yönetir.

---

## ⚙️ Çalışma Mantığı

Pars, hedef portlara **TCP SYN/Connect** mantığıyla yaklaşır. Python'ın yerleşik `connect_ex()` fonksiyonunu kullanır:
* Eğer fonksiyon `0` dönerse, portun **AÇIK** ve bağlantıya hazır olduğunu anlar.
* Zaman aşımı (Timeout) süresi `1` saniye olarak set edilmiştir, böylece kapalı portlarda gereksiz beklemeler yapmaz.

---

## 🚀 Kurulum & Çalıştırma

Herhangi bir harici bağımlılığı yoktur. Python3 kurulu olan her sistemde doğrudan çalıştırılabilir.

```bash
# Depoyu klonlayın
git clone [https://github.com/efekaanakkar/Pars.git](https://github.com/efekaanakkar/Pars.git)

# Proje dizinine girin
cd Pars

# Araca çalıştırma izni verin
chmod +x pars.py

# Aracı çalıştırın
python3 pars.py
