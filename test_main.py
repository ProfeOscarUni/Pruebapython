import pytest
from main import sum,esMayorQue,login

def test_Sum1():
    assert sum(2,5) == 7
    print("La función suma trabaja correctamente")

def test_Sum2():
    assert sum(3,4) == 7
    print("La función suma trabaja correctamente")

def test_EsMayorQue():
    assert esMayorQue(10,2)
    print("La función es mayor trabaja correctamente")

@pytest.mark.parametrize(
    "inX, inY, esperado",
    [
        (3,4,7),
        (2,8,10),
        (100,200,300)
    ]
)
def test_SumParam(inX, inY, esperado):
    assert sum(inX, inY)== esperado
    print("Las funciones parametrizadas trabajan correctamente")
    
def test_LoginPass():
    loginPass = login("Pruebas", "1234")
    assert loginPass

def test_LoginFail():
    loginFail = login("Pruebas","1234")
    assert not loginFail

if __name__ == '__main__':
    test_Sum1()
    test_Sum2()
    test_EsMayorQue()
    test_LoginFail()
    test_LoginPass()
    
    
