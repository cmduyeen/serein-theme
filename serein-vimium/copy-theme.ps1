param([ValidateSet('Auto','Light','Dark')][string]$Mode = 'Auto')
$ErrorActionPreference = 'Stop'
$name = switch ($Mode) { 'Light' {'serein-alabaster.css'} 'Dark' {'serein-obsidian.css'} default {'serein-auto.css'} }
Set-Clipboard -Value (Get-Content -LiteralPath (Join-Path $PSScriptRoot $name) -Raw)
Write-Host "Copied Serein $Mode CSS. Paste into Vimium Options > CSS for Vimium UI, then Save Changes."
