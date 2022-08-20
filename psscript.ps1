#getting user bariable

function GetName(){
$input=Read-Host -Prompt "Give name"

Write-Host "hello $input"
switch($input){
 "paul"{Write-Host "fuck u"}
 "maggy"{echo "lv u" > "psexample.txt" }
 default{"fuck off bitch!!!"}

}
}

for($i=0;$i -lt 10;$i++){
Write-Host ""
}

$i=0;
while($i -le 5){
Write-Host "hello bitch"
$i++
}

Foreach($file in Get-ChildItem *.txt){
mv "$file" "$($file)."
}
Foreach($file in Get-ChildItem *.doc){
$file.Name |Rename-Item -NewName {$_ -replace ".doc",".txt"}
}

echo "helo" | Out-File  "just.txt"