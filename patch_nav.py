#!/usr/bin/env python3
"""
Patch all HTML files:
1. Remove simulator links from Ressources dropdown (targeted to dropdown only)
2. Add 'Nos Produits' dropdown with 3 simulator links (after Missions, before Ressources)
3. Fix nav-cta-inner padding to prevent navbar compression
"""

import os, re

DIR = r"C:\Users\AMJID MOUAD\Desktop\leky project"

NEW_CTA = '.nav-cta-inner{display:flex;align-items:center;gap:8px;padding:6px 12px 6px 8px}'
OLD_CTA = '.nav-cta-inner{display:flex;align-items:center;gap:10px;padding:8px 14px 8px 10px}'

NOS_PRODUITS_HTML = """      <li class="has-drop">
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
      </li>"""


def find_ressources_li(html, start_pos):
    """Find the <li> tag for Ressources in nav starting from start_pos.
    Returns (li_open_start, li_close_end) or None."""
    
    # Look for Ressources has-drop in nav section
    res_match = re.search(
        r'<li[^>]*class="[^"]*has-drop[^"]*"[^>]*>\s*<a[^>]*href="[^"]*[Rr]essources[^"]*"[^>]*>(?:Ressources|Ressources\s*▾)',
        html[start_pos:]
    )
    if not res_match:
        # Type B: href="#" with Ressources text
        res_match = re.search(
            r'<li[^>]*class="[^"]*has-drop[^"]*"[^>]*>\s*<a[^>]*>(?:Ressources|Ressources\s*▾)',
            html[start_pos:]
        )
    
    if not res_match:
        return None
    
    li_open_start = start_pos + res_match.start()
    
    # Find matching </li> - since there are no nested <li> in dropdowns,
    # find the next </li> that closes this one
    li_content = html[li_open_start:]
    close_pos = li_content.find('</li>')
    if close_pos == -1:
        return None
    
    li_close_end = li_open_start + close_pos + len('</li>')
    
    return (li_open_start, li_close_end)


def find_nav_section(content):
    """Find the nav section in the page."""
    nav_start = content.find('<ul class="nav-menu"')
    if nav_start == -1:
        nav_start = content.find('<ul class="nav-menu" id="nav-menu"')
    if nav_start == -1:
        return None
    return nav_start


def remove_simulators_from_dropdown(html, li_start, li_end):
    """Remove simulator <a> tags from within the Ressources dropdown content.
    Only operates within the given bounds."""
    
    section = html[li_start:li_end]
    original_section = section
    
    # Remove separator div if present
    section = re.sub(
        r'<div style="height:1px;background:var\(--gray-200\);margin:4px 8px"></div>\s*',
        '', section
    )
    
    # Remove Type A simulator links (with background:var(--blue) on drop-icon)
    # Match the ENTIRE <a> block
    section = re.sub(
        r'<a[^>]*>\s*<div class="drop-icon" style="background:var\(--blue\)">.*?</div>\s*<div>.*?</div>\s*</a>',
        '', section, flags=re.DOTALL
    )
    
    # Remove Type A Home Loan with navvy background
    section = re.sub(
        r'<a[^>]*>\s*<div class="drop-icon" style="background:var\(--navy\)">.*?</div>\s*<div>.*?</div>\s*</a>',
        '', section, flags=re.DOTALL
    )
    
    # Remove Type B drop-item links containing simulator text
    section = re.sub(
        r'<a[^>]*class="drop-item"[^>]*>.*?(?:CI Payroll Simulation|Home Loan Calculator|Plan d\'Amortissement).*?</a>\s*',
        '', section, flags=re.DOTALL
    )
    
    # Remove plain <a> tags directly containing simulator text (footer-style)
    section = re.sub(
        r'<a[^>]*>(?:CI Payroll Simulation|Home Loan Calculator|Plan d\'Amortissement)\s*[✓✗]?\s*</a>\s*',
        '', section
    )
    
    # Clean extra blank lines
    section = re.sub(r'\n\s*\n\s*\n+', '\n\n', section)
    
    if section != original_section:
        html = html[:li_start] + section + html[li_end:]
    
    return html


def add_nos_produits(content):
    """Add Nos Produits dropdown after Missions li and before Ressources."""
    if 'Nos Produits</a>' in content:
        return content
    
    # Find Missions closing tag
    matches = list(re.finditer(r'Missions</a></li>', content))
    if not matches:
        return content
    
    missions_end = matches[0].end()
    
    # Find Ressources li after Missions
    res = find_ressources_li(content, missions_end)
    if not res:
        return content
    
    li_open_start, _ = res
    
    # Insert Nos Produits dropdown right before Ressources li
    content = content[:li_open_start] + NOS_PRODUITS_HTML + '\n' + content[li_open_start:]
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
    
    # Step 1: Find the nav section and Ressources dropdown, remove simulators within it
    nav_pos = find_nav_section(content)
    if nav_pos:
        res = find_ressources_li(content, nav_pos)
        if res:
            li_start, li_end = res
            content = remove_simulators_from_dropdown(content, li_start, li_end)
    
    # Step 2: Add Nos Produits dropdown
    content = add_nos_produits(content)
    
    # Step 3: Fix CTA button padding
    content = content.replace(OLD_CTA, NEW_CTA)
    
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
