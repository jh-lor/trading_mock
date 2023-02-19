from dataclasses import dataclass
from enum import Enum, auto
import random
import heapq


MAX_PRICE = 100
MIN_PRICE = 0
N_LEVELS = MAX_PRICE - MIN_PRICE + 1


class Side(Enum):
    buy = auto()
    sell = auto()


class Order(Enum):
    buy = auto()
    sell = auto()
    cancel = auto()


@dataclass
class Quote():
    price: int
    id: int
    owner: str
    size: int
    side: Side
    product: str

    def __lt__(self, other):
        if self.side == Side.buy:
            return self.price > other.price
        else:
            return self.price < other.price

    def __eq__(self, other):
        return (self.product == other.product and self.id == other.id)


class Half():
    def __init__(self, side: Side):
        self.side = side
        self.quotes = [[]
                       for _ in range(N_LEVELS)]  # store the quotes in order
        self.size = [0] * N_LEVELS  # store the size on the book
        self.participant_size = {}  # store the quotes for each person in order

    def add_quote(self, quote):
        if self.side != quote.side:
            raise Exception("Adding quote to wrong side of book")
        self.quotes[quote.price].append(quote)
        self.size[quote.price] += quote.size
        if quote.owner not in self.participant_orders:
            self.participant_orders[quote.owner] = [0] * N_LEVELS
        self.participant_orders[quote.owner][quote.price] += quote.size

    def is_crossed(self, quote):
        # if self.side == quote.side:
        #     raise Exception("Cannot cross markets on the same side")
        if self.side == Side.buy:
            return self.quotes[0].price >= quote.price
        else:
            return self.quotes[0].price <= quote.price

    def trade_against_quote(self, quote, positions):
        if self.side == quote.side:
            raise Exception("Trading Quote against same side of book")

        while (quote.size > 0 and self.is_crossed(quote)):
            if self.quotes[0].size < quote.size:
                traded_quote = heapq.heappop(self.quotes)
                quote.size -= traded_quote.size
                self.participant_orders[traded_quote.owner].pop(
                    traded_quote.id)
                self.positions[]


class OrderBook():
    def __init__(self, product):
        self.product = product
        self.bids = Half()
        self.offers = Half()

    def add_new_quote(self, quote):
        pass


class Game():
    def __init__(self, products, seed=None, **traders):
        self.seed = seed
        self.traders = {name: trader() for name, trader in traders.items()}
        self.products = products
        self.position = {trader:
                         {product: 0
                          for product in self.products + ["cash"]}
                         for trader in self.traders.keys()}
        self.books = {product: OrderBook(product) for product in self.products}
        self.id = 0

    def run_game(self, rounds):
        for round in range(rounds):
            for trader in random.shuffle(list(self.traders.keys())):


class Trader():
    def __init__(self):
        pass

    def do_trade():
