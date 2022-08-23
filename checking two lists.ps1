
$locpath = "C:\Users\RICHARD MARTIN\Downloads\"
$csv1 = Import-Csv -Path "C:\Users\RICHARD MARTIN\Downloads\pics\testdata.csv"
$csv2 =Import-Csv -Path "C:\Users\RICHARD MARTIN\Downloads\pics\newdata.csv"
 
$list1 = $csv1 | select -ExpandProperty Name
$list2 = $csv2.Name


$oplists = New-Object System.Collections.ArrayList
$string = python .\order.py $list1 , $list2


Write-Host "---------------------"
Write-Host $string
Write-Host "---------------------"

foreach($el in $oplist){
Write-Host $el
Get-ChildItem "$locpath" *$el*
}
