[CmdletBinding(SupportsShouldProcess)]
param()
$ErrorActionPreference = 'Stop'
$statePath = Join-Path $env:USERPROFILE 'AppData\Local\Serein\Windows\install-state.json'
$state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
if (-not (Test-Path -LiteralPath $state.previousTheme -PathType Leaf)) { throw 'Previous theme snapshot is missing.' }
$current = Get-ItemPropertyValue -LiteralPath 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Themes' -Name CurrentTheme
$current = [Environment]::ExpandEnvironmentVariables($current)
if ([IO.Path]::GetFullPath($current) -ine [IO.Path]::GetFullPath($state.installedTheme)) {
    throw 'Windows is using another theme. To avoid replacing a newer choice, open the saved previous.theme manually from AppData\Local\Serein\Windows\backups.'
}
if ($PSCmdlet.ShouldProcess($state.previousTheme, 'Open previous Windows theme')) {
    Start-Process -FilePath $state.previousTheme
    Write-Host 'Opened previous theme. This restores the saved theme, not every Windows personalization setting.'
}
