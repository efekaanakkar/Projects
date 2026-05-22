 import socket
from concurrent.futures import ThreadPoolExecutor

Hedef = input("Hedefi Girin: ")
Başlangıç_Portu = int(input("Başlangıç Portu: "))
Bitiş_Portu = int(input("Bitiş Portu: "))

Açık_Portlar = []


def Tarama(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((Hedef, port))

        if result == 0:
            print(f"[+] Port {port} AÇIK")
            Açık_Portlar.append(port)

        sock.close()

    except Exception as e:
        print(f"[-] Hata ({port}): {e}")


print(f"\n{Hedef} üzerinde tarama başlatılıyor...\n")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(Tarama, range(Başlangıç_Portu, Bitiş_Portu + 1))

print("\nTarama tamamlandı!")
print("Açık portlar:", Açık_Portlar)
