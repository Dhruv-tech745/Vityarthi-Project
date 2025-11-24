import csv


BREAKDOWN = {}

def load_factors(filename="factors.csv"):
    """Loads emission factors from a CSV file."""
    factors = {}
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # The category is the key, factor_g_per_unit is the value
                factors[row['category']] = int(row['factor_g_per_unit'])
        print(f"Loaded {len(factors)} emission factors from {filename}")
        return factors
    except FileNotFoundError:
        print(f" Error: {filename} not found. Using default hardcoded factors.")
        # Return hardcoded factors if file load fails, as a fallback (Original code structure)
        return {
            "electricity": 450,    # g CO2e / kWh [cite: 4]
            "fuel": 2392,          # g CO2e / Litre (Petrol/Gasoline) [cite: 5]
            "flights": 150         # g CO2e / km (Short Haul) [cite: 6]
        }


FACTORS = load_factors()



def get_number(prompt: str) -> float:
    """Gets a positive number from the user, handling common errors and 'no'."""
    while True:
        try:
            val = input(prompt).strip().lower()
            if val in ('n', 'no', '0'):
                return 0.0

            num = float(val)
            if num < 0:
                print(" Must be a non-negative number. Try again.")
            else:
                return num
        except ValueError:
            print(" Oops! Please enter a number or 'no'.")


def calculate_footprint() -> float:
    """Collects user data, calculates annual emissions, and stores the breakdown."""
    print("\n" + "=" * 50)
    print("       Your Annual Carbon Footprint Estimator")
    print("=" * 50)
    print("Let's estimate your emissions based on typical use...")

    total_g = 0.0


    print("\n--- Home Energy ---")
    kwh_monthly = get_number("Avg. MONTHLY electricity usage (kWh, or 'no'): ")


    annual_elec_g = kwh_monthly * 12 * FACTORS["electricity"]
    BREAKDOWN["Electricity"] = annual_elec_g
    total_g += annual_elec_g
    print(f"   -> Electricity estimate: {annual_elec_g / 1000:,.1f} kg CO2e")

    print("\n---  Driving ---")
    fuel_monthly = get_number("Avg. MONTHLY vehicle fuel (Litres, or 'no'): ")

    annual_fuel_g = fuel_monthly * 12 * FACTORS["fuel"]
    BREAKDOWN["Vehicle Fuel"] = annual_fuel_g
    total_g += annual_fuel_g
    print(f"   -> Vehicle fuel estimate: {annual_fuel_g / 1000:,.1f} kg CO2e")
    print("\n---  Air Travel ---")
    flight_km_annual = get_number("TOTAL flight distance this year (km, or 'no'): ")

    annual_flight_g = flight_km_annual * FACTORS["flights"]
    BREAKDOWN["Flights"] = annual_flight_g
    total_g += annual_flight_g
    print(f"   -> Flight estimate: {annual_flight_g / 1000:,.1f} kg CO2e")

    return total_g


def display_report(total_annual_g: float):
    """Displays the stylized final report."""

    total_annual_kg = total_annual_g / 1000
    total_annual_tonnes = total_annual_g / 1_000_000

    print("\n" + "═" * 50)
    print("        ANNUAL FOOTPRINT REPORT ")
    print("═" * 50)

    print(" Breakdown (in Kilograms CO2e):")
    for category, emission_g in BREAKDOWN.items():
        emission_kg = emission_g / 1000
        print(f"  • {category:<12}: {emission_kg:,.2f} kg")

    print("-" * 50)

    print(f"GRAND TOTAL: {total_annual_kg:,.0f} kg CO2e")
    print(f"   (That's {total_annual_tonnes:,.2f} Tonnes)")

    print("\n Sustainability Check:")
    if total_annual_kg < 2000:
        print("   Fantastic! Your estimated impact is well below the average.")
    elif total_annual_kg < 5000:
        # Global average is approx 4,800 kg
        print("   Doing Great! You're near or below the global average. Keep refining!")
    else:
        print("   Room for Improvement: Your footprint is higher than the average. Check driving/flights!")

    print("═" * 50)

if __name__ == "__main__":
    annual_footprint_g = calculate_footprint()
    display_report(annual_footprint_g)
