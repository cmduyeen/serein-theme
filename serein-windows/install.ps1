[CmdletBinding(SupportsShouldProcess)]
param(
    [ValidateSet('Light','Dark')][string]$Mode = 'Light',
    [switch]$Apply,
    [string]$InstallRoot = (Join-Path $env:USERPROFILE 'AppData\Local\Microsoft\Windows\Themes\Serein')
)
$ErrorActionPreference = 'Stop'
$stateRoot = Join-Path $env:USERPROFILE 'AppData\Local\Serein\Windows'
$selected = if ($Mode -eq 'Light') {'alabaster'} else {'obsidian'}
$installedTheme = Join-Path $InstallRoot "$selected.theme"
# Validate all sources before copying anything.
foreach ($name in @('alabaster','obsidian')) {
    foreach ($relative in @("$name.theme", "wallpapers\$name.png")) {
        if (-not (Test-Path -LiteralPath (Join-Path $PSScriptRoot $relative) -PathType Leaf)) {
            throw "Missing theme asset: $relative"
        }
    }
}
if (-not $PSCmdlet.ShouldProcess($InstallRoot, "Install both Serein Windows themes; Apply=$Apply")) { return }

if ($Apply) {
    # Capture the previous native theme before invoking Windows' theme handler.
    $current = Get-ItemPropertyValue -LiteralPath 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes' -Name CurrentTheme -ErrorAction Stop
    $current = [Environment]::ExpandEnvironmentVariables($current)
    if (-not (Test-Path -LiteralPath $current -PathType Leaf)) {
        throw 'Cannot locate current theme for rollback. Save your current theme in Windows Settings first, or install without -Apply.'
    }
    $backupDir = Join-Path $stateRoot ('backups\' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + [guid]::NewGuid().ToString('N').Substring(0,8))
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
    $backupTheme = Join-Path $backupDir 'previous.theme'
    # Preserve relative wallpaper paths relative to the original theme file.
    $original = [IO.File]::ReadAllText($current)
    $match = [regex]::Match($original, '(?m)^Wallpaper=(.*)\r?$')
    if ($match.Success -and $match.Groups[1].Value.Trim()) {
        $wallpaper = [Environment]::ExpandEnvironmentVariables($match.Groups[1].Value.Trim())
        if (-not [IO.Path]::IsPathRooted($wallpaper)) {
            $wallpaper = [IO.Path]::GetFullPath((Join-Path (Split-Path $current -Parent) $wallpaper))
            $original = [regex]::Replace($original, '(?m)^Wallpaper=.*$', [Text.RegularExpressions.MatchEvaluator]{ param($m) "Wallpaper=$wallpaper" })
        }
    }
    [IO.File]::WriteAllText($backupTheme, $original, [Text.UTF8Encoding]::new($true))
}

New-Item -ItemType Directory -Path (Join-Path $InstallRoot 'wallpapers') -Force | Out-Null
foreach ($name in @('alabaster','obsidian')) {
    Copy-Item -LiteralPath (Join-Path $PSScriptRoot "wallpapers\$name.png") -Destination (Join-Path $InstallRoot "wallpapers\$name.png") -Force
    $wallpaperPath = Join-Path $InstallRoot "wallpapers\$name.png"
    $content = [IO.File]::ReadAllText((Join-Path $PSScriptRoot "$name.theme"))
    $content = $content.Replace("Wallpaper=wallpapers\$name.png", "Wallpaper=$wallpaperPath")
    [IO.File]::WriteAllText((Join-Path $InstallRoot "$name.theme"), $content, [Text.UTF8Encoding]::new($true))
}
Write-Host "Installed Serein themes in: $InstallRoot"
if ($Apply) {
    @{ previousTheme=$backupTheme; originalThemePath=$current; installedTheme=$installedTheme; requested=(Get-Date).ToString('o') } |
        ConvertTo-Json | Set-Content -LiteralPath (Join-Path $stateRoot 'install-state.json') -Encoding utf8
    Start-Process -FilePath $installedTheme
    Write-Host 'Windows theme handler opened. Verify the selected theme in Settings > Personalization > Themes.'
} else {
    Write-Host "Open this file to apply: $installedTheme"
    Write-Host 'Use -Apply on this script if you want a rollback snapshot before activation.'
}
