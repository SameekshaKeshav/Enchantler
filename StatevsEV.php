<?php
    $command = escapeshellcmd('python ./py/StatevsEV.py');
    shell_exec($command);
    echo '<img src="./images/output.jpg" width="100%">'
?>