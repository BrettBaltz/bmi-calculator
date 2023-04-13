from bmi_calculator import calc_bmi, get_bmi_category

def test_calc_bmi():
    assert calc_bmi(59.5, 90) == 18.3
    assert calc_bmi(63, 125) == 22.7
    assert calc_bmi(69, 170) == 25.7
    assert calc_bmi(72, 220) == 30.6

def test_get_bmi_category():
    assert get_bmi_category(0.1) == "Underweight"
    assert get_bmi_category(9.0) == "Underweight"
    assert get_bmi_category(18.4) == "Underweight"

    assert get_bmi_category(18.5) == "Normal weight"
    assert get_bmi_category(20.0) == "Normal weight"
    assert get_bmi_category(24.9) == "Normal weight"

    assert get_bmi_category(25.0) == "Overweight"
    assert get_bmi_category(27.5) == "Overweight"
    assert get_bmi_category(29.9) == "Overweight"

    assert get_bmi_category(30.0) == "Obese"
    assert get_bmi_category(35.0) == "Obese"
    assert get_bmi_category(100.0) == "Obese"