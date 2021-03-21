"""
Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
- A customer with a card id equal to id, gets in the station stationName at time t.
- A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
- A customer with a card id equal to id, gets out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
- Returns the average time to travel between the startStation and the endStation.
- The average time is computed from all the previous traveling from startStation to endStation that happened directly.
- all to getAverageTime is always valid.

You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station, they get out at time t2 with t2 > t1. All events happen in chronological order.
"""
from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.checkins = defaultdict()
        self.routes = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_name, start_time = self.checkins[id]
        del self.checkins[id]
        # concatenate station names to represent a route
        route = station_name + stationName
        # store the route into routes if it doesn't exist
        if route not in self.routes:
            self.routes[route] = (0,0) # route[0]: number of trips, route[1]: time needed
        trip = self.routes[route]
        trip[0] += 1 # increment number of trips
        trip[1] += t - start_time

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip = startStation + endStation
        cnt, _sum = self.routes[trip]
        return _sum / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)