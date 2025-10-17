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
