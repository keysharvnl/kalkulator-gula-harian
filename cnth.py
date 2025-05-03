import streamlit as st

st.set_page_config(page_title="Kalkulator Kadar Gula Total", page_icon="🍭", layout="centered")

# Daftar makanan dengan kadar gula per porsi (gram) - diperluas
KADAR_GULA_MAKANAN = {} 

st.title("🍬 Kalkulator Kadar Gula Total dalam Makanan")
st.markdown(
    """
    Hitung total kadar gula yang Anda konsumsi dari berbagai jenis makanan sehari-hari.
    Masukkan jumlah porsi setiap makanan yang Anda makan.
    """
)

with st.form(key="form_gula_total"):
    jumlah_porsi = {}
    for makanan, gula_per_porsi in KADAR_GULA_MAKANAN.items():
        jumlah_porsi[makanan] = st.number_input(
            f"{makanan} (Gula: {gula_per_porsi} gram per porsi)", min_value=0, step=1, format="%d"
        )
    tombol_hitung = st.form_submit_button("Hitung Total Gula")

if tombol_hitung:
    total_gula = 0
    for makanan, qty in jumlah_porsi.items():
        total_gula += qty * KADAR_GULA_MAKANAN[makanan]

    st.success(f"Total kadar gula yang Anda konsumsi adalah **{total_gula:.1f} gram** per hari.")
    st.markdown(
        """
        ### Batasan Konsumsi Gula Harian yang Disarankan
        - Wanita: maksimal 25 gram gula tambahan per hari.
        - Pria: maksimal 36 gram gula tambahan per hari.

        Jaga pola makan sehat dengan membatasi konsumsi gula sesuai rekomendasi ini!
        """
    )
else:
    st.info("Masukkan jumlah porsi untuk setiap makanan dan klik tombol 'Hitung Total Gula' untuk mengetahui konsumsi gula Anda.")

st.markdown("---")
st.markdown("Dibuat dengan ❤️ menggunakan Streamlit")
