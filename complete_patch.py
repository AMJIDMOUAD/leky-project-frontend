#!/usr/bin/env python3
"""
Complete remaining patches:
1. Remove blue CTA button from ALL navbars (CSS + HTML)
2. Fix Type B page navbars to match home page (direct href, no navigate())
3. Fix Type B page footers (Nos Produits links + all navigate() links)
4. Add footer to article page
"""

import os, re

DIR = r"C:\Users\AMJID MOUAD\Desktop\leky project"

# Type B pages (simulators with navigate-style nav)
TYPE_B_PAGES = [
    "CO.deleky-simulateur-paie-v2.html",
    "CO.deleky-simulateur-immo.html",
    "CO.deleky-plan-amortissement.html",
]

# Mapping of navigate() page names to actual HTML files
PAGE_MAP = {
    'home': 'CO.deleky-home.html',
    'cabinet': 'CO_deleky-cabinet-v2.html',
    'missions': 'CO.deleky-missions.html',
    'ressources': 'CO.deleky-ressources.html',
    'publications': 'CO.deleky-publications.html',
    'blog': 'CO.deleky-publications.html',
    'joinus': 'CO.deleky-joinus.html',
    'contact': 'CO.deleky-contact.html',
    'login': 'CO.deleky-login (7).html',
    # Additional page types from footers
    'solutions': 'CO.deleky-missions.html',
    'simulateur': 'CO.deleky-ressources.html',
}

# Anchor suffixes for specific pages
PAGE_ANCHORS = {
    'ressources': '#res-docs',
}

HOME_NAV_RIGHT_HTML = """    <!-- DROITE : TEL + LANG + LOGIN -->
    <div style="display:flex;gap:8px;align-items:center;flex-shrink:0">

      <a href="tel:+22507000588" class="nav-tel">+225&nbsp;07&nbsp;00&nbsp;05&nbsp;88</a>

      <!-- Switcher FR / EN -->
      <div class="lang-switch">
        <button class="lang-btn active" onclick="switchLang('fr',this)">FR</button>
        <button class="lang-btn" onclick="switchLang('en',this)">EN</button>
      </div>

      <a href="CO.deleky-login (7).html" class="nav-login">Connexion</a>

    </div>"""

FOOTER_HTML = """<footer>
  <div class="footer-top">

    <!-- Brand -->
    <div>
      <div style="display:inline-block;background:#ffffff;padding:10px 16px;border-radius:12px;margin-bottom:16px">
        <img src="logo.jpg" style="height:38px;width:auto;display:block">
      </div>
      <p class="footer-tagline">Comptabilité · Fiscalité · Gestion d'Entreprise<br>Abidjan, Côte d'Ivoire</p>
      <div class="footer-social">
        <a href="#" class="social-btn"><svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
        <a href="#" class="social-btn"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 016 6v7h-4v-7a2 2 0 00-2-2 2 2 0 00-2 2v7h-4v-7a6 6 0 016-6zM2 9h4v12H2z"/><circle cx="4" cy="4" r="2" fill="white" stroke="none"/></svg></a>
        <a href="#" class="social-btn"><svg viewBox="0 0 24 24"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/></svg></a>
        <a href="#" class="social-btn"><svg viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1112.63 8 4 4 0 0116 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg></a>
        <a href="#" class="social-btn"><svg viewBox="0 0 24 24"><path d="M22.54 6.42a2.78 2.78 0 00-1.95-1.96C18.88 4 12 4 12 4s-6.88 0-8.59.46a2.78 2.78 0 00-1.95 1.96A29 29 0 001 12a29 29 0 00.46 5.58A2.78 2.78 0 003.41 19.6C5.12 20 12 20 12 20s6.88 0 8.59-.46a2.78 2.78 0 001.95-1.95A29 29 0 0023 12a29 29 0 00-.46-5.58z"/><polygon points="9.75 15.02 15.5 12 9.75 8.98 9.75 15.02" fill="white" stroke="none"/></svg></a>
      </div>
    </div>

    <!-- Solutions -->
    <div>
      <div class="footer-col-h">Solutions</div>
      <ul class="footer-links">
        <li><a href="CO.deleky-creation-entreprise.html">Création d'Entreprise</a></li>
        <li><a href="CO.deleky-petites-entreprises.html" target="_blank">Petites Entreprises</a></li>
        <li><a href="CO.deleky-entreprises (3).html" target="_blank">Entreprises</a></li>
        <li><a href="CO.deleky-comptabilite-en-retard.html" target="_blank">Comptabilité en Retard</a></li>
        <li><a href="CO.deleky-gestion-de-paie.html" target="_blank">Gestion de Paie</a></li>
        <li><a href="CO.deleky-juridique-ag.html" target="_blank">Juridique &amp; AG</a></li>
        <li><a href="CO.deleky-entreprises (3).html-plan" target="_blank">Business Plan</a></li>
      </ul>
    </div>

    <!-- Formes Juridiques -->
    <div>
      <div class="footer-col-h">Formes Juridiques</div>
      <ul class="footer-links">
        <li><a href="CO.deleky-tableau-comparatif.html">Tableau Comparatif</a></li>
        <li><a href="CO.deleky-creation-sarl.html">SARL</a></li>
        <li><a href="CO.deleky-creation-sa.html">SA</a></li>
        <li><a href="CO.deleky-creation-sas.html">SAS</a></li>
        <li><a href="CO.deleky-creation-snc.html">SNC</a></li>
        <li><a href="CO.deleky-creation-gie.html">GIE</a></li>
        <li><a href="CO.deleky-creation-sci.html">SCI</a></li>
      </ul>
    </div>

    <!-- Nos Produits -->
    <div>
      <div class="footer-col-h">Nos Produits</div>
      <ul class="footer-links">
        <li><a href="CO.deleky-simulateur-paie-v2.html">CI Payroll Simulation</a></li>
        <li><a href="CO.deleky-simulateur-immo.html">Home Loan Calculator</a></li>
        <li><a href="CO.deleky-plan-amortissement.html">Amortization Plan</a></li>
      </ul>
    </div>

    <!-- À Propos -->
    <div>
      <div class="footer-col-h">À Propos</div>
      <ul class="footer-links">
        <li><a href="CO_deleky-cabinet-v2.html">Le Cabinet</a></li>
        <li><a href="CO.deleky-publications.html">Blog &amp; Articles</a></li>
        <li><a href="CO.deleky-publications.html">Événements</a></li>
        <li><a href="CO.deleky-ressources.html">Témoignages</a></li>
        <li><a href="CO.deleky-joinus.html">Nous Rejoindre</a></li>
        <li><a href="CO.deleky-ressources.html">Partenariat</a></li>
        <li><a href="CO.deleky-ressources.html">Simulateur Paie</a></li>
      </ul>
    </div>

  </div>
  <div class="footer-bottom">
    <span>© 2025 Deleky's SARL — Tous droits réservés</span>
    <div class="footer-bottom-links">
      <a href="#">Conditions Générales</a>
      <a href="#">Mentions Légales</a>
      <a href="#">Protection des Données</a>
      <a href="CO.deleky-contact.html">Contact</a>
    </div>
  </div>
</footer>"""


def remove_cta(content):
    """Remove all CTA-related CSS and HTML."""
    # Remove CTA CSS blocks
    content = re.sub(
        r'/\* ── NAV CTA PREMIUM ──.*?nav-cta:hover \.nav-cta-arrow\{transform:translateX\(3px\)\}',
        '', content, flags=re.DOTALL
    )
    # Remove orphan CTA CSS comments
    content = content.replace('/* ── NAV CTA PREMIUM ──────────────────────────────────── */', '')
    # Remove any remaining .nav-cta CSS rules
    content = re.sub(r'\.nav-cta[-\w]*\{[^}]*\}', '', content)
    content = re.sub(r'\.nav-cta:hover[^\{]*\{[^}]*\}', '', content)
    
    # Remove CTA button HTML (any anchor with nav-cta class)
    content = re.sub(
        r'\s*<!--?\s*CTA PREMIUM\s*-->?\s*<a[^>]*class="nav-cta"[^>]*>.*?</a>',
        '', content, flags=re.DOTALL
    )
    content = re.sub(
        r'\s*<a[^>]*class="nav-cta"[^>]*>.*?</a>',
        '', content, flags=re.DOTALL
    )
    
    return content


def replace_navigate_call(m):
    """Replace a navigate('X') call with direct href."""
    full = m.group(0)
    page = m.group(1)
    
    if page in PAGE_MAP:
        href = PAGE_MAP[page]
        anchor = PAGE_ANCHORS.get(page, '')
        return f'href="{href}{anchor}"'
    return full


def fix_navigate_links(content):
    """Replace all navigate() and navigate&&navigate() calls in href/onclick."""
    # Pattern 1: onclick with navigate&&navigate('X')
    content = re.sub(
        r'onclick="navigate&&navigate\(\'([^\']+)\'\)"',
        lambda m: f'onclick="closeNav()"',
        content
    )
    
    # Pattern 2: onclick with navigate('X');closeNav()
    content = re.sub(
        r'onclick="navigate\(\'([^\']+)\'\);closeNav\(\)"',
        lambda m: f'onclick="closeNav()"',
        content
    )
    
    # Pattern 3: onclick with navigate('X') only (no closeNav)
    content = re.sub(
        r'onclick="navigate\(\'([^\']+)\'\)"',
        '',  # remove onclick entirely
        content
    )
    
    # Now replace all href="#" (from navigate links) with proper href
    # But only for links that had navigate - we need to identify them.
    # Since we removed onclick, we need to fix specific patterns.
    
    # Fix known nav links with navigate
    for page, href in PAGE_MAP.items():
        anchor = PAGE_ANCHORS.get(page, '')
        full_href = f'{href}{anchor}'
        # Replace href="#" onclick="closeNav()" for these specific anchors
        # (only when they appear with known link text patterns)
        pass
    
    return content


def fix_type_b_all(content):
    """Comprehensive fix for Type B pages."""
    
    # ---- Fix nav menu links ----
    # Replace the entire nav-menu section with home page equivalent.
    # But it's easier to do targeted replacements.
    
    # Fix the nav structure
    # Remove nav-item class, keep has-drop
    content = content.replace('class="nav-item has-drop"', 'class="has-drop"')
    content = content.replace('"nav-item"', '"nav-item-removed"')  # will clean up later
    content = content.replace('class="nav-link"', '')
    
    # Fix main nav links (they use navigate&&navigate('X'))
    # Accueil
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'home\'\)">Accueil</a>',
        '<a href="CO.deleky-home.html" onclick="closeNav()">Accueil</a>',
        content
    )
    # Le Cabinet
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'cabinet\'\)">Le Cabinet</a>',
        '<a href="CO_deleky-cabinet-v2.html" onclick="closeNav()">Le Cabinet</a>',
        content
    )
    # Missions
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'missions\'\)">Missions</a>',
        '<a href="CO.deleky-missions.html" onclick="closeNav()">Missions</a>',
        content
    )
    # Nous Rejoindre
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'joinus\'\)">Nous Rejoindre</a>',
        '<a href="CO.deleky-joinus.html" onclick="closeNav()">Nous Rejoindre</a>',
        content
    )
    # Contact
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'contact\'\)">Contact</a>',
        '<a href="CO.deleky-contact.html" onclick="closeNav()">Contact</a>',
        content
    )
    
    # Fix dropdown headers
    content = re.sub(
        r'<a href="#" class="active" data-page="ressources">Ressources ▾</a>',
        '<a href="CO.deleky-ressources.html#res-docs">Ressources</a>',
        content
    )
    content = re.sub(
        r'<a href="#" class="active">Ressources ▾</a>',
        '<a href="CO.deleky-ressources.html#res-docs">Ressources</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'ressources\'\)">Ressources ▾</a>',
        '<a href="CO.deleky-ressources.html#res-docs">Ressources</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'ressources\'\)" class="active">Ressources ▾</a>',
        '<a href="CO.deleky-ressources.html#res-docs">Ressources</a>',
        content
    )
    
    content = re.sub(
        r'<a href="#" data-page="publications">Publications ▾</a>',
        '<a href="CO.deleky-publications.html">Publications</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'publications\'\)">Publications ▾</a>',
        '<a href="CO.deleky-publications.html">Publications</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'publications\'\)">Publications ▾</a>',
        '<a href="CO.deleky-publications.html">Publications</a>',
        content
    )
    
    # Fix dropdown items
    # Ressources dropdown items
    content = re.sub(
        r'onclick="navigate&&navigate\(\'ressources\'\)" class="drop-item"',
        'onclick="closeNav()" class="drop-item"',
        content
    )
    content = re.sub(
        r'onclick="navigate&&navigate\(\'ressources\'\)"',
        'onclick="closeNav()"',
        content
    )
    
    # Publications dropdown items  
    content = re.sub(
        r'onclick="navigate&&navigate\(\'blog\'\)"',
        'onclick="closeNav()"',
        content
    )
    content = re.sub(
        r'onclick="navigate&&navigate\(\'publications\'\)"',
        'onclick="closeNav()"',
        content
    )
    
    # Fix logo link
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'home\'\)" class="logo-wrap"',
        '<a href="CO.deleky-home.html" class="logo-wrap"',
        content
    )
    
    # Fix login link
    content = re.sub(
        r'onclick="navigate&&navigate\(\'login\'\)"',
        '',
        content
    )
    # Change href for login
    content = re.sub(
        r'<a href="#" class="nav-login">Connexion</a>',
        '<a href="CO.deleky-login (7).html" class="nav-login">Connexion</a>',
        content
    )
    
    # Fix contact CTA link (nav-cta)
    content = re.sub(
        r'onclick="navigate&&navigate\(\'contact\'\)" class="nav-cta"',
        'href="CO.deleky-contact.html" class="nav-cta"',
        content
    )
    
    # Fix CTA buttons with navigate&&navigate('contact') (qa-cta, contact-cta)
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'contact\'\)" class="qa-cta">',
        '<a href="CO.deleky-contact.html" class="qa-cta">',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate&&navigate\(\'contact\'\)" class="contact-cta">',
        '<a href="CO.deleky-contact.html" class="contact-cta">',
        content
    )
    
    # Fix nav links using navigate('X');closeNav() pattern (plan-amortissement, simulateur-immo style)
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'home\'\);closeNav\(\)"  data-page="home">Accueil</a>',
        '<a href="CO.deleky-home.html" onclick="closeNav()">Accueil</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'cabinet\'\);closeNav\(\)"  data-page="cabinet">Le Cabinet</a>',
        '<a href="CO_deleky-cabinet-v2.html" onclick="closeNav()">Le Cabinet</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'missions\'\);closeNav\(\)"  data-page="missions">Missions</a>',
        '<a href="CO.deleky-missions.html" onclick="closeNav()">Missions</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'joinus\'\);closeNav\(\)"  data-page="joinus">Nous Rejoindre</a>',
        '<a href="CO.deleky-joinus.html" onclick="closeNav()">Nous Rejoindre</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'contact\'\);closeNav\(\)"  data-page="contact">Contact</a>',
        '<a href="CO.deleky-contact.html" onclick="closeNav()">Contact</a>',
        content
    )
    # Fix dropdown items using navigate('ressources');closeNav()
    content = re.sub(
        r'onclick="navigate\(\'ressources\'\);closeNav\(\)"',
        'onclick="closeNav()"',
        content
    )
    
    # Remove the navigate() function definition
    content = re.sub(
        r'function navigate\(p\)\{window\.location\.href="deleky-site\.html#"\+\+?p\}',
        '',
        content
    )
    
    # ---- Fix footer links ----
    # Replace navigate('missions') in footers
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'missions\'\)">([^<]+)</a>',
        lambda m: f'<a href="CO.deleky-missions.html">{m.group(1)}</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'cabinet\'\)">([^<]+)</a>',
        lambda m: f'<a href="CO_deleky-cabinet-v2.html">{m.group(1)}</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'blog\'\)">([^<]+)</a>',
        lambda m: f'<a href="CO.deleky-publications.html">{m.group(1)}</a>',
        content
    )
    content = re.sub(
        r'<a href="#" onclick="navigate\(\'contact\'\)">([^<]+)</a>',
        lambda m: f'<a href="CO.deleky-contact.html">{m.group(1)}</a>',
        content
    )
    
    # Fix footer Nos Produits section specifically
    # It currently has 2 items (no Amortization Plan), with incorrect hrefs
    content = re.sub(
        r'<!-- Nos Produits -->\s*<div>\s*<div class="footer-col-h">Nos Produits</div>\s*<ul class="footer-links">\s*<li><a href="#" onclick="navigate\(\'ressources\'\)">CI Payroll Simulation</a></li>\s*<li><a href="#" onclick="navigate\(\'ressources\'\)">Home Loan Calculator</a></li>\s*</ul>',
        '<!-- Nos Produits -->\n    <div>\n      <div class="footer-col-h">Nos Produits</div>\n      <ul class="footer-links">\n        <li><a href="CO.deleky-simulateur-paie-v2.html">CI Payroll Simulation</a></li>\n        <li><a href="CO.deleky-simulateur-immo.html">Home Loan Calculator</a></li>\n        <li><a href="CO.deleky-plan-amortissement.html">Amortization Plan</a></li>\n      </ul>',
        content
    )
    
    # Fix remaining href="#" with navigate in onclick (general catch-all)
    content = re.sub(
        r'href="#"\s+onclick="navigate\(\'([^\']+)\'\)"',
        lambda m: f'href="{PAGE_MAP.get(m.group(1), "#")}"',
        content
    )
    
    # Clean up extra blank lines
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    return content


def remove_navigate_function(content):
    """Remove the dead navigate() function from all pages."""
    patterns = [
        r'function navigate\(p\)\{window\.location\.href="deleky-site\.html#"\+\+?p\};?',
        r'function navigate\(p\)\s*\{\s*window\.location\.href\s*=\s*"deleky-site\.html#"\+p\s*\}\s*',
        r'function navigate\(p\)\{window\.location\.href="deleky-site\.html#"\+p\};?\s*',
    ]
    for pat in patterns:
        content = re.sub(pat, '', content)
    return content


def fix_article_page(content):
    """Add footer and nav right-side to article page."""
    if '<footer>' in content:
        return content
    
    # Add footer before </body>
    content = content.replace('</body>', FOOTER_HTML + '\n</body>')
    
    # Add nav right-side: look for pattern where the nav ends
    content = re.sub(
        r'(</ul>)\s*\n\s*<div class="lang-switch">',
        lambda m: m.group(1) + '\n' + HOME_NAV_RIGHT_HTML + '\n    <div class="lang-switch">',
        content
    )
    
    # Remove the standalone lang-switch if it's now redundant
    # (it's already inside HOME_NAV_RIGHT_HTML)
    content = re.sub(
        r'\s*<div class="lang-switch">\s*<button class="lang-btn active" onclick="switchLang\(\'fr\', this\)">FR</button>\s*<button class="lang-btn" onclick="switchLang\(\'en\', this\)">EN</button>\s*</div>',
        '',
        content
    )
    
    return content


def process_file(filepath):
    basename = os.path.basename(filepath)
    if not filepath.endswith('.html'):
        return
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'nav-inner' not in content and 'nav-menu' not in content:
        return
    
    original = content
    
    # Remove CTA CSS and HTML
    content = remove_cta(content)
    
    # Fix Type B pages comprehensively
    if basename in TYPE_B_PAGES:
        content = fix_type_b_all(content)
    
    # Fix article page
    if basename == 'CO.deleky-article.html':
        content = fix_article_page(content)
    
    # Remove dead navigate() function from all pages
    content = remove_navigate_function(content)
    
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
