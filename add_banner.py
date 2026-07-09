import os
import re

os.makedirs('assets', exist_ok=True)

svg_content = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4facfe;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#00f2fe;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" rx="15"/>
  
  <text x="50%" y="50%" font-family="Arial, sans-serif" font-size="42" font-weight="bold" fill="white" text-anchor="middle" dominant-baseline="middle">
    Automatic Question Generation (AQG)
  </text>
  <text x="50%" y="75%" font-family="Arial, sans-serif" font-size="20" fill="#f0f0f0" text-anchor="middle" dominant-baseline="middle">
    Powering AI with Intelligent Query Synthesis
  </text>

  <circle cx="100" cy="100" r="10" fill="white" opacity="0.5">
    <animate attributeName="cy" values="100;80;100" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="700" cy="100" r="15" fill="white" opacity="0.3">
    <animate attributeName="cy" values="100;120;100" dur="3s" repeatCount="indefinite" />
  </circle>
</svg>'''

with open('assets/banner.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Add banner at the top
banner_md = '<div align="center">\n  <img src="assets/banner.svg" alt="AQG Banner" width="100%" />\n</div>\n\n'
if banner_md not in text:
    text = banner_md + text

# Add emojis to headings
text = re.sub(r'# Automatic-Question-Generation', '# 🤖 Automatic-Question-Generation', text, 1)
text = re.sub(r'## Automatic Question Generation \(AQG\) in AI: History, Progression, Variants, & Applications', '## 🧠 Automatic Question Generation (AQG) in AI: History, Progression, Variants, & Applications', text, 1)
text = re.sub(r'## 1. The Macro Chronological Evolution', '## ⏳ 1. The Macro Chronological Evolution', text, 1)
text = re.sub(r'## 2. Core Functional & Target-Driven Variants', '## 🎯 2. Core Functional & Target-Driven Variants', text, 1)
text = re.sub(r'## 3. The Synthetic Data Curation & Self-Instruct Matrix', '## 🧬 3. The Synthetic Data Curation & Self-Instruct Matrix', text, 1)
text = re.sub(r'## 4. Production Engineering Challenges & Infrastructure Mitigations', '## 🏭 4. Production Engineering Challenges & Infrastructure Mitigations', text, 1)
text = re.sub(r'## 5. Frontier Real-World AI Industrial Applications', '## 🌍 5. Frontier Real-World AI Industrial Applications', text, 1)
text = re.sub(r'## References', '## 📚 References', text, 1)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
