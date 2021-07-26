from math_series import __version__

from math_series.series import fibonacci,fibonacci_list,lucas_list,sum_series_list

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_list():
    expected=[0,1,1,2,3,5,8,13,21]
    actual=fibonacci_list([0,1,2,3,4,5,6,7,8])
    assert expected == actual

def test_lucas_list():
    expected=[2,1,3,4,7,11,18,29,47]
    actual=lucas_list([0,1,2,3,4,5,6,7,8])
    assert expected == actual
