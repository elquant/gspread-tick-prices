import gspread
import settings
from datetime import date
import pandas_datareader.data as web

gc = gspread.service_account(filename=settings.GOOGLE_API_CREDENTIALS_PATH)

sh = gc.open("tick-prices")

sh.sheet1.update_cell(1, 1, 'Ticker')
sh.sheet1.update_cell(1, 2, 'Price')
sh.sheet1.update_cell(1, 3, 'Volume')

symbols = sh.sheet1.col_values(1)[1:]

for idx, symbol in enumerate(symbols):
    df = web.DataReader(symbol, settings.DATA_SOURCE, date.today(), date.today())
    sh.sheet1.update_cell(idx + 2, 1, symbol)
    sh.sheet1.update_cell(idx + 2, 2, "{}".format(df['Adj Close'][0]))
    sh.sheet1.update_cell(idx + 2, 3, "{}".format(df['Volume'][0]))
    
print(sh.sheet1.get_all_values())