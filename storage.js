(function() {
'use strict';

const PREFIX = 'dlk-';
const SEED_KEY = PREFIX + '_seeded';

const SEED = {
  users: [
    { id:'usr1', fullName:"Administrateur", email:"admin@deleky.com", password:"Admin1234", role:"admin", createdAt:"2024-01-01" },
  ],
  publications: [
    { id:'pub1', title:"Guide Fiscal PME 2024", category:"Fiscal", summary:"Obligations fiscales et leviers d'optimisation.", date:"2024-12-15", status:"published", author:"Leky Kouadio J." },
    { id:'pub2', title:"Échéances Déclaratives 2025 en CI", category:"Fiscal", summary:"Calendrier TVA, IS, IRVM.", date:"2025-01-10", status:"published", author:"Leky Kouadio J." },
    { id:'pub3', title:"SARL vs SAS en Côte d'Ivoire", category:"Juridique", summary:"Comparatif des formes juridiques.", date:"2024-11-20", status:"published", author:"Direction" },
    { id:'pub4', title:"RCCM et Guichet Unique", category:"Juridique", summary:"Immatriculer son entreprise.", date:"2024-10-05", status:"draft", author:"Leky Kouadio J." },
    { id:'pub5', title:"Optimisation Paie PME", category:"Paie", summary:"Réduire le coût de la masse salariale.", date:"2025-02-01", status:"published", author:"Leky Kouadio J." },
  ],
  reviews: [
    { id:'rev1', name:"Konan Michel", company:"Transport Express CI", rating:5, text:"Depuis Deleky's, notre charge fiscale a baissé de 18% et nos données sont fiables.", date:"2025-01-15", status:"approved" },
    { id:'rev2', name:"Diallo Aminata", company:"Agro-CI SARL", rating:5, text:"Structure comptable claire, fiscalité optimisée, reporting mensuel.", date:"2024-12-20", status:"approved" },
    { id:'rev3', name:"Brou Koffi", company:"Groupe Immobilier Abidjan", rating:4, text:"Approche intégrée comptabilité, fiscalité et risques en un cabinet.", date:"2024-11-10", status:"approved" },
    { id:'rev4', name:"Kouamé Yves", company:"TechSarl CI", rating:5, text:"Accompagnement professionnel et réactif. Je recommande.", date:"2025-02-05", status:"pending" },
    { id:'rev5', name:"Gnahoré Béatrice", company:"Beauty Store Abidjan", rating:4, text:"Merci à l'équipe pour leur disponibilité et expertise.", date:"2025-01-28", status:"approved" },
  ],
  messages: [
    { id:'msg1', name:"Kouamé Jean", email:"jean@exemple.ci", phone:"+225 01 02 03 04", subject:"Création d'entreprise", message:"Je souhaite créer une SARL à Abidjan. Délais et coûts ?", date:"2025-02-10", read:false },
    { id:'msg2', name:"Diallo Fatou", email:"fatou@exemple.ci", phone:"+225 05 06 07 08", subject:"Fiscalité", message:"Besoin d'un audit fiscal pour ma société.", date:"2025-02-08", read:false },
    { id:'msg3', name:"Konan Bernard", email:"bernard@exemple.ci", phone:"+225 09 10 11 12", subject:"Gestion de paie", message:"Tarifs pour externaliser la paie (15 salariés) ?", date:"2025-02-05", read:true },
    { id:'msg4', name:"N'Guessan Patrick", email:"patrick@exemple.ci", phone:"+225 13 14 15 16", subject:"Partenariat", message:"Expert-comptable, je propose un partenariat.", date:"2025-02-03", read:false },
    { id:'msg5', name:"Sie Rachelle", email:"rachelle@exemple.ci", phone:"+225 17 18 19 20", subject:"Audit", message:"Audit de conformité pour institution financière.", date:"2025-01-25", read:true },
  ],
  media: [
    { id:'med1', name:"Logo Deleky's", type:"image/png", size:"45 KB", section:"Logo", date:"2025-01-15" },
    { id:'med2', name:"Photo équipe 2025", type:"image/jpg", size:"2.1 MB", section:"Équipe", date:"2025-02-01" },
    { id:'med3', name:"Bannière hero accueil", type:"image/png", size:"890 KB", section:"Hero", date:"2025-01-20" },
    { id:'med4', name:"Photo bureau Plateau", type:"image/jpg", size:"1.5 MB", section:"À propos", date:"2024-12-10" },
    { id:'med5', name:"Icône services", type:"image/svg", size:"12 KB", section:"Services", date:"2025-01-05" },
    { id:'med6', name:"Image mission conseil", type:"image/jpg", size:"1.8 MB", section:"Missions", date:"2025-02-10" },
  ],
};

function _id() { return Date.now().toString(36) + Math.random().toString(36).substr(2,5); }
function _key(n) { return PREFIX + n; }
function _get(n) { try { return JSON.parse(localStorage.getItem(_key(n))); } catch(e){} return null; }
function _set(n, d) { try { localStorage.setItem(_key(n), JSON.stringify(d)); } catch(e){} }

function init() {
  if (_get('_seeded')) return;
  Object.keys(SEED).forEach(k => _set(k, SEED[k]));
  _set('_seeded', true);
}

function getAll(collection) { return _get(collection) || []; }
function getById(collection, id) { return (getAll(collection)).find(i => i.id === id) || null; }
function create(collection, item) {
  const items = getAll(collection);
  const n = { id:_id(), ...item, createdAt: new Date().toISOString() };
  items.push(n); _set(collection, items); return n;
}
function update(collection, id, changes) {
  const items = getAll(collection);
  const idx = items.findIndex(i => i.id === id);
  if(idx===-1) return null;
  items[idx] = { ...items[idx], ...changes, updatedAt: new Date().toISOString() };
  _set(collection, items); return items[idx];
}
function del(collection, id) {
  const items = getAll(collection);
  _set(collection, items.filter(i => i.id !== id));
}

function getCounts() {
  return {
    publications: getAll('publications').filter(p => p.status==='published').length,
    reviews: getAll('reviews').filter(r => r.status==='approved').length,
    messages: getAll('messages').length,
    media: getAll('media').length,
  };
}

/* Auth */
function login(email, password) {
  const users = getAll('users');
  const u = users.find(x => x.email.toLowerCase()===email.toLowerCase());
  if (!u || u.password!==password) return null;
  _set('_auth', { userId:u.id, email:u.email, fullName:u.fullName, role:u.role });
  return _get('_auth');
}
function signup(data) {
  const users = getAll('users');
  if (users.find(x => x.email.toLowerCase()===data.email.toLowerCase())) return null;
  return create('users', data);
}
function logout() { try { localStorage.removeItem(_key('_auth')); } catch(e){} }
function isAuth() { return !!_get('_auth'); }
function currentUser() { return _get('_auth'); }
function requireAuth() { if(!isAuth()) { window.location.href='login.html'; return false; } return true; }

window.dlkData = { init, getAll, getById, create, update, del, getCounts, login, signup, logout, isAuth, currentUser, requireAuth };
init();

})();
