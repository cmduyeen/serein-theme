# Serein VS Code contrast audit

Opaque sRGB pairs only. Alpha overlays, plugin UI, arbitrary terminal backgrounds
and truecolor output need separate rendering checks. This is not full WCAG certification.

| Mode | Text role | Background | Contrast | Minimum |
|---|---|---|---:|---:|
| light | text | canvas | 10.30:1 | 7:1 |
| light | muted | canvas | 6.43:1 | 4.5:1 |
| light | accent | canvas | 5.87:1 | 4.5:1 |
| light | error | canvas | 6.33:1 | 4.5:1 |
| light | warning | canvas | 6.25:1 | 4.5:1 |
| light | success | canvas | 6.71:1 | 4.5:1 |
| light | info | canvas | 6.64:1 | 4.5:1 |
| light | text | surface | 9.42:1 | 7:1 |
| light | muted | surface | 5.88:1 | 4.5:1 |
| light | accent | surface | 5.37:1 | 4.5:1 |
| light | error | surface | 5.79:1 | 4.5:1 |
| light | warning | surface | 5.72:1 | 4.5:1 |
| light | success | surface | 6.13:1 | 4.5:1 |
| light | info | surface | 6.08:1 | 4.5:1 |
| light | text | elevated | 8.51:1 | 7:1 |
| light | muted | elevated | 5.32:1 | 4.5:1 |
| light | accent | elevated | 4.85:1 | 4.5:1 |
| light | error | elevated | 5.23:1 | 4.5:1 |
| light | warning | elevated | 5.16:1 | 4.5:1 |
| light | success | elevated | 5.54:1 | 4.5:1 |
| light | info | elevated | 5.49:1 | 4.5:1 |
| light | text | selection | 8.16:1 | 7:1 |
| light | muted | selection | 5.10:1 | 4.5:1 |
| light | accent | selection | 4.65:1 | 4.5:1 |
| light | error | selection | 5.02:1 | 4.5:1 |
| light | warning | selection | 4.95:1 | 4.5:1 |
| light | success | selection | 5.32:1 | 4.5:1 |
| light | info | selection | 5.27:1 | 4.5:1 |
| light | onAccent | accent | 5.87:1 | 4.5:1 |
| light | border | canvas | 3.81:1 | 3:1 |
| light | border | surface | 3.49:1 | 3:1 |
| light | ANSI 0 | canvas | 10.30:1 | 4.5:1 |
| light | ANSI 1 | canvas | 5.43:1 | 4.5:1 |
| light | ANSI 2 | canvas | 5.80:1 | 4.5:1 |
| light | ANSI 3 | canvas | 5.46:1 | 4.5:1 |
| light | ANSI 4 | canvas | 5.72:1 | 4.5:1 |
| light | ANSI 5 | canvas | 5.00:1 | 4.5:1 |
| light | ANSI 6 | canvas | 5.69:1 | 4.5:1 |
| light | ANSI 7 | canvas | 5.94:1 | 4.5:1 |
| light | ANSI 8 | canvas | 5.01:1 | 4.5:1 |
| light | ANSI 9 | canvas | 6.33:1 | 4.5:1 |
| light | ANSI 10 | canvas | 6.71:1 | 4.5:1 |
| light | ANSI 11 | canvas | 6.25:1 | 4.5:1 |
| light | ANSI 12 | canvas | 6.64:1 | 4.5:1 |
| light | ANSI 13 | canvas | 5.87:1 | 4.5:1 |
| light | ANSI 14 | canvas | 6.60:1 | 4.5:1 |
| light | ANSI 15 | canvas | 7.73:1 | 4.5:1 |
| dark | text | canvas | 10.08:1 | 7:1 |
| dark | muted | canvas | 6.66:1 | 4.5:1 |
| dark | accent | canvas | 6.06:1 | 4.5:1 |
| dark | error | canvas | 5.97:1 | 4.5:1 |
| dark | warning | canvas | 7.09:1 | 4.5:1 |
| dark | success | canvas | 7.56:1 | 4.5:1 |
| dark | info | canvas | 7.38:1 | 4.5:1 |
| dark | text | surface | 9.26:1 | 7:1 |
| dark | muted | surface | 6.11:1 | 4.5:1 |
| dark | accent | surface | 5.57:1 | 4.5:1 |
| dark | error | surface | 5.48:1 | 4.5:1 |
| dark | warning | surface | 6.51:1 | 4.5:1 |
| dark | success | surface | 6.94:1 | 4.5:1 |
| dark | info | surface | 6.78:1 | 4.5:1 |
| dark | text | elevated | 8.25:1 | 7:1 |
| dark | muted | elevated | 5.44:1 | 4.5:1 |
| dark | accent | elevated | 4.96:1 | 4.5:1 |
| dark | error | elevated | 4.88:1 | 4.5:1 |
| dark | warning | elevated | 5.80:1 | 4.5:1 |
| dark | success | elevated | 6.19:1 | 4.5:1 |
| dark | info | elevated | 6.04:1 | 4.5:1 |
| dark | text | selection | 7.79:1 | 7:1 |
| dark | muted | selection | 5.14:1 | 4.5:1 |
| dark | accent | selection | 4.68:1 | 4.5:1 |
| dark | error | selection | 4.61:1 | 4.5:1 |
| dark | warning | selection | 5.48:1 | 4.5:1 |
| dark | success | selection | 5.84:1 | 4.5:1 |
| dark | info | selection | 5.70:1 | 4.5:1 |
| dark | onAccent | accent | 6.06:1 | 4.5:1 |
| dark | border | canvas | 4.34:1 | 3:1 |
| dark | border | surface | 3.98:1 | 3:1 |
| dark | ANSI 0 | canvas | 5.60:1 | 4.5:1 |
| dark | ANSI 1 | canvas | 5.97:1 | 4.5:1 |
| dark | ANSI 2 | canvas | 7.56:1 | 4.5:1 |
| dark | ANSI 3 | canvas | 7.09:1 | 4.5:1 |
| dark | ANSI 4 | canvas | 7.38:1 | 4.5:1 |
| dark | ANSI 5 | canvas | 6.06:1 | 4.5:1 |
| dark | ANSI 6 | canvas | 7.50:1 | 4.5:1 |
| dark | ANSI 7 | canvas | 10.08:1 | 4.5:1 |
| dark | ANSI 8 | canvas | 6.66:1 | 4.5:1 |
| dark | ANSI 9 | canvas | 8.10:1 | 4.5:1 |
| dark | ANSI 10 | canvas | 9.18:1 | 4.5:1 |
| dark | ANSI 11 | canvas | 8.89:1 | 4.5:1 |
| dark | ANSI 12 | canvas | 9.37:1 | 4.5:1 |
| dark | ANSI 13 | canvas | 7.81:1 | 4.5:1 |
| dark | ANSI 14 | canvas | 9.41:1 | 4.5:1 |
| dark | ANSI 15 | canvas | 11.66:1 | 4.5:1 |
