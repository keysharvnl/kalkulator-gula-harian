import streamlit as st

st.set_page_config(
    page_title="Kalkulator Kadar Gula - Pilih Menu Makanan",
    page_icon="🍬",
    layout="centered",
)

# Data makanan dengan kadar gula per porsi dalam gram
DATA_MAKANAN = {
    "Apel (1 buah sedang)": 19,
    "Pisang (1 buah sedang)": 14,
    "Jeruk (1 buah sedang)": 12,
    "Roti tawar (1 iris)": 1.5,
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
}

st.title("🍭 Kalkulator Kadar Gula dalam Makanan")
st.write(
    """
    Pilih menu makanan yang Anda konsumsi hari ini.
    Masukkan jumlah porsi dari makanan yang dipilih,
    kemudian klik tombol hitung untuk melihat total kadar gula.
    """
)

# Pilih makanan dengan checkbox agar tampil sebagai menu pilihan yang mudah dilihat
st.subheader("Pilih makanan:")
pilihan = []
for makanan in DATA_MAKANAN.keys():
    if st.checkbox(f"{makanan} (Gula: {DATA_MAKANAN[makanan]} g/porsi)"):
        pilihan.append(makanan)

if pilihan:
    st.subheader("Masukkan jumlah porsi:")
    jumlah_porsi = {}
    for makanan in pilihan:
        jumlah_porsi[makanan] = st.number_input(
            label=f"Jumlah porsi {makanan}:",
            min_value=0,
            step=1,
            key=f"qty_{makanan}",
        )

    if st.button("Hitung Total Gula"):
        total_gula = 0
        for makanan in pilihan:
            total_gula += jumlah_porsi[makanan] * DATA_MAKANAN[makanan]
        st.success(f"Total kadar gula yang Anda konsumsi adalah **{total_gula:.1f} gram**.")
        st.markdown(
            """
            ### Batasan Konsumsi Gula Harian
            - Wanita: maksimal 25 gram gula tambahan per hari.
            - Pria: maksimal 36 gram gula tambahan per hari.
            
            Jaga pola makan Anda agar tetap sehat!
            """
        )
else:
    st.info("Silakan pilih setidaknya satu makanan untuk menghitung kadar gula.")

st.markdown("---")
st.markdown("Dibuat dengan ❤️ menggunakan Streamlit")
