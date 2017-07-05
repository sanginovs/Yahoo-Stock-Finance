
# Author: Sher Sanginov
# Application Name: Yahoo-Finance




import wget, csv, matplotlib.pyplot as plt,  datetime as dt
import matplotlib.dates as mdates
import requests

class YahooDownload:
    def __init__(self):
        '''hardcoded version of the url'''
        self.first_part="http://chart.finance.yahoo.com/table.csv?s="
        self.second_part="&a="
        self.third_part="&b="
        self.fourth_part="&c="
        self.fifth_part="&d="
        self.sixth_part="&e="
        self.seventh_part="&f="
        self.eight_part="&g=d&ignore=.csv"

    def url_return(self, symbol, start_month, start_day, start_year, end_month, end_day, end_year):
        '''this functions returns a hardcoded 
        full Yahoo specific stock download url 
        after getting user inputs'''
        final_url="{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}{12}{13}{14}"\
                    .format(self.first_part,\
                            symbol,\
                            self.second_part,\
                            start_month,\
                            self.third_part,\
                            start_day,\
                            self.fourth_part,\
                            start_year,\
                            self.fifth_part,\
                            end_month,\
                            self.sixth_part,\
                            end_day,\
                            self.seventh_part,\
                            end_year,\
                            self.eight_part)
        request = requests.get(final_url)
        if request.status_code == 200: # check if it is a valid url
            return final_url
        else:
            print("Given url is incorrect.")
            return False

    def download_csv(self,url):
        '''takes download url as an input and returns a downloaded csv filename'''
        filename = wget.download(url)
        return filename

    def delete_columns(self, oldfile):
        '''this function deletes several columns from the stock csv file which are not necessary'''
        data = []
        r = open(oldfile)
        r.readline()
        for line in r:
           items = line.split(',')
           data.append([items[0], float(items[6])])
        data.reverse()
        return data

    def cal_moving_avg(self, avg_start_day, data):
        '''this function returns the moving average of a stock'''
        start_avg_ind = 0
        end_avg_ind = avg_start_day
        for i in range(avg_start_day - 1, len(data)):
            sum = 0
            for j in range(start_avg_ind, end_avg_ind):
                sum += data[j][1]
            moving_avg = sum/avg_start_day
            data[i].append(moving_avg)
            start_avg_ind +=1
            end_avg_ind +=1
        return data

    def write_moving_average(self, avg_start_day, filename, data):
        '''this function writes moving average data to a file'''
        header = ["Date", "Adj Close", "{}-day Moving Avg".format(avg_start_day)]
        with open(filename, "w", newline="") as f:
          fileWriter = csv.writer(f, delimiter=',')
          fileWriter.writerow(header)
          for row in data:
              fileWriter.writerow(row)

    def graph(self, filename):
        '''this function graphs the stock data'''
        graph_coordinates={}
        list1=[]
        days = []
        adj_close=[]
        with open(filename) as f:
            for line in f:
                list1.append(line.split(","))
                if 'str' in line:
                    break

        for i in range(1, len(list1)):
            try:
                graph_coordinates[i]=float(list1[i][2])
                adj_close.append(float(list1[i][1]))
                splitted_date=list1[i][0].split("-")
                month=splitted_date[1]
                day=splitted_date[2]
                year=splitted_date[0]

                new_format_date=month+"/"+day+"/"+year
                days.append(new_format_date)
            except:
                pass

        x = [dt.datetime.strptime(d, '%m/%d/%Y').date() for d in days]
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=150))
        x_coordinate=[]
        y_coordinate=[]
        for i in graph_coordinates:
            x_coordinate.append(i)
            y_coordinate.append(graph_coordinates[i])
        plt.plot(x, y_coordinate)
        plt.plot(x, adj_close)
        plt.gcf().autofmt_xdate()
        plt.show()
        plt.close()


