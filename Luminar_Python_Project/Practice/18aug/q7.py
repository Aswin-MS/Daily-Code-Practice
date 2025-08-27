""" Question: Car Odometer Fraud Detector
 Scenario: A car's odometer reading should always increase. Take readings until a smaller (or
 equal) value is entered, then print 'Potential fraud detected!'
 Sample Input:
 Readings: 1000, 1500, 1400
 Sample Output:
 Potential fraud detected!"""
def fraud():
    odo=int(input())
    while True:
        new_odo=int(input())
        if odo>=new_odo:
            print('Potential fraud detected!')
            break
        odo=new_odo
fraud()