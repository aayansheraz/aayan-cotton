$lines = [System.IO.File]::ReadAllLines("c:\Users\ayan\Desktop\ACI\aayan-cotton.html");
for($i=3400; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match "^\s*'[a-zA-Z0-9\s/-]+':\s*\{") {
        Write-Host "$i : $($lines[$i])"
    }
}
