[CmdletBinding(SupportsShouldProcess)]
param()
$ErrorActionPreference = 'Stop'
$state = Get-Content -LiteralPath (Join-Path $env:USERPROFILE 'AppData\Local\Serein\Terminal\install-state.json') -Raw | ConvertFrom-Json
if ((Get-FileHash -LiteralPath $state.settingsPath).Hash -ne $state.installedHash) {
    throw 'Settings changed since installation. Restore manually from the backup to avoid losing later edits.'
}
if ($PSCmdlet.ShouldProcess($state.settingsPath, 'Restore exact pre-install Windows Terminal settings')) {
    Copy-Item -LiteralPath $state.backupPath -Destination $state.settingsPath -Force
    Write-Host 'Restored settings. Open a new terminal tab.'
}
