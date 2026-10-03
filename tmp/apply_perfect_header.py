import os
import re

langs = [
    {'code': 'en', 'dir': '', 'prefix': '', 'whyArm': 'Why Armenia', 'whyKap': 'Why Kapan', 'proj': 'Project', 'proto': 'Prototype', 'cont': 'Contact', 'full': 'Full site ↗'},
    {'code': 'ru', 'dir': 'ru', 'prefix': '../', 'whyArm': 'Почему Армения', 'whyKap': 'Почему Капан', 'proj': 'Проект', 'proto': 'Прототип', 'cont': 'Контакты', 'full': 'Полная версия ↗'},
    {'code': 'hy', 'dir': 'hy', 'prefix': '../', 'whyArm': 'Ինչու Հայաստան', 'whyKap': 'Ինչու Կապան', 'proj': 'Նախագիծ', 'proto': 'Նախատիպ', 'cont': 'Կապ', 'full': 'Ամբողջական կայք ↗'},
    {'code': 'de', 'dir': 'de', 'prefix': '../', 'whyArm': 'Warum Armenien', 'whyKap': 'Warum Kapan', 'proj': 'Projekt', 'proto': 'Prototyp', 'cont': 'Kontakt', 'full': 'Zur Hauptseite ↗'},
    {'code': 'fr', 'dir': 'fr', 'prefix': '../', 'whyArm': 'Pourquoi l’Arménie', 'whyKap': 'Pourquoi Kapan', 'proj': 'Projet', 'proto': 'Prototype', 'cont': 'Contact', 'full': 'Site complet ↗'},
    {'code': 'zh', 'dir': 'zh', 'prefix': '../', 'whyArm': '为何选择亚美尼亚', 'whyKap': '为何选择卡潘', 'proj': '项目', 'proto': '原型', 'cont': '联系我们', 'full': '完整主站 ↗'},
    {'code': 'uk', 'dir': 'uk', 'prefix': '../', 'whyArm': 'Чому Вірменія', 'whyKap': 'Чому Капан', 'proj': 'Проєкт', 'proto': 'Прототип', 'cont': 'Контакти', 'full': 'Повна версія ↗'}
]

lang_labels = [
    {'code': 'en', 'label': 'EN', 'path': ''},
    {'code': 'ru', 'label': 'RU', 'path': 'ru/'},
    {'code': 'hy', 'label': 'HY', 'path': 'hy/'},
    {'code': 'de', 'label': 'DE', 'path': 'de/'},
    {'code': 'fr', 'label': 'FR', 'path': 'fr/'},
    {'code': 'zh', 'label': '中文', 'path': 'zh/'},
    {'code': 'uk', 'label': 'UA', 'path': 'uk/'}
]

def clean_and_update_html(content, lang_info):
    code = lang_info['code']
    p = lang_info['prefix']

    # 1. Update Russian phrase to: "Мобильная автономная рассудительная система"
    content = content.replace("Мобильная автономная система рассуждения", "Мобильная автономная рассудительная система")
    content = content.replace("Мобильная автономная система рассуждений", "Мобильная автономная рассудительная система")

    # 2. Extract and preserve the quote terminal style
    quote_css = """
.quote-terminal{
  margin-top:24px;
  padding:18px;
  border-left:4px solid #c1440e !important;
  border-radius:16px;
  background:rgba(193,68,14,.08) !important;
  box-shadow:0 0 20px rgba(193,68,14,.15) !important;
}
.quote-terminal .meta{
  font-size:.78rem;
  letter-spacing:.14em;
  text-transform:uppercase;
  color:#d97f3d !important;
  margin-bottom:8px;
  font-weight:700;
}
.quote-terminal .line{
  font-family:ui-monospace,SFMono-Regular,Consolas,monospace;
  color:#ffaa66 !important;
  line-height:1.7;
  font-size:1rem;
}
"""

    # 3. Replace all orange occurrences (outside quote) with emerald/mint green
    # Temporarily hide quote block
    quote_matches = re.findall(r'<div class="quote-terminal"[\s\S]*?</div></div>', content)
    for i, q in enumerate(quote_matches):
        content = content.replace(q, f"__QUOTE_PLACEHOLDER_{i}__")

    content = re.sub(r'193,\s*68,\s*14', '16, 185, 129', content)
    content = re.sub(r'217,\s*127,\s*61', '52, 211, 153', content)
    content = re.sub(r'232,\s*90,\s*42', '52, 211, 153', content)
    content = re.sub(r'255,\s*170,\s*102', '110, 231, 183', content)

    # Restore quotes
    for i, q in enumerate(quote_matches):
        content = content.replace(f"__QUOTE_PLACEHOLDER_{i}__", q)

    # 4. Construct Header HTML:
    # Row 1 (верхняя шапка): Brand on left, Lang switcher + Mobile toggle on right
    # Row 2 (нижняя шапка): Left-aligned navigation links (.topbar-subbar)
    lang_links = []
    mobile_lang_links = []
    for l in lang_labels:
        target = (p + l['path']) if l['path'] else (p if p else './')
        active = ' class="active"' if l['code'] == code else ''
        lang_links.append(f'<a{active} href="{target}">{l["label"]}</a>')
        mobile_lang_links.append(f'<a{active} href="{target}">{l["label"]}</a>')
    
    desktop_lang_html = ''.join(lang_links)
    mobile_lang_html = ''.join(mobile_lang_links)

    header_html = f"""<header class="topbar">
  <!-- Верхняя шапка: Бренд слева, Языки и Меню справа -->
  <div class="topbar-row-top">
    <a class="brand" href="{p or './'}">
      <img alt="M.A.R.S. Companion" class="brand-logo" src="{p}logo.png"/>
      <span>M.A.R.S. Companion</span>
    </a>
    <div class="topbar-top-actions">
      <nav aria-label="Language switcher" class="lang-switcher">
        {desktop_lang_html}
      </nav>
      <button aria-label="Toggle menu" class="mobile-menu-toggle" type="button">
        <span class="bar"></span>
        <span class="bar"></span>
        <span class="bar"></span>
      </button>
    </div>
  </div>

  <!-- Нижняя шапка: Навигация строго по левому краю (НЕ ПО ЦЕНТРУ!) -->
  <div class="topbar-row-bottom">
    <nav aria-label="Section Navigation" class="nav-subbar">
      <a href="#why-armenia">{lang_info['whyArm']}</a>
      <a href="#why-kapan">{lang_info['whyKap']}</a>
      <a href="#project">{lang_info['proj']}</a>
      <a href="#prototype">{lang_info['proto']}</a>
      <a href="#contact">{lang_info['cont']}</a>
      <a href="https://teduza.com/{code + '/' if code != 'en' else ''}" target="_blank" rel="noopener noreferrer">{lang_info['full']}</a>
    </nav>
  </div>

  <!-- Мобильное выпадающее меню -->
  <div class="mobile-dropdown">
    <div class="mobile-dropdown-lang">
      <div class="mobile-dropdown-label">Language</div>
      <nav aria-label="Language options" class="lang-switcher-grid">
        {mobile_lang_html}
      </nav>
    </div>
    <nav aria-label="Mobile navigation" class="mobile-dropdown-nav">
      <a href="#why-armenia">{lang_info['whyArm']}</a>
      <a href="#why-kapan">{lang_info['whyKap']}</a>
      <a href="#project">{lang_info['proj']}</a>
      <a href="#prototype">{lang_info['proto']}</a>
      <a href="#contact">{lang_info['cont']}</a>
      <a href="https://teduza.com/{code + '/' if code != 'en' else ''}" target="_blank" rel="noopener noreferrer">{lang_info['full']}</a>
    </nav>
  </div>
</header>"""

    # Replace <header ...</header>
    content = re.sub(r'<header.*?</header>', header_html, content, flags=re.DOTALL)

    # 5. Perfect 2-Tier Header CSS (Clean, no duplicates, left-aligned lower bar, emerald theme)
    header_css = f"""
/* ==========================================================================
   2-TIER LIQUID GLASS HEADER & RESPONSIVE ARCHITECTURE
   ========================================================================== */
.topbar {{
  display: flex !important;
  flex-direction: column !important;
  align-items: stretch !important;
  position: sticky !important;
  top: 12px !important;
  z-index: 1000 !important;
  margin: 12px auto 20px !important;
  max-width: var(--max) !important;
  width: 100% !important;
  padding: 10px 18px !important;
  border-radius: 20px !important;
  background: linear-gradient(135deg, rgba(6, 20, 11, 0.88) 0%, rgba(16, 185, 129, 0.10) 50%, rgba(3, 10, 6, 0.92) 100%) !important;
  backdrop-filter: blur(20px) saturate(190%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(190%) !important;
  border: 1px solid rgba(52, 211, 153, 0.28) !important;
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.6), 0 0 28px rgba(16, 185, 129, 0.16), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
  transition: all 0.25s ease !important;
}}
.topbar.is-expanded {{
  border-radius: 24px !important;
}}

/* Верхняя шапка: бренд слева, действия справа */
.topbar-row-top {{
  display: flex !important;
  justify-content: space-between !important;
  align-items: center !important;
  width: 100% !important;
  gap: 12px !important;
}}
.brand {{
  font-family: 'Space Grotesk', 'Inter', system-ui, sans-serif !important;
  font-size: .88rem !important;
  font-weight: 700 !important;
  letter-spacing: .12em !important;
  text-transform: uppercase !important;
  color: #fff !important;
  text-shadow: 0 0 16px rgba(16, 185, 129, 0.5) !important;
  text-decoration: none !important;
  display: flex !important;
  align-items: center !important;
  gap: 8px !important;
  flex-shrink: 0 !important;
  margin-left: 0 !important;
  transition: color 0.25s, text-shadow 0.25s !important;
}}
.brand:hover {{
  color: var(--accent-3) !important;
  text-shadow: 0 0 24px rgba(52, 211, 153, 0.7) !important;
}}
.brand-logo {{
  height: 28px !important;
  width: auto !important;
  display: block !important;
  flex-shrink: 0 !important;
  filter: drop-shadow(0 0 8px rgba(52, 211, 153, 0.4)) !important;
}}
.topbar-top-actions {{
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
}}

/* Нижняя шапка: строго по левому краю (НЕ ПО ЦЕНТРУ!) */
.topbar-row-bottom {{
  display: flex !important;
  justify-content: flex-start !important;
  align-items: center !important;
  width: 100% !important;
  padding-top: 8px !important;
  margin-top: 8px !important;
  border-top: 1px solid rgba(52, 211, 153, 0.14) !important;
}}
.nav-subbar {{
  display: flex !important;
  justify-content: flex-start !important;
  align-items: center !important;
  gap: 4px !important;
  width: 100% !important;
  overflow-x: auto !important;
  white-space: nowrap !important;
  scrollbar-width: none !important;
  -webkit-overflow-scrolling: touch !important;
}}
.nav-subbar::-webkit-scrollbar {{
  display: none !important;
}}
.nav-subbar a {{
  color: var(--muted) !important;
  text-decoration: none !important;
  font-size: .80rem !important;
  font-weight: 600 !important;
  padding: 5px 11px !important;
  border-radius: 999px !important;
  transition: all 0.2s ease !important;
  white-space: nowrap !important;
  flex-shrink: 0 !important;
}}
.nav-subbar a:hover {{
  color: #fff !important;
  background: rgba(16, 185, 129, 0.20) !important;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.28) !important;
  text-shadow: 0 0 8px rgba(52, 211, 153, 0.5) !important;
}}

/* Language switcher */
.lang-switcher {{
  display: flex !important;
  align-items: center !important;
  gap: 2px !important;
  padding: 3px 5px !important;
  border-radius: 999px !important;
  border: 1px solid rgba(52, 211, 153, 0.2) !important;
  background: rgba(4, 15, 8, 0.75) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  flex-shrink: 0 !important;
}}
.lang-switcher a {{
  color: var(--muted-2) !important;
  text-decoration: none !important;
  font-size: .71rem !important;
  font-weight: 700 !important;
  padding: 3px 6px !important;
  border-radius: 999px !important;
  line-height: 1 !important;
  transition: all 0.2s ease !important;
  flex-shrink: 0 !important;
}}
.lang-switcher a:hover {{
  color: #fff !important;
  background: rgba(16, 185, 129, 0.22) !important;
}}
.lang-switcher a.active {{
  color: #fff !important;
  background: linear-gradient(135deg, var(--mars), var(--mars-light)) !important;
  box-shadow: 0 2px 8px rgba(16, 185, 129, 0.45) !important;
}}

/* Мобильная кнопка */
.mobile-menu-toggle {{
  display: none !important;
  flex-direction: column !important;
  justify-content: center !important;
  align-items: center !important;
  gap: 4px !important;
  width: 36px !important;
  height: 36px !important;
  border-radius: 10px !important;
  border: 1px solid rgba(52, 211, 153, 0.3) !important;
  background: rgba(6, 20, 11, 0.7) !important;
  cursor: pointer !important;
  padding: 0 !important;
  transition: all .2s ease !important;
}}
.mobile-menu-toggle:hover {{
  border-color: var(--mars-light) !important;
  background: rgba(16, 185, 129, 0.2) !important;
}}
.mobile-menu-toggle .bar {{
  width: 18px !important;
  height: 2px !important;
  background-color: var(--text) !important;
  border-radius: 2px !important;
  transition: transform 0.25s ease, opacity 0.25s ease !important;
}}
.mobile-menu-toggle.is-active .bar:nth-child(1) {{
  transform: translateY(6px) rotate(45deg) !important;
}}
.mobile-menu-toggle.is-active .bar:nth-child(2) {{
  opacity: 0 !important;
}}
.mobile-menu-toggle.is-active .bar:nth-child(3) {{
  transform: translateY(-6px) rotate(-45deg) !important;
}}

/* Мобильное выпадающее меню */
.mobile-dropdown {{
  display: none !important;
  flex-direction: column !important;
  gap: 14px !important;
  width: 100% !important;
  padding-top: 14px !important;
  margin-top: 10px !important;
  border-top: 1px solid rgba(52, 211, 153, 0.16) !important;
}}
.mobile-dropdown.is-open {{
  display: flex !important;
}}
.mobile-dropdown-nav {{
  display: flex !important;
  flex-direction: column !important;
  align-items: stretch !important;
  gap: 6px !important;
}}
.mobile-dropdown-nav a {{
  color: var(--text) !important;
  text-decoration: none !important;
  font-size: .9rem !important;
  font-weight: 600 !important;
  padding: 8px 12px !important;
  border-radius: 10px !important;
  text-align: left !important;
  transition: background .2s ease !important;
}}
.mobile-dropdown-nav a:hover {{
  background: rgba(16, 185, 129, 0.16) !important;
  color: #fff !important;
}}
.mobile-dropdown-lang {{
  display: flex !important;
  flex-direction: column !important;
  gap: 6px !important;
  border-top: 1px solid rgba(52, 211, 153, 0.12) !important;
  padding-top: 10px !important;
}}
.mobile-dropdown-label {{
  font-size: .72rem !important;
  text-transform: uppercase !important;
  letter-spacing: .1em !important;
  color: var(--muted-2) !important;
  font-weight: 700 !important;
  text-align: left !important;
}}
.lang-switcher-grid {{
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 4px !important;
}}
.lang-switcher-grid a {{
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 6px !important;
  border-radius: 8px !important;
  font-size: .75rem !important;
  font-weight: 700 !important;
  text-decoration: none !important;
  color: var(--muted) !important;
  background: rgba(6, 20, 11, 0.6) !important;
  border: 1px solid rgba(52, 211, 153, 0.16) !important;
  transition: all .2s ease !important;
}}
.lang-switcher-grid a.active {{
  color: #fff !important;
  background: linear-gradient(135deg, var(--mars), var(--mars-light)) !important;
  border-color: var(--mars-light) !important;
}}

/* Responsive Breakpoint */
@media (max-width: 820px) {{
  .topbar-row-bottom {{ display: none !important; }}
  .lang-switcher {{ display: none !important; }}
  .mobile-menu-toggle {{ display: flex !important; }}
}}

{quote_css}
"""

    # Inject or replace header css block before </style>
    if "/* ==========================================================================\n   2-TIER LIQUID GLASS HEADER" in content:
        content = re.sub(r'/\* ==========================================================================\s*2-TIER LIQUID GLASS HEADER[\s\S]*?/\* --- Grand Footer --- \*/', f"{header_css}\n/* --- Grand Footer --- */", content)
    else:
        content = content.replace('</style>', f"{header_css}\n</style>")

    return content

def process():
    for target_dir in ['/app/applet', '/tmp/repo_why', '/tmp/repo_w']:
        for l in langs:
            fpath = os.path.join(target_dir, l['dir'], 'index.html') if l['dir'] else os.path.join(target_dir, 'index.html')
            if os.path.exists(fpath):
                with open(fpath, 'r', encoding='utf-8') as f:
                    c = f.read()
                updated = clean_and_update_html(c, l)
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(updated)
                print(f"Updated: {fpath}")

process()
print("All files processed with 2-tier header and emerald mouse hover!")
