param(
    [ValidateSet('Light','Dark')][string]$Mode = 'Light',
    [ValidateSet('background','foreground','accent')][string]$Color = 'background'
)
$ErrorActionPreference = 'Stop'
$preset = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'presets.json') -Raw | ConvertFrom-Json
$value = $preset.$Mode.$Color
Set-Clipboard -Value $value.TrimStart('#')
Write-Host "Copied $Mode / $Color = $value. Paste into Antigravity > Settings > Appearance."
