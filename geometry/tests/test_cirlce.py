from geometry.circle import calculate_area


def test_calculate_area():
    assert calculate_area(1) == 3.141592653589793, "Wowza!"
    