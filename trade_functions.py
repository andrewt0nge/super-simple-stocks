import pandas as pd
from datetime import datetime as dt, timedelta
from decimal import *


class Trader(object):
	"""class holding trade functions"""


	# function to record each trade, returns the input dataframe with the new trade appended.
	def record_trade(self,input_dataframe, stock, quantity, indicator, tradeprice):
	    tradetime = dt.utcnow()  # timestamp the trade with the current time
	    newtrade = pd.DataFrame({'trade_time': [tradetime], 'stock': [stock], 'quantity': [
	                            quantity], 'indicator': [indicator], 'trade_price': [tradeprice]})
	    output_dataframe = input_dataframe.append(newtrade)
	    return output_dataframe

	# function to calculate the dividend yield for common or preferred stocks. 
	# requires a dataframe of stocks as input
	def calc_dividend_yield(self,input_dataframe,stock, marketprice):
	    current_stock = input_dataframe[input_dataframe['Stock Symbol'] == stock] # Get input stock from dataframe
	    if current_stock['Type'].values == 'COMMON':
	        dividend_yield = current_stock['Last Dividend'].values / Decimal(marketprice)
	        return dividend_yield

	    elif current_stock['Type'].values == 'PREFERRED':
	        dividend_yield = current_stock['Fixed Dividend'].values * current_stock['Par Value'].values / Decimal(marketprice)
	        return dividend_yield
	    else :
	    	print('Stock not COMMON or PREFERRED')

	# function to calculate the PE ratio of a given stock.
	# requires a dataframe of stock data as input	        
	def calc_pe_ratio(self,input_dataframe,stock, marketprice):
	    current_stock = input_dataframe[input_dataframe['Stock Symbol'] == stock] # Get input stock from dataframe
	    pe_ratio =   Decimal(marketprice) / current_stock['Last Dividend'].values
	    return pe_ratio

	# function to calculate the volume weighted stock price 
	# requires a dataframe of trade data as input, timeframe in minutes
	def calc_vw_stock_price(self,input_dataframe,stock,timeframe):
	    stocks_in_timeframe = input_dataframe[ (input_dataframe['stock'] == stock) & (input_dataframe['trade_time'] >  dt.utcnow() - timedelta(minutes=timeframe)) ]
	    
	    trade_price_qty = 0 #
	    for index, row in stocks_in_timeframe.iterrows(): 
	        trade_price_qty = trade_price_qty + Decimal(row['trade_price']) * Decimal(row['quantity'])
	     
	    return  trade_price_qty / Decimal(stocks_in_timeframe.groupby('stock')['quantity'].sum().values[0])	 # divide the sum of each (trade * qty) by the total qty of shares

	#function to calculate the GBC index
	#requires dataframe of stocks in the exchange, dataframe of trades and the timeframe to calculate the index value.
	def calc_gbc_index(self,exchange_dataframe,trades_dataframe,timeframe):
	    index_product = 1 
	    for index, row in exchange_dataframe.iterrows():
	        index_product = index_product * self.calc_vw_stock_price(trades_dataframe,row['Stock Symbol'],timeframe)  # multiply the vol. weighted price of each stock 
	    return index_product ** 1 / exchange_dataframe['Stock Symbol'].count()  # raise the index_product to the power of 1 / no. stocks in the exchange. (looked geometric mean up online as I have not encountered it before...)








