# Serein Reference

**Extreme minimalism. Everyday comfort.**

Serein is a family of warm, low-distraction themes. Alabaster is the light palette; Obsidian is the dark palette. Choose the mode and text size that work for your display, lighting and vision.

## Design benefits

- **Readable text:** declared text/background pairs are checked using WCAG relative luminance. Targets are at least 7:1 for primary text and 4.5:1 for normal secondary text.
- **Less visual competition:** restrained syntax colors, quiet surfaces and a single main accent, while preserving errors, warnings, selection and keyboard focus.
- **Consistent surroundings:** related palettes across applications reduce abrupt stylistic changes. This is a design goal, not evidence of a medical benefit.
- **Reversible setup:** native theme formats and scoped installation instructions; no system-style patchers or background services.

## What the evidence supports

**Visual comfort depends on more than colors.** The American Academy of Ophthalmology recommends managing brightness, glare, viewing position and breaks. A theme addresses only part of that environment. [AAO: Computers, Digital Devices, and Eye Strain](https://www.aao.org/eye-health/diseases/computer-usage).

**Readable size matters.** Reading performance depends on both character size and available display space. Serein offers adjustable typography rather than claiming one font size fits everyone. [Atilgan, Xiong & Legge, 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7720185/).

**Warm colors are a preference, not treatment.** A Cochrane review of 17 randomized trials found that blue-light-filtering spectacles may not reduce short-term computer eye strain; sleep results were uncertain. These studies concern lenses, not Serein themes. [Cochrane, 2023](https://doi.org/10.1002/14651858.CD013244.pub2).

**Dark mode is optional.** Experimental work found an advantage for dark text on a light background in proofreading under its study conditions. It does not establish a universally more comfortable mode. [Piepenbrock et al., 2014](https://pubmed.ncbi.nlm.nih.gov/25135324/).

Serein has not undergone clinical testing. It does not claim to treat dry eye, protect the retina, prevent disease, improve sleep or increase attention. WCAG thresholds are accessibility references, not medical safety limits. [WCAG text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

## Palette

| Role | Alabaster | Obsidian |
|---|---|---|
| Canvas | `#F6F4F0` | `#191817` |
| Surface | `#EDEAE4` | `#21201E` |
| Elevated | `#E3DFD7` | `#2B2926` |
| Primary text | `#3D3A36` | `#C7C3BA` |
| Secondary text | `#5C5852` | `#A39E95` |
| Accent | `#914854` | `#C9848F` |
| Error | `#963D37` | `#CF8179` |
| Warning | `#705711` | `#BAA16B` |
| Success | `#405D3D` | `#9FAE94` |

Adapters may adjust a color for its actual background. Terminal ANSI colors, translucent overlays, embedded content, plugins and truecolor output need separate checks. Base palette checks are not full-application WCAG certification.

## Maintaining a theme

Edit the native source in its product repository. Check light/dark modes, Vietnamese and other accented text, zoom, focus, selection, diagnostics and repeated navigation. Compare comprehension and task accuracy alongside subjective comfort; longer uninterrupted screen time is not the success criterion.

Update the version and packaged download together. Use actual application screenshots with sample content; exclude account details, private conversations, credentials and user configuration backups. Keep screenshots labeled by application and mode.

Native formats: Windows Terminal schemes; Obsidian CSS/manifest; VS Code VSIX; Windows `.theme`; Sublime Text `.sublime-package`; Telegram Desktop `.tdesktop-theme`; Vimium custom CSS; Codex native theme share strings. Antigravity App presets describe values entered in Appearance, not a native import format.

Codex's theme format was checked against the installed application parser. Its contrast slider is an application-specific parameter, not a WCAG contrast ratio. Future application versions may change the supported schema.

## License

MIT. See each repository's LICENSE. Product-specific installation and test limits are documented in its README.
