from BMI import calculate_bmi

def test_bmi_normal_weight():
    expected_return= 0
    actual_return = calculate_bmi(weight = "57", height = "1.65")
    assert actual_return==expected_return

