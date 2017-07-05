import sys

from YahooStockClass import YahooDownload

def testit(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """
    # This function works correctly--it is verbatim from the text
    linenum = sys._getframe(1).f_lineno         # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def yahoo_test_suite():
    """
    The yahoo_test_suite() is designed to test the following:
      yahoo_finance.url_return()
      delete_columns()
      cal_moving_avg()
    :return: None
    """
    yahoo_finance=YahooDownload()
    # The following tests test the url_return() function
    print("\nTesting url_return()")
    testit(yahoo_finance.url_return("AAPL","1","1","2012","1","1","2014") == "http://chart.finance.yahoo.com/table.csv?s=AAPL&a=1&b=1&c=2012&d=1&e=1&f=2014&g=d&ignore=.csv")
    testit(yahoo_finance.url_return("AAPL","1","1","2018","1","1","20144") == False)

    # The following tests test the delete_columns() function
    print("\nTesting delete_columns()")
    testit(yahoo_finance.delete_columns("test_table.csv") == [['3', 144.0], ['2', 143.0], ['1', 142.0]])
    testit(yahoo_finance.delete_columns("test_table.csv") == [['3', 4, 144.0], ['2', 5, 143.0], ['1', 6, 142.0]])

    # The following tests test the cal_moving_avg() function
    print("\nTesting cal_moving_avg()")
    testit(yahoo_finance.cal_moving_avg(2,[['3', 144.0], ['2', 143.0], ['1', 142.0]]) == [['3', 144.0], ['2', 143.0, 143.5], ['1', 142.0, 142.5]])
    testit(yahoo_finance.cal_moving_avg(2,[['3', 144.0], ['2', 143.0], ['1', 142.0]]) == [['3', 144.0], ['2', 143.0], ['1', 142.0, 142.5]])

yahoo_test_suite()
