(function() {
'use strict';

/* ══════════════════════════════════════════════════════════════
   DELEKY — EN/FR LANGUAGE SWITCHER
   - Persists in localStorage
   - Applies on page load (no flash)
   - Comprehensive translation dictionary
   - Missing translations are flagged in console
══════════════════════════════════════════════════════════════ */

const STORAGE_KEY = 'deleky-lang';

const TRANSLATIONS = {

  /* ── GLOBAL UI ─────────────────────────────────── */
  'FR':'FR','EN':'EN',
  'Accueil':'Home',
  'Le Cabinet':'The Firm',
  'Missions':'Our Services',
  'Nos Missions':'Our Services',
  'Ressources':'Resources',
  'Publications':'Publications',
  'Nous Rejoindre':'Join Us',
  'Contact':'Contact',
  'Connexion':'Login',
  'Comptabilité':'Accounting',
  'Fiscalité':'Taxation',
  'Gestion d\'Entreprise':'Business Management',
  'Audit':'Audit',
  'Abidjan, CI':'Abidjan, CI',

  /* ── NAV CTA ────────────────────────────────────── */
  'Consultation offerte':'Free Consultation',
  'Devis Gratuit':'Free Quote',

  /* ── PROMO BANNER ───────────────────────────────── */
  '🎁 Premier échange offert · Diagnostic gratuit · Sans engagement':'🎁 First consultation free · Free diagnosis · No obligation',
  'Prendre rendez-vous →':'Book an appointment →',

  /* ── HERO SECTION ───────────────────────────────── */
  'Comptabilité · Fiscalité · Gestion d\'Entreprise · Abidjan, CI':'Accounting · Taxation · Business Management · Abidjan, CI',
  'Passez d\'une gestion approximative<br>à une gestion <span>maîtrisée</span>':'Move from approximate management<br>to <span>mastered</span> management',
  'Passez d\'une gestion approximative à une gestion maîtrisée':'Move from approximate to mastered management',
  'maîtrisée':'mastered',
  'Deleky\'s accompagne les entreprises en comptabilité, fiscalité et gestion financière, tout en intégrant une approche en gestion des risques et analyse de données pour sécuriser et optimiser leur performance.':'Deleky\'s supports businesses in accounting, taxation and financial management, integrating a risk management and data analysis approach to secure and optimize their performance.',
  'Consultation Gratuite':'Free Consultation',
  'Découvrir le Cabinet':'Discover the Firm',
  'Expertise comptable & fiscale':'Accounting & Tax Expertise',
  'Approche orientée performance':'Performance-oriented approach',
  'PME, startups et groupes':'SMEs, startups and groups',
  'Voir plus':'See more',
  'En savoir plus':'Learn more',
  'Réponse en 5 min':'Response in 5 min',
  'Tableau de Bord Client':'Client Dashboard',
  'Kouamé & Associés SARL':'Kouamé & Associés LLC',
  'Client depuis 3 ans · Abidjan':'Client for 3 years · Abidjan',
  'À jour':'Up to date',
  'Défaut paie':'Payroll default',
  'Charge fiscale':'Tax burden',
  'Délai bilan':'Report deadline',
  'Services Actifs':'Active Services',
  'Gestion de Paie':'Payroll Management',
  'Comptabilité SYSCOHADA':'SYSCOHADA Accounting',
  'Audit de Conformité':'Compliance Audit',
  'Actif':'Active',
  'Planifié':'Planned',
  'Économie réalisée':'Savings achieved',
  'Optimisation fiscale · Exercice 2024':'Tax optimization · Fiscal Year 2024',
  'clients font confiance à Deleky\'s':'clients trust Deleky\'s',
  'entreprises clientes':'client companies',
  'Google':'Google',
  'stars':'stars',
  '★★★★★':'★★★★★',

  /* ── SOCIAL PROOF BAR ──────────────────────────── */
  'Comptabilité fiabilisée':'Reliable accounting',
  'Fiscalité optimisée':'Optimized taxation',
  'Performance pilotée':'Performance driven',
  'Risques maîtrisés':'Risks controlled',
  'Décisions éclairées':'Informed decisions',

  /* ── HOW IT WORKS ──────────────────────────────── */
  'Votre Réalité Aujourd\'hui':'Your Reality Today',
  'Avez-vous Réellement le <span>Contrôle</span> ?':'Do You Really Have <span>Control</span> ?',
  'Beaucoup d\'entreprises donnent l\'impression d\'être bien structurées. Pourtant, leur gestion repose souvent sur des bases fragiles.':'Many businesses appear well-structured, yet their management often rests on fragile foundations.',
  'Données financières peu fiables':'Unreliable financial data',
  'Vos chiffres sont difficiles à exploiter. Vos états financiers ne reflètent pas la réalité — et les décisions stratégiques reposent sur des bases fragiles.':'Your figures are hard to use. Your financial statements don\'t reflect reality — and strategic decisions rest on shaky ground.',
  'Fiscalité subie, non optimisée':'Endured taxation, not optimized',
  'Vous payez vos impôts sans certitude qu\'ils sont calculés et optimisés dans le respect de la réglementation. Chaque exercice est une occasion manquée.':'You pay taxes without certainty they\'re calculated and optimized. Each fiscal year is a missed opportunity.',
  'Absence de pilotage réel':'Lack of real steering',
  'Les décisions sont prises sans visibilité claire sur la performance. Vous gérez à l\'instinct plutôt qu\'avec des données fiables et exploitables.':'Decisions are made without clear visibility. You manage by instinct rather than with reliable data.',
  'Sans système structuré, vous ne pilotez pas votre entreprise.':'Without a structured system, you don\'t steer your business.',
  'Vous la subissez.':'You endure it.',

  /* ── SERVICES SECTION ──────────────────────────── */
  'Notre Approche':'Our Approach',
  'Une Gestion Financière Structurée, Optimisée et <span>Maîtrisée</span>':'Structured, Optimized and <span>Mastered</span> Financial Management',
  'Deleky\'s ne se limite pas à produire des états financiers. Nous mettons en place un système complet qui vous permet de structurer, fiabiliser, optimiser et piloter votre performance.':'Deleky\'s doesn\'t just produce financial statements. We implement a complete system to structure, secure, optimize and drive your performance.',
  'Structuration Financière':'Financial Structuring',
  'Populaire':'Popular',
  'Nous mettons en place des bases solides pour une gestion fiable et durable : tenue comptable SYSCOHADA rigoureuse, flux financiers organisés et données fiabilisées.':'We build solid foundations for reliable, sustainable management: rigorous SYSCOHADA accounting, organized financial flows and reliable data.',
  'Tenue comptable SYSCOHADA':'SYSCOHADA bookkeeping',
  'Fiabilisation des données financières':'Financial data reliability',
  'États financiers conformes et exploitables':'Compliant and usable financial statements',
  'Reporting mensuel structuré':'Structured monthly reporting',
  'Optimisation Fiscale':'Tax Optimization',
  'Nous pilotons votre fiscalité pour réduire légalement vos charges dans le strict respect de la réglementation ivoirienne. Moins d\'impôts, plus de marges, zéro risque fiscal.':'We manage your taxation to legally reduce your costs, in full compliance with Ivorian regulations. Less taxes, more margins, zero tax risk.',
  'Déclarations TVA, IS, IRVM optimisées':'Optimized VAT, CIT, IRVM declarations',
  'Audit fiscal préventif':'Preventive tax audit',
  'Réduction légale de la charge fiscale':'Legal reduction of tax burden',
  'Accompagnement DGI et contrôles fiscaux':'DGI support and tax audits',
  'Pilotage de Performance':'Performance Management',
  'Nous transformons vos chiffres en outils de décision. KPIs clairs, reporting exploitable et accompagnement stratégique pour piloter votre croissance avec précision.':'We turn your numbers into decision-making tools. Clear KPIs, actionable reporting and strategic support to steer your growth with precision.',
  'KPIs et tableaux de bord sur mesure':'Custom KPIs and dashboards',
  'Analyse de rentabilité et de performance':'Profitability and performance analysis',
  'Prévisions et budgets financiers':'Financial forecasts and budgets',
  'Aide à la décision basée sur les données':'Data-driven decision support',
  'Sécurisation & Conformité':'Security & Compliance',
  'En support de nos missions comptables et fiscales, nous intégrons une lecture des risques pour sécuriser votre activité — une couche de protection intégrée à votre gestion.':'Supporting our accounting and tax services, we integrate risk assessment to secure your business — a protection layer built into your management.',
  'Identification des risques financiers':'Identification of financial risks',
  'Audit de conformité comptable':'Accounting compliance audit',
  'Contrôle interne adapté PME':'Internal control adapted for SMEs',
  'Analyse de données opérationnelles':'Operational data analysis',

  /* ── ADVISORY DEPARTMENT ───────────────────────── */
  'Deleky\'s Advisory':'Deleky\'s Advisory',
  'Risque, Conformité &amp;<br>Analyse des Données':'Risk, Compliance &amp;<br>Data Analysis',
  'En complément de nos missions comptables et fiscales, ce département spécialisé accompagne les institutions financières, fintechs et entreprises à enjeux réglementaires dans la maîtrise de leurs risques et la conformité.':'Complementing our accounting and tax services, this specialized department supports financial institutions, fintechs and regulated companies in managing their risks and compliance.',
  'Nous contacter':'Contact us',
  'Gestion des Risques &amp; Conformité Bancaire':'Risk Management &amp; Banking Compliance',
  'Mise en conformité BSA / AML / LCB-FT':'BSA / AML / CFT compliance',
  'Politiques et procédures de conformité':'Compliance policies and procedures',
  'KYC / KYB — Know Your Customer / Business':'KYC / KYB',
  'Monitoring des transactions':'Transaction monitoring',
  'Reporting réglementaire':'Regulatory reporting',
  'Conformité Réglementaire BCEAO &amp; Autres':'BCEAO Regulatory Compliance &amp; Others',
  'Obtention de licences — EME, SFD, fintech':'License acquisition — EMI, MFI, fintech',
  'Diagnostic de conformité':'Compliance diagnostic',
  'Préparation aux inspections réglementaires':'Regulatory inspection preparation',
  'Dispositifs de contrôle interne':'Internal control systems',
  'Gestion des Risques':'Risk Management',
  'Cartographie des risques':'Risk mapping',
  'Risques opérationnels et financiers':'Operational and financial risks',
  'Indicateurs de suivi — KRI':'Monitoring indicators — KRIs',
  'Dispositifs d\'alerte':'Alert systems',
  'Analyse des Données &amp; Scoring':'Data Analysis &amp; Scoring',
  'Modèles de scoring pour prêts bancaires':'Scoring models for bank loans',
  'Analyse comportementale des clients':'Customer behavioral analysis',
  'Analyse de portefeuille &amp; reporting':'Portfolio analysis &amp; reporting',
  'Détection des anomalies et comportements à risque':'Anomaly and risk behavior detection',
  'Service complémentaire spécialisé':'Specialized complementary service',
  'Ce département intervient en renfort de nos missions comptables et fiscales, avec une expertise dédiée aux enjeux réglementaires des institutions financières et fintechs.':'This department supports our accounting and tax services with dedicated expertise in regulatory matters for financial institutions and fintechs.',

  /* ── WHO WE SERVE ─────────────────────────────── */
  'Des Solutions Adaptées':'Tailored Solutions',
  'Des Solutions Adaptées à <span>Votre Réalité</span>':'Tailored Solutions for <span>Your Reality</span>',
  'Chaque entreprise a ses enjeux propres. Nous adaptons notre approche à votre secteur, votre stade de développement et vos objectifs.':'Every business has its own challenges. We adapt our approach to your sector, stage of development and goals.',
  'PME & Entreprises en Croissance':'SMEs & Growing Businesses',
  'Structurez votre gestion, fiabilisez vos données et sécurisez votre croissance avec une comptabilité rigoureuse et une fiscalité optimisée.':'Structure your management, secure your data and protect your growth with rigorous accounting and optimized taxation.',
  'Structurer mon entreprise':'Structure my business',
  'Startups & Fintechs':'Startups & Fintechs',
  'Pilotez votre croissance avec rigueur. Des bases comptables solides et un reporting adapté aux investisseurs pour accélérer en toute confiance.':'Drive your growth with rigor. Solid accounting foundations and investor-ready reporting to accelerate with confidence.',
  'Structurer ma croissance':'Structure my growth',
  'Groupes & Investisseurs':'Groups & Investors',
  'Sécurisez vos opérations et vos investissements avec une approche consolidée, un pilotage multi-entités et une gestion des risques intégrée.':'Secure your operations and investments with a consolidated approach, multi-entity management and integrated risk management.',
  'Structurer mes investissements':'Structure my investments',
  'Institutions Financières &amp; Fintechs':'Financial Institutions &amp; Fintechs',
  'Gestion des risques, conformité réglementaire BCEAO/AML et analyse de données pour sécuriser vos opérations et satisfaire vos exigences réglementaires.':'Risk management, BCEAO/AML regulatory compliance and data analysis to secure your operations and meet regulatory requirements.',
  'Sécuriser mes opérations':'Secure my operations',
  'Structuration':'Structuring','Optimisation':'Optimization',
  'Pilotage':'Steering',
  'Croissance rapide':'Rapid growth',
  'Reporting':'Reporting',
  'Investisseurs':'Investors',
  'Consolidation':'Consolidation',
  'Sécurisation':'Securing',
  'Multi-entités':'Multi-entity',
  'Conformité':'Compliance',
  'AML/KYC':'AML/KYC',
  'Data':'Data',

  /* ── PRODUCTS (METHOD) ─────────────────────────── */
  'Notre Méthode':'Our Method',
  'Une Approche Structurée, <span>Orientée Résultats</span>':'A Structured, <span>Results-Oriented</span> Approach',
  'Une gestion maîtrisée repose sur une méthode claire et une exécution rigoureuse. Voici comment nous travaillons à vos côtés.':'Mastered management relies on a clear method and rigorous execution. Here\'s how we work alongside you.',
  'Diagnostic':'Diagnostic',
  'Point de départ · Offert':'Starting point · Free',
  'Nous analysons votre situation financière, comptable et fiscale pour identifier les zones de risque, les opportunités d\'optimisation et définir les priorités d\'action.':'We analyze your financial, accounting and tax situation to identify risks, optimization opportunities and define action priorities.',
  'Audit de l\'état comptable actuel':'Audit of current accounting state',
  'Identification des risques et opportunités':'Risk and opportunity identification',
  'Plan d\'action concret et priorisé':'Concrete prioritized action plan',
  'Demander mon diagnostic':'Request my diagnostic',
  'Structuration':'Structuring',
  'Mise en place · 2 à 4 semaines':'Setup · 2 to 4 weeks',
  'Nous mettons en place les bases d\'une gestion solide : tenue comptable rigoureuse, organisation des flux financiers et fiabilisation de vos données.':'We establish the foundations of solid management: rigorous bookkeeping, organized financial flows and data reliability.',
  'Mise en conformité SYSCOHADA':'SYSCOHADA compliance setup',
  'Organisation et fiabilisation des données':'Data organization and reliability',
  'Processus et outils adaptés à votre taille':'Processes and tools adapted to your size',
  'Structurer ma gestion':'Structure my management',
  'Optimisation Fiscale':'Tax Optimization',
  'Réduction légale des charges':'Legal cost reduction',
  'Nous analysons votre charge fiscale et mettons en œuvre les leviers d\'optimisation dans le strict respect de la réglementation ivoirienne.':'We analyze your tax burden and implement optimization levers in full compliance with Ivorian regulations.',
  'Audit fiscal et identification des leviers':'Tax audit and leverage identification',
  'Stratégie fiscale personnalisée':'Personalized tax strategy',
  'Suivi déclaratif complet DGI':'Complete DGI filing monitoring',
  'Optimiser ma fiscalité':'Optimize my taxation',
  'Pilotage & Reporting':'Steering & Reporting',
  'Performance en temps réel':'Real-time performance',
  'Nous transformons vos chiffres en outils de décision. Des indicateurs clairs, un reporting exploitable et des réunions de suivi pour piloter avec précision.':'We turn your numbers into decision tools. Clear indicators, actionable reporting and follow-up meetings for precise steering.',
  'Tableaux de bord KPIs personnalisés':'Custom KPI dashboards',
  'Analyse des écarts et tendances':'Variance and trend analysis',
  'Accompagnement décisionnel mensuel':'Monthly decision-support',
  'Piloter ma performance':'Drive my performance',

  /* ── TESTIMONIALS ──────────────────────────────── */
  'Ils Nous Font Confiance':'They Trust Us',
  'Des Résultats Concrets, <span>Pas des Promesses</span>':'Concrete Results, <span>Not Promises</span>',
  '"Depuis que Deleky\'s gère notre comptabilité et notre fiscalité, nous avons réduit notre charge fiscale de 18% et nos données financières sont enfin fiables. On prend des décisions avec confiance."':'"Since Deleky\'s handles our accounting and taxation, we\'ve reduced our tax burden by 18% and our financial data is finally reliable. We make decisions with confidence."',
  '"Deleky\'s a mis de l\'ordre dans notre gestion dès le départ. Structure comptable claire, fiscalité optimisée, reporting mensuel. On sait exactement où on en est à tout moment."':'"Deleky\'s put order into our management from the start. Clear accounting structure, optimized taxation, monthly reporting. We know exactly where we stand at all times."',
  '"Ce qui nous a convaincus, c\'est l\'approche intégrée de Deleky\'s : comptabilité, fiscalité et analyse de risques en un seul cabinet. On ne subit plus notre gestion — on la pilote."':'"What convinced us was Deleky\'s integrated approach: accounting, taxation and risk analysis in one firm. We no longer endure our management — we steer it."',
  'Directeur Général, Transport Express CI':'CEO, Transport Express CI',
  'Co-fondatrice, Agro-CI SARL':'Co-founder, Agro-CI LLC',
  'DAF, Groupe Immobilier Abidjan':'CFO, Abidjan Real Estate Group',

  /* ── CTA BAND ──────────────────────────────────── */
  'Prenez le Contrôle de Votre Gestion Dès Aujourd\'hui':'Take Control of Your Management Today',
  'Échangeons sur vos enjeux et identifions ensemble les premières pistes d\'amélioration. Premier échange offert.':'Let\'s discuss your challenges and identify first improvement areas together. First meeting free.',
  'Parler à un Expert':'Talk to an Expert',
  '📞 Nous contacter':'📞 Contact us',
  '💬 WhatsApp':'💬 WhatsApp',

  /* ── QUOTE FORM ────────────────────────────────── */
  'Premier Échange Offert':'First Meeting Free',
  'Prenez le Contrôle de Votre Gestion':'Take Control of Your Management',
  'Échangeons sur vos enjeux. Notre expert analyse votre situation et vous propose un plan d\'action concret, sans engagement.':'Let\'s discuss your challenges. Our expert analyzes your situation and proposes a concrete action plan, with no obligation.',
  'Premier échange offert — Analyse de votre situation sans frais':'First meeting free — Analysis of your situation at no cost',
  'Réponse rapide — Un expert vous contacte dans la journée':'Quick response — An expert contacts you within the day',
  'Confidentiel — Vos informations restent strictement privées':'Confidential — Your information remains strictly private',
  'Sans engagement — Plan d\'action concret dès le 1er échange':'No obligation — Concrete action plan from the first meeting',
  'Diagnostic Gratuit':'Free Diagnosis',
  '250+ entreprises accompagnées · 4.2/5 Google':'250+ companies served · 4.2/5 Google',
  'Prénom':'First Name',
  'Nom':'Last Name',
  'Téléphone':'Phone',
  'Email':'Email',
  'Votre Besoin':'Your Need',
  'Structuration financière':'Financial structuring',
  'Optimisation fiscale':'Tax optimization',
  'Pilotage de performance':'Performance management',
  'Gestion de la paie':'Payroll management',
  'Gestion des risques':'Risk management',
  'Autre besoin':'Other need',
  'Obtenir Mon Devis Gratuit':'Get My Free Quote',
  'Premier échange offert · Réponse rapide · Confidentiel · Sans engagement':'First meeting free · Quick response · Confidential · No obligation',

  /* ── NEWSLETTER ────────────────────────────────── */
  'La Lettre des Dirigeants qui Maîtrisent leur Gestion':'The Newsletter for Leaders Who Master Their Management',
  'Chaque mois : actualités fiscales, conseils de gestion et analyses pour piloter votre entreprise avec plus de clarté.':'Each month: tax news, management tips and analysis to steer your business with greater clarity.',
  'S\'abonner':'Subscribe',

  /* ── FOOTER ────────────────────────────────────── */
  'Comptabilité · Fiscalité · Gestion d\'Entreprise<br>Abidjan, Côte d\'Ivoire':'Accounting · Taxation · Business Management<br>Abidjan, Ivory Coast',
  'Votre partenaire comptable et fiscal de confiance.':'Your trusted accounting and tax partner.',
  'Services':'Services',
  'Création d\'Entreprise':'Business Creation',
  'Gestion de Paie':'Payroll Management',
  'Comptabilité & Audit':'Accounting & Audit',
  'Conseil Fiscal':'Tax Advisory',
  'Liens Rapides':'Quick Links',
  'Cabinet':'The Firm',
  'Témoignages':'Testimonials',
  'Blog':'Blog',
  'Contactez-Nous':'Contact Us',
  'Plateau, Abidjan, Côte d\'Ivoire':'Plateau, Abidjan, Ivory Coast',
  '+225 07 00 05 88':'+225 07 00 05 88',
  'contact@delekys.ci':'contact@delekys.ci',
  'Lun–Ven : 08h00–17h00':'Mon–Fri: 8:00 AM–5:00 PM',
  '© 2025 Deleky\'s SARL. Tous droits réservés.':'© 2025 Deleky\'s SARL. All rights reserved.',
  'Plan du site':'Sitemap',
  'Mentions légales':'Legal Notice',
  'Politique de confidentialité':'Privacy Policy',

  /* ── CABINET PAGE ──────────────────────────────── */
  'Qui Sommes-Nous ?':'Who Are We?',
  'Notre Cabinet':'Our Firm',
  'Une équipe de professionnels dédiés, spécialisés en gestion d\'entreprise, finance, comptabilité et gestion des risques.':'A team of dedicated professionals, specialized in business management, finance, accounting and risk management.',
  'Années d\'Expérience':'Years of Experience',
  'Entreprises Servies':'Businesses Served',
  'Années d\'Expertise':'Years of Expertise',
  'Clients Satisfaits':'Satisfied Clients',
  'Délai de Réponse':'Response Time',
  'Pays Servis':'Countries Served',
  'Secteurs':'Sectors',
  'Projets Réalisés':'Projects Completed',

  /* ── MISSIONS PAGE ─────────────────────────────── */
  '4 Domaines d\'Expertise au Service de Votre Croissance':'4 Areas of Expertise Serving Your Growth',
  'De la création d\'entreprise à la gestion des risques, DELEKY\'S SARL vous accompagne avec une expertise pluridisciplinaire.':'From business creation to risk management, DELEKY\'S SARL supports you with multidisciplinary expertise.',
  'Conseil en Innovation Entrepreneuriale':'Entrepreneurial Innovation Consulting',
  'Accompagnement de la création d\'entreprise, recherche de financement et développement stratégique.':'Business creation support, funding research and strategic development.',
  'Comptabilité & Gestion Financière':'Accounting & Financial Management',
  'Tenue de comptabilité SYSCOHADA, déclarations fiscales et analyse financière.':'SYSCOHADA bookkeeping, tax declarations and financial analysis.',
  'Gestion des Risques & Data Analytics':'Risk Management & Data Analytics',
  'Cartographie des risques, audit interne et exploitation des données.':'Risk mapping, internal audit and data exploitation.',
  'Conseil & Gestion de la Paie':'Payroll Consulting & Management',
  'Traitement des bulletins de paie, gestion RH et formation paie ivoirienne.':'Payroll processing, HR management and Ivorian payroll training.',

  /* ── CONTACT PAGE ──────────────────────────────── */
  'Riviera Golf, Cocody, Abidjan, Côte d\'Ivoire':'Riviera Golf, Cocody, Abidjan, Ivory Coast',
  'Horaires':'Hours',
  'Lun–Ven : 08h00–17h00':'Mon–Fri: 8:00 AM–5:00 PM',

  /* ── SECTEUR PAGES ─────────────────────────────── */
  'Secteur':'Sector',

  /* ── ADMIN ──────────────────────────────────────── */
  'Tableau de bord':'Dashboard',
  'Vue d\'ensemble':'Overview',
  'Hero · Stats · Services':'Hero · Stats · Services',
  'Présentation · Stats':'Presentation · Stats',
  '4 domaines d\'intervention':'4 areas of expertise',
  'Téléphone · Adresse · Email':'Phone · Address · Email',
  'Membres · Photos · Bios':'Members · Photos · Bios',
  'Upload et gestion des images':'Upload and image management',
  'Bandeau défilant':'Scrolling banner',
  'Palette de couleurs':'Color palette',
  'Activer / masquer':'Enable / hide',
  'Facebook · LinkedIn · etc.':'Facebook · LinkedIn · etc.',
  'Contacts & Infos':'Contacts & Info',
  'Contact & Infos':'Contact & Info',
  'Équipe':'Team',
  'Photos & Médias':'Photos & Media',
  'Actualités':'News',
  'Couleurs & Design':'Colors & Design',
  'Sections visibles':'Visible Sections',
  'Réseaux Sociaux':'Social Networks',
  'Administration':'Administration',
  'Interface d\'administration':'Admin Interface',
  'Administrateur':'Administrator',
  'Deleky\'s SARL':'Deleky\'s SARL',
  'Vue d\'ensemble':'Overview',
  'Pages du site':'Site Pages',
  'Paramètres':'Settings',
  'Prévisualiser':'Preview',
  'Sauvegarder':'Save',
  'Modifications sauvegardées !':'Changes saved!',
  'Enregistrer':'Save',
  'Enregistrer les modifications':'Save changes',
  'Réinitialiser':'Reset',

  /* ── ARTICLES / BLOG ───────────────────────────── */
  'Article publié':'Published article',
  'Lire l\'article':'Read article',
  'Lire la suite':'Read more',

  /* ── CREATION PAGES ────────────────────────────── */
  'Création de SARL':'SARL Creation',
  'Création de SAS':'SAS Creation',
  'Création de SAS':'SAS Creation',
  'Création de SCI':'SCI Creation',
  'Création de GIE':'GIE Creation',
  'Création de SA':'SA Creation',
  'Création de SNC':'SNC Creation',
  'Création de SCS':'SCS Creation',
  'Création d\'Entreprise':'Business Creation',
  'Création de Représentation':'Representation Creation',

  /* ── LOGIN ──────────────────────────────────────── */
  'Se connecter':'Log in',
  'Mot de passe':'Password',
  'Identifiant':'Username',
  'Email ou identifiant':'Email or username',
  'Se souvenir de moi':'Remember me',
  'Mot de passe oublié ?':'Forgot password?',
  'Pas encore de compte ?':'No account yet?',
  'S\'inscrire':'Sign up',

  /* ── JOIN US ────────────────────────────────────── */
  'Nous Rejoindre':'Join Us',
  'Postuler':'Apply',
  'Envoyer ma candidature':'Send my application',
  'Offres disponibles':'Available positions',

  /* ── EXPLORER ───────────────────────────────────── */
  'Explorer':'Explore',
  'Tout voir':'See all',

  /* ── RESSOURCES ─────────────────────────────────── */
  'Documents Utiles':'Useful Documents',
  'Calculateurs':'Calculators',
  'Partenariat':'Partnership',

  /* ── POPUP ──────────────────────────────────────── */
  'Besoin d\'un Expert Comptable ?':'Need an Accounting Expert?',
  'Besoin d\'aide ?':'Need help?',
  'Rappel gratuit — nos experts vous contactent pour répondre à toutes vos questions.':'Free callback — our experts will contact you to answer all your questions.',
  'Me faire rappeler':'Call me back',
  'Nous vous rappelons <strong>dans les 5 minutes</strong> — Données confidentielles':'We\'ll call you back <strong>within 5 minutes</strong> — Confidential data',
  'Prénom & Nom':'First & Last Name',
  'Votre entreprise':'Your company',
  'Numéro de téléphone':'Phone number',
  'Sujet':'Subject',
  'Comptabilité & États Financiers':'Accounting & Financial Statements',
  'Fiscalité & Déclarations':'Taxation & Declarations',
  'Optimisation Fiscale':'Tax Optimization',
  'Audit & Contrôle Interne':'Audit & Internal Control',
  'Création d\'Entreprise':'Business Creation',
  'Conformité BCEAO / AML':'BCEAO / AML Compliance',
  'Autre question':'Other question',
  'Demande <span>envoyée !</span>':'Request <span>sent!</span>',
  'Un expert vous rappelle dans les 5 minutes.':'An expert will call you back within 5 minutes.',
  'Demande reçue !':'Request received!',
  'Un expert Deleky\'s vous rappelle':'A Deleky\'s expert will call you back',
  'dans les 5 minutes':'within 5 minutes',
  'En attendant :':'In the meantime:',
  'Envoyer un message détaillé':'Send a detailed message',
  'Explorer nos ressources gratuites':'Explore our free resources',
  'Fermer':'Close',
  'Envoi...':'Sending...',

  /* ── NEWS / TICKER ─────────────────────────────── */
  'NEWS':'NEWS',
  'Nouveau —':'New —',
  'Service en ligne —':'Online service —',
  'Rappel —':'Reminder —',
  'La Réforme ITS 2024 : ce que vous devez savoir':'The ITS 2024 Reform: what you need to know',
  'Gérez votre paie en toute conformité':'Manage your payroll in full compliance',
  'Primes de fin d\'année (PFA) : la période approche':'Year-end bonuses: the season approaches',
  'Notre guide':'Our guide',
};

/* ── STATE ────────────────────────────────────────── */
let _currentLang = 'fr';

/* ── Get translation ──────────────────────────────── */
function t(french) {
  if (_currentLang === 'fr') return french;
  const en = TRANSLATIONS[french];
  if (en === undefined) {
    console.warn('[deleky-lang] Missing translation for: "' + french + '"');
    return french;
  }
  return en;
}

/* ── Apply current language to DOM ────────────────── */
function applyLang() {
  const walker = document.createTreeWalker(
    document.body,
    NodeFilter.SHOW_TEXT,
    null,
    false
  );
  const nodesToProcess = [];
  while (walker.nextNode()) {
    const node = walker.currentNode;
    const text = node.textContent.trim();
    if (!text) continue;
    const parent = node.parentElement;
    if (!parent) continue;
    if (parent.tagName === 'SCRIPT' || parent.tagName === 'STYLE') continue;
    if (parent.hasAttribute('data-no-i18n')) continue;
    if (parent.closest('[data-no-i18n]')) continue;
    if (text.length < 2) continue;
    nodesToProcess.push(node);
  }

  nodesToProcess.forEach(node => {
    const originalText = node.textContent;
    const trimmed = originalText.trim();

    if (originalText in TRANSLATIONS && _currentLang === 'en') {
      node.textContent = originalText.replace(trimmed, TRANSLATIONS[trimmed] || trimmed);
    } else if (node.parentElement && _currentLang === 'fr' && node.parentElement.hasAttribute('data-fr')) {
      node.textContent = node.parentElement.getAttribute('data-fr');
    }
  });

  /* ── Handle elements with data-i18n ─────────── */
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.getAttribute('data-i18n');
    if (_currentLang === 'en') {
      if (!el.hasAttribute('data-fr')) {
        el.setAttribute('data-fr', el.textContent.trim());
      }
      const enText = TRANSLATIONS[key];
      if (enText) {
        el.textContent = enText;
      } else {
        console.warn('[deleky-lang] Missing translation for data-i18n key: "' + key + '"');
      }
    } else {
      const frText = el.getAttribute('data-fr');
      if (frText) {
        el.textContent = frText;
      }
    }
  });
}

/* ── Switch language ──────────────────────────────── */
function switchLang(lang) {
  _currentLang = lang;
  try { localStorage.setItem(STORAGE_KEY, lang); } catch(e) {}

  /* Update html lang attribute */
  document.documentElement.lang = lang === 'en' ? 'en' : 'fr';

  /* Update active button */
  document.querySelectorAll('.lang-btn').forEach(b => {
    b.classList.toggle('active', b.textContent.trim().toUpperCase() === lang.toUpperCase());
  });

  applyLang();
}

/* ── Init ──────────────────────────────────────────── */
function init() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === 'en' || saved === 'fr') {
      _currentLang = saved;
    }
  } catch(e) {}
  document.documentElement.lang = _currentLang === 'en' ? 'en' : 'fr';
  if (_currentLang === 'en') {
    applyLang();
    document.querySelectorAll('.lang-btn').forEach(b => {
      b.classList.toggle('active', b.textContent.trim().toUpperCase() === 'EN');
    });
  }
}

/* ── Override global switchLang if it exists ──────── */
if (typeof window.switchLang === 'undefined') {
  window.switchLang = switchLang;
}

/* ── Auto-init on DOM ready ───────────────────────── */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

/* ── Make switchLang globally available regardless ── */
window.delekyLang = { switchLang, init, applyLang, t, TRANSLATIONS, get currentLang() { return _currentLang; } };

})();
