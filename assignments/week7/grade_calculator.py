import csv
import random

INPUT_FILE = "Technical Basics I_2025 - Sheet1.csv"
OUTPUT_FILE = "Assignment7_Graded.csv"
WEEKS = [f"Week {i}" for i in range(1, 14) if i != 6]  # Skip Week 6 because of Google Excursion

try:
    rows = []

    # Read CSV using DictReader
    with open(INPUT_FILE, "r") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        # Add missing week columns if any
        for week in WEEKS:
            if week not in headers:
                headers.append(week)

        for row in reader:
            # Fill missing weeks with random points or leave empty
            for week in WEEKS:
                if week not in row or not row[week] or row[week].strip() == "":
                    row[week] = str(random.choice([0, 1, 2, 3, "", " "]))
            rows.append(row)

except FileNotFoundError:
    print(f"❌ File '{INPUT_FILE}' not found. Please check the filename.")
    exit()

# Calculate Total Points and Average
for row in rows:
    points = []
    for week in WEEKS:
        try:
            point = float(row[week])
            points.append(point)
        except ValueError:
            continue  # ignore empty or invalid entries

    # Total = best 10 of 12 assignments
    top_10 = sorted(points, reverse=True)[:10]
    total = sum(top_10)
    average = round(sum(points) / len(points), 2) if points else 0

    row["Total Points"] = total
    row["Average Points"] = average

# Save to New CSV
fieldnames = headers + ["Total Points", "Average Points"]

with open(OUTPUT_FILE, "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"✅ Done! New file saved as: {OUTPUT_FILE}")
