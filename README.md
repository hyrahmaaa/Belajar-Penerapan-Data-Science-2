# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut, sebuah institusi pendidikan yang mapan, menghadapi tantangan serius berupa tingginya tingkat mahasiswa yang tidak menyelesaikan studinya (dropout), meskipun memiliki reputasi baik. Fenomena ini menjadi masalah besar karena berdampak pada kredibilitas institusi dan efisiensi sumber daya. Oleh karena itu, tujuan utama Jaya Jaya Institut adalah mendeteksi mahasiswa berisiko dropout sedini mungkin agar dapat diberikan bimbingan khusus, dengan harapan dapat menurunkan angka putus kuliah secara signifikan.

Untuk mengatasi permasalahan ini, proyek ini akan menganalisis data performa mahasiswa yang disediakan guna mengidentifikasi faktor-faktor pemicu dropout. Kontribusi utama seorang data scientist adalah membangun model prediktif untuk deteksi dini dan mengembangkan dashboard visualisasi interaktif. Solusi ini diharapkan dapat meningkatkan retensi mahasiswa, memungkinkan pengambilan keputusan berbasis data yang lebih proaktif, dan pada akhirnya memperkuat reputasi Jaya Jaya Institut.

### Permasalahan Bisnis

Permasalahan bisnis utama yang akan diselesaikan adalah:
- Perlunya Penurunan Tingkat Dropout Mahasiswa: Angka putus kuliah sebesar 32,1% saat ini membutuhkan upaya strategis untuk dikurangi demi keberlanjutan akademik.
- Mendesaknya Analisis Faktor Pemicu Dropout: Diperlukan investigasi mendalam untuk mengidentifikasi variabel-variabel kunci yang mendorong tingginya tingkat putus kuliah.
- Pentingnya Pengembangan Sistem Monitoring Komprehensif: Untuk mendukung keputusan strategis yang lebih baik, institusi membutuhkan implementasi sistem monitoring yang mampu melacak tren dan faktor-faktor terkait dropout secara real-time.
  
### Cakupan Proyek

Cakupan proyek ini meliputi:
- Eksplorasi Data Mahasiswa: Melakukan analisis mendalam terhadap dataset Jaya Jaya Institut guna mengidentifikasi pola, korelasi, dan faktor-faktor signifikan yang berkorelasi dengan status putus kuliah mahasiswa.
- Pengembangan Model Prediktif: Membangun model machine learning yang mampu memprediksi probabilitas putus kuliah mahasiswa berdasarkan data yang tersedia, dengan fokus pada akurasi identifikasi faktor pemicu.
- Desain Dashboard yang Informatif: Merancang dan mengimplementasikan dasbor visual informatif yang berfungsi sebagai alat monitoring berkelanjutan untuk tingkat putus kuliah, identifikasi faktor kunci, dan pelacakan tren historis nantinya.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

### Setup Environment

Proyek ini dikembangkan menggunakan Python dan disarankan untuk dijalankan dalam lingkungan virtual (virtual environment) untuk mengelola dependensi secara terisolasi.
1.  **Membuat dan Mengaktifkan Virtual Environment (venv)**
    Buka terminal atau command prompt, lalu ikuti langkah-langkah berikut:
    ```bash
    # Membuat virtual environment baru bernama 'venv_attrition'
    python3 -m venv venv_attrition

    # Mengaktifkan virtual environment:
    # Untuk macOS/Linux:
    source venv_attrition/bin/activate
    # Untuk Windows (Command Prompt):
    venv_attrition\Scripts\activate.bat
    # Untuk Windows (PowerShell):
    venv_attrition\Scripts\Activate.ps1
    ```
    Setelah diaktifkan, akan terlihat `(venv_attrition)` di awal baris perintah yang menandakan bahwa sudah berada di lingkungan virtual.

2.  **Menginstal Dependensi dari `requirements.txt`**
    Pastikan  telah mengaktifkan virtual environment (langkah 1). Kemudian, instal semua pustaka Python yang dibutuhkan dari berkas `requirements.txt` menggunakan pip:
    ```bash
    pip install -r requirements.txt
    ```
    Ini akan menginstal semua *library* yang diperlukan.

3.  **Akses Data**
    * **Untuk Lingkungan Lokal:** Pastikan  telah mengunduh dataset dari (https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance) dan meletakkannya di lokasi yang sesuai dengan path yang digunakan dalam skrip Python.
    * **Untuk Google Colab:** Jika  menjalankan proyek di Google Colab maka perlu mengunggah file dataset ke Google Drive  dan melakukan *mount* Google Drive di Colab untuk mengaksesnya. Instruksi *mounting* dapat ditemukan di notebook Colab  (misalnya: `from google.colab import drive; drive.mount('/content/gdrive/')`).

4.  **Cara Menjalankan Skrip Python (.py)**
    Setelah virtual environment diaktifkan dan semua dependensi terinstal, maka dapat dijalankan skrip utama proyek. Skrip utama adalah `notebook.py`. Hasil analisis, model yang disimpan, atau output lainnya akan dihasilkan sesuai dengan logika skrip.

## Business Dashboard

Dashboard ini dirancang untuk menyajikan wawasan mendalam mengenai status dropout mahasiswa. Dengan menampilkan metrik utama, tren, dan perbandingan berdasarkan beragam faktor pemicu yang teridentifikasi dari analisis, dashboard ini bertujuan membantu pihak institut dalam mengidentifikasi area fokus strategis untuk meningkatkan motivasi dan keberhasilan studi mahasiswa.

🔗 URL : https://lookerstudio.google.com/reporting/e66c86a8-4304-4c63-9834-e10ab8286407

## Conclusion

Proyek ini berhasil melakukan analisis komprehensif terhadap data performa mahasiswa Jaya Jaya Institut. Melalui eksplorasi data dan penerapan uji statistik (seperti Chi-square dan t-test), proyek berhasil mengidentifikasi dan mengungkap korelasi serta perbedaan signifikan antara berbagai karakteristik mahasiswa dengan status putus kuliah.

Adapun karakteristik umum mahasiswa yang berstatus dropout:
A. Profil Demografi & Latar Belakang:
- Usia & Nilai Awal: Mahasiswa yang dropout memiliki rata-rata usia saat pendaftaran 26.07 tahun. Nilai kualifikasi sebelumnya rata-rata 131.09, dan nilai masuk rata-rata 124.67. Ini menunjukkan dropout tidak hanya terjadi pada mahasiswa sangat muda atau dengan nilai akademik rendah di awal.
- Jenis Kelamin: Proporsi dropout antara perempuan (50.8%) dan laki-laki (49.2%) hampir seimbang, menunjukkan tidak ada bias gender yang signifikan dalam fenomena dropout.
- Status Perkawinan: Mayoritas besar mahasiswa yang dropout berstatus Lajang (1.184 siswa), jauh melebihi kategori lain. Hal ini bisa mengindikasikan fleksibilitas hidup atau prioritas yang berbeda dibandingkan mereka yang sudah berkeluarga.
- Kualifikasi Pendidikan & Pekerjaan Orang Tua:
    - Mayoritas mahasiswa dropout berasal dari latar belakang di mana orang tua (baik ayah maupun ibu) memiliki kualifikasi pendidikan Menengah (Secondary Education) atau Pendidikan Dasar (Basic Education 3rd Cycle ke bawah).
    - Mengenai pekerjaan, banyak mahasiswa dropout memiliki orang tua (ayah dan ibu) yang berprofesi sebagai Pekerja Tidak Terampil (Unskilled Workers) atau Pekerja Terampil di Industri/Konstruksi. Ini mungkin mengindikasikan adanya tekanan ekonomi atau latar belakang sosial-ekonomi tertentu.
- Kualifikasi Sebelumnya Mahasiswa: Sebagian besar mahasiswa yang dropout masuk dengan kualifikasi Pendidikan Menengah (Secondary Education), menunjukkan bahwa ini adalah jalur masuk paling umum bagi mereka yang kemudian dropout.
  
B. Faktor Keuangan & Dukungan Institusional:
- Biaya Kuliah (Tuition Fees): Jumlah mahasiswa dropout yang biaya kuliahnya belum lunas/tepat waktu jauh lebih tinggi (~1.000 siswa) dibandingkan yang sudah lunas (~500 siswa). Ini adalah indikator kuat masalah keuangan yang berkontribusi pada dropout.
- Beasiswa: Mayoritas besar mahasiswa yang dropout bukanlah penerima beasiswa (~1.250 siswa). Ini mendukung hipotesis bahwa dukungan finansial (beasiswa) berperan penting dalam retensi mahasiswa.
- Status Debitur: Meskipun mayoritas mahasiswa dropout tidak berstatus debitur, ada kelompok signifikan (~250 siswa) yang berstatus debitur saat dropout. Ini menunjukkan bahwa masalah utang juga menjadi faktor bagi sebagian kelompok.
- Displaced: Jumlah mahasiswa dropout yang "Displaced" (tidak tinggal di tempat asal/terpisah dari keluarga) lebih tinggi (~750 siswa) dibandingkan yang tidak (~400 siswa). Ini bisa mengindikasikan kesulitan adaptasi atau kurangnya dukungan sosial/keluarga.

C. Jalur Pendaftaran & Program Studi:
- Mode Aplikasi: Mahasiswa yang mendaftar melalui mode "Over 23 years old" (435 siswa) dan "1st phase - general contingent" (345 siswa) merupakan kelompok terbesar di antara para dropout. Ini perlu diinvestigasi lebih lanjut mengapa mode aplikasi ini berkorelasi dengan dropout.
- Program Studi: Kursus "Management (evening attendance)" dan "Management" menunjukkan jumlah dropout tertinggi. Ini mungkin menunjukkan tantangan spesifik dalam kurikulum, beban kerja, atau harapan karier di program studi tersebut.
- Waktu Perkuliahan: Mayoritas besar mahasiswa yang dropout berasal dari program perkuliahan siang hari (Daytime, 83.2%). Ini menunjukkan bahwa program siang hari mungkin memiliki tantangan retensi yang berbeda dibandingkan program malam hari (yang mungkin lebih banyak diisi oleh pekerja).
  
D. Keterlibatan Akademik & Kurikulum (Sebelum Dropout):
- Rata-rata Unit Kurikulum: Mahasiswa yang dropout umumnya memiliki rata-rata unit yang terdaftar (enrolled) sekitar 21 (semester 1) dan 18 (semester 2). Rata-rata unit yang disetujui (approved) juga cukup tinggi, yaitu 21 (semester 1) dan 16 (semester 2).
- Nilai & Evaluasi: Nilai maksimum yang dicapai di semester 1 dan 2 adalah 18 dan 17. Ada juga unit tanpa evaluasi yang signifikan (maksimal 8 di semester 1, 12 di semester 2).
- Implikasi: Ini mengindikasikan bahwa mahasiswa yang dropout bukan berarti sama sekali tidak terlibat atau berprestasi. Banyak dari mereka sempat mengambil dan bahkan menyelesaikan sejumlah unit dengan nilai yang lumayan, sebelum akhirnya memutuskan untuk putus kuliah. Unit tanpa evaluasi bisa menjadi sinyal dini masalah.

### Rekomendasi Action Items (Optional)

1. Intervensi Finansial & Dukungan Ekonomi:
- Sistem Peringatan Dini Tunggakan Biaya Kuliah: Implementasikan sistem otomatis yang memberikan peringatan dini kepada mahasiswa dan/atau pembimbing/wali jika ada keterlambatan pembayaran biaya kuliah, diikuti dengan penawaran solusi atau bantuan (misalnya, cicilan, penundaan, atau informasi beasiswa).
- Peningkatan Program Beasiswa & Bantuan Keuangan: Perluas cakupan dan jenis beasiswa (terutama beasiswa berbasis kebutuhan) atau program bantuan keuangan lainnya, mengingat mayoritas dropout bukan pemegang beasiswa dan banyak yang memiliki tunggakan biaya.
- Konseling Keuangan: Sediakan layanan konseling keuangan bagi mahasiswa untuk membantu mereka mengelola anggaran, memahami opsi pinjaman pendidikan, dan mencari sumber pendanaan tambahan, terutama bagi mereka yang teridentifikasi sebagai debitur.
  
2. Dukungan Adaptasi & Kesejahteraan Mahasiswa:
- Program Adaptasi untuk Mahasiswa Lajang & Displaced: Kembangkan program orientasi atau komunitas yang lebih terfokus untuk mahasiswa lajang dan mereka yang "displaced" (jauh dari rumah/keluarga). Ini bisa berupa grup dukungan, kegiatan sosial, atau fasilitas tempat tinggal yang terjangkau.
- Dukungan Psikososial Terpadu: Perkuat layanan konseling dan dukungan mental/emosional. Mahasiswa dengan usia rata-rata 26 tahun yang dropout mungkin menghadapi tekanan hidup yang lebih kompleks di luar akademik.
- Program Mentoring Khusus: Pertimbangkan program mentoring di mana mahasiswa senior atau staf pengajar dapat membimbing mahasiswa baru atau mereka dari latar belakang pendidikan/pekerjaan orang tua yang kurang menguntungkan, membantu mereka menavigasi tantangan akademik dan sosial.
  
3. Tinjauan Kurikulum & Dukungan Akademik Khusus Program Studi:
- Evaluasi Program Studi dengan Angka Dropout Tinggi: Lakukan evaluasi menyeluruh terhadap kurikulum, metode pengajaran, beban kerja, dan peluang karier di program studi Management (evening attendance) dan Management yang memiliki tingkat dropout tinggi. Identifikasi titik-titik kesulitan spesifik.
- Sistem Peringatan Dini Keterlibatan Akademik: Kembangkan sistem untuk memonitor keterlibatan mahasiswa pada unit mata kuliah, terutama jika terdapat "unit tanpa evaluasi". Ini bisa menjadi indikator awal masalah akademik atau motivasi, dan memungkinkan intervensi lebih awal (misalnya, konseling akademik atau tutorial).
- Dukungan Akademik Terpersonalisasi: Tawarkan dukungan akademik tambahan (tutorial, bimbingan belajar) untuk mata kuliah-mata kuliah yang seringkali menyebabkan unit tanpa evaluasi atau nilai rendah di kalangan mahasiswa dropout.

4. Optimalisasi Proses Pendaftaran & Orientasi:
- Evaluasi Jalur Aplikasi Berisiko Tinggi: Tinjau proses penerimaan dan orientasi untuk mahasiswa yang mendaftar melalui mode "Over 23 years old" dan "1st phase - general contingent". Pastikan ekspektasi mereka terkelola dengan baik dan mereka mendapatkan dukungan adaptasi yang memadai sejak awal.
- Program Retensi Awal: Pertimbangkan program retensi yang difokuskan pada bulan-bulan atau semester pertama bagi kelompok-kelompok berisiko tinggi yang teridentifikasi dari mode aplikasi.
  
5. Pemantauan Berkelanjutan & Pengambilan Keputusan Berbasis Data:
- Pembentukan Tim Retensi: Bentuk tim lintas departemen (HR, Kemahasiswaan, Akademik, Keuangan) yang secara rutin meninjau dashboard dan menginterpretasikan data untuk mengidentifikasi mahasiswa berisiko.
- Pengembangan Protokol Intervensi: Buat protokol yang jelas tentang jenis intervensi apa yang harus dilakukan ketika seorang mahasiswa teridentifikasi berisiko dropout (misalnya, panggilan dari pembimbing akademik, penawaran konseling, atau bantuan keuangan).
- Iterasi Model & Dashboard: Lakukan pembaruan data dan evaluasi model serta dashboard secara berkala (misalnya, setiap semester) untuk memastikan relevansi dan akurasinya seiring waktu, mengingat kemungkinan adanya perubahan tren atau faktor pemicu.
