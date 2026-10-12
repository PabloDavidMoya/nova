"""Genera reporte-nova.html: el reporte en un solo archivo (CSS incluido) para descargar y abrir sin internet.

Correr después de cada cambio en index.html o style.css:  python build_descarga.py
"""
import pathlib
import re

here = pathlib.Path(__file__).parent
html = (here / 'index.html').read_text(encoding='utf-8')
css = (here / 'style.css').read_text(encoding='utf-8')

link = '<link rel="stylesheet" href="style.css">'
assert link in html
html = html.replace(link, '<style>\n' + css + '\n</style>')
# el botón de descarga no tiene sentido dentro del archivo descargado
html = re.sub(r'<!--descarga-->.*?<!--/descarga-->', '', html, flags=re.S)

(here / 'reporte-nova.html').write_text(html, encoding='utf-8')
print('reporte-nova.html generado')
