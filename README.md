# Wallet KATA in CQRS
This kata is derived from [the original wallet kata](http://codingdojo.org/kata/Wallet/).
The goal is to refactor a working implementation using [CQRS](https://martinfowler.com/bliki/CQRS.html) design pattern.

## Wallet

### Subject

Given a Wallet containing Stocks, build a function that compute the value of wallet in a currency.

The Stocks have a quantity and a StockType. The StockType can be for example petroleum, Euros, bitcoins and Dollars.

To value the portfilio in a Currency you can use external api to provide rate exchanges (some are provided below).


### Object sample

    Value value = Wallet(Stock(5, PETROLEUM)).value(EUR, rateProvider)

With `rateProvider` an implementation of this interface :

    rateProvider.rate(FromCurrency, ToCurrency) -> Amount

and `PETROLEUM` is a `StockType` and `EUR` is a Currency.


### Functional sample

    Value value = compute_value(Wallet(Stock(5, PETROLEUM), EUR, rateProvider))

Where `rateProvider` is a function with this signature :

    rateProvider(FromCurrency, ToCurrency) -> Amount

and `PETROLEUM` is a `StockType` and `EUR` is a Currency.
