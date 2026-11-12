[CmdletBinding(SupportsShouldProcess)]
param(
    [ValidateSet('Light','Dark')][string]$Mode = 'Light',
    [string]$SettingsPath,
    [switch]$SetDefault,
    [switch]$Launch
)
$ErrorActionPreference = 'Stop'
if (-not $SettingsPath) {
    # Resolve the actual user path, not the AppContainer-redirected LOCALAPPDATA.
    $base = Join-Path $env:USERPROFILE 'AppData\Local'
    $candidates = @(
        (Join-Path $base 'Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json'),
        (Join-Path $base 'Microsoft\Windows Terminal\settings.json')
    ) | Where-Object { Test-Path -LiteralPath $_ }
    if (@($candidates).Count -ne 1) { throw 'Specify -SettingsPath: expected exactly one Windows Terminal configuration.' }
    $SettingsPath = @($candidates)[0]
}
$original = [IO.File]::ReadAllText($SettingsPath)
$settings = $original | ConvertFrom-Json -AsHashtable
if (-not $settings.profiles -or -not $settings.profiles.Contains('list')) { throw 'Unsupported profiles structure.' }
$guids = @{ Light='{53889a55-b849-4817-9364-886a4cfeae71}'; Dark='{e1df67f3-cb2d-4a40-b905-84f9b5cf79be}' }
$schemes = @('light','dark' | ForEach-Object {
    Get-Content -LiteralPath (Join-Path $PSScriptRoot "schemes\$_.json") -Raw | ConvertFrom-Json -AsHashtable
})
$schemeNames = @($schemes | ForEach-Object { $_.name }) + @('Healthy Warm Alabaster', 'Healthy Warm Obsidian')
$settings.schemes = @($settings.schemes | Where-Object { $_.name -notin $schemeNames }) + $schemes
$settings.profiles.list = @($settings.profiles.list | Where-Object { $_.guid -notin @($guids.Values) })
foreach ($variant in @('Light','Dark')) {
    $sessionPath = Join-Path $PSScriptRoot 'session.ps1'
    $settings.profiles.list += @{
        guid=$guids[$variant]; name="Serein Terminal $variant"; hidden=$false
        commandline="pwsh.exe -NoLogo -NoExit -File `"$sessionPath`" -Mode $variant"
        startingDirectory=(Split-Path $PSScriptRoot -Parent)
        colorScheme=($schemes | Where-Object { $_.name -eq $(if ($variant -eq 'Light') {'Serein Alabaster'} else {'Serein Obsidian'}) }).name
        font=@{face='Cascadia Mono'; size=14; weight='normal'; cellHeight='1.3'}
        padding='16, 12, 16, 12'; opacity=100; useAcrylic=$false
        cursorShape='bar'; intenseTextStyle='bold'; backgroundImage=$null
    }
}
if ($SetDefault) { $settings.defaultProfile = $guids[$Mode] }
$newJson = $settings | ConvertTo-Json -Depth 100
$null = $newJson | ConvertFrom-Json
if ($PSCmdlet.ShouldProcess($SettingsPath, 'Back up and install Serein Terminal profiles and schemes')) {
    New-Item -ItemType Directory -Path (Join-Path $PSScriptRoot 'backups') -Force | Out-Null
    $backup = Join-Path $PSScriptRoot ("backups\settings-{0}-{1}.json" -f (Get-Date -Format 'yyyyMMdd-HHmmss'), [guid]::NewGuid().ToString('N').Substring(0,8))
    [IO.File]::WriteAllText($backup, $original, [Text.UTF8Encoding]::new($false))
    # Avoid replacing a configuration edited since it was read.
    if ([IO.File]::ReadAllText($SettingsPath) -cne $original) { throw 'Settings changed during install; retry.' }
    [IO.File]::WriteAllText($SettingsPath, $newJson, [Text.UTF8Encoding]::new($false))
    @{ settingsPath=$SettingsPath; backupPath=$backup; installedHash=(Get-FileHash -LiteralPath $SettingsPath).Hash } |
        ConvertTo-Json | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'install-state.json') -Encoding utf8
    Write-Host "Installed both profiles. Backup: $backup"
    if ($Launch) {
        & wt.exe -w new new-tab -p "Serein Terminal $Mode" pwsh.exe -NoLogo -NoExit -File $sessionPath -Mode $Mode -Preview
        if ($LASTEXITCODE -ne 0) { throw "Terminal launch failed: $LASTEXITCODE" }
    }
}
