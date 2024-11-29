import json

f = open('buckets.json')
data = json.load(f)

# Print a summary of each bucket: Name, region, size (in GB),
# and versioning status
for i in data['buckets']:
    print(
        f" buckets name: {i['name']} Region: {i['region']} Size: {i['sizeGB']} GB Versioning_status: {i['versioning']}")
    # print(i)

f.close()

# Identify buckets larger than 80 GB from every region which are unused for 90+ days.
