param([ValidateSet('Light','Dark')][string]$Mode = 'Light')
$ErrorActionPreference = 'Stop'
$name = if ($Mode -eq 'Light') {'alabaster'} else {'obsidian'}
$text = Get-Content -LiteralPath (Join-Path $PSScriptRoot "$name.codex-theme") -Raw
if (-not $text.Trim().StartsWith('codex-theme-v1:')) { throw 'Invalid Codex theme share string.' }
Set-Clipboard -Value $text.Trim()
Write-Host "Copied Serein $Mode. In Codex: Settings > Appearance > $Mode theme > Import."
