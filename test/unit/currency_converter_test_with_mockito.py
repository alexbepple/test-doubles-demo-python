from nose.tools import *
from hamcrest import *
from mockito import *

class CurrencyConverterWithMockitoDoubles_Test:

    def setUp(self):
        self.rates = mock()
        self.validator = mock()
        self.converter = Converter(self.rates, self.validator)

        when(self.rates).get_rate(any(), any()).thenReturn(0)

    @istest
    def multiplies_amount_by_conversion_rate(self):
        when(self.rates).get_rate(any(), any()).thenReturn(3).thenReturn(6)

        assert_that(self.converter.convert(2, 'foo', 'bar'), equal_to(6))

    @istest
    def validates_currencies(self):
        self.converter.convert(0, 'foo', 'bar')
        verify(self.validator).check_exists('foo')
        verify(self.validator).check_exists('bar')


class Converter:
    def __init__(self, rates, validator):
        self.rates = rates
        self.validator = validator

    def convert(self, amount, from_currency, to_currency):
        self.validator.check_exists(from_currency)
        self.validator.check_exists(to_currency)
        return amount * self.rates.get_rate(from_currency, to_currency)
