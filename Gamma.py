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
