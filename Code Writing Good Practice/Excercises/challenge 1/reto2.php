<?php
    $numero = $_POST['Numero'];
    $factorial = factorial($numero);

    printTable($numero, $factorial);

    function printNumberTable($number) {
        echo '<tr>';
        for ($i = 0; $i <= 10; $i++) {

            echo "<td>$number x $i</td>";
            echo "<td>$number * $i</td>";
        }
        echo '</tr>';
    }

    function factorial($number): int {
        $factorial = 1;
        for ($f = $number; $f >= 1; $f--) {
            $factorial *= $f;
        }
        return factorial;
    }

    function printTable($number, $factorial ) {
        echo '<table border="1">';
        printNumberTable($number);
        echo '<tr>';
        echo "<td>$number!</td>";
        echo "<td>$factorial</td>";
        echo '<tr>';
        echo '</table>';
    }
?>
