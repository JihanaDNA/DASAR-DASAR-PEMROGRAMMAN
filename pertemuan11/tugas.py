import streamlit as st

skala_list = ["Celsius", "Fahrenheit", "Kelvin", "Reamur"]
simbol = {"Celsius": "°C", "Fahrenheit": "°F", "Kelvin": "K", "Reamur": "°Re"}


# Fungsi buatan sendiri: ubah semua skala ke Celsius dulu, lalu ke skala tujuan
def konversi_suhu(nilai, asal, tujuan):
    if asal == "Celsius":
        c = nilai
    elif asal == "Fahrenheit":
        c = (nilai - 32) * 5 / 9
    elif asal == "Kelvin":
        c = nilai - 273.15
    else:
        c = nilai * 5 / 4

    if tujuan == "Celsius":
        return c
    elif tujuan == "Fahrenheit":
        return c * 9 / 5 + 32
    elif tujuan == "Kelvin":
        return c + 273.15
    else:
        return c * 4 / 5


st.title("Konverter Suhu")
st.write("Ubah suhu antar skala: Celsius, Fahrenheit, Kelvin, dan Reamur")

# 4 widget input (+ 1 checkbox)
suhu = st.number_input("Masukkan suhu", -1000.0, 1000.0, 25.0)
asal = st.selectbox("Dari skala", skala_list)
tujuan = st.radio("Ke skala", skala_list)
desimal = st.slider("Angka di belakang koma", 0, 4, 1)
tampil_grafik = st.checkbox("Tampilkan perbandingan semua skala")

celsius = konversi_suhu(suhu, asal, "Celsius")

if celsius < -273.15:
    st.error("Suhu tidak mungkin di bawah nol mutlak (-273,15 °C)")
else:
    hasil = konversi_suhu(suhu, asal, tujuan)
    st.metric("Hasil konversi", f"{round(hasil, desimal)} {simbol[tujuan]}")

    if celsius <= 0:
        st.warning("Pada suhu ini air membeku")
    elif celsius >= 100:
        st.warning("Pada suhu ini air mendidih")
    else:
        st.success("Pada suhu ini air berwujud cair")

    if tampil_grafik:
        nilai_semua = [
            round(konversi_suhu(suhu, asal, "Celsius"), desimal),
            round(konversi_suhu(suhu, asal, "Fahrenheit"), desimal),
            round(konversi_suhu(suhu, asal, "Kelvin"), desimal),
            round(konversi_suhu(suhu, asal, "Reamur"), desimal),
        ]
        grafik = {"skala": skala_list, "nilai": nilai_semua}
        st.bar_chart(grafik, x="skala", y="nilai")