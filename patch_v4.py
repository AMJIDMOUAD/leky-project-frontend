#!/usr/bin/env python3
"""
PATCH v4:
1. Remove ADMIN FAB from ALL pages (CSS + HTML)
2. Unify nav menu across ALL pages to match CO.deleky-home.html
3. Sharpen navbar text (font-smoothing + weight)
"""

import os, re

DIR = r"C:\Users\AMJID MOUAD\Desktop\leky project"

# ── REFERENCE NAV HTML from CO.deleky-home.html (lines 738-816) ──
REF_NAV_MENU_AND_RIGHT = r"""    <ul class="nav-menu" id="nav-menu">
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

    </div>"""


def remove_admin_fab(content):
    """Remove ADMIN FAB CSS rules and button HTML."""

    # Remove CSS blocks
    content = re.sub(
        r'\.admin-fab\{position:fixed;bottom:24px;left:24px;z-index:999;[^}]+\}',
        '', content
    )
    content = re.sub(
        r'\.admin-fab:hover\{background:var\(--blue\);transform:translateY\(-2px\)\}',
        '', content
    )
    content = re.sub(
        r'\.admin-fab svg\{width:14px;height:14px;stroke:#fff;fill:none;stroke-width:2\}',
        '', content
    )

    # Remove HTML: the comment + button
    content = re.sub(
        r'<!-- ADMIN FAB -->\s*<button class="admin-fab"[^>]*>.*?</button>',
        '', content, flags=re.DOTALL
    )

    # Also handle case where comment might not be present
    content = re.sub(
        r'\s*<button class="admin-fab"[^>]*>.*?</button>',
        '', content, flags=re.DOTALL
    )

    # Remove CSS selectors referencing admin-fab or fab-group in print/media rules
    content = re.sub(
        r',\.fab-group,#admin-fab,',
        ',', content
    )

    return content


def replace_nav_section(content):
    """Replace existing nav menu + right side with the home page reference."""

    # Match from <ul class="nav-menu" through </nav> (end of nav bar)
    # This avoids issues with nested divs inside the right-side section.
    pattern = r'<ul class="nav-menu"[^>]*>.*?</nav>'

    # The reference ends with the right-side </div> (4-space indent).
    # Pages have </div>\n  </div>\n</nav> after that (nav-inner close + nav close).
    replacement = REF_NAV_MENU_AND_RIGHT + '\n  </div>\n</nav>'

    new_content = re.sub(pattern, replacement, content, count=1, flags=re.DOTALL)

    # Also try alternative with <nav> still present but different nav structure
    if new_content == content and 'nav-right' in content:
        pattern2 = r'<ul class="nav-menu"[^>]*>.*?</ul>\s*<div class="nav-right">.*?</nav>'
        new_content = re.sub(pattern2, replacement, content, count=1, flags=re.DOTALL)

    return new_content


def sharpen_nav_text(content):
    """Add font-smoothing and improve weight for nav menu text."""
    # Replace the .nav-menu a CSS rule with improved rendering
    old = '.nav-menu a{font-size:13px;font-weight:500;color:var(--gray-600);padding:8px 9px;border-radius:8px;transition:all .2s;display:block;white-space:nowrap}'
    new = '.nav-menu a{font-size:13px;font-weight:600;color:var(--gray-600);padding:8px 9px;border-radius:8px;transition:all .2s;display:block;white-space:nowrap;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:optimizeLegibility}'
    content = content.replace(old, new)

    # Also sharpen nav-tel, nav-login, drop items
    old2 = '.nav-tel{font-size:13px;font-weight:600;color:var(--gray-600);white-space:nowrap;flex-shrink:0}'
    new2 = '.nav-tel{font-size:13px;font-weight:600;color:var(--gray-600);white-space:nowrap;flex-shrink:0;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}'
    content = content.replace(old2, new2)

    old3 = '.nav-login{font-size:13px;font-weight:500;color:var(--gray-600);padding:8px 12px;border-radius:8px;border:1px solid var(--gray-200);transition:all .2s;white-space:nowrap;flex-shrink:0}'
    new3 = '.nav-login{font-size:13px;font-weight:600;color:var(--gray-600);padding:8px 12px;border-radius:8px;border:1px solid var(--gray-200);transition:all .2s;white-space:nowrap;flex-shrink:0;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}'
    content = content.replace(old3, new3)

    return content


def process_file(filepath):
    basename = os.path.basename(filepath)
    if not filepath.endswith('.html'):
        return

    # Skip non-site pages
    if basename in ('login.html', 'signup.html', 'deleky-admin.html'):
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove ADMIN FAB
    content = remove_admin_fab(content)

    # 2. Unify nav menu — only if page has a nav menu
    if 'nav-menu' in content:
        content = replace_nav_section(content)

    # 3. Sharpen nav text
    if 'nav-menu a' in content:
        content = sharpen_nav_text(content)

    # Clean up extra blank lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"MODIFIED: {basename}")
    else:
        print(f"UNCHANGED: {basename}")


def main():
    for fname in sorted(os.listdir(DIR)):
        fpath = os.path.join(DIR, fname)
        if os.path.isfile(fpath):
            try:
                process_file(fpath)
            except Exception as e:
                print(f"ERROR: {fname}: {e}")

if __name__ == '__main__':
    main()
