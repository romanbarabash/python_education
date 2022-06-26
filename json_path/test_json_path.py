import json
from typing import List, Any

from jsonpath_ng.ext import parse

from json_path.test_body import search_body, patient_body, books_body, dict_insurances


def get_json_path(json, json_path) -> List[Any]:
    values = []
    for match in parse(json_path).find(json):
        values = match.value
    return values


json_search_body = json.dumps(search_body)
json_patient_body = json.dumps(patient_body)
json_books_body = json.dumps(books_body)

# get name by filter match
insurance_name = get_json_path(dict_insurances, '$[?name=="*Template Commerical"].name')
print(insurance_name)

# get all race ids
get_all_race_ids = get_json_path(patient_body, '$..patientRaces..raceId')
print(get_all_race_ids)

# get races by index
races_by_idx = get_json_path(patient_body, '$..patientRaces[1]')
print(races_by_idx)

# get name by index
values_1st_object = get_json_path(search_body, '$..content[1].name')
print(values_1st_object)

# get races by index slice
get_races = get_json_path(patient_body, '$..patientRaces[1:3]')
print(get_races)

# get races filtered by raceId > 10
get_ids_filtered = get_json_path(patient_body, '$..patientRaces[?(@.raceId>10)]')
print(get_ids_filtered)

# get races filtered by raceId > 10, value
get_exact_id_filtered = get_json_path(patient_body, '$..patientRaces[?(@.raceId>10)].raceId')
print(get_exact_id_filtered)

# get last race id
get_exact_id_filtered = get_json_path(patient_body, '$..patientRaces[-1:].raceId')
print(get_exact_id_filtered)

# get races with exact match
get_exact_id_matched = get_json_path(patient_body, '$..patientRaces.raceId')
print(get_exact_id_filtered)

# get order id with contains
var_1 = '$.content[?firstName=~"Bug"]'

get_contains = get_json_path(search_body, var_1)
print(get_contains)

# get objects qty
qty_objects = get_json_path(books_body, '$.books.`len`')
print(qty_objects)

# TODO not working

# get titles from 2 objects
# values_object = get_json_path(books_body, '$..books[0, 2].title')
# print(values_object)
