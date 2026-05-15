from pathlib import Path
import re
root = Path(r"c:\Users\AMJID MOUAD\Desktop\leky project")
files = list(root.glob('*.html'))
pattern1 = re.compile(r"function navigate\(p\)\{window\.location\.href='deleky-site\.html#'\+p;\}")
pattern2 = re.compile(r"function navigate\(p\) \{ window\.location\.href = 'deleky-site\.html#' \+ p; \}")
replacement = "function navigate(p){const routes={home:'CO.deleky-home.html',cabinet:'CO_deleky-cabinet-v2.html',missions:'CO.deleky-missions.html',ressources:'CO.deleky-ressources.html',blog:'CO.deleky-publications.html',joinus:'CO.deleky-joinus.html',contact:'CO.deleky-contact.html','simulateur-paie':'CO.deleky-simulateur-paie.html'};window.location.href=routes[p]||routes.home;}"
changes = []
for f in files:
    text = f.read_text(encoding='utf-8')
    new_text = text
    new_text = pattern1.sub(replacement, new_text)
    new_text = pattern2.sub(replacement, new_text)
    new_text = new_text.replace("function goHome(){window.location.href='deleky-site.html#home'}","function goHome(){window.location.href='CO.deleky-home.html'}")
    new_text = new_text.replace("window.open('deleky-site.html','_blank')","window.open('CO.deleky-home.html','_blank')")
    new_text = new_text.replace('href="https://tranquil-sfogliatella-b1b574.netlify.app/small_business"','href="CO.deleky-petites-entreprises.html"')
    new_text = new_text.replace('href="https://tranquil-sfogliatella-b1b574.netlify.app/late-accounting"','href="CO.deleky-comptabilite-en-retard.html"')
    new_text = new_text.replace('href="https://tranquil-sfogliatella-b1b574.netlify.app/payrol-management"','href="CO.deleky-gestion-de-paie.html"')
    new_text = new_text.replace('href="https://tranquil-sfogliatella-b1b574.netlify.app/legal&minutesofagm"','href="CO.deleky-juridique-ag.html"')
    if new_text != text:
        f.write_text(new_text, encoding='utf-8')
        changes.append(str(f))
print('changed', len(changes), 'files')
for p in changes:
    print(p)
