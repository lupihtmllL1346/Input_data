#NILAI PTS/PAS
def minta_nilai(pelajaran):
    while True:
        try:
            return int(input(f"{pelajaran}?: "))
        except ValueError:
            print("0")


print("NILAI PTS KELAS 11/12 MIPA")
print()


print("MAPEL WAJIB")

#kelas 11 MTK
M1PTS = minta_nilai('PTS MATEMATIKA')

#kelas 11 BINDO
Bindo1PTS = minta_nilai('PTS BAHASA INDONESIA')

#kelas 11 BINGGRIS
Bingg1PTS = minta_nilai('PTS BAHASA INGGRIS')

#kelas 11 AGAMA
A1PTS= minta_nilai('PTS AGAMA')

#kelas 11 PKN
P1PTS = minta_nilai('PTS PKN')

#kelas 11 SEJARAH
S1PTS = minta_nilai('PTS SEJARAH')

#kelas 11 PJOK
PJOK1PTS = minta_nilai('PTS PJOK')
print()


print("MAPEL PILIHAN")

#kelas 11 FISIKA
F1PTS = minta_nilai('PTS FISIKA')

#kelas 11 KIMIA
K1PTS = minta_nilai('PTS KIMIA')

#kelas 11 BIOLOGI
B1PTS = minta_nilai('PTS BIOLOGI')

#kelas 11 MATEMATIKA LANJUTAN
MTL1PTS = minta_nilai('PTS MATEMATIKA LANJUTAN')

#kelas 11 SENI BUDAYA/INFOMATIKA/PRAKARYA
SF1PTS = minta_nilai('PTS SENI BUDAYA/INFORMATIKA/PRAKARYA')

#Kelas 11 BAHASA ASING SELAIN INGGRIS
BA1PTS = minta_nilai('PTS BAHASA ASING TAMBAHAN')

#RATA-RATA NILAI PTS
totalPTS = (M1PTS + Bindo1PTS + Bingg1PTS + A1PTS + P1PTS + F1PTS + K1PTS + B1PTS + MTL1PTS + SF1PTS + BA1PTS + S1PTS + PJOK1PTS) / 13
print()
print()



print("NILAI PAS KELAS 11/12 MIPA")
print()


print("MAPEL WAJIB")

#kelas 11&12 MTK
M1PAS = minta_nilai('PAS MATEMATIKA')

#kelas 11 BINDO
Bindo1PAS = minta_nilai('PAS BAHASA INDONESIA')

#kelas 11 BINGGRIS
Bingg1PAS = minta_nilai('PAS BAHASA INGGRIS')

#kelas 11 AGAMA
A1PAS = minta_nilai('PAS AGAMA')

#kelas 11 PKN
P1PAS = minta_nilai('PAS PKN')

#kelas 11 SEJARAH
S1PAS = minta_nilai('PAS SEJARAH')

#kelas 11 PJOK
PJOK1PAS = minta_nilai('PAS PJOK')
print()


print("MAPEL PILIHAN")

#kelas 11 FISIKA
F1PAS = minta_nilai('PAS FISIKA')

#kelas 11 KIMIA
K1PAS = minta_nilai('PAS KIMIA')

#kelas 11 BIOLOGI
B1PAS = minta_nilai('PAS BIOLOGI')

#kelas 11 MATEMATIKA LANJUTAN
MTL1PAS = minta_nilai('PAS MATEMATIKA LANJUTAN')

#kelas 11 SENI BUDAYA/INFOMATIKA/PRAKARYA
SF1PAS = minta_nilai('PAS SENI BUDAYA/INFORMATIKA/PRAKARYA')

#Kelas 11 BAHASA ASING SELAIN INGGRIS
BA1PAS = minta_nilai('PAS BAHASA ASING TAMBAHAN')
print()
print()


#RATA-RATA NILAI PAS
totalPAS = (M1PAS + Bindo1PAS + Bingg1PAS + A1PAS + P1PAS + F1PAS + K1PAS + B1PAS + MTL1PAS + SF1PAS + BA1PAS + S1PAS + PJOK1PAS) / 13

print(f"\n Rata-Rata Nilai PTS Kelas 11/12 MIPA: {totalPTS}" )
print()

print(f"\n Rata-Rata Nilai PAS Kelas 11/12 MIPA: {totalPAS}" )
print()


#RATA-RATA NILAI PTS DAN PAS
totalSEMUA = (totalPTS + totalPAS ) / 2
print(f"\n Rata-Rata Nilai PTS dan PAS Kelas 11/12 MIPA: {totalSEMUA}") 
print()

import time
import sys

lyrics = [
    (2.0, "Create By Vii")
]
def type_line(line, delay=0.05):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print() 


prev_time = 0
for t, line in lyrics:
    time.sleep(t - prev_time)
    type_line(line)
    prev_time = t
    print()