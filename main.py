#author: Sher Sanginov
#main.py is used to run the program

import os


from YahooStockClass import YahooDownload



def main():
    symbol=raw_input("Enter stock symbol: ")
    start_month1=int(raw_input("Enter start month: ")) - 1
    start_month=str(start_month1)
    start_day=raw_input("Enter start day: ")
    start_year=raw_input("Enter start year: ")
    end_month1=int(raw_input("Enter end month: "))-1
    end_month=str(end_month1)
    end_day=raw_input("Enter end day: ")
    end_year=raw_input("Enter end year: ")
    yahoo_finance=YahooDownload()

    final_url=yahoo_finance.url_return(symbol,start_month,start_day,start_year,end_month,end_day,end_year)
    oldfile = yahoo_finance.download_csv(final_url)
    data = yahoo_finance.delete_columns(oldfile)
    os.remove(oldfile)
    m_average_input=(int(raw_input("Set moving average interval (number of days)? ")))
    userin = raw_input("Name the file: ")
    final_name = userin +".csv"

    avg_data = yahoo_finance.cal_moving_avg(m_average_input, data)
    yahoo_finance.write_moving_average(m_average_input, final_name, avg_data)

    wantGraph = raw_input("Do you want to see the graph right now (yes/no)? ")
    while wantGraph != "yes" and wantGraph != "no":
        wantGraph = raw_input("Do you want to see the graph right now (yes/no)? ")
    if wantGraph == "yes":
            yahoo_finance.graph(final_name)
    if wantGraph == "no":
        print("Enjoy your ready csv table!")

if __name__ == "__main__":
    main()
