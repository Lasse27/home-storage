# Vue-Projekt bauen
# "--prefix HomeStorage.UI" sagt npm, wo das Package.json liegt
npm run build --prefix HomeStorage.UI

# Alten Flask Static-Ordner leeren
# -Recurse = alle Unterordner einbeziehen
# -Force = auch schreibgeschützte Dateien löschen
Remove-Item -Path "HomeStorage.Server\app\static\*" -Recurse -Force

#  Vue Build in Flask static kopieren
# -Recurse = alle Unterordner und Dateien kopieren
# -Force = bestehende Dateien überschreiben
Copy-Item -Path "HomeStorage.UI\dist\*" -Destination "HomeStorage.Server\app\static" -Recurse -Force

# Status ausgeben
Write-Host "Vue Build nach Flask static/ kopiert"
