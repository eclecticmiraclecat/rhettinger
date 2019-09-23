'Collection of tools used in portfolio analysis'
from validators import OneOf, String, Number
from statistics import mean

class PriceRange:

    kind = OneOf('stock', 'bond', 'currency', 'option', 'bond', 'future')
    symbol = String(minsize=2, maxsize=5, predicate=str.isupper)
    low = Number(minvalue=0)
    high = Number(minvalue=0, maxvalue=100)

    def __init__(self, kind, symbol, low, high):
        self.kind = kind
        self.symbol = symbol
        self.low = low
        self.high = high

    @property
    def midpoint(self):
        return (self.low + self.high) / 2

    def __repr__(s):
        return f'{s.__class__.__name__}({s.kind!r}, {s.symbol!r}, {s.low!r}, {s.high!r})'

if __name__ == '__main__':
    from pprint import pprint

    portfolio = [
        PriceRange('stock', 'CSCO', 26, 35),
        PriceRange('option', 'HP', 11, 45),
        PriceRange('stock', 'BOA', 32, 46),
        PriceRange('stock', 'WLP', 12.87, 34.15),
        PriceRange('option', 'WLP', 1.87, 14.15),
        PriceRange('option', 'BOA', 34, 45),
        PriceRange('bond', 'HP', 62, 67),
    ]

    print('Stock securities:')
    pprint([s for s in portfolio if s.kind == 'stock'])

    print('\nWLP securities:')
    pprint([s for s in portfolio if s.symbol == 'WLP'])

    print('\nBOA securities:')
    pprint([s for s in portfolio if s.symbol == 'BOA'])

    print('\nMininum low:')
    print(min(s.low for s in portfolio))

    print('\nMinimum high:')
    print(max(s.high for s in portfolio))

    print('\nAverage midpoint:')
    print(mean(s.midpoint for s in portfolio))
