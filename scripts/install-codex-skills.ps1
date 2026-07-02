param(
    [string]$CodexHome = "$HOME\.codex"
)

$ErrorActionPreference = "Stop"

$projectRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$source = Join-Path $projectRoot ".codex\skills"
$target = Join-Path $CodexHome "skills"

if (-not (Test-Path -LiteralPath $source)) {
    throw "Project skills folder not found: $source"
}

New-Item -ItemType Directory -Path $target -Force | Out-Null

$skills = Get-ChildItem -LiteralPath $source -Directory | Where-Object { $_.Name -ne ".system" }
foreach ($skill in $skills) {
    $destination = Join-Path $target $skill.Name
    New-Item -ItemType Directory -Path $destination -Force | Out-Null
    Copy-Item -Path (Join-Path $skill.FullName "*") -Destination $destination -Recurse -Force
    Write-Host "Installed skill: $($skill.Name)"
}

Write-Host ""
Write-Host "Done. Restart Codex and open a new thread, then run /skills."

