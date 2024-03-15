import scooter_configuration
import requests
import data

def new_orders_scooter():
    return requests.post(scooter_configuration.URL + scooter_configuration.new_orders,
                         json=data.body)


def receive_orders_track(track):
    return requests.get(scooter_configuration.URL + scooter_configuration.track_orders+str(track))

