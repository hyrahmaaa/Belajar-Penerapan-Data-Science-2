import streamlit as st
import pandas as pd
import numpy as np
import pickle 

# --- 1. Memuat Model dan Pra-pemrosesan (jika ada) ---
try:
    model = pickle.load(open('student_performance_status.pkl', 'rb'))
    st.success("Model berhasil dimuat!")
except Exception as e:
    st.error(f"Gagal memuat model: {e}")
    st.stop() 

# --- 2. Judul Aplikasi Streamlit ---
st.set_page_config(layout="wide") 
st.title('Aplikasi Prediksi Performa Mahasiswa Jaya Jaya Institut')
st.write('Aplikasi ini memprediksi kemungkinan seorang mahasiswa untuk dropout.')

# --- 3. Input Pengguna (sesuaikan dengan fitur model Anda) ---
st.header('Masukkan Data Mahasiswa:')

Gender = st.selectbox('Jenis Kelamin', ['Male', 'Female'])
Marital_status = st.selectbox('Status Pernikahan', ['Single', 'Married', 'Divorced', 'Widower'])
Age_at_enrollment = st.number_input('Usia Saat Pendaftaran', min_value=18, max_value=70, value=20)
Admission_grade = st.number_input('Nilai Rata-rata Masuk', min_value=0.0, max_value=200.0, value=100.0)
Previous_qualification_grade = st.number_input('Nilai Rata-rata Kualifikasi Sebelumnya', min_value=0.0, max_value=200.0, value=100.0)
Scholarship_holder = st.radio('Penerima Beasiswa', ['Ya', 'Tidak'])
GDP = st.number_input('GDP per kapita (nilai pada tahun pendaftaran)', min_value=-5.0, max_value=10.0, value=0.0)

# --- 4. Tombol Prediksi ---
if st.button('Prediksi'):
    # --- 5. Pra-pemrosesan Input (sesuaikan dengan langkah-langkah di notebook Anda) ---
    gender_encoded = 1 if Gender == 'Male' else 0 
    marital_status_encoded = {'Single': 0, 'Married': 1, 'Divorced': 2, 'Widower': 3}[Marital_status]
    scholarship_encoded = 1 if Scholarship_holder == 'Ya' else 0 # Contoh

    input_data = pd.DataFrame([[
        gender_encoded,
        marital_status_encoded,
        Age_at_enrollment,
        Admission_grade,
        Previous_qualification_grade,
        scholarship_encoded,
        GDP
    ]], columns=['Gender_encoded', 'Marital_status_encoded', 'Age_at_enrollment',
                 'Admission_grade', 'Previous_qualification_grade', 'Scholarship_holder_encoded', 'GDP']) # Ganti nama kolom sesuai fitur di model Anda!

    # --- 6. Melakukan Prediksi ---
    try:
        prediction = model.predict(input_data) 
        prediction_proba = model.predict_proba(input_data) 

        st.subheader('Hasil Prediksi:')
        if prediction[0] == 1: 
            st.warning('Mahasiswa diprediksi **DO (Dropout)**')
        else:
            st.success('Mahasiswa diprediksi **TIDAK DO (Tidak Dropout)**')

        st.write(f'Probabilitas Dropout: {prediction_proba[0][1]:.2f}')
        st.write(f'Probabilitas Tidak Dropout: {prediction_proba[0][0]:.2f}')

        st.write("---")
        st.write("Catatan: Prediksi ini bersifat probabilistik dan tidak menjamin hasil mutlak.")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat melakukan prediksi: {e}")
        st.write("Pastikan semua input sudah sesuai dan model termuat dengan benar.")

# --- 7. (Opsional) Informasi Tambahan atau Footer ---
st.sidebar.header('Tentang Aplikasi Ini')
st.sidebar.info('Aplikasi ini dikembangkan sebagai bagian dari proyek Data Science untuk memprediksi performa mahasiswa Jaya Jaya Institut.')
