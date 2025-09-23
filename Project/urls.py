import home, shop, user, cart

home.home.add_url_rule(rule= '/', view_func= home.render_home)
user.user.add_url_rule(rule= '/logout', view_func= user.logout)
shop.shop.add_url_rule(rule= '/delete_product', view_func= shop.delete_product)

user.user.add_url_rule(
    rule= "/registration",
    view_func= user.render_registration,
    methods = ["POST", "GET"]
)

user.user.add_url_rule(
    rule= "/authorization",
    view_func= user.render_authorization,
    methods= ["POST", "GET"]
)

shop.shop.add_url_rule(
    rule= "/shop",
    view_func= shop.render_shop,
    methods= ["POST", "GET"]
)
shop.shop.add_url_rule(
    rule= "/delete_product",
    view_func= shop.delete_product
)
shop.shop.add_url_rule(
    rule= "/shop/filter",
    view_func= shop.filter,
    methods= ["POST", "GET"]
)
cart.cart.add_url_rule(
    rule= "/cart",
    view_func= cart.render_cart
)





