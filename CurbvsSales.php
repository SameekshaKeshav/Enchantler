<?php
    $command = escapeshellcmd('python ./py/CurbvsSales.py');
    $output = shell_exec($command);
    echo '<img src="./images/output.jpg" width="100%">'
?>