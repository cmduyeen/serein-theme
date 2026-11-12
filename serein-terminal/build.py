"""Build Windows Terminal schemes and audit text contrast (Python stdlib only)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ANSI = ('black red green yellow blue purple cyan white '
        'brightBlack brightRed brightGreen brightYellow brightBlue brightPurple brightCyan brightWhite').split()
PALETTES = {
    'Light': {
        'name': 'Serein Alabaster', 'background': '#F6F4F0',
        'foreground': '#3D3A36', 'cursorColor': '#9E525E', 'selectionBackground': '#DED6CE',
        'colors': ['#3D3A36', '#A6443E', '#4F654B', '#796019', '#4D627A', '#9E525E', '#39686A', '#625D56',
                   '#6E6860', '#963D37', '#405D3D', '#705711', '#435872', '#914854', '#305E60', '#514C46'],
        'muted': '#6E6860',
    },
    'Dark': {
        'name': 'Serein Obsidian', 'background': '#191817',
        'foreground': '#C7C3BA', 'cursorColor': '#C9848F', 'selectionBackground': '#35312E',
        'colors': ['#969087', '#CF8179', '#9FAE94', '#BAA16B', '#98A9BD', '#C9848F', '#8FAFAA', '#C7C3BA',
                   '#A39E95', '#DEA099', '#B1BFA6', '#CDB582', '#AFBED0', '#D99CA5', '#A5C3BE', '#D6D1C7'],
        'muted': '#969087',
    },
}


def luminance(value):
    rgb = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    rgb = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
    return sum(v*w for v, w in zip(rgb, (.2126, .7152, .0722)))


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + .05) / (dark + .05)


def main():
    report = ['# Contrast audit', '',
              'Computed from opaque sRGB HEX using WCAG relative luminance.',
              'ANSI foregrounds are tested on the default background only. Arbitrary ANSI',
              'backgrounds, inverse/dim text, 256-color and truecolor app output are outside this guarantee.', '',
              '| Mode | Role | Foreground | Background | Ratio |', '|---|---|---|---|---:|']
    for mode, palette in PALETTES.items():
        scheme = {k: v for k, v in palette.items() if k not in ('colors', 'muted')}
        scheme.update(zip(ANSI, palette['colors']))
        checks = [(role, scheme[role], scheme['background'], 7 if role == 'foreground' else 4.5)
                  for role in ['foreground', *ANSI]]
        checks += [('muted', palette['muted'], scheme['background'], 4.5),
                   ('selected text', scheme['foreground'], scheme['selectionBackground'], 7),
                   ('cursor', scheme['cursorColor'], scheme['background'], 3)]
        for role, fg, bg, threshold in checks:
            ratio = contrast(fg, bg)
            assert ratio >= threshold, f'{mode}/{role}: {ratio:.3f} < {threshold}'
            report.append(f'| {mode} | {role} | `{fg}` | `{bg}` | {ratio:.2f}:1 |')
        (ROOT / 'schemes' / f'{mode.lower()}.json').write_text(json.dumps(scheme, indent=2) + '\n', encoding='utf-8')
    (ROOT / 'contrast-report.md').write_text('\n'.join(report) + '\n', encoding='utf-8')
    print('PASS: 40 contrast checks; two schemes generated.')


if __name__ == '__main__':
    main()
