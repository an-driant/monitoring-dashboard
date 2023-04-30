import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        pusat_gempa = None
        keterangan = None

        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text
            elif i == 4:
                pusat_gempa = res.text
            elif i == 5:
                keterangan = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = koordinat
        hasil['pusat gempa'] = pusat_gempa
        hasil['keterangan'] = keterangan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data')
        return
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"kedalaman : {result['kedalaman']}")
    print(f"Koordinat : {result['koordinat']}")
    print(f"Pusat gempa : {result['pusat gempa']}")
    print(f"Keterangan : {result['keterangan']}")


if __name__ == '__main__':
    print('Ini adalah package gempa terkini')
