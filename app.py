import streamlit as st

# Configurazione della pagina
st.set_page_config(page_title="Mini Karaoke Finder", page_icon="🎤")

# Database di esempio
CANZONI = [
    {"titolo": "Imagine", "artista": "John Lennon", "link": "https://www.youtube.com/watch?v=yRhq-yO1KN8"},
    {"titolo": "Bohemian Rhapsody", "artista": "Queen", "link": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"},
    {"titolo": "Azzurro", "artista": "Adriano Celentano", "link": "https://www.youtube.com/watch?v=sO7N7m4hWWA"},
    {"titolo": "I Will Survive", "artista": "Gloria Gaynor", "link": "https://www.youtube.com/watch?v=ZBR2G-iI3-I"},
    {"titolo": "La solitudine", "artista": "Laura Pausini", "link": "https://www.youtube.com/watch?v=1b5x-Q5yZ0Y"}
]

st.title("🎤 Mini Karaoke Finder")
st.write("Cerca la tua canzone preferita e clicca per cantare!")

# Barra di ricerca interattiva
ricerca = st.text_input("Cerca per titolo o artista:", "").lower()

# Filtra le canzoni
if ricerca:
    risultati = [c for c in CANZONI if ricerca in c["titolo"].lower() or ricerca in c["artista"].lower()]
else:
    risultati = CANZONI

st.write("---")

# Mostra i risultati
if risultati:
    for c in risultati:
        st.markdown(f"🎵 **{c['titolo']}** — *{c['artista']}* [👉 Canta qui]({c['link']})")
else:
    st.warning("Nessuna canzone trovata.")
