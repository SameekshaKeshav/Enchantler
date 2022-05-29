<?php
    $command = escapeshellcmd('python ./py/MakevsAvailable.py');
    $output = shell_exec($command);
    echo '<img src="./images/output.jpg" width="100%">'
?>