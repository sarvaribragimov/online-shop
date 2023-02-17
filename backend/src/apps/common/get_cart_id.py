def _card_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
        cart = request.session.session_key
        return cart