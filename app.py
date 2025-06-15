import os
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# --- 1. Konfigurasi Halaman Streamlit  ---
st.set_page_config(layout="wide", page_title="Prediksi Performa Mahasiswa")

# --- 2. Judul Aplikasi Streamlit ---
st.title('Aplikasi Prediksi Performa Mahasiswa Jaya Jaya Institut')
st.write('Aplikasi ini memprediksi kemungkinan seorang mahasiswa untuk dropout.')

# --- 3. Memuat Model dan Pra-pemrosesan Objects ---
try:
    model = joblib.load('student_performance_status.pkl')
    st.success("Machine Learning Model berhasil dimuat!")
except Exception as e:
    st.error(f"Error memuat Model ML: {e}. Pastikan 'student_performance_status.pkl' ada di direktori yang benar.")
    st.stop()

try:
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    st.success("Scaler berhasil dimuat!")
except Exception as e:
    st.warning(f"Peringatan: Gagal memuat scaler: {e}. Jika model Anda memerlukan scaling, ini akan menyebabkan masalah. Pastikan 'scaler.pkl' ada di direktori yang benar.")
    scaler = None # Set scaler ke None jika gagal dimuat

# --- Definisi Mapping untuk Fitur Kategorikal ---
marital_status_map_rev = {
    'Single': 0, 'Married': 1, 'Widower': 2, 'Divorced': 3, 'Facto Union': 4, 'Legally Separated': 5
}
application_mode_map_rev = {
    '1st phase - general contingent': 0, 'Ordinance No. 612/93': 1, '1st phase - special contingent (Azores Island)': 2,
    'Holders of other higher courses': 3, 'Ordinance No. 854-B/99': 4, 'International student (bachelor)': 5,
    '1st phase - special contingent (Madeira Island)': 6, '2nd phase - general contingent': 7,
    '3rd phase - general contingent': 8, 'Ordinance No. 533-A/99, item b2) (Different Plan)': 9,
    'Ordinance No. 533-A/99, item b3 (Other Institution)': 10, 'Over 23 years old': 11, 'Transfer': 12,
    'Change of course': 13, 'Technological specialization diploma holders': 14, 'Change of institution/course': 15,
    'Short cycle diploma holders': 16, 'Change of institution/course (International)': 17
}
course_map_rev = {
    'Biofuel Production Technologies': 0, 'Animation and Multimedia Design': 1, 'Social Service (evening attendance)': 2,
    'Agronomy': 3, 'Communication Design': 4, 'Veterinary Nursing': 5, 'Informatics Engineering': 6, 'Equinculture': 7,
    'Management': 8, 'Social Service': 9, 'Tourism': 10, 'Nursing': 11, 'Oral Hygiene': 12,
    'Advertising and Marketing Management': 13, 'Journalism and Communication': 14, 'Basic Education': 15,
    'Management (evening attendance)': 16
}
daytime_evening_attendance_map_rev = {'Daytime': 1, 'Evening': 0}
previous_qualification_map_rev = {
    'Secondary education': 0, "Higher education - bachelor's degree": 1, 'Higher education - degree': 2,
    "Higher education - master's": 3, 'Higher education - doctorate': 4, 'Frequency of higher education': 5,
    '12th year of schooling - not completed': 6, '11th year of schooling - not completed': 7,
    'Other - 11th year of schooling': 8, '10th year of schooling': 9, '10th year of schooling - not completed': 10,
    'Basic education 3rd cycle (9th/10th/11th year) or equiv.': 11, 'Basic education 2nd cycle (6th/7th/8th year) or equiv.': 12,
    'Technological specialization course': 13, 'Higher education - degree (1st cycle)': 14,
    'Professional higher technical course': 15, 'Higher education - master (2nd cycle)': 16
}
mothers_qualification_map_rev = {
    'Secondary Education - 12th Year of Schooling or Eq.': 0, "Higher Education - Bachelor's Degree": 1, 'Higher Education - Degree': 2,
    "Higher Education - Master's": 3, 'Higher Education - Doctorate': 4, 'Frequency of Higher Education': 5,
    '12th Year of Schooling - Not Completed': 6, '11th Year of Schooling - Not Completed': 7, '7th Year (Old)': 8,
    'Other - 11th Year of Schooling': 9, '10th Year of Schooling': 10, 'General commerce course': 11,
    'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.': 12, 'Technical-professional course': 13,
    '7th year of schooling': 14, '2nd cycle of the general high school course': 15,
    '9th Year of Schooling - Not Completed': 16, '8th year of schooling': 17, 'Unknown': 18, "Can't read or write": 19,
    'Can read without having a 4th year of schooling': 20, 'Basic education 1st cycle (4th/5th year) or equiv.': 21,
    'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.': 22, 'Technological specialization course': 23,
    'Higher education - degree (1st cycle)': 24, 'Specialized higher studies course': 25,
    'Professional higher technical course': 26, 'Higher Education - Master (2nd cycle)': 27,
    'Higher Education - Doctorate (3rd cycle)': 28
}
fathers_qualification_map_rev = {
    'Secondary Education - 12th Year of Schooling or Eq.': 0, "Higher Education - Bachelor's Degree": 1, 'Higher Education - Degree': 2,
    "Higher Education - Master's": 3, 'Higher Education - Doctorate': 4, 'Frequency of Higher Education': 5,
    '12th Year of Schooling - Not Completed': 6, '11th Year of Schooling - Not Completed': 7, '7th Year (Old)': 8,
    'Other - 11th Year of Schooling': 9, '2nd year complementary high school course': 10, '10th Year of Schooling': 11,
    'General commerce course': 12, 'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.': 13,
    'Complementary High School Course': 14, 'Technical-professional course': 15, 'Complementary High School Course - not concluded': 16,
    '7th year of schooling': 17, '2nd cycle of the general high school course': 18, '9th Year of Schooling - Not Completed': 19,
    '8th year of schooling': 20, 'General Course of Administration and Commerce': 21, 'Supplementary Accounting and Administration': 22,
    'Unknown': 23, "Can't read or write": 24, 'Can read without having a 4th year of schooling': 25,
    'Basic education 1st cycle (4th/5th year) or equiv.': 26, 'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.': 27,
    'Technological specialization course': 28, 'Higher education - degree (1st cycle)': 29,
    'Specialized higher studies course': 30, 'Professional higher technical course': 31,
    'Higher Education - Master (2nd cycle)': 32, 'Higher Education - Doctorate (3rd cycle)': 33
}
mothers_occupation_map_rev = {
    'Student': 0, 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
    'Specialists in Intellectual and Scientific Activities': 2, 'Intermediate Level Technicians and Professions': 3,
    'Administrative staff': 4, 'Personal Services, Security and Safety Workers and Sellers': 5,
    'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6, 'Skilled Workers in Industry, Construction and Craftsmen': 7,
    'Installation and Machine Operators and Assembly Workers': 8, 'Unskilled Workers': 9, 'Armed Forces Professions': 10,
    'Other Situation': 11, '(blank)': 12, 'Health professionals': 13, 'teachers': 14,
    'Specialists in information and communication technologies (ICT)': 15, 'Intermediate level science and engineering technicians and professions': 16,
    'Technicians and professionals, of intermediate level of health': 17,
    'Intermediate level technicians from legal, social, sports, cultural and similar services': 18,
    'Office workers, secretaries in general and data processing operators': 19,
    'Data, accounting, statistical, financial services and registry-related operators': 20,
    'Other administrative support staff': 21, 'personal service workers': 22, 'sellers': 23,
    'Personal care workers and the like': 24, 'Skilled construction workers and the like, except electricians': 25,
    'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like': 26,
    'Workers in food processing, woodworking, clothing and other industries and crafts': 27,
    'cleaning workers': 28, 'Unskilled workers in agriculture, animal production, fisheries and forestry': 29,
    'Unskilled workers in extractive industry, construction, manufacturing and transport': 30, 'Meal preparation assistants': 31
}
fathers_occupation_map_rev = {
    'Student': 0, 'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
    'Specialists in Intellectual and Scientific Activities': 2, 'Intermediate Level Technicians and Professions': 3,
    'Administrative staff': 4, 'Personal Services, Security and Safety Workers and Sellers': 5,
    'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6, 'Skilled Workers in Industry, Construction and Craftsmen': 7,
    'Installation and Machine Operators and Assembly Workers': 8, 'Unskilled Workers': 9, 'Armed Forces Professions': 10,
    'Other Situation': 11, '(blank)': 12, 'Armed Forces Officers': 13, 'Armed Forces Sergeants': 14,
    'Other Armed Forces personnel': 15, 'Directors of administrative and commercial services': 16,
    'Hotel, catering, trade and other services directors': 17, 'Specialists in the physical sciences, mathematics, engineering and related techniques': 18,
    'Health professionals': 19, 'teachers': 20,
    'Specialists in finance, accounting, administrative organization, public and commercial relations': 21,
    'Intermediate level science and engineering technicians and professions': 22,
    'Technicians and professionals, of intermediate level of health': 23,
    'Intermediate level technicians from legal, social, sports, cultural and similar services': 24,
    'Information and communication technology technicians': 25,
    'Office workers, secretaries in general and data processing operators': 26,
    'Data, accounting, statistical, financial services and registry-related operators': 27,
    'Other administrative support staff': 28, 'personal service workers': 29, 'sellers': 30,
    'Personal care workers and the like': 31, 'Protection and security services personnel': 32,
    'Market-oriented farmers and skilled agricultural and animal production workers': 33,
    'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence': 34,
    'Skilled construction workers and the like, except electricians': 35,
    'Skilled workers in metallurgy, metalworking and similar': 36,
    'Skilled workers in electricity and electronics': 37,
    'Workers in food processing, woodworking, clothing and other industries and crafts': 38,
    'Fixed plant and machine operators': 39, 'assembly workers': 40, 'Vehicle drivers and mobile equipment operators': 41,
    'Unskilled workers in agriculture, animal production, fisheries and forestry': 42,
    'Unskilled workers in extractive industry, construction, manufacturing and transport': 43,
    'Meal preparation assistants': 44, 'Street vendors (except food) and street service providers': 45
}
displaced_map_rev = {'No': 0, 'Yes': 1}
debtor_map_rev = {'No': 0, 'Yes': 1}
tuition_fees_map_rev = {'No': 0, 'Yes': 1}
gender_map_rev = {'Female': 0, 'Male': 1}
scholarship_holder_map_rev = {'No': 0, 'Yes': 1}

# --- 4. Input Pengguna  ---
st.header('Masukkan Data Mahasiswa:')

# Menggunakan kolom untuk tata letak yang lebih baik
col1, col2, col3 = st.columns(3)

with col1:
    Marital_status_display = st.selectbox(
        'Marital Status',
        list(marital_status_map_rev.keys()),
        help="Select the student's marital status."
    )

    Application_mode_display = st.selectbox(
        'Application Mode',
        list(application_mode_map_rev.keys()),
        help="Select the mode of application for admission."
    )

    Course_display = st.selectbox(
        'Course',
        list(course_map_rev.keys()),
        help="Select the academic course the student is enrolled in."
    )

    Daytime_evening_attendance_display = st.selectbox(
        'Attendance Type',
        list(daytime_evening_attendance_map_rev.keys()),
        help="Select whether the student attends daytime or evening classes."
    )
    
    Previous_qualification_display = st.selectbox(
        'Previous Qualification',
        list(previous_qualification_map_rev.keys()),
        help="Select the student's previous highest academic qualification."
    )
    
    Mothers_qualification_display = st.selectbox(
        "Mother's Qualification",
        list(mothers_qualification_map_rev.keys()),
        help="Select the highest academic qualification of the student's mother."
    )

    Fathers_qualification_display = st.selectbox(
        "Father's Qualification",
        list(fathers_qualification_map_rev.keys()),
        help="Select the highest academic qualification of the student's father."

with col2:
    Mothers_occupation_display = st.selectbox(
        "Mother's Occupation",
        list(mothers_occupation_map_rev.keys()),
        help="Select the occupation of the student's mother."
    )

    Fathers_occupation_display = st.selectbox(
        "Father's Occupation",
        list(fathers_occupation_map_rev.keys()),
        help="Select the occupation of the student's father."
    )

    Displaced_display = st.radio(
        'Displaced Student',
        list(displaced_map_rev.keys()),
        help="Is the student displaced (e.g., moved due to external factors)?"
    )

    Debtor_display = st.radio(
        'Debtor Status',
        list(debtor_map_rev.keys()),
        help="Is the student a debtor (i.e., has outstanding debts)?"
    )
    
    Tuition_fees_up_to_date_display = st.radio(
        'Tuition Fees Up-to-Date',
        list(tuition_fees_map_rev.keys()),
        help="Is the student's tuition fee payment up-to-date?"
    )

    Gender_display = st.selectbox(
        'Gender',
        list(gender_map_rev.keys()),
        help="Select the student's gender."
    )

    Scholarship_holder_display = st.radio(
        'Scholarship Holder',
        list(scholarship_holder_map_rev.keys()),
        help="Is the student a scholarship holder?"
    )

with col3:
    Age_at_enrollment = st.number_input('Age at Enrollment', min_value=17, max_value=80, value=20, help="Student's age when first enrolling.")
    Admission_grade = st.number_input('Admission Grade', min_value=0.0, max_value=200.0, value=127.0, help="Student's admission grade.")
    Previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0.0, max_value=200.0, value=122.0, help="Student's previous qualification grade.")
    GDP = st.number_input('GDP per capita (year of enrollment)', min_value=-10.0, max_value=20.0, value=1.0, format="%.2f", help="Gross Domestic Product per capita of the student's origin country at enrollment year.")
    Application_order = st.number_input('Application Order', min_value=1, max_value=10, value=5, help="Order of the student's application (e.g., 1st, 2nd, etc.).")
    Curricular_units_1st_sem_enrolled = st.number_input('1st Sem Units Enrolled', min_value=0, max_value=50, value=0, help="Number of curricular units enrolled in the 1st semester.")
    Curricular_units_1st_sem_evaluations = st.number_input('1st Sem Evaluations', min_value=0, max_value=50, value=0, help="Number of evaluations in the 1st semester.")
    Curricular_units_1st_sem_approved = st.number_input('1st Sem Units Approved', min_value=0, max_value=50, value=0, help="Number of curricular units approved in the 1st semester.")
    Curricular_units_1st_sem_grade = st.slider('1st Sem Grade', min_value=0.0, max_value=20.0, value=0.0, step=0.1, help="Grade of curricular units in the 1st semester.")
    Curricular_units_1st_sem_without_evaluations = st.number_input('1st Sem Units without Evaluations', min_value=0, max_value=50, value=0, help="Number of curricular units without evaluations in the 1st semester.")
    Curricular_units_2nd_sem_credited = st.number_input('2nd Sem Units Credited', min_value=0, max_value=50, value=0, help="Number of curricular units credited in the 2nd semester.")
    Curricular_units_2nd_sem_enrolled = st.number_input('2nd Sem Units Enrolled', min_value=0, max_value=50, value=0, help="Number of curricular units enrolled in the 2nd semester.")
    Curricular_units_2nd_sem_evaluations = st.number_input('2nd Sem Evaluations', min_value=0, max_value=50, value=0, help="Number of evaluations in the 2nd semester.")
    Curricular_units_2nd_sem_approved = st.number_input('2nd Sem Units Approved', min_value=0, max_value=50, value=0, help="Number of curricular units approved in the 2nd semester.")
    Curricular_units_2nd_sem_grade = st.slider('2nd Sem Grade', min_value=0.0, max_value=20.0, value=0.0, step=0.1, help="Grade of curricular units in the 2nd semester.")
    Curricular_units_2nd_sem_without_evaluations = st.number_input('2nd Sem Units without Evaluations', min_value=0, max_value=50, value=0, help="Number of curricular units without evaluations in the 2nd semester.")


# --- 5. Tombol Prediksi ---
if st.button('Prediksi'):
    # --- 6. Pra-pemrosesan Input untuk Model ---
    marital_status_encoded = marital_status_map_rev[Marital_status_display]
    application_mode_encoded = application_mode_map_rev[Application_mode_display]
    course_encoded = course_map_rev[Course_display]
    daytime_evening_attendance_encoded = daytime_evening_attendance_map_rev[Daytime_evening_attendance_display]
    previous_qualification_encoded = previous_qualification_map_rev[Previous_qualification_display]
    mothers_qualification_encoded = mothers_qualification_map_rev[Mothers_qualification_display]
    fathers_qualification_encoded = fathers_qualification_map_rev[Fathers_qualification_display]
    mothers_occupation_encoded = mothers_occupation_map_rev[Mothers_occupation_display]
    fathers_occupation_encoded = fathers_occupation_map_rev[Fathers_occupation_display]
    displaced_encoded = displaced_map_rev[Displaced_display]
    debtor_encoded = debtor_map_rev[Debtor_display]
    tuition_fees_encoded = tuition_fees_map_rev[Tuition_fees_up_to_date_display]
    gender_encoded = gender_map_rev[Gender_display]
    scholarship_holder_encoded = scholarship_holder_map_rev[Scholarship_holder_display]

    # Define the exact order of features your model expects
    model_feature_columns = ['Marital_status', 'Application_mode', 'Application_order', 'Course',
                             'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
                             'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation',
                             'Fathers_occupation', 'Admission_grade', 'Displaced', 'Debtor',
                             'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'Age_at_enrollment',
                             'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations',
                             'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
                             'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited',
                             'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations',
                             'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
                             'Curricular_units_2nd_sem_without_evaluations', 'GDP']

    processed_features_dict = {}

    processed_features_dict['Application_order'] = Application_order
    processed_features_dict['Previous_qualification_grade'] = Previous_qualification_grade
    processed_features_dict['Age_at_enrollment'] = Age_at_enrollment
    processed_features_dict['Admission_grade'] = Admission_grade 
    processed_features_dict['Curricular_units_1st_sem_enrolled'] = Curricular_units_1st_sem_enrolled
    processed_features_dict['Curricular_units_1st_sem_evaluations'] = Curricular_units_1st_sem_evaluations
    processed_features_dict['Curricular_units_1st_sem_approved'] = Curricular_units_1st_sem_approved
    processed_features_dict['Curricular_units_1st_sem_grade'] = Curricular_units_1st_sem_grade
    processed_features_dict['Curricular_units_1st_sem_without_evaluations'] = Curricular_units_1st_sem_without_evaluations
    processed_features_dict['Curricular_units_2nd_sem_credited'] = Curricular_units_2nd_sem_credited
    processed_features_dict['Curricular_units_2nd_sem_enrolled'] = Curricular_units_2nd_sem_enrolled
    processed_features_dict['Curricular_units_2nd_sem_evaluations'] = Curricular_units_2nd_sem_evaluations
    processed_features_dict['Curricular_units_2nd_sem_approved'] = Curricular_units_2nd_sem_approved
    processed_features_dict['Curricular_units_2nd_sem_grade'] = Curricular_units_2nd_sem_grade
    processed_features_dict['Curricular_units_2nd_sem_without_evaluations'] = Curricular_units_2nd_sem_without_evaluations
    processed_features_dict['GDP'] = GDP

    processed_features_dict['Marital_status'] = marital_status_encoded
    processed_features_dict['Application_mode'] = application_mode_encoded
    processed_features_dict['Course'] = course_encoded
    processed_features_dict['Daytime_evening_attendance'] = daytime_evening_attendance_encoded
    processed_features_dict['Previous_qualification'] = previous_qualification_encoded
    processed_features_dict['Mothers_qualification'] = mothers_qualification_encoded
    processed_features_dict['Fathers_qualification'] = fathers_qualification_encoded
    processed_features_dict['Mothers_occupation'] = mothers_occupation_encoded
    processed_features_dict['Fathers_occupation'] = fathers_occupation_encoded
    processed_features_dict['Displaced'] = displaced_encoded
    processed_features_dict['Debtor'] = debtor_encoded
    processed_features_dict['Tuition_fees_up_to_date'] = tuition_fees_encoded
    processed_features_dict['Gender'] = gender_encoded
    processed_features_dict['Scholarship_holder'] = scholarship_holder_encoded


    numerical_cols_in_order_for_scaling = [
        'Application_order', 'Previous_qualification_grade', 'Age_at_enrollment',
        'Admission_grade',
        'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations',
        'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
        'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations',
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
        'Curricular_units_2nd_sem_without_evaluations', 'GDP'
    ]

    numerical_data_for_scaling_values = [processed_features_dict[col] for col in numerical_cols_in_order_for_scaling]
    numerical_input_df = pd.DataFrame(
        np.array(numerical_data_for_scaling_values).reshape(1, -1),
        columns=numerical_cols_in_order_for_scaling # Tambahkan nama kolom di sini
    )

    if scaler is not None:
        scaled_numerical_data = scaler.transform(numerical_input_df.values) # <--- GANTI DENGAN INI (tambah .values)
    else:
        scaled_numerical_data = numerical_input_df.values # <--- GANTI DENGAN INI (tambah .values)

    final_features_for_df = {}
    idx_numerical = 0
    for col in model_feature_columns:
        if col in numerical_cols_in_order_for_scaling: 
            final_features_for_df[col] = scaled_numerical_data[0][idx_numerical]
            idx_numerical += 1
        else: 
            final_features_for_df[col] = processed_features_dict[col]

    input_df = pd.DataFrame([final_features_for_df]) 

    # --- 6. Make Prediction ---
    try:
        prediction = model.predict(input_df) 
        prediction_proba = model.predict_proba(input_df)

        st.subheader('Prediction Result:')
        if prediction[0] == 1: 
            st.warning('The student is predicted to **DROP OUT**')
        else:
            st.success('The student is predicted **NOT to DROP OUT**')

        st.write(f'Probability of Dropout: **{prediction_proba[0][1]*100:.2f}%**')
        st.write(f'Probability of Not Dropping Out: **{prediction_proba[0][0]*100:.2f}%**')

        st.write("---")
        st.info("Note: This prediction is probabilistic and should be used as an indicator. Always consider individual circumstances.")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.write("Please ensure all inputs are valid and the model is correctly loaded and configured.")

# --- 7. Optional: Sidebar/Footer Info ---
st.sidebar.header('About This Application')
st.sidebar.info('Aplikasi ini dikembangkan sebagai bagian dari proyek Data Science untuk memprediksi performa mahasiswa Jaya Jaya Institut.')
st.sidebar.write('Developed by Rahayunr') 
