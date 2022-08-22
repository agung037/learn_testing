from product_value import goods_value


def test_base_price():
    # menguji dengan harga dasar / base good price yang valid
    assert goods_value(base_price=89, discount=15, shipping_mode="express") == "78.65"

    # menguji dengan invalid base goods price
    assert goods_value(base_price = -81, discount=17, shipping_mode="priority") == "invalid base price"


def test_discount():
    # menguji dengan presentase diskon yang valid
    assert goods_value(base_price=60, discount=7.5, shipping_mode="regular")  == "56.50"
    
    # menguji dengan  presentase diskon yang invalid (kurang dari 0% dan lebih dari 100%)
    assert goods_value(base_price=60, discount=-7.5, shipping_mode="regular") == "invalid discount"
    assert goods_value(base_price=60, discount=101, shipping_mode="regular") == "invalid discount"


def test_shipping_mode():
    # menguji dengan shipping mode yang valid
    assert goods_value(base_price=100, discount=60, shipping_mode="regular") == "41.00"
    assert goods_value(base_price=100, discount=60, shipping_mode="express") == "43.00"
    assert goods_value(base_price=100, discount=60, shipping_mode="priority") == "45.00"

    # menguji dengan shipping mode yang invalid
    assert goods_value(base_price=100, discount=60, shipping_mode="super") == "invalid shipping mode"