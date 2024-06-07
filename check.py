import alpaca_trade_api as tradeapi
import json
key = json.loads(open('AUTH/auth.txt', 'r').read())
api = tradeapi.REST(key['APCA-API-KEY-ID'], key['APCA-API-SECRET-KEY'], base_url='https://paper-api.alpaca.markets')

# Check if the market is open now.
clock = api.get_clock()
print('The market is {}'.format('open.' if clock.is_open else 'closed.'))

# Check when the market was open on June 7, 2024
date = '2024-06-05'
calendar = api.get_calendar(start=date, end=date)[0]
print('The market opened at {} and closed at {} on {}.'.format(
    calendar.open,
    calendar.close,
    date
))