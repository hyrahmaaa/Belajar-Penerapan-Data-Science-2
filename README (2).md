# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah beroperasi sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di seluruh Indonesia. Sebagai perusahaan yang cukup besar, Jaya Jaya Maju menghadapi tantangan dalam mengelola karyawan, yang tercermin dalam tingkat attrition rate yang tinggi, melebihi 10%. Situasi ini berpotensi mengganggu stabilitas operasional, meningkatkan biaya, dan mengurangi efektivitas organisasi. Manajemen departemen HR menyadari perlunya tindakan proaktif berbasis data untuk memahami dan mengatasi akar permasalahan ini.

### Permasalahan Bisnis

Permasalahan bisnis utama yang akan diselesaikan adalah:
- Tingginya Tingkat Attrition Karyawan: Rasio karyawan yang keluar dari perusahaan (lebih dari 10%) dianggap tidak sehat dan perlu diturunkan.
- Kurangnya Pemahaman Faktor Penyebab Attrition: Departemen HR belum memiliki pemahaman yang mendalam mengenai faktor-faktor spesifik yang secara signifikan berkontribusi terhadap tingginya tingkat attrition.
- Kebutuhan akan Sistem Monitoring Berkelanjutan: Belum adanya alat atau sistem yang efektif untuk memonitor tren attrition dan faktor-faktor terkait secara berkelanjutan, sehingga pengambilan keputusan strategis menjadi kurang optimal.
  
### Cakupan Proyek

Cakupan proyek ini meliputi:
- Analisis Data Karyawan: Menganalisis dataset yang disediakan oleh Jaya Jaya Maju untuk mengidentifikasi pola, korelasi, dan faktor-faktor yang mempengaruhi attrition karyawan.
- Pengembangan Model Machine Learning: Membangun model machine learning yang mampu menganalisis akurasi faktor yang memiliki potensi attrition karyawan berdasarkan data yang ada.
- Pembuatan Dashboard Visualisasi: Merancang dan mengembangkan dashboard interaktif yang memungkinkan departemen HR untuk memonitor tingkat attrition, mengidentifikasi faktor-faktor kunci, dan melacak tren dari waktu ke waktu.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

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
    * **Untuk Lingkungan Lokal:** Pastikan  telah mengunduh dataset dari (https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee) dan meletakkannya di lokasi yang sesuai dengan path yang digunakan dalam skrip Python.
    * **Untuk Google Colab:** Jika  menjalankan proyek di Google Colab maka perlu mengunggah file dataset ke Google Drive  dan melakukan *mount* Google Drive di Colab untuk mengaksesnya. Instruksi *mounting* dapat ditemukan di notebook Colab  (misalnya: `from google.colab import drive; drive.mount('/content/gdrive/')`).

4.  **Cara Menjalankan Skrip Python (.py)**
    Setelah virtual environment diaktifkan dan semua dependensi terinstal, maka dapat dijalankan skrip utama proyek. Skrip utama adalah `notebook.py`. Hasil analisis, model yang disimpan, atau output lainnya akan dihasilkan sesuai dengan logika skrip.

## Business Dashboard

Dashboard ini dirancang untuk memberikan pemahaman yang mendalam tentang attrition karyawan dengan menampilkan metrik utama, tren, dan perbandingan berdasarkan berbagai faktor. Tujuannya adalah untuk membantu departemen HR mengidentifikasi area fokus untuk meningkatkan retensi karyawan. Adapun yang ditampilkan adalah faktor-faktor yang mempengaruhi attration berdasarkan analisis pada notebook.

🔗 URL : https://lookerstudio.google.com/reporting/1df393fd-e55c-43c5-a287-7e2feee0fa0d

## Conclusion

Proyek ini berhasil melakukan analisis mendalam terhadap data karyawan Jaya Jaya Maju untuk mengidentifikasi berbagai faktor yang berpotensi mempengaruhi tingginya tingkat attrition karyawan. Melalui eksplorasi data dan analisis statistik (seperti uji Chi-square dan t-test), korelasi dan perbedaan signifikan antara berbagai fitur karyawan dengan status attrition berhasil diungkap.

Adapun karakteristik umum karyawan yang melakukan attrition:
- Masa Kerja dengan Manajer yang Lebih Singkat:
Karyawan yang memiliki rata-rata masa kerja yang lebih singkat dengan manajer saat ini (sekitar 2.9 tahun) menunjukkan kecenderungan lebih tinggi untuk keluar. Ini mengindikasikan bahwa hubungan atau durasi interaksi dengan manajer langsung bisa menjadi faktor penting dalam keputusan karyawan untuk bertahan.

- Masa Kerja dengan Current Role yang Lebih Singkat:
Mirip dengan masa kerja dengan manajer, karyawan yang memiliki masa kerja lebih pendek di peran mereka saat ini (rata-rata 2.99 tahun) juga memiliki probabilitas attrition yang lebih tinggi. Hal ini mungkin menunjukkan ketidakpuasan dengan peran yang sedang dijalani atau kurangnya kesempatan untuk berkembang dalam peran tersebut.

- Status Pernikahan: Banyak Pekerja yang Masih Single:
Data menunjukkan bahwa proporsi karyawan yang masih single lebih tinggi di antara mereka yang melakukan attrition. Ini bisa berarti karyawan single memiliki fleksibilitas lebih besar atau pertimbangan hidup yang berbeda dibandingkan mereka yang sudah menikah, sehingga lebih mudah untuk berganti pekerjaan.

- Pola Perjalanan Bisnis: Travel Rarely Lebih Berpotensi Attrition:
Karyawan yang jarang melakukan perjalanan bisnis (Travel_Rarely) secara paradoks lebih berpotensi untuk keluar. Ini bisa mengindikasikan bahwa karyawan yang jarang bepergian mungkin merasa kurang terlibat, kurang memiliki kesempatan pengembangan, atau kurang terstimulasi dibandingkan mereka yang lebih sering bepergian.

- Peran Pekerjaan (Job Role): Teknisi Laboratorium (Teknik Laboratorium) Cenderung Menunjukkan Attrition Tertinggi:
Dari semua peran pekerjaan, Teknisi Laboratorium (Teknik Laboratorium) menunjukkan jumlah attrition tertinggi. Hal ini memerlukan investigasi lebih lanjut: apakah ada isu spesifik terkait beban kerja, kompensasi, peluang karir, atau lingkungan di departemen ini?

- Demografi Karyawan yang Attrition:
     - Rata-rata Usia: Karyawan yang melakukan attrition memiliki rata-rata usia sekitar 33.47 tahun. Ini menunjukkan bahwa attrition banyak terjadi pada karyawan di usia produktif awal hingga menengah.
     - Jarak dari Rumah: Rata-rata jarak dari rumah ke tempat kerja bagi karyawan yang keluar adalah 10.37 km. Jarak yang signifikan ini bisa berkontribusi pada kelelahan atau ketidaknyamanan, yang pada akhirnya memicu attrition.
     - Penghasilan Bulanan: Karyawan yang keluar memiliki rata-rata penghasilan bulanan sekitar 4,872.94 dollar. Penting untuk membandingkan angka ini dengan rata-rata penghasilan di seluruh perusahaan dan pasar untuk menilai apakah kompensasi menjadi isu.

- Tingkat Kepuasan Kerja yang rendah pada posisi kedua:
Secara konsisten, karyawan yang melaporkan tingkat kepuasan kerja yang lebih rendah diposisi kedua sebesar 25,7% cenderung memiliki probabilitas attrition yang lebih tinggi. Ini adalah indikator langsung bahwa ketidakpuasan terhadap pekerjaan itu sendiri adalah pendorong utama karyawan untuk mencari peluang lain.

- Tingkat Keterlibatan Kerja yang sangat tinggi:
Terlalu tinggi tingkat keterlibatan dalam pekerjaan juga merupakan indikator kuat potensi attrition. Karyawan yang merasa tertekan dan memiliki beban kerja berlebih secara emosional dalam pekerjaan mereka lebih mudah untuk pergi.

- Kualitas Lingkungan Kerja yang Rendah:
Penilaian lingkungan kerja yang rendah secara signifikan mempengaruhi kecenderungan attrition. Lingkungan yang tidak mendukung, kurang nyaman, atau tidak aman dapat menjadi faktor pendorong karyawan untuk mencari tempat kerja lain.

- Keseimbangan Kerja dan Hidup (Work-Life Balance) yang Terlalu Baik:
Karyawan yang melaporkan keseimbangan kerja dan hidup yang terlalu baik cenderung attrition bisa didukung dengan keterangan tiada tantangan dan pertumbuhan karir.

- Tingkat Opsi Saham yang Rendah:
Ada korelasi antara tingkat opsi saham yang lebih rendah dengan peningkatan attrition. Ini bisa menunjukkan bahwa opsi saham berfungsi sebagai insentif jangka panjang yang signifikan, dan ketiadaannya dapat mengurangi loyalitas karyawan.

- Tingkat Jabatan (Job Level) Tertentu:
Analisis menunjukkan bahwa tingkat jabatan (Job Level) 0 menunjukkan risiko attrition yang lebih tinggi. Ini mengindikasikan potensi isu pada struktur karir atau skema kompensasi yang tidak menarik di level-level tersebut.

- Bidang Pendidikan Spesifik:
Karyawan dari bidang pendidikan Life Sciences menunjukkan kecenderungan lebih tinggi untuk melakukan attrition. Hal ini memerlukan investigasi lebih lanjut untuk memahami mengapa bidang pendidikan ini lebih rentan, apakah karena prospek karir di luar perusahaan lebih menarik atau ada isu spesifik terkait relevansi pendidikan mereka dengan pekerjaan di Jaya Jaya Maju.

Untuk memfasilitasi pemantauan berkelanjutan dan pemahaman yang lebih baik oleh departemen HR, sebuah dashboard visualisasi yang komprehensif telah dirancang dan dikembangkan. Dashboard ini menyajikan metrik kunci terkait attrition, tren dari waktu ke waktu, dan perbandingan attrition berdasarkan berbagai faktor demografis dan terkait pekerjaan. Visualisasi ini bertujuan untuk memberikan wawasan yang actionable bagi HR untuk memahami pola attrition dan mengidentifikasi area fokus untuk upaya retensi karyawan.

Secara keseluruhan, proyek ini telah berhasil mengidentifikasi faktor-faktor penting yang terkait dengan attrition karyawan di Jaya Jaya Maju dan menyediakan alat visualisasi yang berharga bagi departemen HR untuk memonitor dan memahami fenomena ini. Hasil analisis dan dashboard ini dapat menjadi dasar yang kuat bagi perusahaan dalam merumuskan strategi retensi karyawan yang lebih efektif dan tepat sasaran.

### Rekomendasi Action Items (Optional)

- Rata-rata Masa Kerja dengan Manajer (Average Years With Current Manager): dapat melakukan survei untuk memahami gaya kepemimpinan para manajer dan dampak pada tim, pelatihan kepemimpinan, rotasi manajer terstruktur.
- Tingkat Kepuasan Kerja (Job Satisfaction Rate): melakukan survei kepuasan kerja secara anonim secara berkala dan menindaklanjuti hasil surveinya.
- Tingkat Keterlibatan Kerja (Job Involvement Rate): memberikan karyawan lebih banyak otonomi dalam pekerjaan mereka dan libatkan mereka dalam pengambilan keputusan yang relevan, menawarkan pengembangan keterampilan dan promosi internal.
- Keseimbangan Kerja dan Hidup (Attrition by Work Life Balance): mempertimbangkan opsi kerja fleksibel seperti jam kerja yang disesuaikan atau mendorong karyawan untuk mengambil cuti dan istirahat yang cukup, mawarkan program yang mendukung kesehatan fisik dan mental karyawan.
- Tingkat Opsi Saham (Attrition by Stock Option Level): meninjau kembali program opsi saham perusahaan, mekankan nilai jangka panjang dari kepemilikan saham perusahaan kepada karyawan.
- Tingkat Jabatan (Job Level Rate): memaastikan struktur jabatan yang jelas dan kompensasi yang kompetitif untuk setiap level, menyediakan jalur karir yang jelas bagi karyawan untuk naik level dalam organisasi.
- Bidang Pendidikan (Attrition by Education Field): menyelidiki lebih lanjut latar belakang pendidikan tertentu yang lebih cenderung meninggalkan perusahaan dan melakukan survei, mempertimbangkan strategi rekrutmen atau program pengembangan karir untuk kelompok pendidikan tertentu.
