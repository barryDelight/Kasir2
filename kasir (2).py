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
#print(minuman["1"])  

#########input dan menghitung jumlah barang############
pilihMenu = (input("Pilih Menu: "))
while True:
    if pilihMenu not in minuman: 
        print("Kode invalid, silahkan ulangi")
        pilihMenu = (input("Pilih menu yang benar1: "))
        continue
        
    elif pilihMenu in minuman:
        print(minuman[pilihMenu])  
          
    jumlahBarang = int(input("Jumlah barang: "))
    hargaBarang = int(input("Insert harga: "))
    totalBarang = jumlahBarang * hargaBarang
    print("Total harga,", totalBarang) 
    break

#########input dan menghitung jumlah barang ke2############
orderan2 = input("Apakah ada lagi? ")
if orderan2 != "y":
    print("Ini subtotal harga minuman anda", totalBarang)
while orderan2 == "y":
    pilihMenu2 = (input("Pilih Menu untuk item ke-2: "))
    if pilihMenu2 not in minuman:
        print("Kode invalid, silahkan ulangi")
        pilihMenu = (input("Pilih menu lagi, jgn salah mulu: "))
        if pilihMenu2 not in minuman:
            print("Salah kode, ulangi lagi")
        continue
    elif pilihMenu2 in minuman:
        print(minuman[pilihMenu2])
        jumlahBarang2 = int(input("Jumlah barang: "))
        hargaBarang2 = int(input("Insert harga: "))
        totalBarang2 = jumlahBarang2 * hargaBarang2

        print("Item pertama = %s, dengan harga = %s" % (minuman[pilihMenu],  hargaBarang))
        print("Item kedua = %s, dengan harga = %s" % (minuman[pilihMenu2], hargaBarang2))
        
        print("Total harga", totalBarang + totalBarang2)
        print("Ini subtotal harga minuman anda", totalBarang + totalBarang2)
        break
        #########total harga barang 1 dan 2############
    

    #print("Item pertama = %s" %minuman[pilihMenu] )

    
 


