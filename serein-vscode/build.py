"""Generate a declarative VS Code theme; stdlib only, no runtime extension code."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def luminance(value):
    rgb = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    rgb = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in rgb]
    return sum(v*w for v, w in zip(rgb, (.2126, .7152, .0722)))


def contrast(a, b):
    light, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (light + .05) / (dark + .05)


def make_theme(p, mode):
    colors = {}

    def assign(role, *keys):
        for key in keys:
            colors[key] = p[role]

    assign('canvas', 'editor.background', 'editorGutter.background', 'terminal.background',
           'tab.activeBackground', 'tab.unfocusedActiveBackground', 'editorGroupHeader.noTabsBackground',
           'input.background', 'dropdown.background', 'textCodeBlock.background',
           'notebook.cellEditorBackground', 'peekViewEditor.background', 'menu.background')
    assign('surface', 'sideBar.background', 'activityBar.background', 'statusBar.background',
           'statusBar.noFolderBackground', 'statusBar.debuggingBackground', 'titleBar.activeBackground',
           'titleBar.inactiveBackground', 'editorGroupHeader.tabsBackground', 'tab.inactiveBackground',
           'panel.background', 'editorWidget.background', 'editorHoverWidget.background',
           'quickInput.background', 'breadcrumb.background', 'notifications.background',
           'peekViewTitle.background', 'peekViewResult.background', 'settings.dropdownBackground',
           'settings.textInputBackground', 'settings.numberInputBackground', 'settings.checkboxBackground')
    assign('elevated', 'editor.lineHighlightBackground', 'list.hoverBackground',
           'list.inactiveSelectionBackground', 'list.focusBackground', 'list.activeSelectionBackground',
           'toolbar.hoverBackground', 'button.secondaryBackground', 'button.secondaryHoverBackground',
           'welcomePage.tileBackground', 'tab.hoverBackground', 'menu.selectionBackground',
           'notebook.focusedCellBackground', 'editorSuggestWidget.selectedBackground')
    assign('text', 'foreground', 'editor.foreground', 'terminal.foreground',
           'sideBar.foreground', 'sideBarTitle.foreground', 'sideBarSectionHeader.foreground',
           'activityBar.foreground', 'statusBar.foreground', 'statusBar.noFolderForeground',
           'statusBar.debuggingForeground', 'titleBar.activeForeground', 'tab.activeForeground',
           'tab.unfocusedActiveForeground', 'panelTitle.activeForeground', 'input.foreground',
           'dropdown.foreground', 'quickInput.foreground', 'notifications.foreground',
           'list.activeSelectionForeground', 'list.inactiveSelectionForeground', 'list.focusForeground',
           'list.hoverForeground', 'menu.foreground', 'menu.selectionForeground',
           'editorWidget.foreground', 'editorHoverWidget.foreground', 'button.secondaryForeground',
           'editorSuggestWidget.foreground', 'editorSuggestWidget.selectedForeground',
           'settings.dropdownForeground', 'settings.textInputForeground',
           'settings.numberInputForeground', 'settings.checkboxForeground', 'peekViewResult.selectionForeground')
    assign('muted', 'descriptionForeground', 'disabledForeground', 'input.placeholderForeground',
           'activityBar.inactiveForeground', 'tab.inactiveForeground', 'titleBar.inactiveForeground',
           'panelTitle.inactiveForeground', 'editorLineNumber.foreground', 'editorCodeLens.foreground',
           'editorInlayHint.foreground', 'breadcrumb.foreground', 'breadcrumb.focusForeground',
           'editorWhitespace.foreground', 'gitDecoration.ignoredResourceForeground')
    assign('accent', 'focusBorder', 'editorCursor.foreground', 'terminalCursor.foreground',
           'activityBar.activeBorder', 'tab.activeBorderTop', 'tab.unfocusedActiveBorderTop',
           'panelTitle.activeBorder', 'textLink.foreground', 'textLink.activeForeground',
           'list.highlightForeground', 'list.focusHighlightForeground', 'progressBar.background',
           'button.background', 'button.hoverBackground', 'badge.background', 'activityBarBadge.background',
           'textPreformat.foreground', 'editorLink.activeForeground', 'editorLineNumber.activeForeground',
           'editorBracketMatch.border', 'inputOption.activeBorder', 'pickerGroup.foreground')
    assign('onAccent', 'button.foreground', 'badge.foreground', 'activityBarBadge.foreground')
    assign('selection', 'editor.selectionBackground', 'editor.inactiveSelectionBackground',
           'editor.selectionHighlightBackground', 'terminal.selectionBackground',
           'terminal.inactiveSelectionBackground', 'peekViewResult.selectionBackground',
           'editor.findMatchBackground', 'editor.findMatchHighlightBackground')
    assign('text', 'editor.selectionForeground', 'terminal.selectionForeground')
    assign('surface', 'editorInlayHint.background', 'editorSuggestWidget.background',
           'sideBarSectionHeader.background')
    assign('border', 'sideBar.border', 'panel.border', 'editorGroup.border',
           'editorWidget.border', 'editorHoverWidget.border', 'input.border', 'dropdown.border',
           'menu.border', 'notificationCenter.border', 'notifications.border',
           'editorIndentGuide.background1', 'tree.indentGuidesStroke', 'widget.border',
           'settings.dropdownBorder', 'settings.textInputBorder', 'settings.numberInputBorder',
           'settings.checkboxBorder', 'editorSuggestWidget.border')
    assign('accent', 'editorIndentGuide.activeBackground1', 'tree.inactiveIndentGuidesStroke',
           'editor.findMatchBorder', 'list.focusOutline')
    assign('error', 'errorForeground', 'editorError.foreground', 'editorGutter.deletedBackground',
           'gitDecoration.deletedResourceForeground', 'gitDecoration.conflictingResourceForeground',
           'problemsErrorIcon.foreground', 'notificationsErrorIcon.foreground', 'inputValidation.errorBorder')
    assign('warning', 'editorWarning.foreground', 'problemsWarningIcon.foreground',
           'notificationsWarningIcon.foreground', 'gitDecoration.modifiedResourceForeground',
           'editorGutter.modifiedBackground', 'inputValidation.warningBorder')
    assign('info', 'editorInfo.foreground', 'problemsInfoIcon.foreground',
           'notificationsInfoIcon.foreground', 'inputValidation.infoBorder')
    assign('success', 'gitDecoration.addedResourceForeground', 'gitDecoration.untrackedResourceForeground',
           'editorGutter.addedBackground')
    assign('canvas', 'inputValidation.errorBackground', 'inputValidation.warningBackground',
           'inputValidation.infoBackground')
    assign('text', 'inputValidation.errorForeground', 'inputValidation.warningForeground',
           'inputValidation.infoForeground')
    colors.update({
        'diffEditor.insertedTextBackground': p['success'] + '20',
        'diffEditor.removedTextBackground': p['error'] + '20',
        'editor.wordHighlightBackground': p['selection'] + '80',
        'editor.wordHighlightStrongBackground': p['selection'] + '80',
        'editorOverviewRuler.errorForeground': p['error'],
        'editorOverviewRuler.warningForeground': p['warning'],
        'editorOverviewRuler.infoForeground': p['info'],
        'scrollbarSlider.background': p['border'] + '80',
        'scrollbarSlider.hoverBackground': p['border'] + 'B0',
        'scrollbarSlider.activeBackground': p['border'],
    })
    ansi = 'Black Red Green Yellow Blue Magenta Cyan White BrightBlack BrightRed BrightGreen BrightYellow BrightBlue BrightMagenta BrightCyan BrightWhite'.split()
    colors.update({f'terminal.ansi{key}': value for key, value in zip(ansi, p['ansi'])})
    tokens = [
        {'settings': {'foreground': p['text'], 'background': p['canvas']}},
        {'name': 'Comments: readable, upright', 'scope': ['comment', 'punctuation.definition.comment'],
         'settings': {'foreground': p['muted'], 'fontStyle': ''}},
        {'name': 'Structural keywords', 'scope': ['keyword', 'storage.type', 'storage.modifier'],
         'settings': {'foreground': p['accent'], 'fontStyle': ''}},
        {'name': 'Operators and punctuation', 'scope': ['keyword.operator', 'punctuation'],
         'settings': {'foreground': p['text'], 'fontStyle': ''}},
        {'name': 'Strings', 'scope': ['string'], 'settings': {'foreground': p['success']}},
        {'name': 'Literal values', 'scope': ['constant.numeric', 'constant.language'],
         'settings': {'foreground': p['info']}},
        {'name': 'Names', 'scope': ['variable', 'entity.name', 'support', 'entity.other.attribute-name'],
         'settings': {'foreground': p['text'], 'fontStyle': ''}},
        {'name': 'Markup headings', 'scope': ['markup.heading'],
         'settings': {'foreground': p['text'], 'fontStyle': 'bold'}},
        {'name': 'Markup link', 'scope': ['markup.underline.link'],
         'settings': {'foreground': p['accent'], 'fontStyle': 'underline'}},
        {'name': 'Inserted / deleted', 'scope': ['markup.inserted'], 'settings': {'foreground': p['success']}},
        {'scope': ['markup.deleted', 'invalid'], 'settings': {'foreground': p['error']}},
        {'scope': ['markup.bold'], 'settings': {'foreground': p['text'], 'fontStyle': 'bold'}},
        {'scope': ['markup.italic'], 'settings': {'foreground': p['text'], 'fontStyle': 'italic'}},
    ]
    semantic = {'*': {'foreground': p['text'], 'italic': False},
                'comment': {'foreground': p['muted'], 'italic': False},
                'keyword': p['accent'], 'modifier': p['accent'],
                'string': p['success'], 'number': p['info'],
                'operator': p['text'], 'enumMember': p['info']}
    return {'$schema': 'vscode://schemas/color-theme', 'name': p['name'],
            'type': mode, 'semanticHighlighting': True, 'colors': colors,
            'tokenColors': tokens, 'semanticTokenColors': semantic}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Check committed outputs without rewriting')
    args = parser.parse_args()
    palettes = json.loads((ROOT / 'palette.json').read_text(encoding='utf-8'))
    manifest = json.loads((ROOT / 'package.json').read_text(encoding='utf-8'))
    assert len(manifest['contributes']['themes']) == 2
    rows = ['# Serein VS Code contrast audit', '',
            'Opaque sRGB pairs only. Alpha overlays, plugin UI, arbitrary terminal backgrounds',
            'and truecolor output need separate rendering checks. This is not full WCAG certification.', '',
            '| Mode | Text role | Background | Contrast | Minimum |', '|---|---|---|---:|---:|']
    count = 0
    for (mode, p), contribution in zip(palettes.items(), manifest['contributes']['themes']):
        assert p['name'] == contribution['label']
        assert contribution['uiTheme'] == ('vs' if mode == 'light' else 'vs-dark')
        theme = make_theme(p, mode)
        pairs = [(fg, bg, 7 if fg == 'text' else 4.5)
                 for bg in ('canvas', 'surface', 'elevated', 'selection')
                 for fg in ('text', 'muted', 'accent', 'error', 'warning', 'success', 'info')]
        pairs += [('onAccent', 'accent', 4.5), ('border', 'canvas', 3), ('border', 'surface', 3)]
        for fg, bg, minimum in pairs:
            ratio = contrast(p[fg], p[bg])
            assert ratio >= minimum, f'{mode}/{fg}/{bg}: {ratio:.3f} < {minimum}'
            rows.append(f'| {mode} | {fg} | {bg} | {ratio:.2f}:1 | {minimum}:1 |')
            count += 1
        for index, value in enumerate(p['ansi']):
            ratio = contrast(value, p['canvas'])
            assert ratio >= 4.5, f'{mode}/ANSI {index}: {ratio:.3f}'
            rows.append(f'| {mode} | ANSI {index} | canvas | {ratio:.2f}:1 | 4.5:1 |')
            count += 1
        output = json.dumps(theme, ensure_ascii=False, indent=2) + '\n'
        path = ROOT / contribution['path']
        if args.check:
            assert path.read_text(encoding='utf-8') == output, f'Stale generated theme: {path}'
        else:
            path.write_text(output, encoding='utf-8')
    report = '\n'.join(rows) + '\n'
    if args.check:
        assert (ROOT / 'contrast-report.md').read_text(encoding='utf-8') == report
    else:
        (ROOT / 'contrast-report.md').write_text(report, encoding='utf-8')
    print(f'PASS: two theme contributions, TextMate + semantic tokens, {count} contrast checks.')


if __name__ == '__main__':
    main()
