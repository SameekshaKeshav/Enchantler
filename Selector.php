<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="styles.css">  
</head>

<body>
  <?php
    $lowerBudget = (int)$_POST["lowerbudget"];
    $higherBudget = (int)$_POST["higherbudget"];
    if($lowerBudget > $higherBudget)
    {
       $temp = $lowerBudget;
       $lowerBudget = $higherBudget;
       $higherBudget = $temp;
    }
    echo "<h1>Selected Vehicles : $lowerBudget - $higherBudget </h1>";
    $command = escapeshellcmd("python ./py/Selector.py $lowerBudget $higherBudget");
    shell_exec($command);
    $outputfile = fopen("./images/output.txt", "r") or die("Unable to open file!");
    echo fread($outputfile,filesize("./images/output.txt"));
    fclose($outputfile);
  ?>
</body>
</html>