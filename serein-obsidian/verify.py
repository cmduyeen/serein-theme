"""Audit declared palette pairs; not an Obsidian rendering/integration test."""
import json
import colorsys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def luminance(value):
    rgb = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    rgb = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
    return sum(v*w for v, w in zip(rgb, (.2126, .7152, .0722)))


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + .05) / (dark + .05)


manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
assert manifest['name'] == 'Serein'
for key in ('name', 'version', 'minAppVersion', 'author'):
    assert isinstance(manifest[key], str) and manifest[key]
css = (ROOT / 'theme.css').read_text(encoding='utf-8')
assert css.count('{') == css.count('}'), 'Unbalanced CSS blocks'
assert '@import' not in css and 'url(' not in css, 'Unexpected external asset'
rows = ['# Serein Obsidian contrast audit', '',
        'Opaque sRGB token pairs only; actual plugin/embedded/UI rendering needs in-app QA.', '',
        '| Mode | Role | Background | Ratio | Minimum |', '|---|---|---|---:|---:|']
count = 0
for mode in ('light', 'dark'):
    block = re.search(r'\.theme-' + mode + r'\s*\{([^}]+)\}', css).group(1)
    colors = dict(re.findall(r'--serein-([\w-]+):\s*(#[\da-fA-F]{6})\s*;', block))
    channels = dict(re.findall(r'--accent-([hsl]):\s*([\d.]+)%?\s*;', block))
    assert set(channels) == {'h', 's', 'l'}, 'Missing native accent channels'
    rgb = colorsys.hls_to_rgb(float(channels['h']) / 360,
                             float(channels['l']) / 100, float(channels['s']) / 100)
    reconstructed = '#' + ''.join(f'{round(value * 255):02X}' for value in rgb)
    assert reconstructed == colors['accent'], 'Accent picker differs from theme palette'
    pairs = []
    for bg in ('canvas', 'surface', 'elevated'):
        for fg in ('text', 'muted', 'accent', 'error', 'success', 'warning', 'info'):
            pairs.append((fg, bg, 7 if fg == 'text' else 4.5))
        pairs.extend([('focus', bg, 3), ('border', bg, 3)])
    pairs.extend([('text', 'selection', 7), ('on-accent', 'accent', 4.5)])
    for fg, bg, threshold in pairs:
        ratio = contrast(colors[fg], colors[bg])
        assert ratio >= threshold, f'{mode}: {fg}/{bg} = {ratio:.3f} < {threshold}'
        rows.append(f'| {mode} | {fg} | {bg} | {ratio:.2f}:1 | {threshold}:1 |')
        count += 1
(ROOT / 'contrast-report.md').write_text('\n'.join(rows) + '\n', encoding='utf-8')
print(f'PASS: manifest, basic CSS structure, no remote assets, {count} palette contrast checks.')
