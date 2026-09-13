from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Database di esempio con canzoni e link (puoi mettere link YouTube, file locali, ecc.)
CANZONI = [
    {"id": 1, "titolo": "Imagine", "artista": "John Lennon", "link": "https://www.youtube.com/watch?v=yRhq-yO1KN8"},
    {"id": 2, "titolo": "Bohemian Rhapsody", "artista": "Queen", "link": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"},
    {"id": 3, "titolo": "Azzurro", "artista": "Adriano Celentano", "link": "https://www.youtube.com/watch?v=sO7N7m4hWWA"},
    {"id": 4, "titolo": "I Will Survive", "artista": "Gloria Gaynor", "link": "https://www.youtube.com/watch?v=ZBR2G-iI3-I"},
    {"id": 5, "titolo": "La solitudine", "artista": "Laura Pausini", "link": "https://www.youtube.com/watch?v=1b5x-Q5yZ0Y"}
]

# Pagina HTML integrata con grafica pulita e barra di ricerca
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>Mini Karaoke Python</title>
    <style>
        body { font-family: Arial, sans-serif; background: #121212; color: #fff; text-align: center; padding: 50px; }
        h1 { color: #1db954; }
        input[type="text"] { padding: 12px; width: 300px; font-size: 16px; border-radius: 25px; border: none; outline: none; margin-bottom: 20px; }
        ul { list-style: none; padding: 0; }
        li { background: #282828; margin: 10px auto; padding: 15px; width: 400px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; }
        a.btn { background: #1db954; color: white; padding: 8px 15px; border-radius: 5px; text-decoration: none; font-weight: bold; }
        a.btn:hover { background: #1aa34a; }
    </style>
</head>
<body>
    <h1>🎤 Mini Karaoke Finder</h1>
    
    <!-- Barra di ricerca -->
    <form method="GET" action="/">
        <input type="text" name="q" placeholder="Cerca canzone o artista..." value="{{ query }}">
    </form>

    <!-- Lista dei risultati -->
    <ul>
        {% for c in canzoni %}
            <li>
                <span><strong>{{ c.titolo }}</strong> - {{ c.artista }}</span>
                <a class="btn" href="{{ c.link }}" target="_blank">Canta</a>
            </li>
        {% else %}
            <p>Nessuna canzone trovata.</p>
        {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    query = request.args.get("q", "").lower()
    
    # Filtra le canzoni in base alla ricerca (titolo o artista)
    if query:
        risultati = [c for c in CANZONI if query in c["titolo"].lower() or query in c["artista"].lower()]
    else:
        risultati = CANZONI
        
    return render_template_string(HTML_TEMPLATE, canzoni=risultati, query=query)

if __name__ == "__main__":
    app.run(debug=True)

