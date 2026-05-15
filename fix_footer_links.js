const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && !f.includes('deleky-admin'));

const fixes = {
  'href="CO_deleky-cabinet-v2.html">Tableau Comparatif</a>': 'href="CO.deleky-tableau-comparatif.html">Tableau Comparatif</a>',
  'href="CO_deleky-cabinet-v2.html">SARL</a>': 'href="CO.deleky-creation-sarl.html">SARL</a>',
  'href="CO_deleky-cabinet-v2.html">SA</a>': 'href="CO.deleky-creation-sa.html">SA</a>',
  'href="CO_deleky-cabinet-v2.html">SAS</a>': 'href="CO.deleky-creation-sas.html">SAS</a>',
  'href="CO_deleky-cabinet-v2.html">SNC</a>': 'href="CO.deleky-creation-snc.html">SNC</a>',
  'href="CO_deleky-cabinet-v2.html">GIE</a>': 'href="CO.deleky-creation-gie.html">GIE</a>',
  'href="CO_deleky-cabinet-v2.html">SCI</a>': 'href="CO.deleky-creation-sci.html">SCI</a>',
};

let count = 0;
files.forEach(file => {
  if (file === 'fix_footer_links.js') return;
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  let changed = false;
  for (const [oldHref, newHref] of Object.entries(fixes)) {
    if (content.includes(oldHref)) {
      content = content.split(oldHref).join(newHref);
      changed = true;
    }
  }
  if (changed) {
    fs.writeFileSync(filePath, content, 'utf-8');
    count++;
    console.log(`✓ Fixed: ${file}`);
  }
});
console.log(`\nFixed ${count} files.`);
