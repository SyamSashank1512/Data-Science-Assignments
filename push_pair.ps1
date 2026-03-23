# Helper script to push a pair
param (
    [string]$Notebook,
    [string]$CSV,
    [string]$Message
)

if (-not $Notebook -or -not $CSV -or -not $Message) {
    Write-Host "Usage: .\push_pair.ps1 -Notebook 'File.ipynb' -CSV 'File.csv' -Message 'Message'" -ForegroundColor Yellow
    exit
}

git add "Assginment_Codes/$Notebook"
git add "Assginment_CSV/$CSV"
git commit -m "$Message"
git push origin main
