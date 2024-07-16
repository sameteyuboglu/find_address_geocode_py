import pandas as pd
import time
from geopy.geocoders import GoogleV3

# Excel dosyasını yükle
file_path = 'hastaneler.xlsx'
df = pd.read_excel(file_path)

# Koordinatları alma fonksiyonu
def get_coordinates(address, api_key):
    geolocator = GoogleV3(api_key=api_key)
    location = geolocator.geocode(address)
    if location:
        return (location.latitude, location.longitude)
    else:
        return (None, None)

# Google Maps API anahtarı
#api_key = ""

# Yeni kolonlar ekle
df['X koordinat'] = None
df['Y koordinat'] = None

# Toplam satır sayısı
total_rows = len(df)

# Başlama zamanı
start_time = time.time()

# Her satırı işleyip koordinatları al
for index, row in df.iterrows():
    address = f"{row['Adres']} {row['İlçe']} {row['İl']}"
    lat, lon = get_coordinates(address, api_key)
    df.at[index, 'X koordinat'] = lat
    df.at[index, 'Y koordinat'] = lon
    elapsed_time = time.time() - start_time
    remaining_rows = total_rows - (index + 1)
    print(f"Satır: {index + 1}/{total_rows}, Geçen Süre: {elapsed_time:.2f} sn, Kalan Satır: {remaining_rows}")

# Yeni Excel dosyasına kaydet
output_file_path = 'hastaneler_with_coordinates.xlsx'
df.to_excel(output_file_path, index=False)

print(f"Yeni dosya oluşturuldu: {output_file_path}")
