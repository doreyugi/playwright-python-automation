from dataclasses import dataclass

@dataclass
class Payment:
    name_on_card: str
    card_number: str
    cvc: str
    expiration_month: str
    expiration_year: str

payment_info = Payment(
    name_on_card = "banana",
    card_number = "014454657",
    cvc = "123",
    expiration_month = "12",
    expiration_year = "2025"
)