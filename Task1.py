import csv
from datetime import datetime, timedelta

with open('Flights.csv', 'r') as file:
    reader = csv.DictReader(file, skipinitialspace=True)

    flights_list = list(reader)

print(flights_list)

flights_list.sort(key=lambda flight_time: datetime.strptime(flight_time['Arrival'], '%H:%M').time())

print(flights_list)

success_counter = 0

for flight in flights_list:
    time_change = datetime.strptime(flight['Departure '][:-1], '%H:%M') - datetime.strptime(flight['Arrival'] , '%H:%M')
    if success_counter < 20 and time_change > timedelta(hours=3):
        flight['success'] = True
        success_counter += 1
    else:
        flight['success'] = False


headers = flights_list[0].keys()

with open('Flights-readysorted.csv', 'w') as file:
    dict_write = csv.DictWriter(file, headers)
    dict_write.writeheader()
    dict_write.writerows(flights_list)





