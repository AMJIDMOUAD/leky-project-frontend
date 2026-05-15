const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.startsWith('CO.deleky-') && f.endsWith('.html'));

let count = 0;
files.forEach(file => {
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf-8');
  const old = 'href="CO.deleky-home.html" class="nav-login"';
  const updated = 'href="CO.deleky-login (7).html" class="nav-login"';
  if (content.includes(old)) {
    content = content.split(old).join(updated);
    fs.writeFileSync(filePath, content, 'utf-8');
    count++;
    console.log(`✓ Fixed: ${file}`);
  }
});
console.log(`\nFixed ${count} files.`);
