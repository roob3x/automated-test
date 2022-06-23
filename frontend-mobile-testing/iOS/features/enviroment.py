import os
import sys


from common.apis.jira import update_card_jira
from common_ios.environment_iOS import Environment


def after_scenario(context,scenario):
    context.driver.close_app()
    Environment.execution_status(context,scenario)
    if context.config.userdata['move_cards_jira'].upper() in 'TRUE':
        project = conexao_jira()[0]
        product = conexao_jira()[1]
        type_app = conexao_jira()[2]
        platform = conexao_jira()[3]
        actual_round = conexao_jira()[4]
        release = conexao_jira()[5]
        base_url = conexao_jira()[6]
        user = conexao_jira()[7]
        update_card_jira(scenario.name, scenario, project, product, type_app, platform, actual_round, release, base_url, user)