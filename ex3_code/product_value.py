def main():
    print(goods_value(base_price=89, discount=15, shipping_mode="express"))
    print(goods_value(base_price=60, discount=7.5, shipping_mode="regular"))
    print(goods_value(base_price=100, discount=60, shipping_mode="regular"))
    print(goods_value(base_price=100, discount=60, shipping_mode="express"))
    print(goods_value(base_price=100, discount=60, shipping_mode="priority"))
    pass


def goods_value(base_price, discount, shipping_mode):
    if base_price < 0 : return "invalid base price"
    if discount < 0 or discount > 100: return "invalid discount"
    if shipping_mode not in ["regular", "express", "priority"] : return  "invalid shipping mode"


    discount_value = (base_price * (discount/100))
    
    shipping_cost = 0
    if shipping_mode == "regular":
        shipping_cost = 1
    elif shipping_mode == "express":
        shipping_cost = 3
    elif shipping_mode == "priority":
        shipping_cost = 5
    
    goods_final_value = base_price - discount_value + shipping_cost
    
    return "{:.2f}".format(goods_final_value)

if __name__ == "__main__":
    main()