<?php

$type = $_POST["type"];


if ($type == "search_id"){
    $text = $_POST["text"];
    $cmd = '/usr/bin/python ./disease_to_drug.py ' . $text;

}else if($type == "search_drug"){
    $text = $_POST["text"];
    $row_num = $_POST["row_num"];
    $cmd = '/usr/bin/python ./get_clinicaltrial.py "' . $text . '" ' . $row_num;
    #$cmd = '/usr/bin/python ./get_clinicaltrial.py ' . $text;
}


$result = exec($cmd, $output, $status);


print_r ($output[0]);
#print_r ($return_ver);

?>
