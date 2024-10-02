# Nama Teman
# Teman = ["Duan","Fijri","Reja","Paras"]
# print(Teman)

#berikut adalah mendefinisikan list tas
# makanan = ["Crepes Pisang Coklat","Burger Bangor","Ayam Geprek","Nasi Padang", ["+ Nasi","+ Jus Alpuat Milo"]]
# # print(makanan)
# makanan.append("Kamu")
# print(makanan)

# outfit = [ 
#             "Crewneck",
#             ["Baju Hitam",
#             "Jeans Biru",
#             "Chino Hitam",
#             "Sneakers",
#             "Bucket Hat",]
#                 ]
# print(outfit)

# for i in outfit :
#     if isinstance (i, list):
#         for j in i :
#             print(j)

akuna = []

while True:
    print("Halo! Selamat Datang Boskue Di Program Jual Beli Tiket Konser")
    print("Silahkan Pilih Kelanjutannya Boskue")
    print("1. Daftar Akun")
    print("2. Login")
    print("3. Exit")
    print("_________________________________")
    
    pilih = input("Pilih Opsi: ")
    print(" ")
    
    if pilih == "1":
        print("Silahkan Daftar Akun")
        username = input("Username :")
        akuna =  False
        for akun in akuns:
            if akun [0] == username :
                akuna = True
                break
        if akuna:
            print("Username Sudah Terpakai!")
        else:
            password = input("Passwword: ")
            akuns.append([username,password, []])
            print(f"Akun anda sudah jadi bos : {username}")
            