# Removes all pycache folders from the project repository
Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | ForEach-Object {
    Write-Host "Removing folder:" $_.FullName
    Remove-Item -Path $_.FullName -Recurse -Force
}