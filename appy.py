import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard MudaBiz Academy", layout="wide")

st.title("📊 MudaBiz Academy Dashboard")
st.markdown("Platform edukasi entrepreneurship & marketplace B2C berbasis ekonomi sirkular.")

# -----------------------------
# DATA SIMULASI (dummy)
# -----------------------------
data = {
    "Bulan": pd.date_range("2025-01-01", periods=6, freq='M').strftime('%B'),
    "Pengguna Aktif": [1500, 2000, 2800, 3500, 4200, 5000],
    "UMKM Aktif": [80, 100, 140, 160, 200, 240],
    "Produk Terjual": [400, 520, 600, 750, 900, 1100],
    "Partisipan Kelas": [300, 450, 500, 600, 700, 850],
    "CO2 Terselamatkan (kg)": [120, 180, 250, 300, 380, 450],
    "Produk Didaur Ulang": [50, 65, 90, 110, 140, 180],
}
df = pd.DataFrame(data)

# -----------------------------
# GRAFIK 1: PENGGUNA & UMKM
# -----------------------------
st.subheader("📈 Pertumbuhan Pengguna & UMKM")
col1, col2 = st.columns(2)

with col1:
    fig_user = px.line(df, x="Bulan", y="Pengguna Aktif", markers=True, title="Pertumbuhan Pengguna Aktif")
    st.plotly_chart(fig_user, use_container_width=True)

with col2:
    fig_umkm = px.line(df, x="Bulan", y="UMKM Aktif", markers=True, title="Pertumbuhan UMKM Aktif", color_discrete_sequence=["green"])
    st.plotly_chart(fig_umkm, use_container_width=True)

# -----------------------------
# GRAFIK 2: PRODUK & EDUKASI
# -----------------------------
st.subheader("🛍️ Aktivitas Marketplace & Edukasi")
col3, col4 = st.columns(2)

with col3:
    fig_produk = px.bar(df, x="Bulan", y="Produk Terjual", title="Jumlah Produk Terjual", color_discrete_sequence=["indigo"])
    st.plotly_chart(fig_produk, use_container_width=True)

with col4:
    fig_kelas = px.bar(df, x="Bulan", y="Partisipan Kelas", title="Peserta Kelas & Webinar", color_discrete_sequence=["orange"])
    st.plotly_chart(fig_kelas, use_container_width=True)

# -----------------------------
# GRAFIK 3: EKONOMI SIRKULAR
# -----------------------------
st.subheader("🌱 Dampak Ekonomi Sirkular")
col5, col6 = st.columns(2)

with col5:
    fig_co2 = px.area(df, x="Bulan", y="CO2 Terselamatkan (kg)", title="Emisi CO2 Terselamatkan", color_discrete_sequence=["teal"])
    st.plotly_chart(fig_co2, use_container_width=True)

with col6:
    fig_recycle = px.bar(df, x="Bulan", y="Produk Didaur Ulang", title="Produk yang Didaur Ulang", color_discrete_sequence=["brown"])
    st.plotly_chart(fig_recycle, use_container_width=True)

# -----------------------------
# TAMPILKAN DATA
# -----------------------------
with st.expander("📄 Lihat Data Mentah"):
    st.dataframe(df)
