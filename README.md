
# What is this?

An example for how to use test doubles (both stubs and mocks) for testing in Python.

The domain is simple: a currency converter that converts an amount from one currency to another. It uses a dependency to retrieve the conversion rate and another to check that it was given valid currency symbols.

The code contrasts two frameworks

* [Mock](https://pypi.python.org/pypi/mock) and
* [Mockito](https://code.google.com/p/mockito-python/)



# Run tests

Install dependencies.

    pip install -r requirements.txt

Now you should have a green bar.

    make test.once


# Run tests continuously

Install dependencies

    bundle install

If you are not on OS X, you are better off with

    bundle install --without osx

Now the tests will automatically rerun when you change files.

    make test.continuously

