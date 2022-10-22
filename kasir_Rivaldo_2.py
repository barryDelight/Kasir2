import os
import datetime

os.system('CLS') 
#########tempat menyetor variable############
minuman = {
    '1' : [ 'Sprite', 5000 ],
    '2' : [ 'Fanta', 4000 ],
    '3' : [ 'Frestea', 4000 ],
    '4' : [ 'Cocacola', 4000 ],
    '5' : [ 'Pulpy Orange', 3000 ],
    '6' : [ 'Happy Jus', 3000 ],
    '7' : [ 'Fruit Tea', 3000 ],
    '8' : [ 'Frisian Flag', 5000 ],
    '9' : [ 'Clevo', 5000 ],
    '10': [ 'Teh Botol Sosro', 4000],
    '11': [ 'Calpino', 6000 ],
    '12': [ 'Teh Jawa', 4000 ],
    '13': [ 'Teh Gelas', 3000 ],
    '14': [ 'Tiky', 5000 ],
    '15': [ 'ABC Kacang Hijau', 6000 ],
    '16': [ 'Canting SAJ', 4000 ],
    '17': [ 'Teh Rio', 6000 ],
    '18': [ 'Milkuat', 8000 ],
    '19': [ 'Pocari Sweat', 6000 ],
    '20': [ 'Glit Gula Asam', 6000 ],
    '21': [ 'Frute', 5000 ],
    '22': [ 'Larutan Penyegar Sinde', 6000 ],
    '23': [ 'Aqua', 2000 ],
    '24': [ 'Minute Maid', 4000 ],
    '25': [ 'Floridina Orange', 6000 ],
    '26': [ 'Ades', 3000 ],
    '27': [ 'Marjan', 8000 ],
    '28': [ 'Pedia Sure', 8000 ],
    '29': [ 'Enfagrow', 9000 ],
    '30': [ 'Kapal Api Kopi Susu', 6000 ],
    '31': [ 'Tora Bika Full Cream', 7000 ],
    '32': [ 'Sido Muncul Kopi Jahe', 5000 ],
    '33': [ 'Anget Sari Kopi Jahe', 6000 ],
    '34': [ 'Kuku Bima', 8000 ],
    '35': [ 'Jahe Jreeng', 4000 ],
    '36': [ 'Energen Vanila', 6000 ],
    '37': [ 'Indomilk', 5000 ],
    '38': [ 'Sari Wangi', 6000 ],
 
}

#login
currentTime = datetime.datetime.now()
print(currentTime.strftime("%X %p"))
print(currentTime.strftime("%x\n"))
print("Selamat datang")
print("Masukkan username dan password Anda")

while True:
    username = input("Username : ")
    password = input("Password : ")
    os.system('CLS')
    if username == "dora" and password == "buta":
        print("Kamu berhasil login\n")
        break
    elif username != "dora" and password != "buta":
        print("Username dan password anda salah\n")
        continue
    elif username != "dora":
        print("Username anda salah\n")
        continue
    else:
        print("Password anda salah\n")
        continue


#Kasir
itemCount = []
itemName= []
i=0

while True:
    pilihMenu = (input("Pilih Menu: "))
    os.system('CLS')

    if pilihMenu not in minuman: 
        print("Kode '%s' salah, silahkan ulangi\n" % pilihMenu)
        continue
    elif pilihMenu in minuman:
        print(minuman[pilihMenu])  
          
    jumlahBarang = int(input("Jumlah barang: "))
    hargaBarang = int(input("Insert harga: "))
    totalBarang = jumlahBarang * hargaBarang
    print("\nItem ke %s = %s" % (i+1 ,minuman[pilihMenu]))
    print("dengan harga =", f'{totalBarang:,}')

    itemCount.append(totalBarang)
    itemName.append(minuman[pilihMenu])

    i =+ 1

#nambah loop untuk mengulangi input jika ada kesalahan disini (Seperti membuat tombol untuk back atau edit kembali)

    pilihMenu = input("\nApakah ada lagi? \n[Y jika iya, selain itu berarti tidak ada lagi]")
    os.system('CLS')
    if pilihMenu == "y":
        continue
    else:
        break

print(currentTime.strftime("%X %p"))
print(currentTime.strftime("%x\n"))

i = 0
for drinks in itemCount:
    print("item ke %s %s, dengan harga :" % (i+1, itemName[i]) , f'{itemCount[i]:,}' )
    
    i += 1


print("\nTotal harga :", f'{sum(itemCount):,}' )