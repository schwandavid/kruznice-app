import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Body na kružnici")

# --- 1. Vstupy od uživatele ---
st.sidebar.header("Parametry kružnice")
stred_x = st.sidebar.number_input("Střed X", value=0.0)
stred_y = st.sidebar.number_input("Střed Y", value=0.0)
polomer = st.sidebar.number_input("Poloměr", value=5.0, min_value=0.1)
pocet_bodu = st.sidebar.number_input("Počet bodů", value=8, min_value=1, step=1)
barva = st.sidebar.color_picker("Barva bodů", "#ff0000")

# --- 2. Výpočet bodů ---
uhly = np.linspace(0, 2*np.pi, pocet_bodu, endpoint=False)
x_body = stred_x + polomer * np.cos(uhly)
y_body = stred_y + polomer * np.sin(uhly)

# --- 3. Vykreslení ---
fig, ax = plt.subplots()
ax.set_aspect("equal", "box")
ax.scatter(x_body, y_body, c=barva, s=80)
ax.add_artist(plt.Circle((stred_x, stred_y), polomer, color="blue", fill=False))
ax.set_xlabel("x [m]")
ax.set_ylabel("y [m]")
ax.grid(True)

st.pyplot(fig)

# --- 4. Info o autorovi ---
with st.expander("O aplikaci"):
    st.write("""
    **Autor:** Jan Novák  
    **Kontakt:** jan.novak@email.com  
    **Použité technologie:** Python, Streamlit, Matplotlib
    """)
