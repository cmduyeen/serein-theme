param([ValidateSet('Light','Dark')][string]$Mode = 'Light')
$ErrorActionPreference = 'Stop'
$profileRoot = Join-Path $PSScriptRoot '.preview'
$userDirectory = Join-Path $profileRoot 'User'
New-Item -ItemType Directory -Path $userDirectory -Force | Out-Null
$settings = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'recommended-settings.json') -Raw | ConvertFrom-Json -AsHashtable
$settings['workbench.colorTheme'] = if ($Mode -eq 'Light') {'Serein Alabaster'} else {'Serein Obsidian'}
$settings['workbench.startupEditor'] = 'none'
$settings | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath (Join-Path $userDirectory 'settings.json') -Encoding utf8
# A separate preview user-data directory leaves normal user settings untouched.
& code --new-window --user-data-dir $profileRoot "--extensionDevelopmentPath=$PSScriptRoot" (Join-Path $PSScriptRoot 'examples')
if ($LASTEXITCODE -ne 0) { throw "VS Code preview failed: $LASTEXITCODE" }
