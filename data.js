(function() {
'use strict';

const STORAGE_PREFIX = 'dlk-';

/* ── Initial dummy data ────────────────────────────── */
const SEED = {
  publications: [
    { id:'pub1', title:"Guide Fiscal PME 2024 — Obligations et Optimisation", category:"Fiscal", summary:"Résumé des obligations fiscales et leviers d'optimisation.", date:"2024-12-15", status:"published", author:"Leky Kouadio J." },
    { id:'pub2', title:"Les Échéances Déclaratives 2025 en Côte d'Ivoire", category:"Fiscal", summary:"Calendrier complet des déclarations TVA, IS, IRVM.", date:"2025-01-10", status:"published", author:"Leky Kouadio J." },
    { id:'pub3', title:"Comment choisir entre SARL et SAS en CI ?", category:"Juridique", summary:"Comparatif détaillé des deux formes juridiques.", date:"2024-11-20", status:"published", author:"Direction" },
    { id:'pub4', title:"Tout savoir sur le RCCM et le Guichet Unique", category:"Juridique", summary:"Guide pratique pour immatriculer son entreprise.", date:"2024-10-05", status:"draft", author:"Leky Kouadio J." },
    { id:'pub5', title:"Optimisation de la Paie dans le secteur PME", category:"Paie", summary:"Stratégies pour réduire le coût de la masse salariale.", date:"2025-02-01", status:"published", author:"Leky Kouadio J." },
  ],
  reviews: [
    { id:'rev1', name:"Konan Michel", company:"Transport Express CI", rating:5, text:"Depuis que Deleky's gère notre comptabilité et notre fiscalité, nous avons réduit notre charge fiscale de 18%. Nos données financières sont enfin fiables.", date:"2025-01-15", status:"approved" },
    { id:'rev2', name:"Diallo Aminata", company:"Agro-CI SARL", rating:5, text:"Deleky's a mis de l'ordre dans notre gestion dès le départ. Structure comptable claire, fiscalité optimisée, reporting mensuel.", date:"2024-12-20", status:"approved" },
    { id:'rev3', name:"Brou Koffi", company:"Groupe Immobilier Abidjan", rating:4, text:"Ce qui nous a convaincus, c'est l'approche intégrée : comptabilité, fiscalité et analyse de risques en un seul cabinet.", date:"2024-11-10", status:"approved" },
    { id:'rev4', name:"Kouamé Yves", company:"TechSarl CI", rating:5, text:"Un accompagnement professionnel et réactif. Je recommande vivement Deleky's pour toute entreprise.", date:"2025-02-05", status:"pending" },
    { id:'rev5', name:"Gnahoré Béatrice", company:"Beauty Store Abidjan", rating:4, text:"Merci à toute l'équipe pour leur disponibilité et leur expertise comptable.", date:"2025-01-28", status:"approved" },
  ],
  messages: [
    { id:'msg1', name:"Kouamé Jean", email:"jean@exemple.ci", phone:"+225 01 02 03 04", subject:"Création d'entreprise", message:"Bonjour, je souhaite créer une SARL à Abidjan. Quels sont les délais et les coûts ?", date:"2025-02-10", read:false },
    { id:'msg2', name:"Diallo Fatou", email:"fatou@exemple.ci", phone:"+225 05 06 07 08", subject:"Fiscalité", message:"J'ai besoin d'un audit fiscal pour ma société. Pouvez-vous me recevoir ?", date:"2025-02-08", read:false },
    { id:'msg3', name:"Konan Bernard", email:"bernard@exemple.ci", phone:"+225 09 10 11 12", subject:"Gestion de paie", message:"Je voudrais externaliser ma paie. Quels sont vos tarifs pour une PME de 15 salariés ?", date:"2025-02-05", read:true },
    { id:'msg4', name:"N'Guessan Patrick", email:"patrick@exemple.ci", phone:"+225 13 14 15 16", subject:"Partenariat", message:"Je suis expert-comptable et souhaite proposer un partenariat avec Deleky's.", date:"2025-02-03", read:false },
    { id:'msg5', name:"Sie Rachelle", email:"rachelle@exemple.ci", phone:"+225 17 18 19 20", subject:"Audit", message:"Besoin d'un audit de conformité pour notre institution financière.", date:"2025-01-25", read:true },
  ],
  media: [
    { id:'med1', name:"Logo Deleky's", type:"image/png", size:"45 KB", section:"Logo", url:"#", date:"2025-01-15" },
    { id:'med2', name:"Photo équipe 2025", type:"image/jpg", size:"2.1 MB", section:"Équipe", url:"#", date:"2025-02-01" },
    { id:'med3', name:"Bannière hero accueil", type:"image/png", size:"890 KB", section:"Hero", url:"#", date:"2025-01-20" },
    { id:'med4', name:"Photo bureau Plateau", type:"image/jpg", size:"1.5 MB", section:"À propos", url:"#", date:"2024-12-10" },
    { id:'med5', name:"Icône services", type:"image/svg", size:"12 KB", section:"Services", url:"#", date:"2025-01-05" },
    { id:'med6', name:"Image mission conseil", type:"image/jpg", size:"1.8 MB", section:"Missions", url:"#", date:"2025-02-10" },
  ],
  users: [
    { id:'usr1', fullName:"Administrateur", email:"admin@deleky.com", password:"Admin1234", role:"admin", createdAt:"2024-01-01" },
  ],
  membres: [
    { id:'mbr1', nom:"Leky Kouadio J.", poste:"Associé Gérant", email:"delekys@gmail.com", tel:"+225 07 07 000 588", bio:"Expert-comptable et auditeur, il dirige le cabinet avec une vision claire : allier rigueur professionnelle et proximité client." },
    { id:'mbr2', nom:"Koffi Amenan", poste:"Responsable Paie", email:"amenan@delekys.ci", tel:"+225 05 05 05 05", bio:"Spécialiste de la paie ivoirienne, elle assure la conformité de chaque bulletin." },
    { id:'mbr3', nom:"Kouamé Yao", poste:"Auditeur Senior", email:"yao@delekys.ci", tel:"+225 05 05 05 06", bio:"Expert en audit interne et contrôle, maîtrise des risques opérationnels." },
  ],
  docs: [
    { id:'d1', titre:"Guide Fiscal PME 2024", cat:"Fiscal", type:"PDF", taille:"2.4 MB", dl:142 },
    { id:'d2', titre:"Contrat CDI Côte d'Ivoire", cat:"Juridique", type:"Word", taille:"180 KB", dl:89 },
    { id:'d3', titre:"KPI Financiers Template", cat:"Comptable", type:"Excel", taille:"1.1 MB", dl:234 },
    { id:'d4', titre:"Clôture Comptable Checklist", cat:"Comptable", type:"PDF", taille:"850 KB", dl:178 },
    { id:'d5', titre:"Guide CNPS 2024", cat:"Paie", type:"PDF", taille:"1.8 MB", dl:312 },
    { id:'d6', titre:"Bulletin Paie SYSCOHADA", cat:"Paie", type:"Excel", taille:"420 KB", dl:267 },
    { id:'d7', titre:"Création SARL en CI", cat:"Juridique", type:"PDF", taille:"3.2 MB", dl:445 },
    { id:'d8', titre:"Matrice Risques BCEAO", cat:"RH", type:"Excel", taille:"560 KB", dl:98 },
  ],
  ticker: {
    annonces: [
      { id:'t1', badge:'Nouveau', texte:"La Réforme ITS 2024 : ce que vous devez savoir", lien:'#', label:"Lire l'article", actif:true },
      { id:'t2', badge:'Service en ligne', texte:"Gérez votre paie en toute conformité", lien:'#', label:'Consulter', actif:true },
      { id:'t3', badge:'Rappel', texte:"Primes de fin d'année (PFA) : la période approche", lien:'#', label:'Notre guide', actif:true },
    ],
    promo: { text:"🎁 Premier échange offert · Diagnostic gratuit · Sans engagement", link:"contact", btn:"Prendre rendez-vous →", color:"red", visible:true }
  },
  candidatures: [
    { id:'cand1', nom:"Konan Hervé", societe:"TechSarl CI", type:"Partenaire Tech", date:"24 Jan 2025", statut:"Nouveau" },
    { id:'cand2', nom:"Diallo Aminata", societe:"Fiduciaire West", type:"Stratégique", date:"22 Jan 2025", statut:"En cours" },
    { id:'cand3', nom:"Brou Koffi", societe:"KB Conseils", type:"Apporteur", date:"20 Jan 2025", statut:"Accepté" },
  ],
};

/* ── Helpers ───────────────────────────────────────── */
function key(name) { return STORAGE_PREFIX + name; }

function _get(name) {
  try {
    const raw = localStorage.getItem(key(name));
    if (raw) return JSON.parse(raw);
  } catch(e) {}
  return null;
}

function _set(name, data) {
  try { localStorage.setItem(key(name), JSON.stringify(data)); } catch(e) {}
}

function _remove(name) {
  try { localStorage.removeItem(key(name)); } catch(e) {}
}

function _id() { return Date.now().toString(36) + Math.random().toString(36).substr(2,5); }

/* ── Init: seed if first run ──────────────────────── */
function init() {
  let seeded = false;
  try { seeded = !!localStorage.getItem(key('_seeded')); } catch(e) {}
  if (!seeded) {
    Object.keys(SEED).forEach(k => _set(k, SEED[k]));
    _set('_seeded', true);
  }
}

/* ── Generic CRUD ──────────────────────────────────── */
function getAll(collection) {
  return _get(collection) || [];
}

function getById(collection, id) {
  const items = getAll(collection);
  return items.find(i => i.id === id) || null;
}

function create(collection, item) {
  const items = getAll(collection);
  const newItem = { id: _id(), ...item, createdAt: new Date().toISOString() };
  items.push(newItem);
  _set(collection, items);
  return newItem;
}

function update(collection, id, changes) {
  const items = getAll(collection);
  const idx = items.findIndex(i => i.id === id);
  if (idx === -1) return null;
  items[idx] = { ...items[idx], ...changes, updatedAt: new Date().toISOString() };
  _set(collection, items);
  return items[idx];
}

function del(collection, id) {
  const items = getAll(collection);
  const filtered = items.filter(i => i.id !== id);
  _set(collection, filtered);
  return filtered.length < items.length;
}

/* ── Auth ──────────────────────────────────────────── */
const AUTH_KEY = key('_auth');

function login(email, password) {
  const users = getAll('users');
  const user = users.find(u => u.email.toLowerCase() === email.toLowerCase());
  if (!user || user.password !== password) return null;
  const session = { userId: user.id, email: user.email, fullName: user.fullName, role: user.role, loggedInAt: new Date().toISOString() };
  _set('_auth', session);
  return session;
}

function signup(data) {
  const users = getAll('users');
  if (users.find(u => u.email.toLowerCase() === data.email.toLowerCase())) return null;
  const user = create('users', { fullName: data.fullName, email: data.email, password: data.password, role: 'admin' });
  return user;
}

function logout() {
  _remove('_auth');
}

function isAuthenticated() {
  return !!_get('_auth');
}

function getCurrentUser() {
  return _get('_auth');
}

function requireAuth() {
  if (!isAuthenticated()) {
    window.location.href = 'login.html';
    return false;
  }
  return true;
}

/* ── Counts for dashboard ──────────────────────────── */
function getCounts() {
  return {
    publications: getAll('publications').filter(p => p.status === 'published').length,
    reviews: getAll('reviews').filter(r => r.status === 'approved').length,
    messages: getAll('messages').length,
    media: getAll('media').length,
    membres: getAll('membres').length,
    docs: getAll('docs').length,
    users: getAll('users').length,
  };
}

/* ── Export ──────────────────────────────────────── */
window.dlkData = {
  init,
  getAll, getById, create, update, del,
  login, signup, logout, isAuthenticated, getCurrentUser, requireAuth,
  getCounts,
};

/* Auto-init */
init();

})();
