import os
from binance.spot import Spot as Client

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
client = Client(base_url='https://testnet.binance.vision', key=api_key, secret=api_secret)


def get_symbol_data(symbol):
    symbol_data = client.exchange_info(symbol)

    data = {'symbol': symbol_data['symbols'][0]['symbol'],
            'minPrice': symbol_data['symbols'][0]['filters'][0]['minPrice'],
            'maxPrice': symbol_data['symbols'][0]['filters'][0]['maxPrice'],
            'tickSize': symbol_data['symbols'][0]['filters'][0]['tickSize'],
            'minQty': symbol_data['symbols'][0]['filters'][2]['minQty'],
            'maxQty': symbol_data['symbols'][0]['filters'][2]['maxQty'],
            'stepSize': symbol_data['symbols'][0]['filters'][2]['stepSize'],
            'minNotional': symbol_data['symbols'][0]['filters'][3]['minNotional']}

    return data


def get_current_price(symbol):
    data = float(client.ticker_price(symbol)['price'])
    return data


def get_binance_orders_by_symbol(symbol):
    data = client.get_orders(symbol)
    return data


def get_binance_open_orders_by_symbol(symbol):
    data = client.get_open_orders(symbol)
    return data


def get_all_binance_open_orders():
    data = client.get_open_orders()
    return data


def get_binance_order_by_id(symbol, order_id):
    data = client.get_order(symbol, origClientOrderId=order_id)
    return data
