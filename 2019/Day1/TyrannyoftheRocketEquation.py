import math

def compute_fuel(mass):
    fuel = mass // 3 - 2
    if fuel < 0:
        fuel = 0
    return fuel

def compute_rocket_equation(mass):
    total = 0
    fuel = compute_fuel(mass)
    total += fuel
    while fuel > 0:
        fuel = compute_fuel(fuel)
        total += fuel
    return total

if __name__ == "__main__":
    with open("input",'r') as f:
        masses = f.readlines()
    answer = 0
    for each_mass in masses:
        answer += compute_rocket_equation(int(each_mass))
    
    print(answer)