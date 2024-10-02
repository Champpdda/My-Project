from flask import Flask, render_template, request

app = Flask(__name__)

denominations = {
    "500 euro": 500,
    "200 euro": 200,
    "100 euro": 100,
    "50 euro": 50,
    "20 euro": 20,
    "10 euro": 10,
    "5 euro": 5,
    "2 euro": 2,
    "1 euro": 1,
    "50 cent": 0.50,
    "20 cent": 0.20,
    "10 cent": 0.10,
    "5 cent": 0.05,
    "2 cent": 0.02,
    "1 cent": 0.01,
}

def calculate_bill(bill_amount, tax_rate, tip_percentage, num_people):
    tax = bill_amount * (tax_rate / 100)
    tip = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tax + tip
    price_per_person = total_bill / num_people if num_people > 0 else 0
    return tax, tip, total_bill, price_per_person

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    bill_amount = float(request.form['billAmount'])
    tax_rate = float(request.form['taxRate'])
    tip_percentage = float(request.form['tipPercentage'])
    num_people = int(request.form['numPeople'])

    tax, tip, total_bill, price_per_person = calculate_bill(bill_amount, tax_rate, tip_percentage, num_people)

    return render_template('calculate.html', tax=tax, tip=tip, total_bill=total_bill, price_per_person=price_per_person)

@app.route('/payment', methods=['POST'])
def payment():
    total_bill = float(request.form['totalBill'])
    paid_amount = 0
    for denomination, value in denominations.items():
        count = int(request.form.get(denomination.replace(" ", "_"), 0))
        paid_amount += count * value

    if paid_amount >= total_bill:
        change = paid_amount - total_bill
        return render_template('payment.html', paid_amount=paid_amount, change=change)
    else:
        return render_template('payment.html', paid_amount=paid_amount, change=None, not_enough=True)

if __name__ == '__main__':
    app.run(debug=True)
