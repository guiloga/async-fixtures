# Async Fixtures
> A collection of asynchronous fixtures.

This repository is a brief walk over different languages and it's corresponding **async IO libraries** exploring concurrency features.
It serves as a quick reference to explore asynchronous or concurrency code.

## Python
Pre-requisites to run python async fixtures are:
- [**python3.9**](https://www.python.org/downloads/release/python-390/)
- [**poetry**](https://python-poetry.org/)

### asyncio
[**asyncio**](https://docs.python.org/3/library/asyncio.html)
is the Python standard library for writing asynchronous code.
It provides both a High-level and Low-level API for concurrency control.
\
You can use this repo to do a quick overview of **asyncio** concepts and features,
by running the fixture scripts located under *python/asyncio/*.

#### Run fixtures
```shell
cd python
poetry install

# Run the hello_world.py fixture
poetry run python hello_world.py
```
