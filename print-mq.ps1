$lines = [System.IO.File]::ReadAllLines("c:\Users\ayan\Desktop\ACI\aayan-cotton.html");
for($i=1200; $i -lt 1700; $i++) {
    if ($lines[$i] -match 'grid') {
        Write-Host "$i : $($lines[$i])"
    }
}
