from packages import firebase
from flask import abort
import time


def main(request):

    if request.method == 'POST':
        resp = add_order(request)
        return resp
    elif request.method == 'GET':
        return 'Success', 200
    else:
        return abort(405)


def add_order(request):

    request_json = request.get_json(silent=True)
    symbol = request_json['symbol']
    amount = request_json['amount']
    percentage = request_json['percentage']
    refresh_rate = request_json['refresh_rate']

    # convert minutes to milliseconds
    refresh_rate = refresh_rate * 60000

    data = {
        'symbol': symbol,
        'amount': amount,
        'percentage': percentage,
        'refreshRate': refresh_rate,
        'status': 'PENDING',
        'timeadded': time.time() * 1000
    }

    order_id = firebase.add_document('orders', data)
    print(f"order added: {order_id}")

    return order_id
