#----------------------------------------------Library------------------------------------------

import time         #Untuk mengimplementasikan fitur timer dan fitur jam serta untuk memberi delay saat user memasukkan input tidak valid
import shutil       #Untuk mengatur posisi remote AC sehingga selalu berada di tengah terminal
import os           #Untuk membersihkan terminal sebelum meng-update remote AC

#----------------------------------------------Fungsi-------------------------------------------

def seven_segment(N, string_awal, string_akhir): #Menggambar angka dengan menggunakan konsep seven segment display
    N = str(N)
    arr = [[0 for i in range(7)] for i in range(len(N))]
    for i in range(len(N)):
        #Data referensi seven segment untuk setiap digit
        if N[i] == "0":
            arr[i] = [1, 1, 1, 1, 1, 1, 0]
        elif N[i] == "1":
            arr[i] = [0, 1, 1, 0, 0, 0, 0]
        elif N[i] == "2":
            arr[i] = [1, 1, 0, 1, 1, 0, 1]
        elif N[i] == "3":
            arr[i] = [1, 1, 1, 1, 0, 0, 1]
        elif N[i] == "4":
            arr[i] = [0, 1, 1, 0, 0, 1, 1]
        elif N[i] == "5":
            arr[i] = [1, 0, 1, 1, 0, 1, 1]
        elif N[i] == "6":
            arr[i] = [1, 0, 1, 1, 1, 1, 1]
        elif N[i] == "7":
            arr[i] = [1, 1, 1, 0, 0, 0, 0]
        elif N[i] == "8":
            arr[i] = [1, 1, 1, 1, 1, 1, 1]
        elif N[i] == "9":
            arr[i] = [1, 1, 1, 1, 0, 1, 1]
        
    #-----Line 1-----

    print(string_awal, end="")
    for i in range(len(N)):
        if arr[i][0] == 1:
            print(" ______ ", end="")
        else:
            print(end="        ")
        print(end="  ")
    print(" __ ", end="")           # Untuk menggambar simbol derajat
    print(string_akhir[4:])

    #-----Line 2-----

    print(string_awal, end="")
    for i in range(len(N)):
        if arr[i][5] == 1:
            print("|", end="      ")
        else:
            print(end="       ")
        
        if arr[i][1] == 1:
            print("|", end="")
        else:
            print(end=" ")

        print(end="  ")
    print("|__|", end="")           # Untuk menggambar simbol derajat
    print(string_akhir[4:])

    #-----Line 3-----

    print(string_awal, end="")
    for i in range(len(N)):
        if arr[i][5] == 1:
            print("|", end="")
        else:
            print(end=" ")

        if arr[i][6] == 1:
            print("______", end="")
        else:
            print(end="      ")
        
        if arr[i][1] == 1:
            print("|", end="")
        else:
            print(end=" ")
        print(end="  ")
    print(string_akhir)

    #-----Line 4-----

    print(string_awal, end="")
    for i in range(len(N)):
        if arr[i][4] == 1:
            print("|", end="      ")
        else:
            print(end="       ")
        
        if arr[i][2] == 1:
            print("|", end="")
        else:
            print(end=" ")
        print(end="  ")
    print(string_akhir)

    #-----Line 5-----

    print(string_awal, end="")
    for i in range(len(N)):
        if arr[i][4] == 1:
            print("|", end="")
        else:
            print(end=" ")

        if arr[i][3] == 1:
            print("______", end="")
        else:
            print(end="      ")
        
        if arr[i][2] == 1:
            print("|", end="")
        else:
            print(end=" ")
        print(end="  ")
    print(string_akhir)

def render(): #Menggambar UI dari Remote AC
    print(offset + f"     ______________________________________________________________")
    print(offset + f"   /                                                                \\ ")
    print(offset + f"  /                [ Kelompok 11 / K-29 / STEI-K' 24 ]               \\ ")
    print(offset + f" /  ________________________________________________________________  \\")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |    FAN : " + ("■ "*fan) + ("  "*(5 - fan)) + f"          {tipe_suhu}               {current_time}    |  |")
    seven_segment(display_suhu, offset + "|  |                      ", "                      |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |    MODE  : {mode[index_mode]}   SWING : {string_swing}                                    |  |")
    print(offset + f"|  |    TIMER : {display_timer}    TIME  : {time_left}                " + (" "*(10 - len(time_left))) + "           |  |")
    print(offset + f"|  |________________________________________________________________|  |") 
    print(offset + f"|   ________________________________________________________________   |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                                                  0 ► ON/OFF    |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        1  ▲ Naikkan suhu                       |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        2  ▼ Turunkan suhu                      |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        3  ► Ubah satuan suhu                   |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        4  ► MODE                               |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        5  ► FAN                                |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        6  ► SWING                              |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        7  ► ON Timer                           |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                        8  ► OFF Timer                          |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |                                                                |  |")
    print(offset + f"|  |________________________________________________________________|  |")
    print(offset + f" \\____________________________________________________________________/")
    print(offset + f"  \\__________________________________________________________________/")
    print(offset + f"   \\________________________________________________________________/")

#--------------------------------------Deklarasi Variabel-----------------------------------------

#--------------------String----------------------

tipe_suhu = "Celcius   "
string_swing = "■"
display_timer = "OFF"
time_left = "OFF"
mode = ["Auto", "Cool", "Dry ", "Fan ", "Heat"]
current_time = time.strftime("%H:%M")

#------------------Integer----------------------

suhu = 16
display_suhu = suhu
batas_atas = 30
batas_bawah = 16
index_mode = 1
fan = 3
swing = 1
timer = 0
waktu_timer_start = 0
choice = 0

#------------------Boolean-------------------

on = False

#---------------------------------------Algoritma-------------------------------------------------

#Atur posisi remote AC berdasarkan ukuran terminal
offset = " "*(((shutil.get_terminal_size((80, 20))).columns - 72) // 2)

while True:

    #Bersihkan terminal
    os.system('cls')

    #Ingin menyalakan AC?
    yn = input("Apakah anda ingin menyalakan AC (Y/N)? ")
    if yn == "Y": #Jika AC ingin dinyalakan
        on = True
    elif yn == "N": #Jika AC ingin dimatikan
        print("AC tetap dimatikan!")
        time.sleep(2)
        break
    else: #Jika input tidak valid
        print("-------------------------!ERROR!--------------------------")
        print("Input tidak valid! Tolong masukkan input yang sesuai (Y/N)")
        print("-------------------------!ERROR!--------------------------")
        time.sleep(2)

    while on: #Selama AC masih menyala

        #Update posisi remote AC sesuai ukuran terminal
        offset = " "*(((shutil.get_terminal_size((80, 20))).columns - 72) // 2)

        #Update waktu saat ini
        current_time = time.strftime("%H:%M")

        #Update waktu time yang tersisa jika timer masih menyala
        if display_timer == "ON ":
            time_left = str(round(timer - (time.time() - waktu_timer_start)))
        else:
            time_left = "OFF"


        #Cek apakah timer sudah habis
        if (display_timer == "ON ") and (int(time_left) <= 0):
            display_timer = "OFF"
            print("Timer habis, AC dimatikan")
            time.sleep(2)
            break

        #Bersihkan terminal
        os.system('cls')

        #Print UI Remote AC
        render()

        #Tentukan masukan dari pengguna
        print("\nApa yang ingin anda lakukan?\n")
        print("0: Matikan AC")
        print("1: Menaikkan suhu")
        print("2: Menurunkan suhu")
        print("3: Konversi satuan suhu")
        print("4: Ubah mode")
        print("5: Ubah pengaturan fan")
        print("6: Toggle swing")
        print("7: On timer")
        print("8: Off timer\n")
        
        #Pastikan masukan sesuai dengan batasan
        try:
            choice = int(input("Masukkan pilihan anda: "))
        except ValueError:
            print("-----------------------------!ERROR!-------------------------------")           
            print("Input tidak valid! Masukkan input berupa bilangan bulat antara 0-8!")
            print("-----------------------------!ERROR!-------------------------------")             
            time.sleep(2)
            continue

        if (choice == 0): #Jika masukan 0, matikan AC
            print("AC berhasil dimatikan!")
            time.sleep(2)
            on = False
            break

        elif (choice == 1): #Jika masukan 1, naikkan suhu AC sebesar 1 derajat sesuai dengan satuan
            suhu = min(suhu + 1, batas_atas)
            display_suhu = round(suhu)

        elif (choice == 2): #Jika masukan 2, turunkan suhu AC sebesar 1 derajat sesuai dengan satuan
            suhu = max(suhu - 1, batas_bawah)
            display_suhu = round(suhu)

        elif (choice == 3): #Jika masukan 3, ubah satuan dari Celcius ke Fahrenheit dan Fahrenheit ke Celcius

            if tipe_suhu == "Celcius   ":
                tipe_suhu = "Fahrenheit"
                batas_atas = 86
                batas_bawah = 61
                suhu = max((suhu * 9/5) + 32, batas_bawah)
                display_suhu = round(suhu)

            else:
                tipe_suhu = "Celcius   "
                batas_atas = 30
                batas_bawah = 16
                suhu = (suhu - 32) * 5/9
                display_suhu = round(suhu)

        elif (choice == 4): #Jika masukan 4, ubah mode AC
            index_mode = (index_mode + 1) % 5
            
        elif (choice == 5): #Jika masukan 5, ubah kecepatan kipas/fan
            fan = (fan + 1) % 6

        elif (choice == 6): #Jika masukan 6, toggle swing AC
            swing ^= 1

            if swing:
                string_swing = "■"
            else:
                string_swing = "□"

        elif (choice == 7): #Jika masukan 7, nyalakan timer dan atur berapa lama
            input_valid = True

            try:
                timer = int(input("Masukkan durasi timer (dalam detik): "))
                display_timer = "ON "
                waktu_timer_start = time.time()
                if timer <= 0:
                    input_valid = False                     
            except ValueError:
                input_valid = False

            if not input_valid: #Jika masukan tidak valid
                display_timer = "OFF"
                print("----------------------------------------!ERROR!------------------------------------------")           
                print("Input tidak valid! Masukkan input durasi timer berupa bilangan bulat positif lebih dari 0")
                print("----------------------------------------!ERROR!------------------------------------------")           
                time.sleep(2)               

        elif (choice == 8): #Jika masukan 8, matikan timer
            display_timer = "OFF"

        else: #Jika masukan tidak valid, outoput pesan peringatan
            print("-----------------------------!ERROR!-------------------------------")           
            print("Input tidak valid! Masukkan input berupa bilangan bulat antara 0-8!")
            print("-----------------------------!ERROR!-------------------------------")           
            time.sleep(2)
            continue