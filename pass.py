import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # Include all letters (a-z, A-Z)

    if use_digits:
        characters += string.digits # Adds digits (0-9)

    if use_special:
        characters += string.punctuation  # Adds special Characters (!, @, #, $, %, ^, &, *)

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password Lenght", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generate Password: `{password}`")

st.write("----------------------")

st.write("Build with 💞 by [SAYYED JALEES](https://github.com/syedjalees)")