from maker_taker_base import Taker, Maker, Side, Market, test
import random
from typing import Type

class Rafael_and_Eduardo_Maker(Maker):
    def __init__(self) -> None:
        self.fair = 13.5

    def get_market(self, round: int) -> Market():
        if self.fair == 13.5:
            return Market(self.fair - 4.5, 1, self.fair + 4.5, 1)
        if self.fair == 90:
            return Market(self.fair - 5, 1, self.fair + 5, 1)
        if self.fair == 55:
            return Market(self.fair - 5, 1, self.fair + 5, 1)
        return Market(self.fair - 5, 1000, self.fair + 5, 1000)

    def update_trade(self, side: Type[Side]) -> None:
        if side == Side.sell and self.fair == 13.5:
            self.fair = 7
        elif side == Side.sell and self.fair == 7:
            self.fair = 5
        elif side == Side.sell and self.fair == 90:
            self.fair = 55
        elif side == Side.buy and self.fair == 13.5:
            self.fair = 90
        elif side == Side.buy and self.fair == 90:
            self.fair = 95
        elif side == Side.buy and self.fair == 7:
            self.fair = 10

class RandomTaker(Taker):
    def do_trade(self, market: Type[Market], round: int) -> Type[Side]:
        return random.choice([Side.buy, Side.sell])


class GreedyTaker(Taker):
    def do_trade(self, market: Type[Market], round: int) -> Type[Side]:
        return market.better_side(self.true_value)


class CenterMaker(Maker):
    def get_market(self, round: int) -> Market():
        return Market(45, 1, 55, 1)

    def update_trade(self, side: Type[Side]) -> None:
        return


class FaderMaker(Maker):
    side_map = {Side.buy: 1, Side.sell: -1, Side.notrade: 0}

    def __init__(self) -> None:
        self.fair = 50

    def get_market(self, round: int) -> Market():
        return Market(self.fair - 5, 1, self.fair + 5, 1)

    def update_trade(self, side: Type[Side]) -> None:
        self.fair += self.side_map[side] * 10


def main():
    # test(GreedyTaker, CenterMaker)
    test(GreedyTaker, FaderMaker)


if __name__ == "__main__":
    main()
