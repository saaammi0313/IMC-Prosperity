from datamodel import OrderDepth, UserId, TradingState, Order
from datamodel import Listing, Trade
from typing import List
import string

class Trader:
    
    def run(self, state: TradingState):
        """
        Only method required. It takes all buy and sell orders for all symbols as an input,
        and outputs a list of orders to be sent
        """
        print("traderData: " + state.traderData)
        print("Observations: " + str(state.observations))

				# Orders to be placed on exchange matching engine
        result = {}
        acceptable_price_range = {'AMETHYSTS':[10001,9999], 'STARFRUIT':[4999,4997]}
        product = 'AMETHYSTS'
        order_depth: OrderDepth = state.order_depths[product]
        # Initialize the list of Orders to be sent as an empty list
        orders: List[Order] = []

        # Define a fair value for the PRODUCT. Might be different for each tradable item
        # Note that this value of 10 is just a dummy value, you should likely change it!
        acceptable_price = acceptable_price_range[product]
        # All print statements output will be delivered inside test results
        print("Acceptable price : " + str(acceptable_price))
        print("Buy Order depth : " + str(len(order_depth.buy_orders)) + ", Sell order depth : " + str(len(order_depth.sell_orders)))

        if len(order_depth.sell_orders) != 0:
          total_ask_amount = 0
          for ask in list(order_depth.sell_orders.keys()):
              if ask <= 9999:
                  total_ask_amount+=order_depth.sell_orders[ask]
          print("BUY", str(-total_ask_amount) + "x", 9999) # buy 29, amount = -29
          orders.append(Order(product, 9999, -total_ask_amount)) # order(29)

        if len(order_depth.buy_orders) != 0:
          total_bid_amount = 0
          for bid in list(order_depth.buy_orders.keys()):
              if bid >= 10001:
                  total_bid_amount+=order_depth.buy_orders[bid]
          print("SELL", str(total_bid_amount) + "x", 10001) # sell 22, amount = 22 
          orders.append(Order(product, 10001, -total_bid_amount)) # order(-22)

    
        result[product] = orders
    
		    # String value holding Trader state data required. 
				# It will be delivered as TradingState.traderData on next execution.
        traderData = "SAMPLE" 
        
				# Sample conversion request. Check more details below. 
        conversions = 1
        return result, conversions, traderData