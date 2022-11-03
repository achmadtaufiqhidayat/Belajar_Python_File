#deklarasi file txt untuk dibuka, parameter 'r' menyesuaikan dengan yang ada di python dokumentasi, bisa 'w'
#ketika kita membaca file txt yang sudah memiliki isi, maka dapat menggunakan 'r', namun untuk menulis menggunakan 'w'
#kemudian, jika kita menulis pada file yang sudah ada isinya mengguanakn 'w' isi teks akan hilang
#maka solusinya gunakan a+ untuk menambahkan, jika pakai r+ maka akan tertambah data baru namun di awal
#ketika kita ingin membaca dan menulis, maka menggunakan seek


file = open('data.txt', 'a+')

file.write('\ni am fine thanks')


file.seek(0)
text = file.read()
print(text)
