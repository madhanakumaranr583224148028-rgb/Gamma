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