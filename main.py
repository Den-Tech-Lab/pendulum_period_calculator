import math

def calculate_period(length, gravity=9.81):
    try:
        period = 2 * math.pi * math.sqrt(length / gravity)
        return round(period, 3)
    except Exception as e:
        return f"Error: {e}"

# User input
print("🔁 Simple Pendulum Period Calculator")
L = float(input("Enter the length of the pendulum (in meters): "))
g = float(input("Enter gravity (in m/s²) [default is 9.81]: ") or 9.81)

T = calculate_period(L, g)
print(f"\n✅ The period of the pendulum is: {T} seconds")
