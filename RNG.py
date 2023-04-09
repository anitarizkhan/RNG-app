import streamlit as st 
import string
import secrets 

st.title('Random Number Generator')
st.balloons()

n= st.number_input ("Masukkan nilai n:", 0)
st.caption(':blue[Note: Masukkan berapa banyak nilai yang ingin dibangkitkan] ')


Generate = st.radio ('Generate', ['bytes', 'hexadecimal', 'alphabet'])


if Generate == 'bytes' :
    alphabet = string.ascii_letters + string.digits + string.punctuation
    random_byte = ''.join(secrets.choice(alphabet) for _ in range(n))
    #st.write("Kunci Bytes = " ,str(random_byte))
    st.success (f"Kunci Bytes = {random_byte}")

elif Generate == 'hexadecimal' :
    random_hex = secrets.token_hex(n)
    #st.write("kunci hexadecimal: ",(random_hex))
    st.success (f"Kunci Hexadecimal = {random_hex}")

else : 
    alphabet1 = string.ascii_letters
    random_alphabet = ''.join(secrets.choice(alphabet1) for _ in range(n))
    #st.write("kunci alphabet: " ,(random_alphabet))
    st.success (f"Kunci Alphabet = {random_alphabet}")
