import streamlit as st
import urllib.parse

st.set_page_config(page_title="Karaoke Italiano Universale", page_icon="🎤")

st.title("🎤 Karaoke Italiano Universale")
st.write("Scrivi qualsiasi canzone o artista italiano (anche gli ultimi successi) e aprila subito su YouTube!")

# Barra di ricerca libera
ricerca = st.text_input("Cerca un brano o un artista italiano:", "")

if ricerca:
    # Aggiunge automaticamente la parola "karaoke" alla ricerca per trovare subito la base
    query_completa = ricerca + " karaoke italiano"
    query_encoded = urllib.parse.quote(query_completa)
    
    # Link diretto ai risultati di ricerca di YouTube
    url_yt = f"https://www.youtube.com/results?search_query={query_encoded}"
    
    st.write("---")
    st.success(Risultati pronti per: **{ricerca}**)
    
    # Pulsante grande per aprire la ricerca su YouTube
    st.markdown(f"""
        <div style="text-align: center; margin-top: 20px;">
            <a href="{url_yt}" target="_blank" style="background-color: #FF0000; color: white; padding: 15px 30px; text-decoration: none; font-size: 18px; font-weight: bold; border-radius: 30px; display: inline-block;">
                ▶ Canta "{ricerca}" su YouTube
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 Cliccando sul pulsante si aprirà YouTube con tutte le basi karaoke disponibili per la tua ricerca.")
else:
    st.write("---")
    st.markdown("### Suggerimenti del momento:")
    st.write("- 🎵 *Tredici Pietro*")
    st.write("- 🎵 *Annalisa*")
    st.write("- 🎵 *Marco Mengoni*")
    st.write("- 🎵 *Geolier*")
    st.write("Digita pure qualsiasi altro nome o canzone nello spazio in alto!")
