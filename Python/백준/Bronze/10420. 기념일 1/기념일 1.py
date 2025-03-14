import datetime as dt

n = int(input())
d = "2014-04-02"

a = dt.datetime.strptime(d, '%Y-%m-%d')
print((a + dt.timedelta(days=n-1)).strftime('%Y-%m-%d'))
