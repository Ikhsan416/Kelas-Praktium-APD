# favorite = {
#     "film" : "Spiderman",
#     "makanan" : "Ice Cream Oreo",
#     "outfit" : "Sneakers"
# }

# print(favorite["film"])
# print(favorite["makanan"])
# print(favorite["outfit"])

# Biodata = {
# "Nama" : "Ikhsan",
# "NIM" : 2409106118,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
#     "Instagram" : "@ykhsann",
#     "Discord" : "Sanzy#8693"
#     }
# }

# print(Biodata)

# film = dict(
#     Horror = {
#         "Horror1" : "Lembayung",
#         },
#     Sad = {
#         "Home Sweet Loan",
#         "Miracle in Cell No.7",
#         },
#     )
# print((film.get('Horror')).get('Horror1'))

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")
# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }
# #Sebelum Ditambah
# print(Film)

# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller", "Home Sweet Loan" : "Sedih Banget Broww"})
# #Setelah Ditambah
# print(Film)

# data = {
#     "Nama" : "Ikhsan",
#     "Umur" : 19,
#     "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# del data["Nama"]
# #Setelah diubah
# print(data)
# #memanggil data yang telah dihapus
# print(data.get("Nama"))

# data = {
#     "Nama" : "Ikhsan",
#     "Umur" : 19,
#     "Jurusan" : "Informatika"
# }
# #Sebelum Dihapus
# print(data)
# cache = data.pop("Nama")
# #Setelah dihapus
# print(data)
# #memanggil data yang telah dihapus pada dictionary
# print(data.get("Nama"))
# #memanggil data yang telah dihapus pada variabel cache
# print(cache)

# print("Jumlah Data = ", len(data))

# pinjam = Film.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80

# Musik = {
# "Hindia" : ["Rumah Ke Rumah", "Evaluasi"],
# "Mahalini" : ["Bawa Dia Kembali", "Sisa Rasa"],
# "Lo-fi" : ["Minecraft 1Hour", "Rain With Melody 10Hour"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
# for song in j:
#     print(song)
# print("")

# #menggunakan keys
# for i in Nilai.keys():
#     print(i)
# print("")
# #menggunakan value
# for i in Nilai.values():
#     print(i)
# while True:
#     data = []

#     print("╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
#     print("╠ 1. Tambah                      ╣")
#     print("╠ 2. Lihat                       ╣")
#     print("╠ 3. Edit                        ╣")
#     print("╠ 4. Hapus                       ╣")
#     print("╠ 5. Exit                        ╣")
#     print("╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝")
#     status = input("Pilih opsi: ")
#     print(" ")
#     if status == "1":
#         nama = input("nama: ")
#         umur = input("umur: ")
#         nim = int(input("nim: "))
#         jurusan = input("jurusan: ")
#         angkatan = int(input("Angkatan : "))
#         data.append([nama, umur, nim, jurusan, angkatan])  # Menambahkan tiket ke dalam list
#         print("Konser berhasil ditambahkan!\n")
#     elif status == "2":
#         for data in data:  
#             print("nama: {data[0]}\nUmur: {data[1]}\nNim: {data[2]}\nJurusan: {data[3]}\nAngkatan: {data[4]}\n")
#     elif status == "3":
#         if not data:
#             print( "Tidak ada konser yang bisa diedit.")
#         else:
#             edit = int(input("Data nomor berapa yang ingin kamu edit: ")) - 1
#         if 0 <= edit < len(data):
#             nama = input("nama baru: ")
#             umur = input("umur baru: ")
#             nim = int(input("nim baru: "))
#             jurusan = input("jurusan baru: ")
#             angkatan = int(input("angkatan baru: "))
#             print("Apa kamu yakin ingin mengedit ko1nser ?")
#             print("1. Iya")
#             print("2. Tidak")
#             memastikan_edit = input("Pilih: ")
#             if memastikan_edit == "1":
#                 data[edit] = [nama, umur, nim, jurusan, angkatan]  # Mengedit konser
#                 print("Konser yang kamu pilih sudah di edit ya!\n")
#             elif memastikan_edit == "2":
#                 print("Aksi untuk mengedit konser dibatalkan")
#             else:
#                 print("Mohon pilih '1' atau '2'")

