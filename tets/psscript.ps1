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