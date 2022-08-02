import csv
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
FLIGHTS_FILE_NAME = 'Flights.csv'
FLIGHT_ID_HEADER = 'flight ID'
ARRIVAL_TIME_HEADER = 'Arrival'
DEPARTURE_TIME_HEADER = 'Departure '
SUCCESS_HEADER = 'success'


def update_flights_file(flights_dict, flight_data_from_user):
    flights_dict[flight_data_from_user[FLIGHT_ID_HEADER]] = {FLIGHT_ID_HEADER: flight_data_from_user[FLIGHT_ID_HEADER],
                                                             ARRIVAL_TIME_HEADER: flight_data_from_user[
                                                                 ARRIVAL_TIME_HEADER],
                                                             DEPARTURE_TIME_HEADER: flight_data_from_user[
                                                                                        DEPARTURE_TIME_HEADER] + ' ',
                                                             SUCCESS_HEADER: '’’'}
    with open(FLIGHTS_FILE_NAME, 'w') as file:
        flights_list = list(flights_dict.values())
        headers = flights_list[0].keys()
        dict_write = csv.DictWriter(file, headers)
        dict_write.writeheader()
        dict_write.writerows(flights_list)


def open_flights_file():
    with open(FLIGHTS_FILE_NAME, 'r') as file:
        reader = csv.DictReader(file, skipinitialspace=True)
        flights_list = list(reader)
        flights_dict_by_flight_id = {flights_list[i][FLIGHT_ID_HEADER]: flights_list[i] for i in
                                     range(0, len(flights_list))}

    return flights_dict_by_flight_id


@app.route('/flights/flight_info/<flight_id>')
def get_flight_info(flight_id):
    flights_dict_by_flight_id = open_flights_file()
    try:
        if flight_id in flights_dict_by_flight_id.keys():
            return flights_dict_by_flight_id[flight_id]
        else:
            return 'Flight does not exist'
    except:
        return 'The input is not in the correct format'


@app.route('/flights/add_flight', methods=['POST'])
def add_flight():
    flights_dict_by_flight_id = open_flights_file()
    flight_data_from_user = dict(request.values)
    if (FLIGHT_ID_HEADER and ARRIVAL_TIME_HEADER and DEPARTURE_TIME_HEADER) in flight_data_from_user.keys():
        flight_id = flight_data_from_user[FLIGHT_ID_HEADER]
        try:
            arrival_time = datetime.strptime(flight_data_from_user[ARRIVAL_TIME_HEADER], '%H:%M')
            departure_time = datetime.strptime(flight_data_from_user[DEPARTURE_TIME_HEADER], '%H:%M')
            flight_data_from_user[DEPARTURE_TIME_HEADER] = str(departure_time.strftime('%H:%M'))
            flight_data_from_user[ARRIVAL_TIME_HEADER] = str(arrival_time.strftime('%H:%M'))
        except:
            return 'The arrival time and departure time are not in the needed format'
        if departure_time < arrival_time:
            return 'The arrival time and departure time are not good, please keep the departure time biggger than the' \
                   ' arrival time'
        else:
            if flight_id in flights_dict_by_flight_id.keys():
                update_flights_file(flights_dict_by_flight_id, flight_data_from_user)
                return f'The flight existed in the flights list, it got updated. flight details: ' \
                       f'{flight_data_from_user}'
            else:
                update_flights_file(flights_dict_by_flight_id, flight_data_from_user)
                return f'The flight added to the flights file. flight details: {flight_data_from_user}'

    else:
        return 'The data is not in the correct format'


if __name__ == '__main__':
    app.run()
