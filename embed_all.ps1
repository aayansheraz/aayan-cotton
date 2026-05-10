$htmlPath = 'c:\Users\ayan\Desktop\ACI\aayan-cotton.html'
$aciPath = 'c:\Users\ayan\Desktop\ACI'
$html = [System.IO.File]::ReadAllText($htmlPath, [System.Text.Encoding]::UTF8)

for ($i = 1; $i -le 4; $i++) {
    $certFile = Join-Path $aciPath "cert$i.jpg"
    
    if (Test-Path $certFile) {
        $certData = [System.IO.File]::ReadAllBytes($certFile)
        $b64 = [Convert]::ToBase64String($certData)
        $dataUri = "data:image/jpeg;base64,$b64"
        
        $html = $html -replace "src=`"cert$i\.jpg`"", "src=`"$dataUri`""
        $html = $html -replace "href=`"cert$i\.jpg`"", "href=`"$dataUri`""
        
        Write-Host "Embedded cert$i.jpg"
    }
}

[System.IO.File]::WriteAllText($htmlPath, $html, [System.Text.Encoding]::UTF8)
Write-Host "All certificates embedded!"
