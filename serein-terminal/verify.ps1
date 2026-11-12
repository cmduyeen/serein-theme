$ErrorActionPreference = 'Stop'
function Assert-Serein([bool]$Condition, [string]$Message) {
    if (-not $Condition) { throw $Message }
}
# Isolate installer tests so they cannot overwrite a real install receipt or user settings.
$testRoot = Join-Path ([IO.Path]::GetTempPath()) ('serein-terminal-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $testRoot, (Join-Path $testRoot 'schemes'), (Join-Path $testRoot 'backups') | Out-Null
foreach ($name in @('install.ps1','restore.ps1','session.ps1','preview.ps1')) {
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot $name) -Destination $testRoot
}
Copy-Item -Path (Join-Path $PSScriptRoot 'schemes\*.json') -Destination (Join-Path $testRoot 'schemes')
foreach ($script in Get-ChildItem -LiteralPath $PSScriptRoot -Filter '*.ps1') {
    $tokens=$null; $parseErrors=$null
    $null = [Management.Automation.Language.Parser]::ParseFile($script.FullName,[ref]$tokens,[ref]$parseErrors)
    Assert-Serein (@($parseErrors).Count -eq 0) "Syntax error: $($script.Name): $parseErrors"
}
$settingsPath = Join-Path $testRoot 'settings.json'
$fixture = @'
{
  // Preserve semantic settings and back up original comments exactly.
  "defaultProfile": "original",
  "profiles": {"defaults": {"historySize": 1234}, "list": [{"guid":"original", "name":"Existing", "font":{"size":13}}]},
  "schemes": [{"name":"Existing scheme","background":"#000000"}],
  "actions": [{"command":"paste", "keys":"ctrl+v"}],
  "customData": {"untouched": true},
}
'@
[IO.File]::WriteAllText($settingsPath, $fixture)
& (Join-Path $testRoot 'install.ps1') -SettingsPath $settingsPath -Mode Dark -SetDefault -WhatIf
Assert-Serein ([IO.File]::ReadAllText($settingsPath) -ceq $fixture) 'WhatIf changed settings.'
& (Join-Path $testRoot 'install.ps1') -SettingsPath $settingsPath -Mode Dark -SetDefault
$first = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json -AsHashtable
Assert-Serein ($first.profiles.list.Count -eq 3 -and $first.schemes.Count -eq 3) 'Profiles or schemes missing.'
Assert-Serein ($first.profiles.list[0].font.size -eq 13 -and $first.profiles.defaults.historySize -eq 1234) 'Existing profile changed.'
Assert-Serein ($first.customData.untouched -and $first.actions[0].command -eq 'paste') 'Unrelated settings changed.'
$firstState = Get-Content -LiteralPath (Join-Path $testRoot 'install-state.json') -Raw | ConvertFrom-Json
Assert-Serein ([IO.File]::ReadAllText($firstState.backupPath) -ceq $fixture) 'Backup was not exact.'
& (Join-Path $testRoot 'install.ps1') -SettingsPath $settingsPath -Mode Light -SetDefault
$second = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json -AsHashtable
Assert-Serein ($second.profiles.list.Count -eq 3 -and $second.schemes.Count -eq 3) 'Repeat install duplicated entries.'
Assert-Serein ($second.defaultProfile -eq '{53889a55-b849-4817-9364-886a4cfeae71}') 'Default profile not selected.'
$installed = [IO.File]::ReadAllText($settingsPath)
[IO.File]::AppendAllText($settingsPath, ' ')
$refused = $false
try { & (Join-Path $testRoot 'restore.ps1') } catch { $refused = $true }
Assert-Serein $refused 'Restore overwrote later edits.'
[IO.File]::WriteAllText($settingsPath, $installed, [Text.UTF8Encoding]::new($false))
& (Join-Path $testRoot 'restore.ps1')
$restored = Get-Content -LiteralPath $settingsPath -Raw | ConvertFrom-Json -AsHashtable
Assert-Serein ($restored.defaultProfile -eq $first.defaultProfile) 'Restore did not recover previous installation.'
Write-Host 'PASS: syntax, JSONC, dry-run, preservation, exact backup, repeat install, default selection, guarded restore.'
