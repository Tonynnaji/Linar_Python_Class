import datetime
satrt_time = datetime.datetime.now()

#code start
print('hello World')
#code end

end_time = datetime.datetime.now()
total_time = end_time - satrt_time
print("Total time taken = ", total_time)



import datetime
today = datetime.date.today()
print("Today's Date is ", today)

yesterday = today - datetime.timedelta (days=1)
print("Yesterday's Date was", yesterday)

tomorrow = today = datetime.timedelta (days=1)
print("Tomorrow's Date will be", tomorrow)

