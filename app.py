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

try:
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    st.success("Scaler loaded successfully!")
except Exception as e:
    st.warning(f"Warning: Failed to load scaler: {e}. If your model requires numerical scaling, this will cause issues. Make sure 'scaler.pkl' is in the correct directory.")
    scaler = None

# --- 2. Judul Aplikasi Streamlit ---
st.set_page_config(layout="wide") 
st.title('Aplikasi Prediksi Performa Mahasiswa Jaya Jaya Institut')
st.write('Aplikasi ini memprediksi kemungkinan seorang mahasiswa untuk dropout.')

# --- 3. Input Pengguna (sesuaikan dengan fitur model Anda) ---
st.header('Masukkan Data Mahasiswa:')

Marital_status_display = st.selectbox(
    'Marital Status',
    ['Single', 'Married', 'Widower', 'Divorced', 'Facto Union', 'Legally Separated'],
    help="Select the student's marital status."
)
Application_mode_options = [
    '1st phase - general contingent',
    'Ordinance No. 612/93',
    '1st phase - special contingent (Azores Island)',
    'Holders of other higher courses',
    'Ordinance No. 854-B/99',
    'International student (bachelor)',
    '1st phase - special contingent (Madeira Island)',
    '2nd phase - general contingent',
    '3rd phase - general contingent',
    'Ordinance No. 533-A/99, item b2) (Different Plan)',
    'Ordinance No. 533-A/99, item b3 (Other Institution)',
    'Over 23 years old',
    'Transfer',
    'Change of course',
    'Technological specialization diploma holders',
    'Change of institution/course',
    'Short cycle diploma holders',
    'Change of institution/course (International)'
]

Application_mode_display = st.selectbox(
    'Application Mode',
    Application_mode_options,
    help="Select the mode of application for admission."
)

Course_options = [
    'Biofuel Production Technologies',
    'Animation and Multimedia Design',
    'Social Service (evening attendance)',
    'Agronomy',
    'Communication Design',
    'Veterinary Nursing',
    'Informatics Engineering',
    'Equinculture',
    'Management',
    'Social Service',
    'Tourism',
    'Nursing',
    'Oral Hygiene',
    'Advertising and Marketing Management',
    'Journalism and Communication',
    'Basic Education',
    'Management (evening attendance)'
]

Course_display = st.selectbox(
    'Course',
    Course_options,
    help="Select the academic course the student is enrolled in."
)
Daytime_evening_attendance = st.selectbox(
    'Attendance Type',
    ['Daytime', 'Evening'],
    help="Select whether the student attends daytime or evening classes."
)

Previous_qualification_options = [
    'Secondary education',
    "Higher education - bachelor's degree",
    'Higher education - degree',
    "Higher education - master's",
    'Higher education - doctorate',
    'Frequency of higher education',
    '12th year of schooling - not completed',
    '11th year of schooling - not completed',
    'Other - 11th year of schooling',
    '10th year of schooling',
    '10th year of schooling - not completed',
    'Basic education 3rd cycle (9th/10th/11th year) or equiv.',
    'Basic education 2nd cycle (6th/7th/8th year) or equiv.',
    'Technological specialization course',
    'Higher education - degree (1st cycle)',
    'Professional higher technical course',
    'Higher education - master (2nd cycle)'
]

Previous_qualification_display = st.selectbox(
    'Previous Qualification',
    Previous_qualification_options,
    help="Select the student's previous highest academic qualification."
)

Mothers_qualification_options = [
    'Secondary Education - 12th Year of Schooling or Eq.',
    "Higher Education - Bachelor's Degree",
    'Higher Education - Degree',
    "Higher Education - Master's",
    'Higher Education - Doctorate',
    'Frequency of Higher Education',
    '12th Year of Schooling - Not Completed',
    '11th Year of Schooling - Not Completed',
    '7th Year (Old)',
    'Other - 11th Year of Schooling',
    '10th Year of Schooling',
    'General commerce course',
    'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
    'Technical-professional course',
    '7th year of schooling',
    '2nd cycle of the general high school course',
    '9th Year of Schooling - Not Completed',
    '8th year of schooling',
    'Unknown',
    "Can't read or write",
    'Can read without having a 4th year of schooling',
    'Basic education 1st cycle (4th/5th year) or equiv.',
    'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
    'Technological specialization course',
    'Higher education - degree (1st cycle)',
    'Specialized higher studies course',
    'Professional higher technical course',
    'Higher Education - Master (2nd cycle)',
    'Higher Education - Doctorate (3rd cycle)'
]

Mothers_qualification_display = st.selectbox(
    "Mother's Qualification",
    Mothers_qualification_options,
    help="Select the highest academic qualification of the student's mother."
)

Fathers_qualification_options = [
    'Secondary Education - 12th Year of Schooling or Eq.',
    "Higher Education - Bachelor's Degree",
    'Higher Education - Degree',
    "Higher Education - Master's",
    'Higher Education - Doctorate',
    'Frequency of Higher Education',
    '12th Year of Schooling - Not Completed',
    '11th Year of Schooling - Not Completed',
    '7th Year (Old)',
    'Other - 11th Year of Schooling',
    '2nd year complementary high school course',
    '10th Year of Schooling',
    'General commerce course',
    'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.',
    'Complementary High School Course',
    'Technical-professional course',
    'Complementary High School Course - not concluded',
    '7th year of schooling',
    '2nd cycle of the general high school course',
    '9th Year of Schooling - Not Completed',
    '8th year of schooling',
    'General Course of Administration and Commerce',
    'Supplementary Accounting and Administration',
    'Unknown',
    "Can't read or write",
    'Can read without having a 4th year of schooling',
    'Basic education 1st cycle (4th/5th year) or equiv.',
    'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.',
    'Technological specialization course',
    'Higher education - degree (1st cycle)',
    'Specialized higher studies course',
    'Professional higher technical course',
    'Higher Education - Master (2nd cycle)',
    'Higher Education - Doctorate (3rd cycle)'
]

Fathers_qualification_display = st.selectbox(
    "Father's Qualification",
    Fathers_qualification_options,
    help="Select the highest academic qualification of the student's father."
)

Mothers_occupation_options = [
    'Student',
    'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
    'Specialists in Intellectual and Scientific Activities',
    'Intermediate Level Technicians and Professions',
    'Administrative staff',
    'Personal Services, Security and Safety Workers and Sellers',
    'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
    'Skilled Workers in Industry, Construction and Craftsmen',
    'Installation and Machine Operators and Assembly Workers',
    'Unskilled Workers',
    'Armed Forces Professions',
    'Other Situation',
    '(blank)', # Note: Be careful with (blank), ensure it's handled correctly if it represents NaN or a specific category
    'Health professionals',
    'teachers',
    'Specialists in information and communication technologies (ICT)',
    'Intermediate level science and engineering technicians and professions',
    'Technicians and professionals, of intermediate level of health',
    'Intermediate level technicians from legal, social, sports, cultural and similar services',
    'Office workers, secretaries in general and data processing operators',
    'Data, accounting, statistical, financial services and registry-related operators',
    'Other administrative support staff',
    'personal service workers',
    'sellers',
    'Personal care workers and the like',
    'Skilled construction workers and the like, except electricians',
    'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like',
    'Workers in food processing, woodworking, clothing and other industries and crafts',
    'cleaning workers',
    'Unskilled workers in agriculture, animal production, fisheries and forestry',
    'Unskilled workers in extractive industry, construction, manufacturing and transport',
    'Meal preparation assistants'
]

Mothers_occupation_display = st.selectbox(
    "Mother's Occupation",
    Mothers_occupation_options,
    help="Select the occupation of the student's mother."
)

Fathers_occupation_options = [
    'Student',
    'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers',
    'Specialists in Intellectual and Scientific Activities',
    'Intermediate Level Technicians and Professions',
    'Administrative staff',
    'Personal Services, Security and Safety Workers and Sellers',
    'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry',
    'Skilled Workers in Industry, Construction and Craftsmen',
    'Installation and Machine Operators and Assembly Workers',
    'Unskilled Workers',
    'Armed Forces Professions',
    'Other Situation',
    '(blank)', # Note: Be careful with (blank), ensure it's handled correctly if it represents NaN or a specific category
    'Armed Forces Officers',
    'Armed Forces Sergeants',
    'Other Armed Forces personnel',
    'Directors of administrative and commercial services',
    'Hotel, catering, trade and other services directors',
    'Specialists in the physical sciences, mathematics, engineering and related techniques',
    'Health professionals',
    'teachers',
    'Specialists in finance, accounting, administrative organization, public and commercial relations',
    'Intermediate level science and engineering technicians and professions',
    'Technicians and professionals, of intermediate level of health',
    'Intermediate level technicians from legal, social, sports, cultural and similar services',
    'Information and communication technology technicians',
    'Office workers, secretaries in general and data processing operators',
    'Data, accounting, statistical, financial services and registry-related operators',
    'Other administrative support staff',
    'personal service workers',
    'sellers',
    'Personal care workers and the like',
    'Protection and security services personnel',
    'Market-oriented farmers and skilled agricultural and animal production workers',
    'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence',
    'Skilled construction workers and the like, except electricians',
    'Skilled workers in metallurgy, metalworking and similar',
    'Skilled workers in electricity and electronics',
    'Workers in food processing, woodworking, clothing and other industries and crafts',
    'Fixed plant and machine operators',
    'assembly workers',
    'Vehicle drivers and mobile equipment operators',
    'Unskilled workers in agriculture, animal production, fisheries and forestry',
    'Unskilled workers in extractive industry, construction, manufacturing and transport',
    'Meal preparation assistants',
    'Street vendors (except food) and street service providers'
]

Fathers_occupation_display = st.selectbox(
    "Father's Occupation",
    Fathers_occupation_options,
    help="Select the occupation of the student's father."
)

Displaced_display = st.radio(
    'Displaced Student',
    ['Yes', 'No'], 
    help="Is the student displaced (e.g., moved due to external factors)?"
)
Debtor_display = st.radio(
    'Debtor Status',
    ['Yes', 'No'], 
    help="Is the student a debtor (i.e., has outstanding debts)?"
)
Tuition_fees_up_to_date_display = st.radio(
    'Tuition Fees Up-to-Date',
    ['Yes', 'No'], 
    help="Is the student's tuition fee payment up-to-date?"
)
Gender_display = st.selectbox(
    'Gender',
    ['Female', 'Male'],
    help="Select the student's gender."
)
Scholarship_holder_display = st.radio(
    'Scholarship Holder',
    ['Yes', 'No'], 
    help="Is the student a scholarship holder?"
)
Age_at_enrollment = st.number_input('Age at Enrollment', min_value=17, max_value=80, value=20, help="Student's age when first enrolling.")
Admission_grade = st.number_input('Admission Grade Average', min_value=0.0, max_value=200.0, value=100.0, help="Average grade from admission exams/criteria.")
Previous_qualification_grade = st.number_input('Previous Qualification Grade Average', min_value=0.0, max_value=200.0, value=100.0, help="Average grade from previous academic qualification.")
GDP = st.number_input('GDP per capita (year of enrollment)', min_value=-10.0, max_value=20.0, value=0.0, format="%.2f", help="GDP per capita of the student's origin country at enrollment year.")
Application_order = st.number_input('Application Order', min_value=1, max_value=10, value=1, help="Order of the student's application (e.g., 1st, 2nd, etc.).")
Curricular_units_1st_sem_enrolled = st.number_input('1st Sem Units Enrolled', min_value=0, max_value=50, value=6, help="Number of curricular units enrolled in the 1st semester.")
Curricular_units_1st_sem_evaluations = st.number_input('1st Sem Evaluations', min_value=0, max_value=50, value=7, help="Number of evaluations in the 1st semester.")
Curricular_units_1st_sem_approved = st.number_input('1st Sem Units Approved', min_value=0, max_value=50, value=6, help="Number of curricular units approved in the 1st semester.")
Curricular_units_1st_sem_grade = st.slider('1st Sem Grade Average', min_value=0.0, max_value=20.0, value=10.0, step=0.1, help="Average grade of curricular units in the 1st semester.")
Curricular_units_1st_sem_without_evaluations = st.number_input('1st Sem Units without Evaluations', min_value=0, max_value=50, value=0, help="Number of curricular units without evaluations in the 1st semester.")
Curricular_units_2nd_sem_credited = st.number_input('2nd Sem Units Credited', min_value=0, max_value=50, value=0, help="Number of curricular units credited in the 2nd semester.")
Curricular_units_2nd_sem_enrolled = st.number_input('2nd Sem Units Enrolled', min_value=0, max_value=50, value=6, help="Number of curricular units enrolled in the 2nd semester.")
Curricular_units_2nd_sem_evaluations = st.number_input('2nd Sem Evaluations', min_value=0, max_value=50, value=7, help="Number of evaluations in the 2nd semester.")
Curricular_units_2nd_sem_approved = st.number_input('2nd Sem Units Approved', min_value=0, max_value=50, value=6, help="Number of curricular units approved in the 2nd semester.")
Curricular_units_2nd_sem_grade = st.slider('2nd Sem Grade Average', min_value=0.0, max_value=20.0, value=10.0, step=0.1, help="Average grade of curricular units in the 2nd semester.")

# --- 4. Tombol Prediksi ---
if st.button('Prediksi'):
    # --- 5. Pra-pemrosesan Input  ---
    marital_status_map_rev = {
        'Single': 0,
        'Married': 1,
        'Widower': 2,
        'Divorced': 3,
        'Facto Union': 4,
        'Legally Separated': 5
    }
    marital_status_encoded = marital_status_map_rev[Marital_status_display]

    application_mode_map_rev = {
        '1st phase - general contingent': 0,
        'Ordinance No. 612/93': 1,
        '1st phase - special contingent (Azores Island)': 2,
        'Holders of other higher courses': 3,
        'Ordinance No. 854-B/99': 4,
        'International student (bachelor)': 5,
        '1st phase - special contingent (Madeira Island)': 6,
        '2nd phase - general contingent': 7,
        '3rd phase - general contingent': 8,
        'Ordinance No. 533-A/99, item b2) (Different Plan)': 9,
        'Ordinance No. 533-A/99, item b3 (Other Institution)': 10,
        'Over 23 years old': 11,
        'Transfer': 12,
        'Change of course': 13,
        'Technological specialization diploma holders': 14,
        'Change of institution/course': 15,
        'Short cycle diploma holders': 16,
        'Change of institution/course (International)': 17
    }
    application_mode_encoded = application_mode_map_rev[Application_mode_display]

    course_map_rev = {
        'Biofuel Production Technologies': 0,
        'Animation and Multimedia Design': 1,
        'Social Service (evening attendance)': 2,
        'Agronomy': 3,
        'Communication Design': 4,
        'Veterinary Nursing': 5,
        'Informatics Engineering': 6,
        'Equinculture': 7,
        'Management': 8,
        'Social Service': 9,
        'Tourism': 10,
        'Nursing': 11,
        'Oral Hygiene': 12,
        'Advertising and Marketing Management': 13,
        'Journalism and Communication': 14,
        'Basic Education': 15,
        'Management (evening attendance)': 16
    }
    course_encoded = course_map_rev[Course_display]
    
    daytime_evening_attendance_map_rev = {
        'Daytime': 1,
        'Evening': 0
    }
    daytime_evening_attendance_encoded = daytime_evening_attendance_map_rev[Daytime_evening_attendance_display]
    
    previous_qualification_map_rev = {
        'Secondary education': 0,
        "Higher education - bachelor's degree": 1,
        'Higher education - degree': 2,
        "Higher education - master's": 3,
        'Higher education - doctorate': 4,
        'Frequency of higher education': 5,
        '12th year of schooling - not completed': 6,
        '11th year of schooling - not completed': 7,
        'Other - 11th year of schooling': 8,
        '10th year of schooling': 9,
        '10th year of schooling - not completed': 10,
        'Basic education 3rd cycle (9th/10th/11th year) or equiv.': 11,
        'Basic education 2nd cycle (6th/7th/8th year) or equiv.': 12,
        'Technological specialization course': 13,
        'Higher education - degree (1st cycle)': 14,
        'Professional higher technical course': 15,
        'Higher education - master (2nd cycle)': 16
    }
    previous_qualification_encoded = previous_qualification_map_rev[Previous_qualification_display]
    
     mothers_qualification_map_rev = {
        'Secondary Education - 12th Year of Schooling or Eq.': 0,
        "Higher Education - Bachelor's Degree": 1,
        'Higher Education - Degree': 2,
        "Higher Education - Master's": 3,
        'Higher Education - Doctorate': 4,
        'Frequency of Higher Education': 5,
        '12th Year of Schooling - Not Completed': 6,
        '11th Year of Schooling - Not Completed': 7,
        '7th Year (Old)': 8,
        'Other - 11th Year of Schooling': 9,
        '10th Year of Schooling': 10,
        'General commerce course': 11,
        'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.': 12,
        'Technical-professional course': 13,
        '7th year of schooling': 14,
        '2nd cycle of the general high school course': 15,
        '9th Year of Schooling - Not Completed': 16,
        '8th year of schooling': 17,
        'Unknown': 18,
        "Can't read or write": 19,
        'Can read without having a 4th year of schooling': 20,
        'Basic education 1st cycle (4th/5th year) or equiv.': 21,
        'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.': 22,
        'Technological specialization course': 23,
        'Higher education - degree (1st cycle)': 24,
        'Specialized higher studies course': 25,
        'Professional higher technical course': 26,
        'Higher Education - Master (2nd cycle)': 27,
        'Higher Education - Doctorate (3rd cycle)': 28
    }
    mothers_qualification_encoded = mothers_qualification_map_rev[Mothers_qualification_display]
       
    fathers_qualification_map_rev = {
        'Secondary Education - 12th Year of Schooling or Eq.': 0,
        "Higher Education - Bachelor's Degree": 1,
        'Higher Education - Degree': 2,
        "Higher Education - Master's": 3,
        'Higher Education - Doctorate': 4,
        'Frequency of Higher Education': 5,
        '12th Year of Schooling - Not Completed': 6,
        '11th Year of Schooling - Not Completed': 7,
        '7th Year (Old)': 8,
        'Other - 11th Year of Schooling': 9,
        '2nd year complementary high school course': 10,
        '10th Year of Schooling': 11,
        'General commerce course': 12,
        'Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.': 13,
        'Complementary High School Course': 14,
        'Technical-professional course': 15,
        'Complementary High School Course - not concluded': 16,
        '7th year of schooling': 17,
        '2nd cycle of the general high school course': 18,
        '9th Year of Schooling - Not Completed': 19,
        '8th year of schooling': 20,
        'General Course of Administration and Commerce': 21,
        'Supplementary Accounting and Administration': 22,
        'Unknown': 23,
        "Can't read or write": 24,
        'Can read without having a 4th year of schooling': 25,
        'Basic education 1st cycle (4th/5th year) or equiv.': 26,
        'Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.': 27,
        'Technological specialization course': 28,
        'Higher education - degree (1st cycle)': 29,
        'Specialized higher studies course': 30,
        'Professional higher technical course': 31,
        'Higher Education - Master (2nd cycle)': 32,
        'Higher Education - Doctorate (3rd cycle)': 33
    }
    fathers_qualification_encoded = fathers_qualification_map_rev[Fathers_qualification_display]

    mothers_occupation_map_rev = {
        'Student': 0,
        'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
        'Specialists in Intellectual and Scientific Activities': 2,
        'Intermediate Level Technicians and Professions': 3,
        'Administrative staff': 4,
        'Personal Services, Security and Safety Workers and Sellers': 5,
        'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6,
        'Skilled Workers in Industry, Construction and Craftsmen': 7,
        'Installation and Machine Operators and Assembly Workers': 8,
        'Unskilled Workers': 9,
        'Armed Forces Professions': 10,
        'Other Situation': 11,
        '(blank)': 12, # Ensure this mapping matches your training data for (blank) values
        'Health professionals': 13,
        'teachers': 14,
        'Specialists in information and communication technologies (ICT)': 15,
        'Intermediate level science and engineering technicians and professions': 16,
        'Technicians and professionals, of intermediate level of health': 17,
        'Intermediate level technicians from legal, social, sports, cultural and similar services': 18,
        'Office workers, secretaries in general and data processing operators': 19,
        'Data, accounting, statistical, financial services and registry-related operators': 20,
        'Other administrative support staff': 21,
        'personal service workers': 22,
        'sellers': 23,
        'Personal care workers and the like': 24,
        'Skilled construction workers and the like, except electricians': 25,
        'Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like': 26,
        'Workers in food processing, woodworking, clothing and other industries and crafts': 27,
        'cleaning workers': 28,
        'Unskilled workers in agriculture, animal production, fisheries and forestry': 29,
        'Unskilled workers in extractive industry, construction, manufacturing and transport': 30,
        'Meal preparation assistants': 31
    }
    mothers_occupation_encoded = mothers_occupation_map_rev[Mothers_occupation_display]


    fathers_occupation_map_rev = {
        'Student': 0,
        'Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers': 1,
        'Specialists in Intellectual and Scientific Activities': 2,
        'Intermediate Level Technicians and Professions': 3,
        'Administrative staff': 4,
        'Personal Services, Security and Safety Workers and Sellers': 5,
        'Farmers and Skilled Workers in Agriculture, Fisheries and Forestry': 6,
        'Skilled Workers in Industry, Construction and Craftsmen': 7,
        'Installation and Machine Operators and Assembly Workers': 8,
        'Unskilled Workers': 9,
        'Armed Forces Professions': 10,
        'Other Situation': 11,
        '(blank)': 12, # Ensure this mapping matches your training data for (blank) values
        'Armed Forces Officers': 13,
        'Armed Forces Sergeants': 14,
        'Other Armed Forces personnel': 15,
        'Directors of administrative and commercial services': 16,
        'Hotel, catering, trade and other services directors': 17,
        'Specialists in the physical sciences, mathematics, engineering and related techniques': 18,
        'Health professionals': 19,
        'teachers': 20,
        'Specialists in finance, accounting, administrative organization, public and commercial relations': 21,
        'Intermediate level science and engineering technicians and professions': 22,
        'Technicians and professionals, of intermediate level of health': 23,
        'Intermediate level technicians from legal, social, sports, cultural and similar services': 24,
        'Information and communication technology technicians': 25,
        'Office workers, secretaries in general and data processing operators': 26,
        'Data, accounting, statistical, financial services and registry-related operators': 27,
        'Other administrative support staff': 28,
        'personal service workers': 29,
        'sellers': 30,
        'Personal care workers and the like': 31,
        'Protection and security services personnel': 32,
        'Market-oriented farmers and skilled agricultural and animal production workers': 33,
        'Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence': 34,
        'Skilled construction workers and the like, except electricians': 35,
        'Skilled workers in metallurgy, metalworking and similar': 36,
        'Skilled workers in electricity and electronics': 37,
        'Workers in food processing, woodworking, clothing and other industries and crafts': 38,
        'Fixed plant and machine operators': 39,
        'assembly workers': 40,
        'Vehicle drivers and mobile equipment operators': 41,
        'Unskilled workers in agriculture, animal production, fisheries and forestry': 42,
        'Unskilled workers in extractive industry, construction, manufacturing and transport': 43,
        'Meal preparation assistants': 44,
        'Street vendors (except food) and street service providers': 45
    }
    fathers_occupation_encoded = fathers_occupation_map_rev[Fathers_occupation_display]

    displaced_map_rev = {
        'No': 0,
        'Yes': 1
    }
    displaced_encoded = displaced_map_rev[Displaced_display]
    
    debtor_map_rev = {
        'No': 0,
        'Yes': 1
    }
    debtor_encoded = debtor_map_rev[Debtor_display]
    
    tuition_fees_map_rev = {
        'No': 0,
        'Yes': 1
    }
    tuition_fees_encoded = tuition_fees_map_rev[Tuition_fees_up_to_date_display]
    
    gender_map_rev = {
        'Female': 0,
        'Male': 1
    }
    gender_encoded = gender_map_rev[Gender_display]
    
    scholarship_holder_map_rev = {
        'No': 0,
        'Yes': 1
    }
    scholarship_holder_encoded = scholarship_holder_map_rev[Scholarship_holder_display]

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

    all_features_data = list(scaled_numerical_input[0]) + ['marital_status_encoded', 'application_mode_encoded', 'Application_order', 'course_encoded', 
                             'daytime_evening_attendance_encoded', 'previous_qualification_encoded', 'Previous_qualification_grade', 
                             'mothers_qualification_encoded', 'fathers_qualification_encoded', 'mothers_occupation_encoded', 
                             'fathers_occupation_encoded', 'Admission_grade', 'displaced_encoded', 'debtor_encoded', 
                             'tuition_fees_encoded', 'gender_encoded', 'scholarship_holder_encoded', 'Age_at_enrollment', 
                             'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations', 
                             'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 
                             'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited', 
                             'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 
                             'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 
                             'Curricular_units_2nd_sem_without_evaluations', 'GDP']

    numerical_features_raw = [
        Application_order,
        Previous_qualification_grade,
        Age_at_enrollment,
        Curricular_units_1st_sem_enrolled,
        Curricular_units_1st_sem_evaluations,
        Curricular_units_1st_sem_approved,
        Curricular_units_1st_sem_grade,
        Curricular_units_1st_sem_without_evaluations,
        Curricular_units_2nd_sem_credited,
        Curricular_units_2nd_sem_enrolled,
        Curricular_units_2nd_sem_evaluations,
        Curricular_units_2nd_sem_approved,
        Curricular_units_2nd_sem_grade,
        Curricular_units_2nd_sem_without_evaluations,
        GDP
    ]

    numerical_input_array = np.array(numerical_features_raw).reshape(1, -1)

    if scaler is not None:
        scaled_numerical_input = scaler.transform(numerical_input_array)
    else:
        scaled_numerical_input = numerical_input_array


    # --- 6. Melakukan Prediksi ---
    try:
        prediction = model.predict(input_data) # Atau scaled_input jika digunakan
        prediction_proba = model.predict_proba(input_data) 
        st.subheader('Hasil Prediksi:')
        if prediction[0] == 1: # Asumsi 1 = Dropout, 0 = Tidak Dropout
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
