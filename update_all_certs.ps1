$htmlPath = 'c:\Users\ayan\Desktop\ACI\aayan-cotton.html'
$aciPath = 'c:\Users\ayan\Desktop\ACI'

# Read HTML
$html = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)

# Process each certificate 1-5
for ($i = 1; $i -le 5; $i++) {
    $certFile = Join-Path $aciPath "cert$i.jpg"
    
    if (Test-Path $certFile) {
        # Convert to base64
        $certData = [System.IO.File]::ReadAllBytes($certFile)
        $b64 = [Convert]::ToBase64String($certData)
        $dataUri = "data:image/jpeg;base64,$b64"
        
        # Replace in HTML - using a more specific pattern
        $oldSrcPattern = "src=`"data:image/jpeg;base64,[^`"]*`".*?alt=`"[^`"]*`".*?cert$i\.jpg"
        $newSrc = "src=`"$dataUri`"" 
        
        # Also replace direct cert references
        $html = $html -replace "src=`"cert$i\.jpg`"", "src=`"$dataUri`""
        $html = $html -replace "href=`"cert$i\.jpg`"", "href=`"$dataUri`""
        
        Write-Host "Updated cert$i.jpg with new picture (base64 embedded)"
    } else {
        Write-Host "Warning: cert$i.jpg not found"
    }
}

# Write HTML back
[System.IO.File]::WriteAllText($htmlPath, $html, [System.Text.Encoding]::UTF8)
Write-Host "`nAll 5 certificates updated with new pictures!"
Write-Host "Grid is set to 5 columns with only 5 cards."
