from nose.tools import *
from hamcrest import *
from mock import Mock

class CurrencyConverter_Test:
    def setUp(self):
        self.rates = Mock()
        self.rates.get_rate.return_value = 0
        self.validator = Mock()
        self.converter = Converter(self.rates, self.validator)

    @istest
    def multiplies_amount_by_rate(self):
        self.rates.get_rate.return_value = 3

        result = self.converter.convert(2, 'foo', 'bar')

        assert_that(result, equal_to(6))
        self.rates.get_rate.assert_called_with('foo', 'bar')

    @istest
    def validates_currencies(self):
        self.converter.convert(0, 'foo', 'bar')

        self.validator.check_exists.assert_any_call('foo')
        self.validator.check_exists.assert_any_call('bar')


class Converter:
    def __init__(self, rates, validator):
        self.rates = rates
        self.validator = validator

    def convert(self, amount, from_currency, to_currency):
        self.validator.check_exists(from_currency)
        self.validator.check_exists(to_currency)
        return amount * self.rates.get_rate(from_currency, to_currency)
