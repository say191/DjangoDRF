import stripe
from config.settings import STRIPE_API_KEY
stripe.api_key = STRIPE_API_KEY


def create_stripe_product_and_price(payment):
    """Create product and prie as objects using stripeApi"""
    stripe_product = stripe.Product.create(name=payment.paid_course.title)
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=payment.value * 100,
        product_data={"name": stripe_product['name']},
    )
    return stripe_price['id']


def create_stripe_session(stripe_price_id):
    """Create session as object using stripeApi"""
    stripe_session = stripe.checkout.Session.create(
        success_url="http://localhost:8000/",
        line_items=[{"price": stripe_price_id, "quantity": 1}],
        mode="payment",
    )
    return stripe_session['url'], stripe_session['id'], stripe_session['status']
