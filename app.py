from flask import Flask, render_template, request
from utils import get_updates
import time

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def converter():
    update_data = get_updates()

    if not update_data:
        return "Failed to load exchange rates.", 500

    base_currency = update_data['base_code']
    rates = update_data['rates']
    currencies = list(rates.keys())
    last_update_unix = update_data['time_last_update_unix']

    result = None
    from_currency = to_currency = ''
    amount = 0.0

    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = float(request.form['amount'])

        if from_currency in rates and to_currency in rates:
            conversion_to_INR = amount / rates[from_currency]
            conversion_to_required = conversion_to_INR * rates[to_currency]
            result = round(conversion_to_required, 2)

    return render_template(
        "index.html",
        currencies=currencies,
        result=result,
        from_currency=from_currency,
        to_currency=to_currency,
        amount=amount,
        last_updated=time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(last_update_unix))
    )

if __name__ == "__main__":
    app.run(debug=True)
