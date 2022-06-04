from datetime import date
 

def get_custom_birhtday(number):
    todays_date = date.today()
    year = todays_date.year- int(number)
    data = todays_date.strftime('%d/%m/')
    data = str(data) + str(year)
    return data