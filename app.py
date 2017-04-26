import pandas as pd
import trade_functions

tf = trade_functions.Trader()

#example script using trade_functions

# dataframe to hold given stock data
GBCData = pd.DataFrame({'Stock Symbol': ['TEA', 'POP', 'ALE', 'GIN', 'JOE'], 'Type': ['COMMON', 'COMMON', 'COMMON', 'PREFERRED', 'COMMON'], 'Last Dividend': [0, 8, 23, 8, 13
                                                                                                                                                              ], 'Fixed Dividend': [0, 0, 0, 2, 0], 'Par Value': [100, 100, 60, 100, 250]})

# empty dataframe to hold records of trades
tradeRecords = pd.DataFrame(columns=('trade_time', 'stock', 'quantity', 'indicator', 'trade_price'))

# populate dataframe with example trades
tradeRecords = tf.record_trade(tradeRecords, 'GIN', 100, 'SELL', 5000)
tradeRecords = tf.record_trade(tradeRecords, 'GIN', 200, 'SELL', 4000)
tradeRecords = tf.record_trade(tradeRecords, 'ALE', 300, 'SELL', 3000)
tradeRecords = tf.record_trade(tradeRecords, 'TEA', 300, 'SELL', 3000)
tradeRecords = tf.record_trade(tradeRecords, 'POP', 300, 'SELL', 3000)
tradeRecords = tf.record_trade(tradeRecords, 'JOE', 300, 'SELL', 3000)

# example usage of the functions in trade_functions.

#result = tf.calc_dividend_yield(GBCData, 'GIN', 800)
#result = tf.calc_pe_ratio(GBCData, 'GIN', 750)
#result = tf.calc_vw_stock_price(tradeRecords, 'GIN', 15)

result = tf.calc_gbc_index(GBCData,tradeRecords,15)
print result
