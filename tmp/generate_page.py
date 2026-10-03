import os

html_content = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Aleksandr Sarkisian — Official Identity Hub & Master Directory</title>
  <meta name="description" content="Verified master index of intellectual property, academic citations, state company registrations, and official resources of Aleksandr Sarkisian (Саркисян Александр Давидович).">
  <meta name="author" content="Aleksandr Sarkisian">
  <link rel="canonical" href="https://aleksandrsarkisian.space/">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">

  <!-- Open Graph / Social -->
  <meta property="og:type" content="profile">
  <meta property="og:url" content="https://aleksandrsarkisian.space/">
  <meta property="og:title" content="Aleksandr Sarkisian — Official Identity Hub">
  <meta property="og:description" content="Verified master index of patents, academic citations, and official entities of Aleksandr Sarkisian.">
  <meta property="og:image" content="https://upload.wikimedia.org/wikipedia/commons/4/42/%D0%A1%D0%B0%D1%80%D0%BA%D0%B8%D1%81%D1%8F%D0%BD_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%94%D0%B0%D0%B2%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87.jpg">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">

  <!-- Typography: Cormorant Garamond (Editorial Luxury) + Inter (Precision Sans) + JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: "class",
      theme: {
        extend: {
          fontFamily: {
            serif: ["Cormorant Garamond", "Georgia", "serif"],
            sans: ["Inter", "system-ui", "sans-serif"],
            mono: ["JetBrains Mono", "monospace"],
          },
          colors: {
            obsidian: {
              950: "#040507",
              900: "#07090e",
              850: "#0c0f17",
              800: "#121722",
              700: "#1a2232",
              600: "#27334a",
            }
          }
        }
      }
    }
  </script>

  <!-- Complete Canonical Schema.org JSON-LD -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "ProfilePage",
        "@id": "https://aleksandrsarkisian.space/#profilepage",
        "url": "https://aleksandrsarkisian.space/",
        "name": "Aleksandr Sarkisian — Official Master Directory & Identity Hub",
        "isPartOf": {
          "@type": "WebSite",
          "@id": "https://aleksandrsarkisian.space/#website",
          "url": "https://aleksandrsarkisian.space/",
          "name": "Aleksandr Sarkisian Space"
        },
        "about": {
          "@id": "https://aleksandrsarkisian.space/#person"
        },
        "mainEntity": {
          "@id": "https://aleksandrsarkisian.space/#person"
        }
      },
      {
        "@type": "Person",
        "@id": "https://aleksandrsarkisian.space/#person",
        "name": "Aleksandr Sarkisian",
        "givenName": "Aleksandr",
        "familyName": "Sarkisian",
        "additionalName": "Davidovich",
        "alternateName": [
          "Саркисян Александр Давидович",
          "Александр Саркисян",
          "Ալեքսանդր Սարգսյան",
          "Aleksandr Sargsyan",
          "teduza"
        ],
        "birthDate": "2008-05-14",
        "url": "https://aleksandrsarkisian.space/",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/42/%D0%A1%D0%B0%D1%80%D0%BA%D0%B8%D1%81%D1%8F%D0%BD_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%94%D0%B0%D0%B2%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87.jpg",
        "jobTitle": "Founder, Director & Systems Architect",
        "description": "Founder and Director of M.A.R.S. COMPANION LLC, Inventor of sovereign offline voice artificial intelligence with sequential resource orchestration and semantic memory. Based in Kapan, Syunik Province, Armenia.",
        "nationality": {
          "@type": "Country",
          "name": "Republic of Armenia"
        },
        "homeLocation": {
          "@type": "Place",
          "name": "Kapan, Syunik Province, Armenia"
        },
        "worksFor": {
          "@type": "Organization",
          "@id": "https://company.teduza.com/#organization",
          "name": "M.A.R.S. COMPANION LLC"
        },
        "founder": {
          "@type": "Organization",
          "@id": "https://company.teduza.com/#organization"
        },
        "sameAs": [
          "https://www.google.com/search?kgmid=/g/11zyrqjbq9",
          "https://share.google/ewTTrgxnU5UzLJeWD",
          "https://www.wikidata.org/wiki/Q141447666",
          "https://commons.wikimedia.org/wiki/File:%D0%A1%D0%B0%D1%80%D0%BA%D0%B8%D1%81%D1%8F%D0%BD_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%94%D0%B0%D0%B2%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87.jpg",
          "https://sarkisian.teduza.com",
          "https://sarkisian.teduza.com/ru/",
          "https://teduza.com",
          "https://company.teduza.com",
          "https://why.teduza.com",
          "https://meet.teduza.com",
          "https://news.teduza.com",
          "https://orcid.org/0009-0007-6747-2634",
          "https://isni.org/isni/0000000530338018",
          "https://scholar.google.ru/citations?user=KVpNW_QAAAAJ",
          "https://www.webofscience.com/wos/author/record/QIT-7789-2026",
          "https://doi.org/10.5281/zenodo.20457487",
          "https://zenodo.org/records/20457488",
          "https://github.com/teduza",
          "https://devpost.com/sarkisian",
          "https://t.me/teduza",
          "https://futurium.ec.europa.eu/en/user/59082",
          "https://www.search-for-intellectual-property.service.gov.uk/GB2611463.7"
        ],
        "identifier": [
          {
            "@type": "PropertyValue",
            "propertyID": "Google Knowledge Graph",
            "name": "Google Knowledge Graph ID",
            "value": "/g/11zyrqjbq9",
            "url": "https://www.google.com/search?kgmid=/g/11zyrqjbq9"
          },
          {
            "@type": "PropertyValue",
            "propertyID": "Wikidata",
            "name": "Wikidata QID",
            "value": "Q141447666",
            "url": "https://www.wikidata.org/wiki/Q141447666"
          },
          {
            "@type": "PropertyValue",
            "propertyID": "ORCID",
            "name": "ORCID ID",
            "value": "0009-0007-6747-2634",
            "url": "https://orcid.org/0009-0007-6747-2634"
          },
          {
            "@type": "PropertyValue",
            "propertyID": "ISNI",
            "name": "International Standard Name Identifier",
            "value": "0000 0005 3033 8018",
            "url": "https://isni.org/isni/0000000530338018"
          },
          {
            "@type": "PropertyValue",
            "propertyID": "Web of Science ResearcherID",
            "name": "ResearcherID",
            "value": "QIT-7789-2026",
            "url": "https://www.webofscience.com/wos/author/record/QIT-7789-2026"
          },
          {
            "@type": "PropertyValue",
            "propertyID": "State Registry of Armenia",
            "name": "Company State Registration Code",
            "value": "999.110.1603426",
            "url": "https://www.e-register.am/"
          }
        ]
      }
    ]
  }
  </script>

  <style>
    :root {
      color-scheme: dark;
    }
    body {
      background-color: #040508;
      color: #e2e8f0;
      background-image: 
        radial-gradient(circle at 50% -10%, rgba(59, 130, 246, 0.12) 0%, transparent 60%),
        radial-gradient(circle at 10% 40%, rgba(217, 119, 6, 0.03) 0%, transparent 40%),
        radial-gradient(circle at 90% 80%, rgba(14, 165, 233, 0.03) 0%, transparent 50%);
      background-attachment: fixed;
    }
    
    .hairline-b { border-bottom: 1px solid rgba(255, 255, 255, 0.08); }
    .hairline-t { border-top: 1px solid rgba(255, 255, 255, 0.08); }
    .hairline-all { border: 1px solid rgba(255, 255, 255, 0.08); }

    .index-row {
      position: relative;
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    .index-row:hover {
      background: linear-gradient(90deg, rgba(255, 255, 255, 0.04) 0%, rgba(255, 255, 255, 0.01) 100%);
      padding-left: 0.75rem;
    }
    .index-row:hover .row-arrow {
      transform: translateX(4px);
      color: #ffffff;
    }
    .index-row:hover .row-title {
      color: #ffffff;
    }

    #spotlight {
      pointer-events: none;
      position: fixed;
      inset: 0;
      z-index: 1;
      background: radial-gradient(700px circle at var(--x, 50%) var(--y, 25%), rgba(255, 255, 255, 0.03), transparent 45%);
    }

    .custom-scrollbar::-webkit-scrollbar { width: 5px; }
    .custom-scrollbar::-webkit-scrollbar-track { background: #07090e; }
    .custom-scrollbar::-webkit-scrollbar-thumb { background: #1c2434; border-radius: 2px; }
  </style>
</head>
<body class="min-h-screen flex flex-col font-sans selection:bg-stone-200 selection:text-stone-900 relative">

  <!-- Interactive Spotlight -->
  <div id="spotlight"></div>

  <!-- Top Minimalist Bar -->
  <nav class="sticky top-0 z-40 hairline-b bg-[#040508]/90 backdrop-blur-xl">
    <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
      
      <!-- Brand & Canonical Pill -->
      <div class="flex items-center gap-3">
        <a href="/" class="group flex items-center gap-2.5">
          <span class="w-2 h-2 rounded-full bg-emerald-400 shadow-[0_0_8px_rgba(52,211,153,0.8)]"></span>
          <span class="font-mono text-xs tracking-wider uppercase text-slate-300 group-hover:text-white transition">aleksandrsarkisian.space</span>
        </a>
        <span class="text-white/20 text-xs hidden sm:inline">/</span>
        <span class="font-mono text-[11px] text-slate-500 hidden sm:inline tracking-wider">CANONICAL IDENTITY HUB</span>
      </div>

      <!-- Live Clock & Official KG Badge -->
      <div class="flex items-center gap-4">
        <!-- Live Clock in Kapan, Armenia -->
        <div class="hidden md:flex items-center gap-2 text-xs font-mono text-slate-400">
          <span class="w-1.5 h-1.5 rounded-full bg-amber-400/60"></span>
          <span>KAPAN, AM</span>
          <span id="kapanTime" class="text-slate-300 tabular-nums">16:15 GMT+4</span>
        </div>

        <!-- Google Knowledge Graph Direct Link -->
        <a href="https://www.google.com/search?kgmid=/g/11zyrqjbq9" target="_blank" rel="noopener noreferrer" 
           class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-white/[0.04] hover:bg-white/[0.08] hairline-all text-xs font-mono text-slate-300 hover:text-white transition group">
          <svg class="w-3.5 h-3.5 text-blue-400" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12.48 10.92v3.28h7.84c-.24 1.84-.853 3.187-1.787 4.133-1.147 1.147-2.933 2.4-6.053 2.4-4.827 0-8.6-3.893-8.6-8.72s3.773-8.72 8.6-8.72c2.6 0 4.507 1.027 5.907 2.347l2.307-2.307C18.747 1.44 16.133 0 12.48 0 5.867 0 .307 5.387.307 12s5.56 12 12.173 12c3.573 0 6.267-1.173 8.373-3.36 2.16-2.16 2.84-5.213 2.84-7.667 0-.76-.053-1.467-.173-2.053H12.48z"/>
          </svg>
          <span class="text-slate-400 group-hover:text-slate-200">KG: /g/11zyrqjbq9</span>
          <svg class="w-3 h-3 text-slate-500 group-hover:translate-x-0.5 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
        </a>

        <!-- Schema Modal Trigger -->
        <button onclick="toggleJsonLdModal()" class="text-xs font-mono text-slate-400 hover:text-white px-2.5 py-1.5 rounded-full hover:bg-white/5 transition" title="Inspect Schema.org JSON-LD">
          &lt;/&gt;
        </button>
      </div>

    </div>
  </nav>

  <!-- Hero Section: Editorial Luxury Presentation -->
  <main class="flex-grow max-w-6xl mx-auto px-6 py-12 lg:py-20 w-full relative z-10">

    <!-- Top Headline & Portrait Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-start pb-16 hairline-b">
      
      <!-- Left: Portrait in Fine Framing -->
      <div class="lg:col-span-4 flex flex-col items-center lg:items-start">
        <div class="relative group">
          <!-- Fine Frame Shadow & Glow -->
          <div class="absolute -inset-0.5 bg-gradient-to-b from-white/20 via-white/5 to-transparent rounded-2xl blur opacity-30 group-hover:opacity-60 transition duration-700"></div>
          
          <div class="relative w-56 h-72 sm:w-64 sm:h-80 rounded-2xl overflow-hidden bg-obsidian-900 hairline-all shadow-2xl">
            <img src="https://upload.wikimedia.org/wikipedia/commons/4/42/%D0%A1%D0%B0%D1%80%D0%BA%D0%B8%D1%81%D1%8F%D0%BD_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%94%D0%B0%D0%B2%D0%B8%D0%B4%D0%BE%D0%B2%D0%B8%D1%87.jpg" 
                 alt="Aleksandr Sarkisian"
                 class="w-full h-full object-cover object-top grayscale-[15%] group-hover:grayscale-0 group-hover:scale-105 transition-all duration-700 ease-out"
                 onerror="this.src='/logo.png'">
            
            <!-- Vignette gradient -->
            <div class="absolute inset-0 bg-gradient-to-t from-obsidian-950/80 via-transparent to-transparent"></div>
            
            <!-- Floating Verified Tag inside photo -->
            <div class="absolute bottom-3 left-3 right-3 flex items-center justify-between text-[11px] font-mono text-slate-300 bg-black/60 backdrop-blur-md px-3 py-1.5 rounded-lg hairline-all">
              <span class="flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
                VERIFIED CITIZEN & FOUNDER
              </span>
              <span class="text-slate-400">AM // 🇦🇲</span>
            </div>
          </div>
        </div>

        <!-- Quick Links beneath photo -->
        <div class="w-full max-w-[16rem] mt-6 flex flex-col gap-2">
          <a href="https://sarkisian.teduza.com" target="_blank" rel="noopener noreferrer" 
             class="w-full flex items-center justify-between px-4 py-2.5 rounded-xl bg-white/[0.04] hover:bg-white/[0.08] hairline-all text-xs font-medium text-slate-200 transition group">
            <span>Read Biography & CV</span>
            <svg class="w-3.5 h-3.5 text-slate-400 group-hover:text-white group-hover:translate-x-0.5 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
          </a>
          <button onclick="copyMasterUrl()" 
                  class="w-full flex items-center justify-center gap-2 px-4 py-2 rounded-xl text-slate-400 hover:text-slate-200 text-xs font-mono transition">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
            <span id="copyText">Copy Canonical URL</span>
          </button>
        </div>
      </div>

      <!-- Right: Grand Typographic Title & Credentials -->
      <div class="lg:col-span-8 flex flex-col justify-center text-left">
        
        <!-- Category Pill -->
        <div class="flex flex-wrap items-center gap-2 mb-4 font-mono text-xs">
          <span class="text-amber-400/90 tracking-wider uppercase font-semibold">PERSON DIRECTORY &bull; SOVEREIGN ENTITY</span>
          <span class="text-white/20">&bull;</span>
          <span class="text-slate-400">STATE REGISTRY #999.110.1603426</span>
        </div>

        <!-- Monumental Name -->
        <h1 class="font-serif text-5xl sm:text-6xl lg:text-7xl font-semibold tracking-tight text-white leading-[1.08] mb-4">
          Aleksandr Sarkisian
        </h1>

        <!-- Multilingual Sub-Identity -->
        <div class="flex flex-wrap items-baseline gap-x-4 gap-y-1 text-slate-400 text-base sm:text-lg font-light mb-6">
          <span class="text-slate-300 font-serif italic text-xl">Саркисян Александр Давидович</span>
          <span class="text-white/20 hidden sm:inline">&bull;</span>
          <span class="font-serif text-slate-400">Ալեքսանդր Դավիթի Սարգսյան</span>
        </div>

        <!-- Core Mission Definition -->
        <p class="text-base sm:text-lg text-slate-300/90 leading-relaxed font-light max-w-2xl mb-8">
          Systems architect, inventor, and founder of <strong class="text-white font-medium">M.A.R.S. COMPANION LLC</strong>. Author of the United Kingdom patent for autonomous offline voice AI with Sequential Resource Orchestration and private semantic long-term memory. Based in <span class="text-white font-medium">Kapan, Syunik Province, Republic of Armenia</span>.
        </p>

        <!-- The 4 Monolith Stats -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 w-full pt-6 hairline-t">
          <div class="p-3">
            <div class="font-mono text-xs text-slate-500 uppercase tracking-wider mb-1">UK Patents</div>
            <div class="font-serif text-2xl sm:text-3xl text-white font-semibold">07 <span class="text-xs font-mono font-normal text-emerald-400">REG</span></div>
          </div>

          <div class="p-3">
            <div class="font-mono text-xs text-slate-500 uppercase tracking-wider mb-1">CERN Zenodo</div>
            <div class="font-serif text-2xl sm:text-3xl text-white font-semibold">10.5281 <span class="text-xs font-mono font-normal text-cyan-400">DOI</span></div>
          </div>

          <div class="p-3">
            <div class="font-mono text-xs text-slate-500 uppercase tracking-wider mb-1">Wikidata</div>
            <div class="font-serif text-2xl sm:text-3xl text-white font-semibold">Q141447666</div>
          </div>

          <div class="p-3">
            <div class="font-mono text-xs text-slate-500 uppercase tracking-wider mb-1">Google KG</div>
            <div class="font-serif text-2xl sm:text-3xl text-white font-semibold">/g/11zyrqjbq9</div>
          </div>
        </div>

      </div>

    </div>

    <!-- Master Index Section (Swiss / Architectural Editorial Table) -->
    <div class="pt-16 pb-12">
      
      <!-- Section Header with Category Selector & Live Search -->
      <div class="flex flex-col md:flex-row md:items-end justify-between gap-6 mb-10 pb-6 hairline-b">
        <div>
          <span class="font-mono text-xs uppercase text-slate-500 tracking-widest block mb-2">VERIFIED MASTER INDEX</span>
          <h2 class="font-serif text-3xl sm:text-4xl text-white font-medium">Canonical Records & References</h2>
        </div>

        <!-- Filter Tabs & Search -->
        <div class="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
          <!-- Filter Buttons -->
          <div class="flex items-center gap-1 p-1 bg-obsidian-900 hairline-all rounded-xl text-xs font-mono">
            <button onclick="setFilter('all')" class="filter-tab px-3 py-1.5 rounded-lg text-white bg-white/10 active-tab transition" data-filter="all">All (17)</button>
            <button onclick="setFilter('ecosystem')" class="filter-tab px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition" data-filter="ecosystem">Official</button>
            <button onclick="setFilter('patents')" class="filter-tab px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition" data-filter="patents">Patents</button>
            <button onclick="setFilter('academic')" class="filter-tab px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition" data-filter="academic">Science</button>
            <button onclick="setFilter('authority')" class="filter-tab px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition" data-filter="authority">Registries</button>
          </div>

          <!-- Instant Search -->
          <div class="relative">
            <input type="text" id="masterSearch" oninput="applySearch()" placeholder="Filter records (e.g. patent, cern, kapan)..." 
                   class="bg-obsidian-900 hairline-all focus:border-white/30 rounded-xl px-3.5 py-1.5 pl-8 text-xs font-mono text-white placeholder-slate-500 focus:outline-none transition w-full sm:w-64">
            <svg class="w-3.5 h-3.5 text-slate-500 absolute left-2.5 top-2.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          </div>
        </div>
      </div>

      <!-- The Editorial Index Table -->
      <div id="indexContainer" class="flex flex-col">

        <!-- 01. sarkisian.teduza.com -->
        <a href="https://sarkisian.teduza.com" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="ecosystem" data-search="biography cv curriculum vitae sarkisian teduza com official narrative">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">01</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Official Biography & Curriculum Vitae</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">Biography</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Primary autobiographical record: Cadet military background (KMKVK), intellectual development, engineering philosophy, and architectural roots.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">sarkisian.teduza.com</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 02. company.teduza.com -->
        <a href="https://company.teduza.com" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="ecosystem" data-search="company mars companion llc corporate registry kapan syunik armenia">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">02</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">M.A.R.S. COMPANION LLC</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Corporate Entity</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Legal corporate headquarters of the autonomous AI enterprise. State registration in the Republic of Armenia #999.110.1603426.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">company.teduza.com</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 03. teduza.com -->
        <a href="https://teduza.com" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="ecosystem" data-search="teduza flagship offline voice ai product companion sovereign">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">03</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">M.A.R.S. Companion Flagship Product</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-white/10 text-slate-300 border border-white/15">Flagship Product</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Autonomous voice artificial intelligence operating with full sovereignty without telemetry, cloud dependency, or external surveillance.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">teduza.com</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 04. why.teduza.com -->
        <a href="https://why.teduza.com" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="ecosystem" data-search="why armenia kapan syunik strategic manifesto sovereignty">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">04</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Why Armenia & Why Kapan (Strategic Manifesto)</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">Manifesto</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                The philosophical and geopolitical rationale for establishing the deep tech sovereign research base in Kapan, Syunik Province.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">why.teduza.com</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 05. UK Patent GB2611463.7 -->
        <a href="https://www.search-for-intellectual-property.service.gov.uk/GB2611463.7" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="patents" data-search="patent gb2611463.7 uk ipo sequential resource orchestration semantic memory sro">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">05</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">UK Patent GB2611463.7 — Sequential Resource Orchestration</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">UK IPO Patent</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Registered United Kingdom intellectual property: Portable autonomous offline voice assistant with sequential orchestrator pipeline and hierarchical semantic memory.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-amber-400/90 font-medium">GB2611463.7</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 06. Patent Family Portfolio -->
        <a href="https://teduza.com/patents/" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="patents" data-search="patents gb2613965.9 gb2613966.7 gb2613968.3 gb2613969.1 gb2613970.9 gb2614145.7 portfolio">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">06</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">UK IPO Patent Portfolio (Family of 6 Patents)</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">Patent Family</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Family of acoustic vector extraction, edge speech recognition, and offline embedding patents (GB2613965.9 through GB2614145.7).
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">teduza.com/patents</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 07. Google Knowledge Graph -->
        <a href="https://www.google.com/search?kgmid=/g/11zyrqjbq9" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="authority" data-search="google knowledge graph panel search entity /g/11zyrqjbq9 disambiguation">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">07</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Google Knowledge Graph Entity</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">Google Knowledge Panel</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Official Google Search entity index for Aleksandr Sarkisian, certifying verified identity, founding roles, and disambiguated authority.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-blue-400">/g/11zyrqjbq9</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 08. Wikidata Entity Q141447666 -->
        <a href="https://www.wikidata.org/wiki/Q141447666" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="authority" data-search="wikidata q141447666 structured knowledge base semantic web">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">08</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Wikidata Entity Q141447666</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-red-500/10 text-red-400 border border-red-500/20">Wikidata</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Structured global knowledge graph entry connecting patents, citizenship, company founding, and international research identifiers.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">Q141447666</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 09. ORCID Identifier -->
        <a href="https://orcid.org/0009-0007-6747-2634" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="academic" data-search="orcid researcher id 0009-0007-6747-2634 scientific publishing">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">09</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">ORCID International Researcher Record</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Research ID</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Open Researcher and Contributor ID certifying authorship of scientific papers, preprints, and technological breakthroughs.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-emerald-400 font-mono">0009-0007-6747-2634</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 10. Zenodo / CERN DOI -->
        <a href="https://doi.org/10.5281/zenodo.20457487" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="academic" data-search="zenodo cern doi 10.5281/zenodo.20457487 preprint open science">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">10</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Zenodo (CERN) Open Science Publication</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">CERN DOI</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Cryptographically anchored open-access research publication hosted on CERN repositories under DOI 10.5281/zenodo.20457487.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-cyan-400 font-mono">10.5281/zenodo.20457487</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 11. Google Scholar Citations -->
        <a href="https://scholar.google.ru/citations?user=KVpNW_QAAAAJ" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="academic" data-search="google scholar citations kvpnw_qaaaaj metrics academic">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">11</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Google Scholar Citations Profile</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">Citations Profile</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Official Google Scholar index tracking academic citations, algorithmic papers, and references in decentralized voice processing.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">KVpNW_QAAAAJ</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 12. Web of Science -->
        <a href="https://www.webofscience.com/wos/author/record/QIT-7789-2026" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="academic" data-search="web of science clarivate analytics researcherid qit-7789-2026">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">12</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Web of Science ResearcherID (Clarivate)</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">Clarivate WoS</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Clarivate Analytics scientific record linking peer-reviewed articles, citations, and verified academic output.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">QIT-7789-2026</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 13. ISNI Authority Record -->
        <a href="https://isni.org/isni/0000000530338018" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="authority" data-search="isni international standard name identifier 0000 0005 3033 8018 authority">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">13</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">ISNI International Authority Record (ISO 27729)</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-slate-500/10 text-slate-300 border border-slate-500/20">ISO Certified</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                International Standard Name Identifier certifying public authorship and identity worldwide.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">0000 0005 3033 8018</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 14. Electronic Register of Armenia -->
        <a href="https://www.e-register.am/" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="authority" data-search="armenia electronic register ministry of justice 999.110.1603426 legal company registration">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">14</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">State Registry of Legal Entities of Armenia</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">Gov Registered</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Ministry of Justice of Armenia corporate registration #999.110.1603426 for M.A.R.S. COMPANION LLC (Kapan, Syunik).
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-emerald-400 font-mono">999.110.1603426</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 15. GitHub -->
        <a href="https://github.com/teduza" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="ecosystem" data-search="github teduza source code repositories git software engineering">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">15</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">GitHub Organization & Repositories (@teduza)</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-white/10 text-slate-300 border border-white/15">Open Source</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Open-source repositories, engineering tools, and offline voice AI architecture implementations.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">github.com/teduza</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 16. Telegram -->
        <a href="https://t.me/teduza" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="ecosystem" data-search="telegram teduza news channel broadcast updates">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">16</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">Official Telegram Channel (@teduza)</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">Direct Channel</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                Direct broadcasts, engineering logs, architectural notes, and public company statements.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">t.me/teduza</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

        <!-- 17. European Commission Futurium -->
        <a href="https://futurium.ec.europa.eu/en/user/59082" target="_blank" rel="noopener noreferrer" 
           class="index-row py-5 flex flex-col md:flex-row md:items-center justify-between gap-4 group"
           data-group="authority" data-search="european union commission futurium 59082 digital sovereignty ai policy">
          <div class="flex items-start md:items-center gap-4">
            <span class="font-mono text-xs text-slate-500 w-8 pt-0.5 md:pt-0">17</span>
            <div>
              <div class="flex items-center gap-2 mb-1">
                <h3 class="row-title text-base sm:text-lg font-medium text-slate-200 transition">European Commission Futurium Platform</h3>
                <span class="font-mono text-[10px] uppercase px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">EU Forum</span>
              </div>
              <p class="text-xs text-slate-400 font-light max-w-xl">
                European Commission digital stakeholder forum identity for tech sovereignty and AI policy dialogues.
              </p>
            </div>
          </div>
          <div class="flex items-center gap-4 self-end md:self-center font-mono text-xs text-slate-400">
            <span class="text-slate-500">User: 59082</span>
            <svg class="row-arrow w-4 h-4 text-slate-500 transition" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
          </div>
        </a>

      </div>

      <!-- No Results State -->
      <div id="noMatchState" class="hidden text-center py-16 text-slate-500 font-mono text-xs">
        [!] No records match the query. Try "patent", "scholar", "cern", or "kapan".
      </div>

    </div>

    <!-- Editorial Identity Citation Block -->
    <div class="mt-8 p-6 sm:p-8 rounded-2xl bg-obsidian-900 hairline-all flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
      <div>
        <span class="font-mono text-xs uppercase tracking-wider text-slate-500 block mb-1">CANONICAL DISAMBIGUATION NOTICE</span>
        <h4 class="font-serif text-xl sm:text-2xl text-white font-medium mb-1">Sarkisian Aleksandr Davidovich (b. May 14, 2008)</h4>
        <p class="text-xs text-slate-400 font-light max-w-2xl leading-relaxed">
          This portal constitutes the sole authoritative index for Aleksandr Sarkisian, Armenian AI inventor and founder of M.A.R.S. COMPANION LLC. It is distinct and independent from other individuals named Alex Sarkisian.
        </p>
      </div>
      <button onclick="toggleJsonLdModal()" 
              class="flex-shrink-0 px-4 py-2.5 rounded-xl bg-white/[0.05] hover:bg-white/[0.1] text-xs font-mono text-slate-200 hairline-all transition">
        View Schema.org Data &rarr;
      </button>
    </div>

  </main>

  <!-- Elegant Swiss Footer -->
  <footer class="hairline-t bg-[#040508] py-12 text-xs text-slate-500 relative z-10">
    <div class="max-w-6xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-6">
      <div class="flex items-center gap-3">
        <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
        <span>&copy; 2026 Aleksandr Sarkisian &bull; M.A.R.S. COMPANION LLC</span>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-6 font-mono text-[11px] text-slate-500">
        <a href="https://sarkisian.teduza.com" class="hover:text-slate-300 transition">sarkisian.teduza.com</a>
        <a href="https://company.teduza.com" class="hover:text-slate-300 transition">company.teduza.com</a>
        <a href="https://teduza.com" class="hover:text-slate-300 transition">teduza.com</a>
        <a href="https://why.teduza.com" class="hover:text-slate-300 transition">why.teduza.com</a>
      </div>
    </div>
  </footer>

  <!-- Schema.org Inspector Modal -->
  <div id="jsonModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-md hidden items-center justify-center p-4">
    <div class="bg-obsidian-900 hairline-all rounded-2xl max-w-2xl w-full max-h-[85vh] flex flex-col shadow-2xl overflow-hidden">
      <div class="p-4 hairline-b flex items-center justify-between">
        <div class="flex items-center gap-2 font-mono text-xs text-slate-300">
          <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
          <span>Schema.org JSON-LD (Canonical Person)</span>
        </div>
        <button onclick="toggleJsonLdModal()" class="text-slate-400 hover:text-white p-1 rounded-lg">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
        </button>
      </div>
      <div class="p-4 overflow-y-auto custom-scrollbar bg-obsidian-950 font-mono text-xs text-slate-300 leading-relaxed flex-grow">
        <pre><code id="jsonCode"></code></pre>
      </div>
      <div class="p-3 hairline-t flex items-center justify-between bg-obsidian-900">
        <span class="text-[11px] font-mono text-slate-500">Validated for Google Knowledge Graph</span>
        <button onclick="copySchema()" id="copySchemaBtn" class="px-3 py-1.5 rounded-lg bg-white/10 hover:bg-white/20 text-white text-xs font-mono transition">
          Copy JSON-LD
        </button>
      </div>
    </div>
  </div>

  <!-- Toast Notification -->
  <div id="toast" class="fixed bottom-6 right-6 z-50 transform translate-y-16 opacity-0 transition-all duration-300 bg-obsidian-850 hairline-all text-slate-200 px-4 py-2.5 rounded-xl shadow-2xl text-xs font-mono flex items-center gap-2">
    <svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
    <span id="toastText">Link copied to clipboard</span>
  </div>

  <!-- View Switcher to why.teduza.com -->
  <div class="fixed bottom-4 left-4 z-40 flex items-center gap-2 bg-obsidian-900/90 backdrop-blur-md hairline-all text-xs font-mono px-3 py-1.5 rounded-xl shadow-2xl">
    <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="text-slate-300 font-medium">aleksandrsarkisian.space</span>
    <span class="text-white/20">|</span>
    <a href="/why-teduza.html" class="text-slate-400 hover:text-white flex items-center gap-1 transition">
      <span>why.teduza.com</span>
      <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
    </a>
  </div>

  <script>
    // Spotlight cursor effect
    window.addEventListener("pointermove", (e) => {
      document.getElementById("spotlight").style.setProperty("--x", e.clientX + "px");
      document.getElementById("spotlight").style.setProperty("--y", e.clientY + "px");
    });

    // Kapan Armenia Clock
    function updateClock() {
      try {
        const now = new Date();
        const opts = { timeZone: "Asia/Yerevan", hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false };
        const timeStr = new Intl.DateTimeFormat([], opts).format(now);
        document.getElementById("kapanTime").innerText = timeStr + " (GMT+4)";
      } catch(e) {}
    }
    setInterval(updateClock, 1000);
    updateClock();

    // Category Tabs Filter
    function setFilter(cat) {
      document.querySelectorAll(".filter-tab").forEach(t => {
        if (t.getAttribute("data-filter") === cat) {
          t.classList.add("bg-white/10", "text-white");
          t.classList.remove("text-slate-400");
        } else {
          t.classList.remove("bg-white/10", "text-white");
          t.classList.add("text-slate-400");
        }
      });

      const rows = document.querySelectorAll(".index-row");
      let visible = 0;
      rows.forEach(r => {
        const group = r.getAttribute("data-group");
        if (cat === "all" || group === cat) {
          r.style.display = "flex";
          visible++;
        } else {
          r.style.display = "none";
        }
      });
      document.getElementById("masterSearch").value = "";
      document.getElementById("noMatchState").style.display = visible === 0 ? "block" : "none";
    }

    // Live Instant Search
    function applySearch() {
      const q = document.getElementById("masterSearch").value.toLowerCase().trim();
      const rows = document.querySelectorAll(".index-row");
      let visible = 0;
      rows.forEach(r => {
        const text = (r.getAttribute("data-search") || "") + " " + r.innerText.toLowerCase();
        if (!q || text.includes(q)) {
          r.style.display = "flex";
          visible++;
        } else {
          r.style.display = "none";
        }
      });
      document.getElementById("noMatchState").style.display = visible === 0 ? "block" : "none";
    }

    // Copy URL
    function copyMasterUrl() {
      navigator.clipboard.writeText("https://aleksandrsarkisian.space/").then(() => {
        showToast("https://aleksandrsarkisian.space/ copied");
        document.getElementById("copyText").innerText = "Copied to clipboard!";
        setTimeout(() => document.getElementById("copyText").innerText = "Copy Canonical URL", 2000);
      });
    }

    // Toast
    function showToast(msg) {
      const t = document.getElementById("toast");
      document.getElementById("toastText").innerText = msg;
      t.classList.remove("translate-y-16", "opacity-0");
      t.classList.add("translate-y-0", "opacity-100");
      setTimeout(() => {
        t.classList.add("translate-y-16", "opacity-0");
        t.classList.remove("translate-y-0", "opacity-100");
      }, 3000);
    }

    // Schema Modal
    function toggleJsonLdModal() {
      const modal = document.getElementById("jsonModal");
      if (modal.classList.contains("hidden")) {
        const s = document.querySelector('script[type="application/ld+json"]').innerText;
        document.getElementById("jsonCode").innerText = s.trim();
        modal.classList.remove("hidden");
        modal.classList.add("flex");
      } else {
        modal.classList.add("hidden");
        modal.classList.remove("flex");
      }
    }

    function copySchema() {
      const s = document.getElementById("jsonCode").innerText;
      navigator.clipboard.writeText(s).then(() => {
        const b = document.getElementById("copySchemaBtn");
        b.innerText = "Copied!";
        setTimeout(() => b.innerText = "Copy JSON-LD", 2000);
      });
    }
  </script>
</body>
</html>"""

for path in ["/app/applet/index.html", "/app/applet/space/index.html", "/tmp/aleksandrsarkisian.space/index.html"]:
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)

print("Saved elegant design to all targets!")
