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