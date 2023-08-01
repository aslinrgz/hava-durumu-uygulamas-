
import requests

api_anahtari = "8749efc112d631404526046aaa3a6093"

temel_url = "http://api.openweathermap.org/data/2.5/weather?"

sehir = input("Lütfen hava durumu bilgisini öğrenmek istediğiniz şehri giriniz:")
ulke_kodu = input("Ülke kodunu giriniz (örn. tr, us, fr):")

tam_url = f"{temel_url}q={sehir},{ulke_kodu}&APPID={api_anahtari}"

sonuc = requests.get(tam_url)
jsonsonuc = sonuc.json()

sicaklik = jsonsonuc["main"]["temp"] - 273.15  
basinc = jsonsonuc["main"]["pressure"]
nem = jsonsonuc["main"]["humidity"]
print(f"Sıcaklık: {sicaklik:.2f} °C")
print(f"Basınç: {basinc} paskal.")
print(f"Nem oranı: {nem} %")


