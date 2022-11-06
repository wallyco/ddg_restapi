import requests
import pytest


def test_response_for_presidents():
    list_of_pres_lastnames = []
    list_of_ddg_results = []
    list_of_corresponding_result = []

    ddg_url = "https://api.duckduckgo.com"
    ddg_response = requests.get(ddg_url + "/?q=presidents of the united states&format=json")
    ddg_rsp_data = ddg_response.json()

    pres_url = 'https://www.govtrack.us/api/v2/'
    pres_response = requests.get(pres_url + "role?role_type=president")
    pres_data = pres_response.json()

    for data in ddg_rsp_data['RelatedTopics']:
        list_of_ddg_results.append(data['Text'])

    for data in pres_data['objects']:
        data = data['person']
        list_of_pres_lastnames.append(data['lastname'])

    for data in list_of_ddg_results:
        for lastname in list_of_pres_lastnames:
            if data.__contains__(lastname):
                list_of_corresponding_result.append(lastname)

    assert set(list_of_corresponding_result) == set(list_of_pres_lastnames)
