import json
import yaml
import requests



people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

with open('people.json', 'r') as people_json:
    people = json.load(people_json)

with open('people.yaml', 'r') as people_yaml:
    people = yaml.load(people_yaml)

print(people)