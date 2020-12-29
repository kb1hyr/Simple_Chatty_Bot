# put your python code here
vaca_days = int(input())
food_per_day = int(input())
one_way_flight = int(input())
night_in_hotel = int(input())

food_cost = vaca_days * food_per_day
flight_cost = 2 * one_way_flight
hotel_cost = night_in_hotel * (vaca_days - 1)
total_cost = food_cost + flight_cost + hotel_cost
print(total_cost)
