from __future__ import print_function
import exp_utils
from exp_utils import Order
import sys


def dummy(prices):
    return True


def bondBuyExec(prices):
    price = prices.getStockSell('BOND')
    if price[0] < 1000:
        order = Order('add', 0, 'BOND', 'BUY', price[0], price[1])
        print(order.getOrderString(), file=prices.exchange)
        print(order.getOrderString())


def bondSellExec(prices):
    price = prices.getStockBuy('BOND')
    if price[0] > 1000:
        order = Order('add', 0, 'BOND', 'SELL', price[0], price[1])
        print(order.getOrderString(), file=prices.exchange)
        print(order.getOrderString())


"""
Determines if buying XLF, converting it to the bundle and reselling the bundle is a good idea and executes
Should be attacked to: ["XLF","BOND","GS","MS","WFC"]
"""
def XLFtoStockTest(prices):
    XLFTuple = prices.getStockBuy("XLF")
    BondTuple = prices.getStockSell("BOND")
    GSTuple = prices.getStockSell("GS")
    MSTuple = prices.getStockSell("MS")
    WFCTuple = prices.getStockSell("WFC")

    max_trade = min(XLFTuple[1]/10, BondTuple[1]/3, GSTuple[1]/2, MSTuple[1]/3, WFCTuple[1]/2)
    XLFValue = XLFTuple[0]*max_trade*10
    BundleValue = sum([BondTuple[0]*max_trade*3, GSTuple[0]*max_trade*2, MSTuple[0]*max_trade*3, WFCTuple[0]*max_trade*2])
    if XLFValue + 100 < BundleValue:
        tradeXLF(prices, max_trade, XLFTuple[0], BondTuple[0], GSTuple[0], MSTuple[0], WFCTuple[0])

def tradeXLF(trade_sz, XFLprice, BONDprice, GSprice, MSprice, WFCprice):
    exp_utils.buy(prices, "XLF", trade_sz*10, XFLprice)
    exp_utils.convert(prices, "XLF", False, trade_sz*10) #True = BUY
    exp_utils.sell(prices, "BOND", trade_sz*3, BONDprice)
    exp_utils.sell(prices, "GS", trade_sz*2, GSprice)
    exp_utils.sell(prices, "MS", trade_sz*3, MSprice)
    exp_utils.sell(prices, "WFC", trade_sz*2, WFCprice)


"""
Determines if buying the XLF components, converting it to an XLF ETF and reselling the ETF is a good idea and executes
Should be attacked to: ["XLF","BOND","GS","MS","WFC"]
"""
def StocktoXFLTest(prices):
    XLFTuple = prices.getStockSell("XLF")
    BondTuple = prices.getStockBuy("BOND")
    GSTuple = prices.getStockBuy("GS")
    MSTuple = prices.getStockBuy("MS")
    WFCTuple = prices.getStockBuy("WFC")

    max_trade = min(XLFTuple[1]/10, BondTuple[1]/3, GSTuple[1]/2, MSTuple[1]/3, WFCTuple[1]/2)
    XLFValue = XLFTuple[0]*max_trade*10
    BundleValue = sum([BondTuple[0]*max_trade*3, GSTuple[0]*max_trade*2, MSTuple[0]*max_trade*3, WFCTuple[0]*max_trade*2])
    if BundleValue + 100 < XLFValue:
        tradeXLFBundle(prices, max_trade, XLFTuple[0], BondTuple[0], GSTuple[0], MSTuple[0], WFCTuple[0])


def tradeXLFBundle(prices, trade_sz, XFLprice, BONDprice, GSprice, MSprice, WFCprice):
    exp_utils.buy(prices, "BOND", trade_sz*3, BONDprice)
    exp_utils.buy(prices, "GS", trade_sz*2, GSprice)
    exp_utils.buy(prices, "MS", trade_sz*3, MSprice)
    exp_utils.buy(prices, "WFC", trade_sz*2, WFCprice)
    exp_utils.convert(prices, "XLF", True, trade_sz*10) #True = BUY
    exp_utils.sell(prices, "XLF", trade_sz*10, XFLprice)


"""
Checks for a possible transaction between VALE and VALBZ and executes it
"""
def tradeVALEAndVALBZ(prices):
    VALEBuyTuple = prices.getStockSell("VALE")
    VALESellTuple = prices.getStockBuy("VALE")
    VALBZBuyTuple = prices.getStockSell("VALBZ")
    VALBZSellTuple = prices.getStockSell("VALBZ")
    max_tradeVALE2VALBZ = min(VALEBuyTuple[1], VALBZSellTuple[1])
    max_tradeVALBZ2VALE = min(VALBZBuyTuple[1], VALESellTuple[1])
    if VALEBuyTuple[0]*max_tradeVALE2VALBZ + 10 < VALBZSellTuple[0]*max_tradeVALE2VALBZ:
        tradeVALEforVALBZ(prices, max_tradeVALE2VALBZ, VALEBuyTuple[0], VALBZSellTuple[0])
    if VALBZBuyTuple[0]*max_tradeVALBZ2VALE + 10 < VALESellTuple[0]*max_tradeVALBZ2VALE:
        tradeVALBZforVALE(prices, max_tradeVALBZ2VALE, VALESellTuple[0], VALBZBuyTuple[0])

def tradeVALEforVALBZ(prices, trade_sz, VALEprice, VALBZprice):
    exp_utils.buy(prices, "VALE", trade_sz, VALEprice)
    exp_utils.convert(prices, "VALE", False, trade_sz)
    exp_utils.sell(prices, "VALBZ", trade_sz, VALBZprice)


def tradeVALBZforVALE(prices, trade_sz, VALEprice, VALBZprice):
    exp_utils.buy(prices, "VALBZ", trade_sz, VALBZprice)
    exp_utils.convert(prices, "VALE", True, trade_sz)
    exp_utils.sell(prices, "VALE", trade_sz, VALEprice)



