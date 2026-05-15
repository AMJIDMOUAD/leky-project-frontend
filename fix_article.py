#!/usr/bin/env python3
"""Fix article page: replace full nav (CSS + HTML), add footer CSS, add mobile nav JS."""

import re

FILE = r"C:\Users\AMJID MOUAD\Desktop\leky project\CO.deleky-article.html"

with open(FILE, 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ── 1. Replace nav CSS rules with home page versions ──
# Article uses different nav-inner, nav-menu, drop, etc.
# Remove old nav CSS and replace with home page nav CSS

# Remove old nav-specific CSS rules (between <style> and </style>)
old_nav_css_patterns = [
    r'nav\{position:sticky;top:0;z-index:50;background:rgba\(255,255,255,\.98\);backdrop-filter:blur\(12px\);border-bottom:1px solid var\(--gray-200\)\}',
    r'\.nav-inner\{max-width:1200px;margin:auto;padding:14px 24px;display:flex;align-items:center;justify-content:space-between;gap:18px\}',
    r'\.logo-wrap img\{height:48px;width:auto\}',
    r'\.nav-menu\{display:flex;gap:0;align-items:center;flex-wrap:wrap;list-style:none\}',
    r'\.nav-menu li\{position:relative\}',
    r'\.nav-menu a\{font-size:13px;font-weight:600;color:var\(--gray-600\);padding:10px 12px;border-radius:10px;display:inline-flex;align-items:center;transition:all \.2s\}',
    r'\.nav-menu a:hover\{background:var\(--gray-100\);color:var\(--black\)\}',
    r'\.nav-menu \.has-drop>a::after\{content:\'▾\';font-size:10px;margin-left:6px;opacity:\.7\}',
    r'\.drop\{display:none;position:absolute;top:110%;left:0;width:260px;background:#fff;border:1px solid var\(--gray-200\);border-radius:18px;box-shadow:0 20px 60px rgba\(0,0,0,\.08\);padding:14px;overflow:hidden\}',
    r'\.has-drop:hover \.drop\{display:block\}',
    r'\.drop a\{display:flex;align-items:center;gap:12px;padding:12px;border-radius:14px;color:var\(--gray-700\);transition:background \.2s\}',
    r'\.drop a:hover\{background:var\(--gray-50\)\}',
    r'\.drop-icon\{width:36px;height:36px;border-radius:14px;background:var\(--gray-100\);display:flex;align-items:center;justify-content:center;flex-shrink:0\}',
]
for pat in old_nav_css_patterns:
    content = re.sub(pat, '', content)

# Inject new nav CSS at the start of <style> (after the first few rules)
# We'll add it after the body rule
home_nav_css = """
nav{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.98);backdrop-filter:blur(12px);border-bottom:1px solid var(--gray-200)}
.nav-inner{max-width:1200px;margin:auto;padding:0 24px;height:72px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:nowrap}
.logo-wrap img{height:52px;width:auto;display:block}
.nav-menu{display:flex;gap:0;list-style:none;align-items:center;flex-shrink:0}
.nav-menu a{font-size:13px;font-weight:600;color:var(--gray-600);padding:8px 9px;border-radius:8px;transition:all .2s;display:block;white-space:nowrap;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:optimizeLegibility}
.nav-menu a:hover{color:var(--black);background:var(--gray-100)}
.nav-menu .has-drop{position:relative}
.nav-menu .has-drop>a::after{content:'▾';font-size:10px;margin-left:4px;opacity:.6}
.drop{display:none;position:absolute;top:calc(100%+4px);left:0;width:240px;background:#fff;border:1px solid var(--gray-200);border-radius:14px;box-shadow:0 16px 40px rgba(0,0,0,.08);padding:10px;z-index:100}
.has-drop:hover .drop{display:block}
.drop a{font-size:13px;color:var(--gray-600);padding:10px 14px;border-radius:8px;display:flex!important;align-items:center;gap:12px;transition:all .2s;font-weight:500}
.drop a:hover{background:var(--gray-50);color:var(--black)}
.drop-icon{width:32px;height:32px;border-radius:8px;background:var(--blue-pale);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.drop-icon svg{width:16px;height:16px;stroke:var(--blue);fill:none;stroke-width:2}
.nav-tel{font-size:13px;font-weight:600;color:var(--gray-600);white-space:nowrap;flex-shrink:0;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}
.nav-login{font-size:13px;font-weight:600;color:var(--gray-600);padding:8px 12px;border-radius:8px;border:1px solid var(--gray-200);transition:all .2s;white-space:nowrap;flex-shrink:0;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}
.nav-login:hover{border-color:var(--blue);color:var(--blue)}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;padding:8px;border:none;background:transparent}
.hamburger span{display:block;width:22px;height:2px;background:var(--black);border-radius:2px;transition:all .3s}
"""

# Insert nav CSS after "a{text-decoration:none;color:inherit}"
content = content.replace(
    'a{text-decoration:none;color:inherit}',
    'a{text-decoration:none;color:inherit}\n' + home_nav_css.strip()
)

# Add footer CSS before </style>
footer_css = """
footer{background:var(--gray-800);color:rgba(255,255,255,.6)}
.footer-top{max-width:1200px;margin:auto;padding:64px 32px 48px;display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr;gap:40px}
.footer-tagline{font-size:13px;line-height:1.7;margin-bottom:20px;color:rgba(255,255,255,.45)}
.footer-social{display:flex;gap:8px}
.social-btn{width:36px;height:36px;border-radius:10px;background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center;transition:all .25s}
.social-btn:hover{background:rgba(255,255,255,.16);transform:translateY(-2px)}
.social-btn svg{width:16px;height:16px;stroke:rgba(255,255,255,.4);fill:none;stroke-width:2}
.footer-col-h{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.12em;color:rgba(255,255,255,.9);margin-bottom:16px}
.footer-links{list-style:none;display:flex;flex-direction:column;gap:9px}
.footer-links a{font-size:13px;color:rgba(255,255,255,.45);transition:color .2s}
.footer-links a:hover{color:var(--blue)}
.footer-bottom{border-top:1px solid rgba(255,255,255,.08);max-width:1200px;margin:0 auto;padding:20px 32px;display:flex;justify-content:space-between;align-items:center;font-size:12px;gap:16px;flex-wrap:wrap}
.footer-bottom-links{display:flex;gap:20px}
.footer-bottom-links a{color:rgba(255,255,255,.4);transition:color .2s}
.footer-bottom-links a:hover{color:rgba(255,255,255,.8)}
"""

content = content.replace('</style>', footer_css.strip() + '\n</style>')

# Add mobile nav responsive CSS
mobile_nav_css = """
@media(max-width:768px){
  .nav-menu{display:none}
  .hamburger{display:flex}
  .nav-menu.open{display:flex;flex-direction:column;position:absolute;top:68px;left:0;right:0;background:#fff;border-bottom:1px solid var(--gray-200);padding:12px 16px;box-shadow:0 12px 32px rgba(0,0,0,.08)}
  .nav-menu.open .drop{display:none}
}
@media(max-width:1024px){.footer-top{grid-template-columns:1fr 1fr;gap:28px}}
@media(max-width:768px){.footer-top{grid-template-columns:1fr;gap:20px}.footer-bottom{flex-direction:column;text-align:center;padding:16px 20px}}
"""

content = content.replace('</style>', mobile_nav_css.strip() + '\n</style>')

# ── 2. Replace entire <nav> HTML block ──
# Remove old <nav>...</nav> and replace with home page version
home_nav_html = """<nav>
  <div class="nav-inner">
    <button class="hamburger" id="hamburger" onclick="toggleNav()" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>

    <!-- LOGO — hauteur fixe, pas de compression -->
    <a href="CO.deleky-home.html" class="logo-wrap" style="flex-shrink:0">
      <img src="logo.jpg" alt="Deleky's SARL" style="height:52px;width:auto;display:block">
    </a>

    <!-- MENU PRINCIPAL -->
    <ul class="nav-menu" id="nav-menu">
      <li><a href="CO.deleky-home.html" onclick="closeNav()">Accueil</a></li>
      <li><a href="CO_deleky-cabinet-v2.html" onclick="closeNav()">Le Cabinet</a></li>
      <li><a href="CO.deleky-missions.html" onclick="closeNav()">Missions</a></li>
            <li class="has-drop">
        <a href="#">Nos Produits</a>
        <div class="drop">
          <a href="CO.deleky-simulateur-paie-v2.html" onclick="closeNav()">
            <div class="drop-icon" style="background:var(--blue)"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#fff" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="9" y1="7" x2="15" y2="7"/><line x1="9" y1="11" x2="15" y2="11"/></svg></div>
            <div>
              <div style="font-weight:700;font-size:13px;color:var(--blue)">CI Payroll Simulation</div>
              <div style="font-size:11px;color:var(--gray-400)">Calculateur gratuit</div>
            </div>
          </a>
          <a href="CO.deleky-simulateur-immo.html" onclick="closeNav()">
            <div class="drop-icon" style="background:var(--blue)"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#fff" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg></div>
            <div>
              <div style="font-weight:700;font-size:13px;color:var(--blue)">Home Loan Calculator</div>
              <div style="font-size:11px;color:var(--gray-400)">Calculateur gratuit</div>
            </div>
          </a>
          <a href="CO.deleky-plan-amortissement.html" onclick="closeNav()">
            <div class="drop-icon" style="background:var(--blue)"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="#fff" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></div>
            <div>
              <div style="font-weight:700;font-size:13px;color:var(--blue)">Amortization Plan</div>
              <div style="font-size:11px;color:var(--gray-400)">Calculateur gratuit</div>
            </div>
          </a>
        </div>
      </li>
<li class="has-drop">
        <a href="CO.deleky-ressources.html#res-docs">Ressources</a>
        <div class="drop">
          <a href="CO.deleky-ressources.html#res-docs" onclick="closeNav()">
            <div class="drop-icon"><svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/></svg></div>
            Documents Utiles
          </a>
          <a href="CO.deleky-ressources.html#res-calc" onclick="closeNav()">
            <div class="drop-icon"><svg viewBox="0 0 24 24"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="6" x2="16" y2="6"/></svg></div>
            Calculateurs
          </a>

          <a href="CO.deleky-ressources.html#res-part" onclick="closeNav()">
            <div class="drop-icon"><svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/></svg></div>
            Partenariat
          </a>
        </div>
      </li>
      <li class="has-drop">
        <a href="CO.deleky-publications.html">Publications</a>
        <div class="drop">
          <a href="CO.deleky-publications.html" onclick="closeNav()">
            <div class="drop-icon"><svg viewBox="0 0 24 24"><path d="M4 22h16a2 2 0 002-2V4a2 2 0 00-2-2H8a2 2 0 00-2 2v2"/></svg></div>
            Blog & Articles
          </a>
          <a href="CO.deleky-publications.html" onclick="closeNav()">
            <div class="drop-icon"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/></svg></div>
            Événements
          </a>
        </div>
      </li>
      <li><a href="CO.deleky-joinus.html" onclick="closeNav()">Nous Rejoindre</a></li>
      <li><a href="CO.deleky-contact.html" onclick="closeNav()">Contact</a></li>
    </ul>

    <!-- DROITE : TEL + LANG + LOGIN + CTA -->
    <div style="display:flex;gap:8px;align-items:center;flex-shrink:0">

      <a href="tel:+22507000588" class="nav-tel">+225&nbsp;07&nbsp;00&nbsp;05&nbsp;88</a>

      <!-- Switcher FR / EN -->
      <div class="lang-switch">
        <button class="lang-btn active" onclick="switchLang('fr',this)">FR</button>
        <button class="lang-btn" onclick="switchLang('en',this)">EN</button>
      </div>

      <a href="CO.deleky-login (7).html" class="nav-login">Connexion</a>

    </div>
  </div>
</nav>"""

# Replace from <nav> to </nav>
content = re.sub(r'<nav>.*?</nav>', home_nav_html, content, count=1, flags=re.DOTALL)

# ── 3. Add toggleNav/closeNav JS before </body> ──
toggle_js = """
<script>
function toggleNav(){document.getElementById('nav-menu').classList.toggle('open');document.getElementById('hamburger').classList.toggle('open');}
function closeNav(){document.getElementById('nav-menu').classList.remove('open');document.getElementById('hamburger').classList.remove('open');}
</script>
"""
content = content.replace('</body>', toggle_js + '\n</body>')

# Clean up
content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)

if content != original:
    with open(FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    print("MODIFIED: CO.deleky-article.html")
else:
    print("UNCHANGED")
