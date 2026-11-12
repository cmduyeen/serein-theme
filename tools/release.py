"""Build shareable Serein archives offline. Only allowlisted files are shipped."""
import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
TERMINAL_VERSION = '0.1.0'
NS = 'http://schemas.microsoft.com/developer/vsx-schema/2011'


def read(relative):
    return (ROOT / relative).read_bytes()


def archive(name, entries):
    path = DIST / name
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for member, data in sorted(entries.items()):
            assert not member.startswith('/') and '..' not in Path(member).parts
            assert not any(part in member.split('/') for part in ('backups', '.preview', '.git', '__pycache__'))
            assert not member.endswith(('install-state.json', 'last-session.json'))
            info = zipfile.ZipInfo(member, (2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        assert set(z.namelist()) == set(entries)
    print(f'Built {name} ({len(entries)} files)')
    return path


def vscode_package():
    p = json.loads(read('serein-vscode/package.json'))
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="{NS}">
  <Metadata>
    <Identity Language="en-US" Id="{escape(p['name'])}" Version="{escape(p['version'])}" Publisher="{escape(p['publisher'])}"/>
    <DisplayName>{escape(p['displayName'])}</DisplayName>
    <Description xml:space="preserve">{escape(p['description'])}</Description>
    <Categories>Themes</Categories><GalleryFlags>Public</GalleryFlags>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="{escape(p['engines']['vscode'])}"/>
      <Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="ui"/>
      <Property Id="Microsoft.VisualStudio.Code.ExecutesCode" Value="false"/>
    </Properties><License>extension/LICENSE</License>
  </Metadata>
  <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation>
  <Dependencies/>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true"/>
    <Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE" Addressable="true"/>
  </Assets>
</PackageManifest>'''
    ET.fromstring(xml)
    content_types = '''<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json"/>
  <Default Extension="md" ContentType="text/markdown"/>
  <Default Extension="vsixmanifest" ContentType="text/xml"/>
  <Override PartName="/extension/LICENSE" ContentType="text/plain"/>
</Types>'''
    entries = {'extension.vsixmanifest': xml.encode(), '[Content_Types].xml': content_types.encode(),
               'extension/package.json': read('serein-vscode/package.json'), 'extension/LICENSE': read('LICENSE'),
               'extension/README.md': read('serein-vscode/README.md').replace(b'../docs/', b'docs/'),
               'extension/docs/scientific-basis.vi.md': read('docs/scientific-basis.vi.md'),
               'extension/contrast-report.md': read('serein-vscode/contrast-report.md'),
               'extension/recommended-settings.json': read('serein-vscode/recommended-settings.json')}
    for theme in p['contributes']['themes']:
        relative = theme['path'].removeprefix('./')
        entries['extension/' + relative] = read('serein-vscode/' + relative)
    return archive(f"serein-vscode-{p['version']}.vsix", entries)


def main():
    for relative in ('serein-terminal/build.py', 'serein-obsidian/verify.py', 'serein-vscode/build.py'):
        subprocess.run([sys.executable, str(ROOT / relative)], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / 'serein-vscode/build.py'), '--check'], cwd=ROOT, check=True)
    DIST.mkdir(exist_ok=True)
    outputs = [vscode_package()]
    science = read('docs/scientific-basis.vi.md')
    terminal = {name: read('serein-terminal/' + name) for name in
                ('install.ps1', 'restore.ps1', 'session.ps1', 'preview.ps1', 'build.py', 'verify.ps1',
                 'schemes/light.json', 'schemes/dark.json', 'contrast-report.md')}
    terminal.update({'LICENSE': read('LICENSE'), 'docs/scientific-basis.vi.md': science,
                     'README.md': read('serein-terminal/README.md').replace(b'../docs/', b'docs/')})
    outputs.append(archive(f'serein-terminal-{TERMINAL_VERSION}.zip', terminal))
    obsidian_version = json.loads(read('serein-obsidian/manifest.json'))['version']
    obsidian = {'Serein/theme.css': read('serein-obsidian/theme.css'),
                'Serein/manifest.json': read('serein-obsidian/manifest.json'),
                'snippets/serein-focus.css': read('serein-obsidian/snippets/serein-focus.css'),
                'Preview.md': read('serein-obsidian/Preview.md'), 'LICENSE': read('LICENSE'),
                'docs/scientific-basis.vi.md': science,
                'README.md': read('serein-obsidian/README.md').replace(b'../docs/', b'docs/'),
                'contrast-report.md': read('serein-obsidian/contrast-report.md')}
    outputs.append(archive(f'serein-obsidian-{obsidian_version}.zip', obsidian))
    # Source archive uses explicit top-level roots and excludes all local state.
    source = {}
    for root_name in ('serein-terminal', 'serein-obsidian', 'serein-vscode', 'docs', 'tools'):
        for path in (ROOT / root_name).rglob('*'):
            if not path.is_file():
                continue
            parts = path.relative_to(ROOT).parts
            if any(part in ('backups', '.preview', '__pycache__') for part in parts):
                continue
            if path.name in ('install-state.json', 'last-session.json'):
                continue
            if path.suffix not in ('.py', '.ps1', '.md', '.json', '.css') and path.name != '.gitignore':
                continue
            source['serein-theme/' + path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for name in ('README.md', 'LICENSE', '.gitignore', '.gitattributes', 'theme-protect-eyes.md'):
        source['serein-theme/' + name] = read(name)
    outputs.append(archive('serein-source-0.1.0.zip', source))
    checksums = '\n'.join(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}' for path in outputs) + '\n'
    (DIST / 'SHA256SUMS.txt').write_text(checksums, encoding='ascii')
    print('PASS: archive integrity, allowlisted contents, SHA-256 checksums.')


if __name__ == '__main__':
    main()
