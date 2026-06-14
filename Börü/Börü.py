#!/usr/bin/env python3
import argparse
import sys
import time
import requests

# Renklendirme için terminal kodları
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_banner():
    print(f"{BLUE}===================================={RESET}")
    print(f"{BLUE}             BÖRÜ v1.1              {RESET}")
    print(f"{BLUE}      Dizin Tarama Asistanı         {RESET}")
    print(f"{BLUE}===================================={RESET}\n")

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(description="Börü - Gelişmiş Dizin Tarama Aracı")
    parser.add_argument("--url", required=True, help="Hedef URL (Örn: http://example.com)")
    parser.add_argument("--wordlist", required=True, help="Wordlist dosyasının yolu")
    parser.add_argument("-v", "--verbose", action="store_true", help="Tüm denemeleri ve durum kodlarını anlık gösterir")
    parser.add_argument("--attackmode", choices=["Attack", "Peace"], default="Peace", 
                        help="Tarama modu: 'Attack' (Hızlı/Sert) veya 'Peace' (Sakin/Yavaş)")
    
    args = parser.parse_args()
    target_url = args.url.rstrip('/')
    
    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            words = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"{RED}[-] Hata: '{args.wordlist}' dosyası bulunamadı.{RESET}")
        sys.exit(1)
        
    print(f"{GREEN}[+] Tarama başlatılıyor...{RESET}")
    print(f"[+] Hedef: {target_url}")
    print(f"[+] Mod: {args.attackmode}")
    print(f"[+] Toplam Kelime: {len(words)}\n")
    print("-" * 60)

    delay = 0.4 if args.attackmode == "Peace" else 0.0
    all_results = []

    try:
        for idx, word in enumerate(words, 1):
            path = word.lstrip('/')
            full_url = f"{target_url}/{path}"
            
            # Anlık durumu tek satırda hızlıca gösterme (Canlı Gösterge)
            # Eğer verbose aktifse satırın üstüne yazmasın diye bunu atlıyoruz
            if not args.verbose:
                progress = f"[{idx}/{len(words)}] Deneniyor: /{path}"
                # Satırı temizlemek için boşluk bırakıp \r ile başa dönüyoruz
                sys.stdout.write(f"\r{progress:<60}")
                sys.stdout.flush()
            
            try:
                headers = {'User-Agent': 'Boru-Scanner/1.1'}
                response = requests.get(full_url, headers=headers, timeout=5, allow_redirects=False)
                status = response.status_code
                
                all_results.append((path, status))
                
                # verbose KAPALIYKEN Önemli bir şey (200, 3xx, 5xx vb.) bulunursa alta listeleme mantığı
                if not args.verbose:
                    if status == 200:
                        # Mevcut satırı temizle ve kalıcı olarak yaz
                        sys.stdout.write("\r" + " " * 60 + "\r")
                        print(f"{GREEN}/{- path:<25} ({status} OK){RESET}")
                    elif status in [301, 302, 307, 308]:
                        sys.stdout.write("\r" + " " * 60 + "\r")
                        print(f"{YELLOW}/{path:<25} ({status} Redirect){RESET}")
                    elif status >= 500:
                        sys.stdout.write("\r" + " " * 60 + "\r")
                        print(f"{RED}/{path:<25} ({status} Server Error){RESET}")
                
                # verbose AÇIKSA her şeyi tek tek alt alta yazdır
                else:
                    if status == 200:
                        print(f"{GREEN}/{path:<25} ({status}){RESET}")
                    elif status in [301, 302]:
                        print(f"{YELLOW}/{path:<25} ({status}){RESET}")
                    elif status == 404:
                        print(f"{RED}/{path:<25} ({status}){RESET}")
                    else:
                        print(f"/{path:<25} ({status})")
                            
            except requests.exceptions.RequestException:
                all_results.append((path, "HATA"))
                if args.verbose:
                    print(f"{RED}/{path:<25} (Bağlantı Hatası){RESET}")
                    
            if delay > 0:
                time.sleep(delay)
                
        # Döngü bitince canlı gösterge satırını temizle
        if not args.verbose:
            sys.stdout.write("\r" + " " * 60 + "\r")
        print(f"\n{GREEN}[+] Tarama başarıyla tamamlandı.{RESET}")

    except KeyboardInterrupt:
        # Satırı temizle ki çirkin durmasın
        sys.stdout.write("\r" + " " * 60 + "\r")
        print(f"\n{YELLOW}[!] Tarama kullanıcı tarafından durduruldu! Durum raporu hazırlanıyor...{RESET}\n")
        
        if args.verbose and all_results:
            print("-" * 60)
            print(f"{BLUE}Önem Sırasına Göre Sonuçlar (En Önemli -> En Önemsiz):{RESET}")
            print("-" * 60)
            
            def sort_key(item):
                code = item[1]
                if code == "HATA": return 5
                if 200 <= code < 300: return 0
                if 300 <= code < 400: return 1
                if code >= 500: return 2
                if code == 404: return 4
                return 3

            sorted_results = sorted(all_results, key=sort_key)
            
            for path, status in sorted_results:
                if status == "HATA":
                    print(f"{RED}/{path:<25} (Bağlantı Hatası){RESET}")
                elif 200 <= status < 300:
                    print(f"{GREEN}/{path:<25} ({status}){RESET}")
                elif 300 <= status < 400:
                    print(f"{YELLOW}/{path:<25} ({status}){RESET}")
                elif status == 404:
                    print(f"{RED}/{path:<25} ({status}){RESET}")
                else:
                    print(f"/{path:<25} ({status})")
        else:
            print("[*] Raporlama için '-v' parametresi aktif edilmediğinden canlı yakalananlar yukarıda bırakıldı.")
            
        sys.exit(0)

if __name__ == "__main__":
    main()
