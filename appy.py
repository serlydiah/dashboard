import streamlit as st
import pandas as pd
import plotly as py

# -------------------------------
# Judul dan deskripsi dashboard
# -------------------------------
st.set_page_config(page_title="MudaBiz Academy Dashboard", layout="wide")
st.title("🌱 MudaBiz Academy Dashboard")
st.markdown("""
MudaBiz Academy adalah platform edukasi entrepreneurship dan marketplace B2C berbasis ekonomi sirkular.  
Dashboard ini menyajikan data dan insight untuk mendukung pengambilan keputusan bisnis kreatif.
""")

# -------------------------------
# Data dummy
# -------------------------------
data = {
    "Bulan": ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun"],
    "Pengguna Baru": [120, 150, 180, 200, 230, 260],
    "UMKM Aktif": [30, 45, 50, 65, 75, 85],
    "Produk Terjual": [300, 400, 450, 500, 550, 620],
    "Edukasi Terselenggara": [5, 7, 6, 9, 10, 12],
    "Ton CO2 Dikurangi": [1.2, 1.5, 1.7, 2.0, 2.3, 2.7]
}
df = pd.DataFrame(data)

# -------------------------------
# Sidebar filter
# -------------------------------
st.sidebar.header("Filter Data")
bulan_terpilih = st.sidebar.multiselect(
    "Pilih Bulan", options=df["Bulan"].unique(), default=list(df["Bulan"])
)

# Filter data
if bulan_terpilih:
    df_filtered = df[df["Bulan"].isin(bulan_terpilih)]

    # -------------------------------
    # Visualisasi interaktif
    # -------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Pertumbuhan Pengguna & UMKM")
        fig1 = px.line(df_filtered, x="Bulan", y=["Pengguna Baru", "UMKM Aktif"],
                       markers=True, labels={"value": "Jumlah", "variable": "Kategori"})
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("🛍️ Produk Terjual & Edukasi")
        fig2 = px.bar(df_filtered, x="Bulan", y=["Produk Terjual", "Edukasi Terselenggara"],
                      barmode="group", labels={"value": "Jumlah", "variable": "Kategori"})
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🌍 Dampak Ekonomi Sirkular (CO2)")
    fig3 = px.area(df_filtered, x="Bulan", y="Ton CO2 Dikurangi", color_discrete_sequence=["green"])
    st.plotly_chart(fig3, use_container_width=True)

    with st.expander("📄 Lihat Data Mentah"):
        st.dataframe(df_filtered)

else:
    st.warning("Silakan pilih setidaknya satu bulan untuk menampilkan data dashboard.")
