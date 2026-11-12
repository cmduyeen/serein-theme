[CmdletBinding(SupportsShouldProcess)]
param([string]$DataPath = (Join-Path $env:USERPROFILE 'AppData\Roaming\Sublime Text'))
$ErrorActionPreference = 'Stop'
$source = Join-Path $PSScriptRoot 'Serein.sublime-package'
if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw 'Serein.sublime-package is missing.' }
$destination = Join-Path $DataPath 'Installed Packages\Serein.sublime-package'
if ($PSCmdlet.ShouldProcess($destination, 'Install Serein color schemes and interface themes without changing user preferences')) {
    if (Test-Path -LiteralPath $destination) {
        $backupRoot = Join-Path $env:USERPROFILE 'AppData\Local\Serein\SublimeText\backups'
        New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
        $backup = Join-Path $backupRoot ('Serein-' + (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + [guid]::NewGuid().ToString('N').Substring(0,8) + '.sublime-package')
        Copy-Item -LiteralPath $destination -Destination $backup
        Write-Host "Previous Serein package saved at: $backup"
    }
    New-Item -ItemType Directory -Path (Split-Path $destination -Parent) -Force | Out-Null
    Copy-Item -LiteralPath $source -Destination $destination -Force
    Write-Host 'Installed Serein. In Sublime Text, select both the Serein Color Scheme and UI Theme under Preferences.'
    Write-Host 'User preferences were not changed. Portable/Sublime Text 3 users can specify -DataPath.'
}
