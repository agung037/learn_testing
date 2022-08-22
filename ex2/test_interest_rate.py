from interest_rate import interest_rate_of


def test_3_percent_rate():
    assert interest_rate_of(-50) == "invalid"
    assert interest_rate_of(89) == 0.03


def test_5_percent_rate():
    assert interest_rate_of(502) == 0.05


def test_7_percent_rate():
    assert interest_rate_of(91000) == 0.07