const fs = require('fs');
const path = require('path');

const dir = __dirname;
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const LANG_SCRIPT = '<script src="assets/js/lang.js"></script>';

function patchSwitchLang(content) {
  // Replace the old switchLang function with one that calls the shared version
  const oldPattern = /function switchLang\(lang,btn\)\{[^}]+\}/;
  const newFunc = `function switchLang(lang,btn){
  try{ window.delekyLang.switchLang(lang); }catch(e){}
  document.querySelectorAll('.lang-btn').forEach(b=>b.classList.remove('active'));
  if(btn) btn.classList.add('active');
}`;
  return content.replace(oldPattern, newFunc);
}

function injectScriptTag(content) {
  // Insert lang.js before the first <script> tag
  return content.replace('<script>', LANG_SCRIPT + '\n<script>');
}

files.forEach(file => {
  if (file === 'patch_lang.js') return;
  const filePath = path.join(dir, file);
  let content = fs.readFileSync(filePath, 'utf-8');

  // Skip if already patched
  if (content.includes('assets/js/lang.js')) {
    console.log(`✓ Already patched: ${file}`);
    return;
  }

  // Check if file has <script> tag
  if (!content.includes('<script>')) {
    console.log(`✗ No <script> found: ${file}`);
    return;
  }

  // Check if file uses the old switchLang pattern
  if (content.includes('function switchLang(lang,btn)')) {
    content = patchSwitchLang(content);
  }

  content = injectScriptTag(content);
  fs.writeFileSync(filePath, content, 'utf-8');
  console.log(`✓ Patched: ${file}`);
});

console.log('\nDone patching ' + files.filter(f => f !== 'patch_lang.js').length + ' files.');
