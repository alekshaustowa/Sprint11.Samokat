#Хаустова Александра, 14 когорта, спринт 11 - финальный проект. Инженер по тестированию плюс.
import sender_stand_request

def test_get_orders():
    orders_track = sender_stand_request.new_orders_scooter().json()['track']
    status_code = sender_stand_request.receive_orders_track(orders_track).status_code
    assert status_code == 200