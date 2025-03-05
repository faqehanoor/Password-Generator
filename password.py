import re
import streamlit as st

st.set_page_config(page_title="Password Generator", layout="centered")


st.markdown("""
<style>
    .stButton { display: flex; justify-content: center; }
    .stButton button { width: 50%; background-color:rgb(175, 76, 158); color: white; font-size: 18px; }
    .stButton button:hover { background-color: #45a049; }
</style>
""", unsafe_allow_html=True)


if "saved_passwords" not in st.session_state:
    st.session_state.saved_passwords = []


st.sidebar.title("Saved Passwords ♐")
if st.session_state.saved_passwords:
    for i, saved_pass in enumerate(st.session_state.saved_passwords, 1):
        st.sidebar.write(f"{i}. {saved_pass}")


st.title("🔓𝐏𝐚𝐬𝐬𝐰𝐨𝐫𝐝 𝐒𝐭𝐫𝐞𝐧𝐠𝐭𝐡 𝐌𝐞𝐭𝐞𝐫 🌎")
password = st.text_input("Enter your password ➡:", type="password")

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&* etc.).")

    return score, feedback


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Check Strength ✅"):
        if password:
       
            if password not in st.session_state.saved_passwords:
                st.session_state.saved_passwords.append(password)

            strength, suggestions = check_password_strength(password)

            if strength == 4:
                st.success("Wow! Your Password is Strong  ✅")
            elif strength == 3:
                st.warning("Moderate Password ⚠️")
            else:
                st.error("Hmm! Your  Password is Weak ❌")

            if suggestions:
                st.write("Suggestions:")
                for tip in suggestions:
                    st.write(f"- {tip}")
        else:
            st.warning("Please enter a password first!")
