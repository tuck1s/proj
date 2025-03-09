from proj.module1 import f1

def test_f1():
    assert f1(2) == 4
    assert f1(0) == 0
    assert f1(-3) == -6
