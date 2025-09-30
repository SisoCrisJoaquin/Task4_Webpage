import streamlit as st
import string

# ---- Page Config ----
st.set_page_config(page_title="Three-point-Hackaton", layout="centered")

# ---- Custom CSS (Matches your HTML design) ----
st.markdown("""
    <style>
        /* Full background image */
        .stApp {
            background-image: url("blackboard-background-2268-x-1276-eaxyg9odzdsotzk1.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        h1 {
            color: #1a1a1a;
            text-align: center;
            font-family: "Segoe UI", Arial, sans-serif;
            font-weight: 700;
        }

        .box {
            background: #ffffff;
            padding: 25px;
            border-radius: 12px;
            margin: 20px auto;
            max-width: 600px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }

        .stTextInput>div>div>input, 
        .stPasswordInput>div>div>input {
            width: 100% !important;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 14px;
        }

        .stButton>button {
            padding: 10px 18px;
            border: none;
            border-radius: 6px;
            background-color: #004085;
            color: white;
            font-size: 14px;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #003366;
        }

        .result {
            margin-top: 12px;
            font-size: 16px;
            font-weight: 600;
            color: #004085;
            background: #e2e6ea;
            padding: 10px;
            border-radius: 6px;
        }

        .error {
            margin-top: 12px;
            font-size: 16px;
            font-weight: 600;
            color: #721c24;
            background: #f8d7da;
            padding: 10px;
            border-radius: 6px;
        }

        .success {
            margin-top: 12px;
            font-size: 16px;
            font-weight: 600;
            color: #155724;
            background: #d4edda;
            padding: 10px;
            border-radius: 6px;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.title("Three-point-Hackaton")

# ---- Task 1: Count Consonants ----
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Counting Consonants")
    text_input = st.text_input("Enter text here")
    if st.button("Count"):
        vowels = "aeiouAEIOU"
        consonant_count = sum(1 for char in text_input if char.isalpha() and char not in vowels)
        st.markdown(f'<div class="result">Number of consonants: {consonant_count}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Task 2: Find Smallest Number ----
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Smallest Number Indicator")
    numbers_input = st.text_input("Enter numbers separated by commas")
    if st.button("Start"):
        try:
            numbers = list(map(int, numbers_input.split(",")))
            smallest = min(numbers)
            st.markdown(f'<div class="success">Indicated Smallest Number: {smallest}</div>', unsafe_allow_html=True)
        except:
            st.markdown('<div class="error">Invalid input. Please enter numbers separated by commas.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Task 3: Password Validator ----
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Password Validator")
    password_input = st.text_input("Enter password")
    if st.button("Validate Password"):
        has_upper = any(ch.isupper() for ch in password_input)
        has_lower = any(ch.islower() for ch in password_input)
        has_digit = any(ch.isdigit() for ch in password_input)
        has_special = any(ch in string.punctuation for ch in password_input)
        if has_upper and has_lower and has_digit and has_special:
            st.markdown('<div class="success">Strong password. Account created.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="error">Invalid password. Password strength: Weak.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)










