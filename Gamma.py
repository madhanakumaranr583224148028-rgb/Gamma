<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>GAMMA — Games Portal</title>
    <meta name="description" content="GAMMA — Play web games, discover new titles, and join the community." />
    <link rel="icon" href="favicon.ico" />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        :root{
            --bg:#0b1020; --card:#0f1724; --accent:#7c5cff; --muted:#9aa4b2; --glass: rgba(255,255,255,0.03);
            --radius:12px; color-scheme: dark;
        }
        *{box-sizing:border-box}
        html,body{height:100%}
        body{
            margin:0; font-family:Inter,system-ui,Segoe UI,Roboto,"Helvetica Neue",Arial;
            background: linear-gradient(180,#05060a 0%, #0b1020 60%);
            color:#e6eef8; -webkit-font-smoothing:antialiased;
            -moz-osx-font-smoothing:grayscale; padding:32px;
        }

        .container{max-width:1100px;margin:0 auto;display:grid;gap:24px}
        header{display:flex;align-items:center;justify-content:space-between;gap:16px}
        .brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:inherit}
        .logo{
            width:46px;height:46px;border-radius:10px;background:linear-gradient(135deg,var(--accent),#3ec5ff);
            display:inline-flex;align-items:center;justify-content:center;font-weight:700;color:#061028;
            box-shadow:0 6px 18px rgba(124,92,255,0.12);
        }
        nav a{color:var(--muted);text-decoration:none;padding:8px 12px;border-radius:8px}
        nav a:hover{background:var(--glass);color:#fff}

        .hero{
            display:grid;grid-template-columns:1fr 360px;gap:24px;align-items:center;
            background:linear-gradient(180deg, rgba(124,92,255,0.06), transparent);
            padding:28px;border-radius:var(--radius);backdrop-filter: blur(6px);
        }
        .hero h1{margin:0;font-size:28px;letter-spacing:-0.6px}
        .hero p{margin:8px 0 18px;color:var(--muted);line-height:1.45}
        .cta-row{display:flex;gap:12px;align-items:center}
        .btn{
            display:inline-flex;align-items:center;gap:8px;padding:10px 14px;border-radius:10px;
            background:var(--accent);color:#04102a;border:0;font-weight:600;cursor:pointer;
            box-shadow:0 8px 24px rgba(124,92,255,0.12)
        }
        .btn.ghost{background:transparent;border:1px solid rgba(255,255,255,0.04);color:var(--muted)}
        .stats{display:flex;gap:14px;color:var(--muted);font-size:14px}

        .card{
            background:linear-gradient(180deg, rgba(255,255,255,0.02), transparent);
            padding:14px;border-radius:12px;border:1px solid rgba(255,255,255,0.03);
        }

        .games-grid{
            display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;
        }
        .game{
            background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.02));
            border-radius:12px;overflow:hidden;border:1px solid rgba(255,255,255,0.03);
            display:flex;flex-direction:column;
        }
        .thumb{height:140px;background-size:cover;background-position:center}
        .game-body{padding:12px;display:flex;flex-direction:column;gap:8px}
        .game-title{font-weight:600}
        .meta{font-size:13px;color:var(--muted);display:flex;justify-content:space-between;align-items:center}
        .play-row{display:flex;gap:8px;margin-top:8px}
        .small-btn{padding:8px 10px;border-radius:8px;border:0;background:rgba(255,255,255,0.04);color:#fff;cursor:pointer;font-weight:600}

        footer{padding:18px 0;color:var(--muted);font-size:13px;display:flex;justify-content:space-between;align-items:center}

        /* responsive */
        @media (max-width:880px){
            .hero{grid-template-columns:1fr}
            body{padding:18px}
        }
    </style>
</head>
<body>
    <div class="container" role="main">
        <header>
            <a class="brand" href="#">
                <div class="logo">G</div>
                <div>
                    <div style="font-weight:700">GAMMA</div>
                    <div style="font-size:12px;color:var(--muted)">Play. Discover. Create.</div>
                </div>
            </a>

            <nav aria-label="Main navigation">
                <a href="#games">Games</a>
                <a href="#about">About</a>
                <a href="#community">Community</a>
            </nav>
        </header>

        <section class="hero card" aria-labelledby="hero-heading">
            <div>
                <h1 id="hero-heading">Welcome to GAMMA — browser games portal</h1>
                <p>Discover curated web games, play instantly, and join a growing community of creators and players. No installs — just click and play.</p>

                <div class="cta-row">
                    <button class="btn" id="playFeatured">Play Featured</button>
                    <button class="btn ghost" id="browseBtn">Browse Games</button>
                </div>

                <div style="height:18px"></div>
                <div class="stats">
                    <div><strong>120+</strong> Games</div>
                    <div><strong>8k</strong> Players online</div>
                    <div><strong>25</strong> New this week</div>
                </div>
            </div>

            <div style="display:flex;flex-direction:column;gap:12px">
                <div class="card" style="padding:12px;">
                    <div style="font-size:13px;color:var(--muted);margin-bottom:10px">Featured</div>
                    <div style="height:160px;border-radius:10px;background-image:linear-gradient(135deg, #3ec5ff33, #7c5cff33);display:flex;align-items:center;justify-content:center">
                        <div style="text-align:center">
                            <div style="font-weight:700;font-size:18px">Neon Drift</div>
                            <div style="color:var(--muted);margin-top:6px">Arcade racer · 3 min demo</div>
                            <div style="margin-top:10px"><button class="small-btn" onclick="openDemo('Neon Drift')">Open Demo</button></div>
                        </div>
                    </div>
                </div>

                <div class="card" style="padding:12px;">
                    <div style="font-size:13px;color:var(--muted);margin-bottom:8px">Join</div>
                    <div style="display:flex;gap:8px">
                        <input id="email" type="email" placeholder="your@email.com" style="flex:1;padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,0.03);background:transparent;color:inherit">
                        <button class="small-btn" onclick="subscribe()">Subscribe</button>
                    </div>
                </div>
            </div>
        </section>

        <section id="games">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">
                <h2 style="margin:0">Popular Games</h2>
                <div style="color:var(--muted);font-size:14px">Sorted by trending</div>
            </div>

            <div class="games-grid">
                <article class="game" role="article" aria-label="Neon Drift">
                    <div class="thumb" style="background-image:url('https://via.placeholder.com/600x400/2b2b6b/ffffff?text=Neon+Drift')"></div>
                    <div class="game-body">
                        <div class="game-title">Neon Drift</div>
                        <div class="meta"><span>Arcade • 2D</span><span>4.8 ★</span></div>
                        <div class="play-row">
                            <button class="small-btn" onclick="openGame('Neon Drift')">Play</button>
                            <button class="small-btn" onclick="showInfo('Neon Drift','A fast-paced neon racer with synthwave soundtrack.')">Info</button>
                        </div>
                    </div>
                </article>

                <article class="game" role="article" aria-label="Aqua Colony">
                    <div class="thumb" style="background-image:url('https://via.placeholder.com/600x400/0b6b6b/ffffff?text=Aqua+Colony')"></div>
                    <div class="game-body">
                        <div class="game-title">Aqua Colony</div>
                        <div class="meta"><span>Strategy • City-builder</span><span>4.6 ★</span></div>
                        <div class="play-row">
                            <button class="small-btn" onclick="openGame('Aqua Colony')">Play</button>
                            <button class="small-btn" onclick="showInfo('Aqua Colony','Build and manage an underwater city.')">Info</button>
                        </div>
                    </div>
                </article>

                <article class="game" role="article" aria-label="Skybound">
                    <div class="thumb" style="background-image:url('https://via.placeholder.com/600x400/4b2b6b/ffffff?text=Skybound')"></div>
                    <div class="game-body">
                        <div class="game-title">Skybound</div>
                        <div class="meta"><span>Action • Platformer</span><span>4.7 ★</span></div>
                        <div class="play-row">
                            <button class="small-btn" onclick="openGame('Skybound')">Play</button>
                            <button class="small-btn" onclick="showInfo('Skybound','Run, jump and soar across floating islands.')">Info</button>
                        </div>
                    </div>
                </article>

                <article class="game" role="article" aria-label="Puzzle Forge">
                    <div class="thumb" style="background-image:url('https://via.placeholder.com/600x400/6b4b2b/ffffff?text=Puzzle+Forge')"></div>
                    <div class="game-body">
                        <div class="game-title">Puzzle Forge</div>
                        <div class="meta"><span>Puzzle • Casual</span><span>4.5 ★</span></div>
                        <div class="play-row">
                            <button class="small-btn" onclick="openGame('Puzzle Forge')">Play</button>
                            <button class="small-btn" onclick="showInfo('Puzzle Forge','Craft and solve increasingly challenging puzzles.')">Info</button>
                        </div>
                    </div>
                </article>
            </div>
        </section>

        <footer>
            <div>© <span id="year"></span> GAMMA. All rights reserved.</div>
            <div style="display:flex;gap:12px">
                <a href="#privacy" style="color:var(--muted);text-decoration:none">Privacy</a>
                <a href="#terms" style="color:var(--muted);text-decoration:none">Terms</a>
            </div>
        </footer>
    </div>

    <script>
        // small interactive helpers
        document.getElementById('year').textContent = new Date().getFullYear();

        function openGame(name){
            alert('Launching "' + name + '" in a new tab (demo).');
            // real implementation would open embed or iframe
        }

        function showInfo(name, desc){
            alert(name + '\\n\\n' + desc);
        }

        function openDemo(name){
            alert('Opening demo for ' + name);
        }

        function subscribe(){
            const email = document.getElementById('email').value.trim();
            if(!email || !email.includes('@')) {
                alert('Please enter a valid email.');
                return;
            }
            alert('Subscribed: ' + email);
            document.getElementById('email').value = '';
        }

        // smooth scroll for "Browse Games" button
        document.getElementById('browseBtn').addEventListener('click', function(){
            document.getElementById('games').scrollIntoView({behavior:'smooth', block:'start'});
        });

        // featured play
        document.getElementById('playFeatured').addEventListener('click', function(){
            openGame('Neon Drift');
        });
    </script>
</body>
</html>
from dataclasses import dataclass, asdict
from typing import List, Optional
from flask import Flask, jsonify, render_template_string, request, url_for

"""
Gamma.py

A small Flask-based "Categories" component for a game website.
- Provides a JSON API at /api/categories
- Provides an embeddable HTML section at /categories (query params: limit, display=grid|list, show_counts=true|false)

Usage:
    pip install flask
    python Gamma.py
"""


app = Flask(__name__)


@dataclass
class Category:
    id: int
    name: str
    slug: str
    icon: str  # emoji or CSS class
    description: str
    game_count: int


# Example seed data; replace or load from DB as needed
CATEGORIES: List[Category] = [
    Category(1, "Action", "action", "🎮", "Fast-paced games focused on reflexes.", 124),
    Category(2, "Adventure", "adventure", "🗺️", "Exploration and story-driven gameplay.", 78),
    Category(3, "Puzzle", "puzzle", "🧩", "Logic and problem-solving challenges.", 95),
    Category(4, "Strategy", "strategy", "♟️", "Tactical and planning-focused games.", 64),
    Category(5, "Racing", "racing", "🏎️", "Speed and driving competitions.", 40),
    Category(6, "Sports", "sports", "⚽", "Sports simulations and arcade sports.", 58),
]


def find_categories(limit: Optional[int] = None, query: Optional[str] = None) -> List[Category]:
    results = CATEGORIES
    if query:
        q = query.lower()
        results = [c for c in results if q in c.name.lower() or q in c.description.lower()]
    if limit:
        results = results[:limit]
    return results


@app.route("/api/categories")
def api_categories():
    """Return categories as JSON. Query params: limit, q (search)"""
    try:
        limit = int(request.args.get("limit")) if request.args.get("limit") else None
    except ValueError:
        limit = None
    q = request.args.get("q")
    cats = find_categories(limit=limit, query=q)
    return jsonify([asdict(c) for c in cats])


# Simple embeddable HTML template for the categories section
HTML_TEMPLATE = """
<style>
/* Minimal styles for embedding */
.gamma-cats { font-family: Arial, sans-serif; }
.gamma-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin: 0; padding: 0; list-style: none; }
.gamma-card { background: #f8f9fb; border-radius: 8px; padding: 12px; display: flex; gap: 10px; align-items: center; text-decoration: none; color: inherit; transition: box-shadow .12s ease; }
.gamma-card:hover { box-shadow: 0 4px 10px rgba(0,0,0,0.08); }
.gamma-icon { font-size: 28px; width: 40px; height: 40px; display:flex; align-items:center; justify-content:center; border-radius:8px; background: #fff; box-shadow: 0 1px 2px rgba(0,0,0,0.04); }
.gamma-meta { flex: 1; min-width: 0; }
.gamma-title { font-weight: 600; margin: 0 0 4px 0; font-size: 14px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.gamma-desc { margin: 0; color: #58616a; font-size: 12px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.gamma-badge { background: #eef3ff; color: #2b5cff; padding: 4px 8px; border-radius: 999px; font-size: 12px; }
.gamma-list { display: flex; flex-direction: column; gap: 8px; padding: 0; margin: 0; list-style: none; }
</style>

<section class="gamma-cats">
  <h3>{{ title }}</h3>
  {% if display == 'grid' %}
    <ul class="gamma-grid" aria-label="Game categories">
      {% for c in categories %}
      <li><a class="gamma-card" href="{{ base_url }}/{{ c.slug }}">
        <div class="gamma-icon">{{ c.icon }}</div>
        <div class="gamma-meta">
          <div class="gamma-title">{{ c.name }}</div>
          <div class="gamma-desc">{{ c.description }}</div>
        </div>
        {% if show_counts %}
        <div class="gamma-badge">{{ c.game_count }}</div>
        {% endif %}
      </a></li>
      {% endfor %}
    </ul>
  {% else %}
    <ul class="gamma-list" aria-label="Game categories">
      {% for c in categories %}
      <li><a class="gamma-card" href="{{ base_url }}/{{ c.slug }}">
        <div class="gamma-icon">{{ c.icon }}</div>
        <div class="gamma-meta">
          <div class="gamma-title">{{ c.name }}{% if show_counts %} <span style="color:#7b8794;font-weight:500">({{ c.game_count }})</span>{% endif %}</div>
          <div class="gamma-desc">{{ c.description }}</div>
        </div>
      </a></li>
      {% endfor %}
    </ul>
  {% endif %}
</section>
"""

@app.route("/categories")
def categories_section():
    """
    Render an HTML categories section.
    Query params:
      - limit: int (how many categories to show)
      - display: 'grid' or 'list' (default grid)
      - show_counts: 'true' or 'false' (default true)
      - title: section title
    """
    try:
        limit = int(request.args.get("limit")) if request.args.get("limit") else None
    except ValueError:
        limit = None
    display = request.args.get("display", "grid")
    show_counts = request.args.get("show_counts", "true").lower() in ("1", "true", "yes")
    title = request.args.get("title", "Categories")
    cats = find_categories(limit=limit)
    base_url = request.args.get("base_url", "/categories")
    return render_template_string(HTML_TEMPLATE, categories=cats, display=display, show_counts=show_counts, title=title, base_url=base_url)


if __name__ == "__main__":
    # Development server for quick testing
    app.run(host="127.0.0.1", port=8000, debug=True)
from flask import Flask, request, redirect, url_for, render_template_string, jsonify, abort

# Gamma.py
# Simple Flask-based "Help" section for a game website.
# Single-file app that serves a help index, article pages, search, and contact form.
# Run: pip install flask && python Gamma.py

app = Flask(__name__)

# Example help articles (replace or extend with real content or load from DB)
ARTICLES = [
    {
        "id": 1,
        "title": "How to start a new game",
        "category": "Getting Started",
        "tags": ["new", "start", "tutorial"],
        "content": "To start a new game, click 'New Game' from the main menu, choose a difficulty, and confirm."
    },
    {
        "id": 2,
        "title": "Controls & Keyboard Shortcuts",
        "category": "Gameplay",
        "tags": ["controls", "keyboard"],
        "content": "Use WASD or arrow keys to move. Press 'Space' to jump and 'Esc' to open the menu."
    },
    {
        "id": 3,
        "title": "Multiplayer: Creating and joining rooms",
        "category": "Multiplayer",
        "tags": ["multiplayer", "rooms", "matchmaking"],
        "content": "To create a room, open Multiplayer > Create Room. Share the room code with friends to join."
    },
    {
        "id": 4,
        "title": "Troubleshooting connection issues",
        "category": "Support",
        "tags": ["network", "connection", "support"],
        "content": "If you experience connection issues, try restarting the game, checking your firewall, and ensuring your NAT type allows matchmaking."
    },
]

# Simple HTML templates inlined for single-file convenience
BASE_TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Game Help</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; background: #f7f9fb; color: #222; }}
    .container {{ max-width: 900px; margin: auto; }}
    header {{ margin-bottom: 18px; }}
    .card {{ background: white; padding: 16px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,.08); margin-bottom: 12px; }}
    .meta {{ color: #666; font-size: 0.9em; }}
    input[type="text"] {{ width: 60%; padding: 8px; }}
    select {{ padding: 8px; }}
    button {{ padding: 8px 12px; }}
    .tags {{ font-size: 0.9em; color: #007acc; }}
    nav a {{ margin-right: 10px; color: #007acc; text-decoration: none; }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>Help & Support</h1>
      <nav>
        <a href="{{ url_for('help_index') }}">Home</a>
        <a href="{{ url_for('help_search') }}">Search</a>
        <a href="{{ url_for('help_contact_get') }}">Contact</a>
      </nav>
    </header>
    {% block body %}{% endblock %}
    <footer style="margin-top:24px;color:#888;font-size:.9em">If an article doesn't solve your issue, use the contact form.</footer>
  </div>
</body>
</html>
"""

INDEX_TEMPLATE = """
{% extends base %}
{% block body %}
<div class="card">
  <form method="get" action="{{ url_for('help_search') }}">
    <input name="q" type="text" placeholder="Search help articles..." value="{{ q|default('') }}">
    <select name="category">
      <option value="">All categories</option>
      {% for c in categories %}
      <option value="{{ c }}" {% if c==category %}selected{% endif %}>{{ c }}</option>
      {% endfor %}
    </select>
    <button type="submit">Search</button>
  </form>
</div>

{% for a in articles %}
<div class="card">
  <h2><a href="{{ url_for('help_article', article_id=a.id) }}">{{ a.title }}</a></h2>
  <div class="meta">{{ a.category }} • <span class="tags">{{ a.tags|join(', ') }}</span></div>
  <p>{{ a.content[:200] }}{% if a.content|length > 200 %}...{% endif %}</p>
</div>
{% endfor %}
{% endblock %}
"""

ARTICLE_TEMPLATE = """
{% extends base %}
{% block body %}
<div class="card">
  <h2>{{ article.title }}</h2>
  <div class="meta">{{ article.category }} • <span class="tags">{{ article.tags|join(', ') }}</span></div>
  <p>{{ article.content }}</p>
  <p><a href="{{ url_for('help_index') }}">← Back to Help</a></p>
</div>
{% endblock %}
"""

SEARCH_TEMPLATE = """
{% extends base %}
{% block body %}
<div class="card">
  <form method="get" action="{{ url_for('help_search') }}">
    <input name="q" type="text" placeholder="Search help articles..." value="{{ q|default('') }}">
    <select name="category">
      <option value="">All categories</option>
      {% for c in categories %}
      <option value="{{ c }}" {% if c==category %}selected{% endif %}>{{ c }}</option>
      {% endfor %}
    </select>
    <button type="submit">Search</button>
  </form>
</div>

<p>Found {{ results|length }} result(s) for "{{ q }}"</p>
{% for a in results %}
<div class="card">
  <h3><a href="{{ url_for('help_article', article_id=a.id) }}">{{ a.title }}</a></h3>
  <div class="meta">{{ a.category }} • <span class="tags">{{ a.tags|join(', ') }}</span></div>
  <p>{{ a.content[:300] }}{% if a.content|length > 300 %}...{% endif %}</p>
</div>
{% endfor %}
{% endblock %}
"""

CONTACT_TEMPLATE = """
{% extends base %}
{% block body %}
<div class="card">
  <h2>Contact Support</h2>
  {% if success %}
    <p style="color:green">Message sent. We'll get back to you shortly.</p>
  {% endif %}
  <form method="post" action="{{ url_for('help_contact_post') }}">
    <div>
      <label>Your email</label><br>
      <input type="text" name="email" value="{{ email|default('') }}" required style="width:100%;padding:8px">
    </div>
    <div style="margin-top:8px">
      <label>Message</label><br>
      <textarea name="message" rows="6" style="width:100%;padding:8px">{{ message|default('') }}</textarea>
    </div>
    <div style="margin-top:8px">
      <button type="submit">Send</button>
    </div>
  </form>
</div>
{% endblock %}
"""

# Utility functions
def get_article(article_id):
    for a in ARTICLES:
        if a["id"] == article_id:
            return a
    return None

def list_categories():
    cats = sorted({a["category"] for a in ARTICLES})
    return cats

def search_articles(query=None, category=None):
    q = (query or "").strip().lower()
    results = ARTICLES
    if category:
        results = [a for a in results if a["category"].lower() == category.lower()]
    if q:
        def matches(a):
            return q in a["title"].lower() or q in a["content"].lower() or any(q in t.lower() for t in a["tags"])
        results = [a for a in results if matches(a)]
    return results

# Routes
@app.route("/help")
def help_index():
    q = request.args.get("q", "")
    category = request.args.get("category", "")
    if q or category:
        # If search parameters provided, redirect to search view
        return redirect(url_for("help_search", q=q, category=category))
    return render_template_string(
        INDEX_TEMPLATE, base=BASE_TEMPLATE,
        articles=ARTICLES, categories=list_categories(), q=q, category=category
    )

@app.route("/help/article/<int:article_id>")
def help_article(article_id):
    a = get_article(article_id)
    if not a:
        abort(404)
    return render_template_string(ARTICLE_TEMPLATE, base=BASE_TEMPLATE, article=a)

@app.route("/help/search")
def help_search():
    q = request.args.get("q", "")
    category = request.args.get("category", "")
    results = search_articles(q, category)
    # Support JSON API with ?format=json
    if request.args.get("format") == "json":
        return jsonify({"query": q, "category": category, "results": results})
    return render_template_string(SEARCH_TEMPLATE, base=BASE_TEMPLATE, results=results, categories=list_categories(), q=q, category=category)

@app.route("/help/contact", methods=["GET"])
def help_contact_get():
    return render_template_string(CONTACT_TEMPLATE, base=BASE_TEMPLATE, success=False, email="", message="")

@app.route("/help/contact", methods=["POST"])
def help_contact_post():
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()
    # In a real app: validate email, captcha, store message or send email via SMTP/third-party service.
    # For demo, just pretend we accepted it and show a success message.
    success = bool(email and message)
    return render_template_string(CONTACT_TEMPLATE, base=BASE_TEMPLATE, success=success, email=email, message="")

# Small JSON API endpoint to fetch an article
@app.route("/api/help/article/<int:article_id>")
def api_article(article_id):
    a = get_article(article_id)
    if not a:
        return jsonify({"error": "Not found"}), 404
    return jsonify(a)

if __name__ == "__main__":
    # Development server
    app.run(debug=True, port=5000)
