# Project Title

Yahoo Stock Finance

## Description

Yahoo Stock Finance is an application that works with any stock data. What does it do?

* a) program queries a user for a stock symbol and time period.
* b) program downloads the historical data(.csv) from the Yahoo Finance website based on the user's query.
* c) program deletes **Open**/**High**/**Low** columns from the downloaded file
* d) program calculates the moving average based on a time period specified by a user
* e) program graphs the moving average and the stock data which allows a user to predict the behavior of a stock


## Motivation

I was motivated to work on this project because of my interest in stocks. I used to go to Yahoo website
very often looking for some stock's historical data out of curiousity to understand
the behavior of a stock. In order to make my job easier, I decided to make a program that
 retrieves the stock data and doesn't require me to go to the Yahoo Finance website. It's very handy
 for me because I only need to provide the stock symbol and time period in the program. And then, magic
 happens.

## File descriptions

* [main.py](main.py) - this is the file that runs the program
* [YahooStockClass.py](YahooStockClass.py) - the full implementation of the program is is located in this file as a YahooDownload class.
* [setup.sh](setup.sh) - installs all the dependencies to get started with the development environment
* [testsuite_YahooStockClass.py](testsuite_YahooStockClass.py) - this file contains all the test cases for each function of Yahoo Stock Finance program


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

What things you need to install the software and how to install them

```
a)It is necessary to have Python2.7 or Python3.5 installed on your local machine.
b)Required libraries: wget, matlotlib, requests
```

### Installing

You can simply run the [setup.sh](setup.sh) file which installs all the dependecies for you.
<br /> <code> source setup.sh </code>


## Running the program

In order to run the program, you just need to run [main.py](main.py) file. You can run it from your IDE or terminal.
Make sure you are inside this directory. In the terminal, type:
<br /><code>python [main.py](main.py)</code>

## Running the tests

The testsuite file is located in this directory.
 Run the file that is named **[testsuite_YahooStockClass.py](testsuite_YahooStockClass.py)** .
 <br /> <code> python [testsuite_YahooStockClass.py](testsuite_YahooStockClass.py)</code>


## Built With

* [Python](https://www.python.org/)


## Authors

* **Sher Sanginov**



## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* **StackOverflow**

