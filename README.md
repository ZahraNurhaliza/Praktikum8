# Praktikum8

Buat program sederhana dengan mengaplikasikan penggunaan class. 
Buatlah class untuk menampilkan daftar nilai mahasiswa, dengan ketentuan:
• Method tambah() untuk menambah data
• Method tampilkan() untuk menampilkan data
• Method hapus(nama) untuk menghapus data berdasarkan nama
• Method ubah(nama) untuk mengubah data berdasarkan nama
• Buat diagram class, flowchart dan penjelasan programnya pada
README.md.

## Program
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/Program.1.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/Program.2.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/Program.3.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/Program.4.png)

## RUN
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/RUN.1.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/RUN.2.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/RUN.3.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/RUN.4.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/RUN.5.png)
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/RUN.6.png)

## Penjelasan
• Pertama kita harus mendeklarasikan bahwa variabel data sebagai penyimpanan (dictionary) sebuah data inputan 
• Selanjutnya adalah membuat Class 
• Selanjutnya membuat constructor 
• Kemudian menambahkan definisi fungsi 
• Menggunakan Perulangan while True: dapat diartikan perulangan akan terus mengulang jika inputan benar dan masuk kedalam proses jika tidak maka perulangan berhenti atau lanjut ke proses selanjutnya
• Gunakan statement if untuk memproses perintah yang diinginkan sesuai inputan

1. Menambahkan Data
Perintah dijalankan jika input yang dimasukan adalah '2', Kondisi berikut digunakan untuk melakukan input data seperti Nama, NIM, Nilai Tugas, UTS dan UAS 
Untuk nilai akhir dibuat berdasarkan operasi dari variabel self.tugas, self.uts, self.uas yang mewakili Nilai Tugas, Nilai UTS, dan Nilai UAS.
Class Mahasiswa diturunkan dari Class data

2. Menampilkan Data
Perintah dijalankan jika input yang dimasukan adalah '1', Jika sebelumnya data sudah ditambahkan atau data tersedia, maka data tersebut akan ditampilkan sebanyak data yang ditambahkan. Jika data tersebut belum ditambahkan atau tidak tersedia, maka akan menampilkan bahwa tidak ada data 

3. Mengubah Data
Perintah dijalankan jika input yang dimasukan adalah '3', di dalam kondisi ini terdapat input dan kondisi, dimana jika ada di dalam variabel (data.keys) 
Jika nama tersebut ada pada data, maka user akan diminta untuk menginputkan data apa saja yang ingin dirubah. Jika nama tersebut tidak ada, maka akan menampilkan bahwa data tidak ditemukan.

4. Menghapus Data
Perintah dijalankan jika input yang digunakan adalah '4', sama seperti mengubah data, untuk menghapus data yang dipilih menggunakan variabel (data.keys)
Jika nama tersebut ada pada data, maka data tersebut akan di-delete pada dictionary sehingga data tidak tersedia lagi. Jika nama tersebut tidak ada pada data, maka akan menampilkan bahwa data tidak ditemukan.

## Diagram
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/diagram.png)

## Flowchart
![image](https://github.com/ZahraNurhaliza/Praktikum8/blob/main/screenshot/fw.png)

## Commit dan push repository ke github
