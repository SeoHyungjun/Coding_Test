import sys
PI = 3.141592

trip = 1
while True:
    diameter, spin, time = map(float, sys.stdin.readline().split())

    if spin == 0:
        break

    miles = 2*PI * diameter/2/63360 * spin
    print("Trip #%d: %.2f %.2f"%(trip, round(miles, 2), round(miles / time*3600, 2)))
    trip += 1