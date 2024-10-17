"""Dessa Shapiro"""
import csv

def find_streets(filename, street_name):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            next(reader)
            found_streets = []
            for record in reader:
                current_street_name = record[0].upper() if record[0] else ""  # Convert to uppercase for case-insensitive comparison
                if current_street_name == street_name.upper():
                    street_type = record[1] if record[1] else ""
                    post_direction = record[2] if record[2] else ""
                    full_street_name = f"{current_street_name} {street_type} {post_direction}".strip()
                    found_streets.append(full_street_name)

            if found_streets:
                for street in found_streets:
                    print(street)
            else:
                print("No streets found with the name:, ",street_name)
    except FileNotFoundError:
        print("File:", filename, "not found")

def popular(filename):
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            street_counts = {}

            for record in reader:
                street_name = record[0].lower()
                if street_name not in street_counts:
                    street_counts[street_name] = 1
                else:
                    street_counts[street_name] += 1
                
            if street_counts:
                most_popular_street = max(street_counts, key=street_counts.get)
                print("The most popular street name is:", most_popular_street)
            else:
                print("No streets found in the file.")
    except FileNotFoundError:
         print("File:", filename, "not found")

def main():
    find_streets("data/streets.csv", "mission bay")
    popular("data/streets.csv")

if __name__ == "__main__":
    main()

