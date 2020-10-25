from datetime import date
from yfinance import Ticker

# try out another library
from yahoo_fin import stock_info

# arr is an array of tuples, in the form (name, value)
def sort_fields(arr):
    # by the time we get to the last element, it will already be in its sorted
    # position, so we can stop one short of the last element
    for i in range(len(arr) - 1):
        local_min_index = i
        local_min_value = arr[i][1]

        # find the min value in the unsorted portion of the array, and swap it
        # into the sorted portion, as the last element of the sorted portion of
        # the array
        for curr_unsorted_index in range(i, len(arr)):
            curr_value = arr[curr_unsorted_index][1]
            if curr_value < local_min_value:
                local_min_index = curr_unsorted_index
                local_min_value = curr_value

        # do the swap
        temp_entry = arr[i]
        arr[i] = arr[local_min_index]
        arr[local_min_index] = temp_entry

def main():
    # get netflix ticker
    netflix_ticker = Ticker("NFLX")

    # decide what is stock price related and what is not
    probably_stock_prices = []
    probably_not_stock_prices = []
    for key in netflix_ticker.info:
        value = netflix_ticker.info[key]

        # skip over anything that's not a floating point number
        if type(value) != type(1.0):
            continue

        # separate things that are likely stock price related from things that
        # are not
        if value > 200:
            probably_stock_prices.append((key, value))
        else:
            probably_not_stock_prices.append((key, value))

    # sort the numbers
    sort_fields(probably_stock_prices)
    sort_fields(probably_not_stock_prices)

    # print everything out
    print("Using yfinance")
    print("Probably Stock Prices:")
    print("-------------------------------------")
    for entry in probably_stock_prices:
        print(format("{:40}{}".format(str(entry[0]) + ":", entry[1])))
    print()

    print("Probably Not Stock Prices:")
    print("-------------------------------------")
    for entry in probably_not_stock_prices:
        print("{:40}{}".format(str(entry[0]) + ":", entry[1]))
    print()


    # try with yahoo_fin library
    # http://theautomatic.net/2018/07/31/how-to-get-live-stock-prices-with-python/
    print("Using yahoo_fin")
    print("{:40}{}".format("Live Stock Price: ", stock_info.get_live_price("NFLX")))

main()
