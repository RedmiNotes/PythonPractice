import pytest

def sum(a,b):
    return a+b

@pytest.mark.parametrize("input1,input2,output",
                  [(5,5,10),
                       (4,3,7)])
def test_add_1(input1,input2,output):
    result = sum(input1,input2)
    assert result == output

def test_add_2(input1,input2,output):
    result = sum(input1,input2)
    assert result == output