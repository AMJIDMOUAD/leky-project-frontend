#!/usr/bin/env python3
"""Fix nav on all pages: hide phone at tablet widths so Connexion always fits."""

import os, re

DIR = r"C:\Users\AMJID MOUAD\Desktop\leky project"

NAV_RESP_CSS = """
/* Nav responsive — hide phone on medium screens so Connexion is always visible */
@media(max-width:1100px){.nav-tel{display:none}}
"""

for fname in os.listdir(DIR):
    if not fname.endswith('.html'):
        continue
    if fname in ('login.html', 'signup.html', 'deleky-admin.html', 'CO.deleky-login (7).html'):
        continue
    fpath = os.path.join(DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    if '.nav-tel' not in content:
        continue
    original = content
    content = re.sub(r'/\* Nav responsive.*?</style>', NAV_RESP_CSS.strip() + '\n</style>', content, flags=re.DOTALL)
    if content == original:
        content = content.replace('</style>', NAV_RESP_CSS.strip() + '\n</style>')
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"MODIFIED: {fname}")
    else:
        print(f"UNCHANGED: {fname}")
