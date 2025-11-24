# Build ui
npm run build --prefix HomeStorage.UI
$staticP = "HomeStorage.Server\app"
$staticF = "HomeStorage.Server\app\static"

# Alten Flask Static-Ordner löschen
if ((Test-Path $staticF)) {
    Remove-Item -Path $staticF -Recurse -Force
}

# Ordner neu erstellen
New-Item $staticP -Name "static" -ItemType Directory

#  Vue Build in Flask static kopieren
Copy-Item -Path "HomeStorage.UI\dist\*" -Destination "HomeStorage.Server\app\static" -Recurse -Force

# Status ausgeben
Write-Host "Vue Build nach Flask static/ kopiert"

