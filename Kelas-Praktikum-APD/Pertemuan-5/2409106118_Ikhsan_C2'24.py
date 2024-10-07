# # Nama Teman
# # Teman = ["Duan","Fijri","Reja","Paras"]
# # print(Teman)

# #berikut adalah mendefinisikan list tas
# # makanan = ["Crepes Pisang Coklat","Burger Bangor","Ayam Geprek","Nasi Padang", ["+ Nasi","+ Jus Alpuat Milo"]]
# # # print(makanan)
# # makanan.append("Kamu")
# # print(makanan)

# # outfit = [ 
# #             "Crewneck",
# #             ["Baju Hitam",
# #             "Jeans Biru",
# #             "Chino Hitam",
# #             "Sneakers",
# #             "Bucket Hat",]
# #                 ]
# # print(outfit)

# # for i in outfit :
# #     if isinstance (i, list):
# #         for j in i :
# #             print(j)

# akuns = []

# while True:
#     print("Halo! Selamat Datang di Pemesanan Tiket Konser")
#     print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
#     print("1. Daftar akun")
#     print("2. Login")
#     print("3. Exit")
#     print("――――――――――――――――――――――――")
#     opsi = input("Pilih opsi: ")
#     print(" ")

#     if opsi == "1":
#         print("Halo Pengguna baru! Ayo buat akun dulu")
#         Username = input("Username: ")
#         akuna = False
#         for akun in akuns:
#             if akun[0] == Username:  # Memeriksa apakah username sudah ada
#                 akuna = True
#                 break
#         if akuna:
#             print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
#         else:
#             Password = input("Password: ")
#             akuns.append([Username, Password, []])  # Simpan username, password, dan catatan (sebagai list kosong)
#             print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")
 

#     elif opsi == "2":
#         print("Hi, Silahkan login dulu ya!")
#         Username = input("Username: ")
#         Password = input("Password: ")
#         for akun in akuns:
#             if akun[0] == Username and akun[1] == Password:  # Cocokkan username dan password
#                 while True:
#                     print(f"\nSelamat datang {Username}!")
#                     print("―――Silakan pilih aksi!―――")
#                     print("1. Tambah catatan baru")
#                     print("2. Lihat catatan yang ada")
#                     print("3. Edit catatan yang ada")
#                     print("4. Hapus catatan yang ada")
#                     print("5. Exit")
#                     print("―――――――――――――――――――――――――――――")

#                     status = input("Pilih opsi: ")
#                     print(" ")

#                     if status == "1":
#                         judul_catatan = input("Judul catatan: ")
#                         isi_catatan = input("Isi catatan: ")
#                         akun[2].append([judul_catatan, isi_catatan])  # Menambahkan catatan ke dalam list
#                         print("Catatan baru kamu sudah disimpan!\n")

#                     elif status == "2":
#                         for indeks, note in enumerate(akun[2]):  # Menampilkan semua catatan
#                             print(f"{indeks + 1}. Judul: {note[0]}\nIsi: {note[1]}\n")
#                         if not akun[2]:
#                             print("Opps, saat ini kamu belum punya catatan, silahkan buat catatan baru terlebih dahulu.\n")

#                     elif status == "3":
#                         if not akun[2]:
#                             print("Tidak ada catatan yang bisa diedit.")
#                         else:
#                             edit = int(input("Catatan nomor berapa yang ingin kamu edit: ")) - 1
#                             if 0 <= edit < len(akun[2]):
#                                 judul_baru = input("Masukkan judul yang baru: ")
#                                 isi_baru = input("Masukkan isi yang baru: ")
#                                 print("Apa kamu yakin ingin mengedit catatan ?")
#                                 print("1. Iya")
#                                 print("2. Tidak")
#                                 memastikan_edit = input("Pilih: ")
#                                 if memastikan_edit == "1":
#                                     akun[2][edit] = [judul_baru, isi_baru]  # Mengedit catatan
#                                     print("Catatan yang kamu pilih sudah di edit ya!\n")
#                                 elif memastikan_edit == "2":
#                                     print("Aksi untuk mengedit catatan dibatalkan")
#                                 else:
#                                     print("Mohon pilih '1' atau '2'")
#                             else:
#                                 print("Tidak ada nomor catatan yang kamu maksud, silahkan input ulang.\n")
                    
#                     elif status == "4":
#                         if not akun[2]:
#                             print("Tidak ada catatan yang bisa dihapus.")
#                         else:
#                             hapus = int(input("Catatan nomor berapa yang ingin dihapus: ")) - 1
#                             if 0 <= hapus < len(akun[2]):
#                                 print(f"Apa kamu yakin ingin menghapus catatan ? ")
#                                 print("1. Iya")
#                                 print("2. Tidak")
#                                 memastikan_hapus = input("Pilih: ")
#                                 if memastikan_hapus == "1":
#                                     del akun[2][hapus]  # Menghapus catatan dari list
#                                     print("Catatan yang kamu pilih sudah dihapus!\n")
#                                 elif memastikan_hapus == "2":
#                                     print("Aksi untuk menghapus dibatalkan")
#                                 else:
#                                     print("Mohon pilih '1' atau '2'")
#                             else:
#                                 print("Tidak ada nomor catatan yang kamu maksud, silahkan input ulang\n")

#                     elif status == "5":
#                         print("Aplikasi Catatan ditutup.\n")
#                         break

#                     else:
#                         print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
#                 break
#         else:
#             print("Username dan password anda salah, silahkan coba lagi\n")

#     elif opsi == "3":
#         print("Apakah kamu yakin ingin keluar dari aplikasi? ")
#         print("1. Iya")
#         print("2. Tidak")
#         pilih = input("Input pilihan: ")
#         print(" ")
#         if pilih == "1":
#             print("Terimakasih sudah menggunakan aplikasi, semoga harimu menyenangkan!")
#             break
#         elif pilih == "2":
#             continue
#         else:
#             print("Input tidak valid, silahkan pilih '1' atau '2'\n")
#     else:
#         print("Input tidak valid, silahkan pilih 1, 2, atau 3")
