import pytest

from orderlab.pricing import subtotal


def test_subtotal_normal():
    assert subtotal(10_000, 2) == 20_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)


from orderlab.pricing import final_total


@pytest.mark.parametrize(
    "price, expected",
    [
        (49_999, 52_999),
        (50_000, 50_000),
        (50_001, 50_001),
    ],
)
def test_shipping_boundary(price, expected):
    assert final_total(price, 1, 0) == expected


@pytest.mark.parametrize("discount", [-1, 101])
def test_invalid_discount(discount):
    with pytest.raises(ValueError):
        final_total(10_000, 1, discount)


def test_discount():
    assert final_total(10_000, 2, 10) == 21_000

def test_subtotal_large_order():
    assert subtotal(10000, 10) == 100000
