import streamlit as st

def nilai_huruf(skor):
    if skor >= 90:
        return "A"
    elif skor >= 80:
        return "B"
    elif skor >= 70:
        return "C"
    elif skor >= 60:
        return "D"
    else:
        return "E"

st.title("Kalkulator Nilai Mahasiswa")
nama = st.text_input("Masukkan Nama Mahasiswa:")
tugas = st.slider("Nilai Tugas:", 0, 100, 75)
uts = st.number_input("Nilai UTS:", 0, 100, 70)
uas = st.number_input("Nilai UAS:", 0, 100, 80)

if st.button("Hitung Nilai Akhir"):
    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas
    st.metric("Nilai Akhir", round(akhir, 1))
    st.success(f"Nilai Huruf: {nilai_huruf(akhir)}")

    grafik = {
        "komponen": ["Tugas", "UTS", "UAS"],
        "nilai": [tugas, uts, uas]
    }
    st.bar_chart(grafik, x="komponen", y="nilai")