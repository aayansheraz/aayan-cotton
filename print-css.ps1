$lines = [System.IO.File]::ReadAllLines("c:\Users\ayan\Desktop\ACI\aayan-cotton.html");
for($i=0; $i -lt $lines.Length; $i++) {
    if ($lines[$i] -match '\.products-grid\s*\{' -or $lines[$i] -match '\.sisters-grid\s*\{') {
        Write-Host "$i : $($lines[$i])"
        for($j=1; $j -lt 10; $j++) {
            Write-Host "$($i+$j) : $($lines[$i+$j])"
        }
    }
}
