import csv
import json
from collections import defaultdict

data = defaultdict(lambda: {"region": "", "region_ja": "", "cities": []})

with open("../csv/timezones.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        region = row["region"]
        data[region]["region"] = row["region"]
        data[region]["region_ja"] = row["region_ja"]
        data[region]["cities"].append({
            "timezone": row["timezone"],
            "city": row["city"],
            "country": row["country"],
            "city_ja": row["city_ja"],
            "country_ja": row["country_ja"],
        })

with open("../timezones.json", "w") as jsonfile:
    json.dump(list(data.values()), jsonfile, ensure_ascii=False, indent=2)
