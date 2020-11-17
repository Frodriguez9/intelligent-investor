
'''Work in progress'''

#TO DO:
#   Check what method to call
#   pool the record of dividends
#   perform operation to detemine range. (current div - ave 20 years)

from yahoofinancials import YahooFinancials

#data2 = d._scrape_data('https://finance.yahoo.com/quote/appl','','financials')  THIS MAY BE A WAY TO ACCESS DIVIDENS

company = 'AAPL'
yahoo_financials = YahooFinancials(company)
data = yahoo_financials.get_financial_stmts('annual', 'income')
print(f'{data} \n\n')  # uncoment to see how data is structured


# Organizing Data.
# Note to self: You will use this data to evaluate if the company is an OPM Addict

annual_statements = data["incomeStatementHistory"][company] #a list containing dictionaries

print(f'4 YEARS OF INCOME STATEMETS FOR {company}\n')
for index in range(len(annual_statements)): #looping over each yearly statement
    for date in annual_statements[index]: # this loops over each key in my dictionary
        print(date)
        for accounting_item, value in annual_statements[index][date].items(): #loops over each of the accounting item of the Financial Statement (each item is the key of a dictionary)
            print(f"\t {accounting_item}: {value}")
        print('')



'''
Note to self: If you know the market cap of a company and you know its share
price, then figuring out the number of outstanding shares is easy. Just take
the market capitalization figure and divide it by the share price. The result
is the number of shares on which the market capitalization number was based.
'''

# TO DO: fork API and see if you can edit code to get EPS yearly for 10 years
print(yahoo_financials.get_earnings_per_share())
