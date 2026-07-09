import os

with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
seo_text = '<!-- SEO: Automatic Question Generation, AQG, NLP, NLG, AI Education, Synthetic Data, EdTech, LLM, Verifiable Self-Play, RLVR -->\n'

# Find the heading and insert badges below it
if '# 🤖 Automatic-Question-Generation' in text:
    text = text.replace('# 🤖 Automatic-Question-Generation', f'# 🤖 Automatic-Question-Generation\n\n{seo_text}\n<div align="center">\n{badges_left}\n</div>\n')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(text)
