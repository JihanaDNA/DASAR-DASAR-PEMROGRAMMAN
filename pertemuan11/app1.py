import streamlit as st

st.title('Aplikasi Saya')
st.write('Selamat datang di aplikasi saya')
st.success ('Berhasil melalukam sesuatu')
st.info ('Ini adalah Informasi')
st.warning ('Ini adalah peringatan')
st.error ('Terjadi kesalahan')
# st.markdown

nama = "Jian"
alamat = "depok"
st.write("Nama saya adalah", nama)
st.write("Alamat saya adalah", alamat)

mhs = {"nama": "Sari", "prodi": "TI", "ipk": 3.6}
nilai = [{"matkul": "Python", "nilai": 85},
         {"matkul": "Basis Data", "nilai": 78}]

st.header("Profil Mahasiswa")
st.write("Nama:", mhs["nama"])
st.metric("IPK", mhs["ipk"])
st.table(nilai)

if mhs["ipk"] >= 3.5:
    st.success("Predikat: dengan pujian")


suhu = [29, 31, 30, 33, 32, 28, 30]
st.line_chart(suhu)

data = {"komponen": ["Tugas", "UTS", "UAS"],
        "nilai": [80, 72, 88]}
st.bar_chart(data, x="komponen", y="nilai")
 