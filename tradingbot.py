from lumibot.brokers import Alpaca
from lumibot.backtesting import YahooDataBacktesting
from lumibot.strategies.strategy import Strategy
from lumibot.traders import Trader
from datetime import datetime
from dotenv import load_dotenv, dotenv_values
from alpaca_trade_api import REST
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.trading.requests import GetOrdersRequest
from timedelta import Timedelta
from finbert_utils import estimate_sentiment
from NLP_Strategy import MLTrader


config=dotenv_values(".env")
API_KEY = config['API_KEY']
API_SECRET = config['SECRET_KEY']
BASE_URL ="https://paper-api.alpaca.markets"

ALPACA_CREDS = {
    "API_KEY":API_KEY,
    "API_SECRET":API_SECRET,
    "PAPEr":True
}   

# Function to create and place order
def place_order(trading_client, symbol, qty, side):
  market_order_data = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=side,
        time_in_force=TimeInForce.DAY
        )

# Preparing Market order
  market_order = trading_client.submit_order(
        order_data=market_order_data
        )
  

start_date = datetime(2023,1,1)
end_date = datetime(2024,5,10)

broker = Alpaca(ALPACA_CREDS)
strategy = MLTrader(name='mlstrat',
                    broker=broker,
                    parameters={"symbol":"SPY",
                                "cash_at_risk":0.5})

# strategy.backtest(YahooDataBacktesting,
#                    start_date,
#                    end_date,
#                    parameters={"symbol":"SPY","cash_at_risk":0.5})


trader = Trader()
trader.add_strategy(strategy)
trader.run_all()