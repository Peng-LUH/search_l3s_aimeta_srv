from logic import Trends
import sys

aims = Trends()

job = "Elektrotechniker/in"
city = "Bielefeld"
radius = 30 #km
if len(sys.argv) == 3:
    job = sys.argv[1]
    city = sys.argv[2]


# Search for jobs
jwt = aims.get_jwt()
print(jwt)
print('#'*50)
results = aims.search(jwt["access_token"], job, city, radius)
print("result", results)