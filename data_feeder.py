from nsetools import Nse
from tinydb import TinyDB, Query
import json
from datetime import datetime

print "Script started at: " + str(datetime.now())
try:
    nse = Nse()
    stocks_db = TinyDB("all_stocks.json")
    all_symbols = json.loads(nse.get_stock_codes(as_json=True))
    current_date = datetime.now()
    for each_symbol in all_symbols.keys():
        try:
            current_data = json.loads(nse.get_quote(str(each_symbol), as_json=True))
            final_data = {"high": current_data["dayHigh"],
                          "previousClose": current_data["previousClose"],
                          "open": current_data["open"],
                          "close": current_data["closePrice"],
                          "symbol": current_data["symbol"],
                          "low": current_data["dayLow"],
                          "date": str(current_date)}
            stocks_db.insert(final_data)
        except IndexError as ex:
            print "IndexError occurred for: " + each_symbol
            continue
        except ValueError as val:
            print "ValueError occurred for: " + each_symbol
            continue
        except Exception as ex:
            raise ex.message()
except Exception as ex:
    print(ex.message())
    raise ex
print "Script completed successfully at: " + str(datetime.now())
