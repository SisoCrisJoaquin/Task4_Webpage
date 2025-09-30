import streamlit as st
import string

# ---- Page Config ----
st.set_page_config(page_title="Combined Python Programs", layout="centered")

# ---- Custom CSS to make it look like your HTML ----
st.markdown("""
    <style>
        body { font-family: Arial, sans-serif; }
        h1 { color: #333; }
        .stTextInput, .stPasswordInput { width: 100% !important; }
        .box {
            border: 1px solid #ccc; 
            padding: 20px; 
            border-radius: 10px; 
            margin-bottom: 30px;
            background-color: #f9f9f9;
        }
        .result {
            margin-top: 10px; 
            color: rgb(9, 9, 150); 
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.title("Python Programs Combined")

# ---- Task 1: Count Consonants ----
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Count Consonants")
    text_input = st.text_input("Enter text here")
    if st.button("Count Consonants"):
        vowels = "aeiouAEIOU"
        consonant_count = sum(1 for char in text_input if char.isalpha() and char not in vowels)
        st.markdown(f'<div class="result">Number of consonants: {consonant_count}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Task 2: Find Smallest Number ----
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Find Smallest Number")
    numbers_input = st.text_input("Enter numbers separated by commas")
    if st.button("Find Smallest"):
        try:
            numbers = list(map(int, numbers_input.split(",")))
            smallest = min(numbers)
            st.markdown(f'<div class="result">The smallest number is: {smallest}</div>', unsafe_allow_html=True)
        except:
            st.markdown('<div class="result" style="color:red;">Invalid input. Please enter numbers separated by commas.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Task 3: Password Validator ----
with st.container():
    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.subheader("Password Validator")
    password_input = st.text_input("Enter password", type="password")
    if st.button("Validate Password"):
        has_upper = any(ch.isupper() for ch in password_input)
        has_lower = any(ch.islower() for ch in password_input)
        has_digit = any(ch.isdigit() for ch in password_input)
        has_special = any(ch in string.punctuation for ch in password_input)
        if has_upper and has_lower and has_digit and has_special:
            st.markdown('<div class="result">Strong password. Account created.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="result" style="color:red;"> Invalid password. Must include uppercase, lowercase, number, and special character.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

