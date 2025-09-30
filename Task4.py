import streamlit as st
import string

# Task 1: Count Consonants
st.header("Count Consonants")
text_input = st.text_input("Enter text here")
if st.button("Count Consonants"):
    if text_input:
        vowels = "aeiouAEIOU"
        consonant_count = sum(1 for char in text_input if char.isalpha() and char not in vowels)
        st.success(f"Number of consonants: {consonant_count}")

# Task 2: Find Smallest Number
st.header("Find Smallest Number")
numbers_input = st.text_input("Enter numbers separated by commas")
if st.button("Find Smallest"):
    if numbers_input:
        try:
            numbers = list(map(int, numbers_input.split(",")))
            smallest = numbers[0]
            for num in numbers:
                if num < smallest:
                    smallest = num
            st.success(f"The smallest number is: {smallest}")
        except:
            st.error("Invalid input. Please enter numbers separated by commas.")

# Task 3: Password Validator
st.header("Password Validator")
password_input = st.text_input("Enter password", type="password")
if st.button("Validate Password"):
    if password_input:
        has_upper = any(ch.isupper() for ch in password_input)
        has_lower = any(ch.islower() for ch in password_input)
        has_digit = any(ch.isdigit() for ch in password_input)
        has_special = any(ch in string.punctuation for ch in password_input)
        if has_upper and has_lower and has_digit and has_special:
            st.success("Strong password. Account created.")
        else:
            st.error("Invalid password. Too weak.")

