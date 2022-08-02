import requests as r

API_URL = 'http://127.0.0.1:5000'
GET_FLIGHT_URL = f'{API_URL}/flights/flight_info'
ADD_FLIGHT_URL = f'{API_URL}/flights/add_flight'
FLIGHT_ID_HEADER = 'flight ID'
ARRIVAL_TIME_HEADER = 'Arrival'
DEPARTURE_TIME_HEADER = 'Departure '

if __name__ == '__main__':
    req1 = r.get(url=f'{GET_FLIGHT_URL}/C1223')
    print(req1.text)

    req2 = r.get(url=f'{GET_FLIGHT_URL}/dsfsdfsd')
    print(req2.text)

    req3 = r.post(ADD_FLIGHT_URL, data={FLIGHT_ID_HEADER: 'Hellp', ARRIVAL_TIME_HEADER: '17:00', DEPARTURE_TIME_HEADER: '22:00'})
    print(req3.text)

    req4 = r.post(ADD_FLIGHT_URL,
                  data={FLIGHT_ID_HEADER: 'Hellp', ARRIVAL_TIME_HEADER: '17:00', DEPARTURE_TIME_HEADER: '26:00'})
    print(req4.text)

    req5 = r.post(ADD_FLIGHT_URL,
                  data={FLIGHT_ID_HEADER: 'CC546', ARRIVAL_TIME_HEADER: '23:00', DEPARTURE_TIME_HEADER: '15:00'})
    print(req5.text)

    req6 = r.post(ADD_FLIGHT_URL,
                  data={FLIGHT_ID_HEADER: 'CC546', ARRIVAL_TIME_HEADER: '2000:00', DEPARTURE_TIME_HEADER: '15:00'})
    print(req6.text)



