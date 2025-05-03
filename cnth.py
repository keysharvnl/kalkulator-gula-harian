import streamlit as st

st.set_page_config(page_title="Kalkulator Kadar Gula Total", page_icon="🍭", layout="centered")

# Daftar makanan dengan kadar gula per porsi (gram) - diperluas
KADAR_GULA_MAKANAN = {
    "Apel (1 buah sedang)": 19,
    "Pisang (1 buah sedang)": 14,
    "Jeruk (1 buah sedang)": 12,
    "Anggur (100g)": 16,
    "Semangka (100g)": 6,
    "Mangga (1 buah sedang)": 45,
    "Roti tawar (1 iris)": 1.5,
    "Nasi putih (1 piring)": 0.1,
    "Kentang goreng (100g)": 0.3,
    "Cokelat batang (50g)": 25,
    "Minuman bersoda (kaleng 330ml)": 35,
    "Yogurt rasa (100g)": 12,
    "Es krim (100g)": 21,
    "Kue kering (1 potong)": 7,
    "Permen (1 buah)": 5,
    "Sereal manis (1 mangkuk)": 9,
    "Jus buah (250ml)": 26,
    "Madu (1 sendok makan)": 17,
    "Selai (1 sendok makan)": 10,
    "Kue ulang tahun (1 potong)": 22,
    "Susu cokelat (250ml)": 24,
    "Minuman energi (250ml)": 27,
    "Es teh manis (1 gelas)": 25,
    "Puding (100g)": 18,
    "Kue donat (1 buah)": 15,
    "Roti manis (1 buah)": 12,
    "Susu sapi (250ml)": 12,
    "Sayur bening bayam (100g)": 0.4,
    "Buah naga (100g)": 8,
}

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
