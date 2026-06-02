def paytm():
    print("Processing Paytm payment")


def phonepe():
    print("Processing PhonePe payment")


def process_payment(payment_method):
    payment_method()


process_payment(paytm)
process_payment(phonepe)