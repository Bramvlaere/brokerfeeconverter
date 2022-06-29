

#webapplication that calculates the monthly rental price with broker fee included

from flask import Flask, render_template, request
import os

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, 'brokerfeeconverter/templates')
print(TEMPLATE_PATH)
app = Flask(__name__,template_folder=TEMPLATE_PATH)



@app.route('/')
def first():
    return render_template('index.html', title='Home')

@app.route('/get_data', methods =["GET", "POST"])
def get_data():
    new_calc=''
    print('in get_data')
    if request.method == "GET":
        brokerfee = request.values.get('Brokerfee')
        price = request.values.get('RentM')
        print(brokerfee, price)
        new_calc=BrokerFeeCalculator(price,brokerfee)
        new_calc=f'Factual Monthly Price\n {new_calc.calculate_monthly_with_broker_feepercentage()}'
        print(new_calc,'this')
    return render_template("index.html",new_calc=new_calc)

class BrokerFeeCalculator:
    def __init__(self, price, broker_fee):
        self.price = float(price)
        self.broker_fee = float(broker_fee)
    
    def calculate_monthly_with_broker_feepercentage(self):
        return self.price + self.broker_fee * self.price / 100
    
    
if __name__ == '__main__':
    app.run()
    
    
    