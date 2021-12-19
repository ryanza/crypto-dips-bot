from packages import firebase, binanceapi
from flask import abort
from binance.spot import Spot as client


def main(request):

    if request.method == 'POST':
        resp = cancel_order(request)
        return resp
    elif request.method == 'GET':
        return 'Success', 200
    else:
        return abort(405)


def cancel_order(request):
    request_json = request.get_json(silent=True)
    symbol = request_json['symbol']
    order_id = request_json['order_id']
    firebase_order = firebase.get_document('orders', order_id)
    if firebase_order['status'] != 'PENDING':
        client.cancel_order(symbol, origClientOrderId=order_id)
    firebase.set_field('orders', order_id, 'status', 'CANCELLED')
    resp = f'Order {order_id} cancelled'
    return resp
