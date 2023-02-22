def _cart_id(request) -> str:
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()  # TTL= Time to Live
        print(f"sesssssssss{cart}")
    return cart
