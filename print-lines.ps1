$lines = [System.IO.File]::ReadAllLines("c:\Users\ayan\Desktop\ACI\aayan-cotton.html");
for($i=3620; $i -lt 3635; $i++) {
    Write-Host "$i : $($lines[$i].Substring(0, [math]::Min($lines[$i].Length, 150)))"
}
