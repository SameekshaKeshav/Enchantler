<?php
    $command = escapeshellcmd('python ./py/PricevsAvailable.py');
    $output = shell_exec($command);
    echo '<img src="./images/output.jpg" width="100%">'
?>