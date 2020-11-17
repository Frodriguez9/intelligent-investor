from yahoofinancials import YahooFinancials
#tickers = 'AAPL'
#or
tickers = ['AAPL', 'WFC', 'F', 'JPY=X', 'XRP-USD', 'GC=F']
yahoo_financials = YahooFinancials(tickers)
balance_sheet_data = yahoo_financials.get_financial_stmts('quarterly', 'balance')
earnings_data = yahoo_financials.get_stock_earnings_data()
historical_prices = yahoo_financials.get_historical_price_data('2015-01-15', '2017-10-15', 'weekly')

line = '-' * 64


print(balance_sheet_data)
print(line)
