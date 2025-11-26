import pytest
@pytest.mark.ramesh
def test_add():
    assert 5 + 5 == 10, "sum is not equal"
@pytest.mark.tippu
def test_sub():
    assert 5 - 4== 0, "sub is not equal"
@pytest.mark.sidhu
def test_login4():
    assert 5 - 4 == 0, "sub is not equl"
def test_validate_char():
    str1="hello"
    assert "h" in str1, "invalid character in 'h'"


