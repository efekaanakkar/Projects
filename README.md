# 🛠️ Cybersecurity & Automation Projects

Bu depo, siber güvenlik, sızma testleri (Pentesting) ve sistem analizleri için Python3 ile geliştirdiğim açık kaynaklı araçları ve projeleri bir arada barındırmaktadır. İçerideki her araç, siber güvenlik süreçlerindeki farklı bir ihtiyaca (Bilgi toplama, şifre analizi, dizin tarama) hizmet etmek üzere tasarlanmıştır.

---

## Projeler ve Araç Listesi

Depo içerisinde yer alan aktif projeler ve kısa açıklamaları aşağıdadır. Her projenin kendi dizini içerisinde detaylı kullanım kılavuzu (`README.md`) yer almaktadır.


### 1. 🐆 PARS - Multi-Threaded Port Tarayıcı
Hedef sistemlerdeki açık kapıları tespit etmek için Python'ın native socket yapısını kullanan, yüksek hızlı ve eşzamanlı (Multi-threaded) çalışan bir port tarama aracı.
* **Öne Çıkan Özellik:** `ThreadPoolExecutor` ile 100 eşzamanlı worker sayesinde maksimum hız.
* **Dizin:** `./Pars/`

### 2. ⚓ BARBAROS - Şifre Güçlülük Analiz Aracı
Belirlenen şifreleri siber güvenlik standartlarına (uzunluk, karakter çeşitliliği vb.) göre analiz ederek bir güvenlik skoru ve seviyesi (Zayıf/Orta/Güçlü) çıkaran hafif bir analiz aracı.
* **Öne Çıkan Özellik:** Regex tabanlı akıllı karakter kontrolü ve puanlama sistemi.
* **Dizin:** `./Barbaros/`

### 3. 🐺 BÖRÜ (v1.0 & v1.1) - Gelişmiş Dizin Tarama Aracı
Web sitelerindeki gizli dizinleri ve dosyaları tespit etmek için geliştirilmiş, akıllı filtreleme ve canlı gösterge (Dirb tarzı) özelliklerine sahip gelişmiş bir Directory Brute-Forcer.
* **Öne Çıkan Özellik:** `Attack` ve `Peace` modları, Ctrl+C ile akıllı önem sırası raporlaması.
* **Dizin:** `./Boru/`
---

## 🚀 Genel Kurulum ve Başlangıç

Projelerin tamamı Python3 ile yazılmıştır ve harici bağımlılıkları minimum düzeydedir. Depoyu tamamen klonlamak için:

```bash
# Ana depoyu sisteminize indirin
git clone [https://github.com/kullaniciadi/Projects.git](https://github.com/kullaniciadi/Projects.git)

# Depo dizinine girin
cd Projects
