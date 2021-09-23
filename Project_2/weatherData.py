# printing out weather data from input file
def weather(fileName):
    with open(fileName, 'r') as infile:
        infile.readline().strip()
        infile = infile.read().split('\n')
        for line in infile:
            date, airTemp, airTempMin, airTempMax, glob, UVglob = line.split(';')
            day, month, year = date.split('.')
            formattedDate = year + "-" + month + "-" + day

            # returns a dictionary since there can only be one max an min temperature every day, giving us one key
            # (the date)
            temperatureDictionary = {
                "Date": formattedDate,
                "Air temp": airTemp,
                "Minimum air temp": airTempMin,
                "Maximum air temp": airTempMax,
                "Global temp": glob,
                "Global % UV": UVglob
            }
            print(temperatureDictionary)


weather('weather_umb_2012.csv')
