import pytest
from main import sum,esMayorQue

def testSum1():
    assert sum(2,5) == 7
    print("La función suma trabaja correctamente")

def testSum2():
    assert sum(3,4) == 7
    print("La función suma trabaja correctamente")

def testEsMayorQue():
    assert esMayorQue(10,2)
    print("La función es mayor trabaja correctamente")

@pytest.mark.parametrize(
    "inX,inY, esperado",
    [
        (3,4,7),
        (2,8,10),
        (100,200,300)
    ]
)
def testSumParam(inX, inY, esperado):
    assert sum(inX, inY)== esperado
    print("Las funciones parametrizadas trabajan correctamente")

if __name__ == '__main__':
    testSum1()
    testSum2()
    testEsMayorQue()
    
    
