from cgi import print_exception
from email import header
import json
import requests
import urllib3
urllib3.disable_warning()


def get_id_scenario(scenario_name):
    id_scenario = scenario_name.split(' ')
    return id_scenario[0]


def get_card_id_jira(scenario_name, project, product, type_app, platform, actual_round, release, base_url, user):
    url = base_url + "/search"
    id_cenario = get_id_scenario(scenario_name)
    query = {"jql": "project = '"+project+"' And 'Produto -"+product+"' = '"+type_app+"' \
        and 'Plataforma'= "+platform+" and Código ~ '"+id_cenario+"' and \
                Round='"+actual_round+" Round' and Release ~'"+release+"'",
                "fields": ["id","key"]
    }
    query = json.dumps(query)
    header = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'Authorization': 'Basic'+ user  
    }

    try:
        response = requests.post(url, headers=header, data = query, verify = False)
        result_card_id = response.json()
        card_id = result_card_id['issues'][0]['key']
        return card_id
    except OSError as err:
        print_exception("Error", err)


def get_status_transition_id_jira(scenario_name, scenario, project, product, type_app, platform, actual_round, release, base_url, user):
    card_id = get_card_id_jira(scenario_name,project, product, type_app, platform, actual_round, release, base_url, user)
    url = base_url + "/issue/" + card_id + "/transitions"
    status_execucao_cenario = str(scenario.status)
    if str(scenario.status) == "Status.passed":
        status_execucao_cenario = 'Passed'
    else:
        status_execucao_cenario = 'Failed'

    status_id = ''
    header = {
        'Contet-Type': 'application/json',
        'Authorization':'Basic' + user
    }
    try:
        response = requests.get(url, headers=header, verify=False)
        response = response.json()
        result_transitions = response['transitions']
        count = len(result_transitions)
        for i in range(count):
            if response['transitions'][i]['name'] == status_execucao_cenario:
                status_id = response['transitions'][i]['id']
                break
            return status_id
    except OSError as err:
        print_exception("Error", err)