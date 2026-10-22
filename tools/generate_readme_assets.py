#!/usr/bin/env python3
"""Generate script-free animated SVGs for the Telex Cues repository README."""
from html import escape
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'assets/readme'

def text(x, y, value, size=18, color='#F8FAFC', weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(value)}</text>'

def write(name, height, title, body):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">Telex Cues converts supplied text into visible section headings and a Telex-ready script. Animation is decorative; all information is available as static text.</desc>
<defs><radialGradient id="glow"><stop stop-color="#0066FF" stop-opacity=".65"/><stop offset="1" stop-color="#0066FF" stop-opacity="0"/></radialGradient><pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse"><path d="M30 0H0V30" stroke="#8BA4DF" stroke-opacity=".09" fill="none"/></pattern></defs>
<style>text{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}.mono{{font-family:Menlo,Consolas,monospace}}.pulse{{animation:breathe 6s ease-in-out infinite}}.scan{{animation:scan 8s ease-in-out infinite}}@keyframes breathe{{0%,100%{{opacity:.5}}50%{{opacity:1}}}}@keyframes scan{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(64px)}}}}@media(prefers-reduced-motion:reduce){{.pulse,.scan{{animation:none}}}}</style>
<rect width="1000" height="{height}" rx="20" fill="#090D16"/><rect width="1000" height="{height}" rx="20" fill="url(#grid)"/><ellipse class="pulse" cx="650" cy="110" rx="420" ry="220" fill="url(#glow)"/><rect x="1" y="1" width="998" height="{height-2}" rx="19" fill="none" stroke="#334B75"/>{body}</svg>\n''', encoding='utf-8')

def main():
    hero = text(48, 50, 'TELEX / OPEN-SOURCE CODEX SKILL', 12, '#90ADFF', 700)
    hero += text(45, 119, 'Your text.', 61, weight=800) + text(45, 182, 'Ready for your next take.', 51, weight=800)
    hero += text(48, 230, 'Natural sections. Navigable cues. Your original voice.', 21, '#BAC8E4')
    hero += text(48, 284, '$telex-cues', 20, '#8EAEFF', 700)
    hero += '<rect x="696" y="0" width="260" height="244" rx="24" fill="#000"/><rect x="696" width="260" height="40" fill="#000"/><circle cx="826" cy="20" r="3" fill="#253452"/>'
    hero += '<rect class="scan" x="716" y="62" width="220" height="35" rx="6" fill="#0066FF" opacity=".18"/>'
    for y, line in [(86, '# Opening'), (118, 'Your words, close.'), (150, '# The big idea'), (182, 'Keep your eyes up.')]:
        hero += text(728, y, line, 17, '#D9E4FF')
    write('hero.svg', 324, 'Telex Cues — Your text, ready for your next take', hero)
    flow = ''
    for x, num, title, lines in [(24,'01','Bring your words',['Paste prose, notes or a script.','Keep the language and facts.']), (350,'02','Shape the sections',['Add short, meaningful cue titles.','Preserve wording by default.']), (676,'03','Read in Telex',['Copy or import UTF-8 text.','Jump to the thought you need.'])]:
        flow += f'<rect x="{x}" y="24" width="300" height="164" rx="12" fill="#0B1426" stroke="#2A416A"/>'
        flow += text(x+20,54,num,13,'#759FFF',700) + text(x+20,91,title,23,weight=700)
        for row, line in enumerate(lines): flow += text(x+20,127+row*25,line,15,'#ACBBD6')
    write('workflow.svg',212,'Bring your words, shape the sections, read in Telex',flow)
    sample = text(35,45,'SAME WORDS. CLEARER WAYPOINTS.',12,'#90ADFF',700)
    sample += '<rect x="24" y="67" width="420" height="190" rx="12" fill="#0B1426" stroke="#2A416A"/><rect x="526" y="67" width="450" height="190" rx="12" fill="#0B1426" stroke="#2A416A"/>'
    for y,line in [(100,'YOUR TEXT'),(141,'Welcome, everyone.'),(176,'Today we review our progress.'),(211,'Next, we will gather feedback.')]: sample += text(46,y,line,16,'#B8C7E0')
    sample += text(467,169,'→',35,'#759FFF')
    sample += '<rect class="scan" x="545" y="115" width="410" height="29" rx="4" fill="#0066FF" opacity=".14"/>'
    for y,line in [(99,'TELEX-READY'),(133,'# Progress'),(164,'Welcome, everyone.'),(195,'Today we review our progress.'),(225,'# Next steps'),(247,'Next, we will gather feedback.')]: sample += text(547,y,line,15,'#B8C7E0')
    write('cue-preview.svg',281,'Original wording preserved with Progress and Next steps cues',sample)
    print('Generated 3 animated SVGs with reduced-motion fallbacks.')

if __name__ == '__main__': main()
