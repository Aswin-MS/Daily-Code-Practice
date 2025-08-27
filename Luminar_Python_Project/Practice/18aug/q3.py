"""
 Question: Car Rental System
 Scenario: A car rental charges: $50 per day, $0.10 per km, Minimum $100 for 3 days. Write a
 program to calculate the total cost.
 Sample Input:
 Days: 5, Distance: 250 km
 Sample Output:
 Total cost: $275
"""
def cost(days,dis):
    day_cost=50*days
    dis_cost=0.10*dis
    total_cost=int(day_cost+dis_cost)
    print(f'Total cost=${total_cost}')
    return
days=int(input())
dis=int(input())
cost(days,dis)
