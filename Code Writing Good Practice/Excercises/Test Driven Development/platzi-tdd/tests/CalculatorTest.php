<?php

use PHPUnit\Framework\TestCase;

class CalculatorTest extends TestCase {

    public function testAddWillReturnTheSumOfItsParameters(){
        $sut = new Calculator(); # Suject under test Es un nombre común para las pruebas
        
        $this->assertEquals(8, $sut->add(5,3));
        $this->assertEquals(5, $sut->add(5,0));
    }

}