<?php
    $command = escapeshellcmd('python ./py/MakevsEV.py');
    shell_exec($command);
    echo '<img src="./images/output.jpg" width="100%">'
?>