param([ValidateSet('Light', 'Dark')][string]$Mode = 'Light', [switch]$Preview)
$ErrorActionPreference = 'Stop'
$palette = Get-Content -LiteralPath (Join-Path $PSScriptRoot "schemes\$($Mode.ToLower()).json") -Raw | ConvertFrom-Json
$esc = [char]27
function Get-SereinColor([string]$Hex) {
    $rgb = @(1,3,5 | ForEach-Object { [Convert]::ToInt32($Hex.Substring($_,2),16) })
    return "$esc[38;2;$($rgb[0]);$($rgb[1]);$($rgb[2])m"
}
if (Get-Module -ListAvailable PSReadLine) {
    Import-Module PSReadLine
    Set-PSReadLineOption -Colors @{
        Default = (Get-SereinColor $palette.foreground)
        Command = (Get-SereinColor $palette.foreground)
        Keyword = (Get-SereinColor $palette.purple)
        String = (Get-SereinColor $palette.green)
        Operator = (Get-SereinColor $palette.foreground)
        Variable = (Get-SereinColor $palette.blue)
        Parameter = (Get-SereinColor $palette.foreground)
        Type = (Get-SereinColor $palette.cyan)
        Number = (Get-SereinColor $palette.yellow)
        Member = (Get-SereinColor $palette.foreground)
        Comment = (Get-SereinColor $palette.brightBlack)
        Error = (Get-SereinColor $palette.red)
        InlinePrediction = (Get-SereinColor $palette.brightBlack)
    }
}
if ($PSVersionTable.PSVersion.Major -ge 7) {
    $PSStyle.Formatting.Error = Get-SereinColor $palette.red
    $PSStyle.Formatting.Warning = Get-SereinColor $palette.yellow
    $PSStyle.Formatting.Verbose = Get-SereinColor $palette.brightBlack
    $PSStyle.Formatting.Debug = Get-SereinColor $palette.brightBlack
    $PSStyle.Formatting.TableHeader = Get-SereinColor $palette.foreground
    $PSStyle.Formatting.FormatAccent = Get-SereinColor $palette.purple
}
Write-Host "Serein Terminal - $Mode"
if ($Preview) { & (Join-Path $PSScriptRoot 'preview.ps1') }
# A local receipt proves this session started inside Windows Terminal; no telemetry is sent.
if ($env:WT_SESSION) {
    @{ mode=$Mode; terminalSession=$env:WT_SESSION; pid=$PID; started=(Get-Date).ToString('o') } |
        ConvertTo-Json | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'last-session.json') -Encoding utf8
}
