# -*- coding: utf-8 -*-

# -- Sheet --

import json
import requests
import time
import csv

#1 Grab a list of quotes to get form Yahoo
apikey='B0s2lHE1CG6UECCaIeix07sHG90PSurea5gMzT3U'
url = "https://yfapi.net/v6/finance/quote"

headers = {
  'x-api-key': apikey
   }
# Takes stock input, makes call to API, returns stock information
# https://docs.python.org/3/tutorial/errors.html :
while True:
    try:
        # Takes stock input
        stock = input("Enter stock ticker:")
        # Makes API call
        querystring = {"symbols":stock}
        response = requests.request("GET", url, headers=headers, params=querystring)
        response.raise_for_status()
        stock_json = response.json()
        # Prints company name, current price, and (converted) market time
        # https://www.epochconvert.com/programming/python :
        print("Company Name: " + stock_json['quoteResponse']['result'][0]["displayName"] + "," + " Current Price:$" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]) + "," + " Market Time: " + (time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(stock_json['quoteResponse']['result'][0]["regularMarketTime"])))) 
        # Information to write to csv (stock ticker, converted time, market price)
        to_csv = [stock.upper() + ", " + str(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(stock_json['quoteResponse']['result'][0]["regularMarketTime"]))) + ", " + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])]
        # Appends to csv
        # https://realpython.com/python-csv/ : writing to a csv
        with open('yahoofinance.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows([to_csv])
            # Ends program if a valid stock ticker is entered
            break
    # Prompts user to enter a new stock ticker if they enter something invalid        
    except IndexError:
        print("Error: not a valid stock ticker")
    


# Resources: 
# https://docs.python.org/3/tutorial/errors.html : While True, try, except
# https://www.epochconvert.com/programming/python : converted time
# https://realpython.com/python-csv/ : writing to a csv


