import json
from datetime import datetime


def json_file(filename):
    with open(filename, 'r') as file:
        json_open = json.load(file)
    return json_open


def executed_is(operation):
    executed_data = [item for item in operation if item.get('state') == 'EXECUTED']
    return executed_data


def re_format_data(day):
    for item in day:
        original_date = datetime.strptime(item['date'], '%Y-%m-%dT%H:%M:%S.%f')
        item['date'] = original_date.strftime('%d.%m.%Y')
        item['original_date'] = original_date
    return day

def reverse_data(days):
    sorted_data = sorted(days, key=lambda x: x['original_date'], reverse=True)
    return sorted_data[:5]



def hidden_card(card_operations):
    for operation in card_operations:
        card_split = operation.get('from', '').split()
        if len(card_split) == 2 and len(card_split[1]) == 16:
            first_element = card_split[0]
            second_element = card_split[1]
            mask_card = f"{first_element} {second_element[:4]} {second_element[5:7]} ** **** {second_element[-4:]}"
            operation['from'] = mask_card
            continue
        elif len(card_split) == 2 and len(card_split[1]) == 20:
            first_element = card_split[0]
            second_element = card_split[1]
            mask_card = f"{first_element} {second_element[:4]} {second_element[5:7]} ** **** {second_element[-4:]}"
            operation['from'] = mask_card
            continue
        elif len(card_split) >= 3 and len(card_split[2]) == 16:
            first_element = card_split[0]
            second_element = card_split[1]
            third_element = card_split[2]
            mask_card = f"{first_element} {second_element} {third_element[:4]} {third_element[5:7]} ** **** {third_element[-4:]}"
            operation['from'] = mask_card
    return card_operations



def hidden_account(account_operations):
    for operation in account_operations:
        account_split = operation.get('to').split()
        if len(account_split) == 2 and len(account_split[1]) == 16:
            first_element = account_split[0]
            second_element = account_split[1]
            account_card = f"{first_element} ** {second_element[-4:]}"
            operation['to'] = account_card
            continue
        elif len(account_split) == 2 and len(account_split[1]) == 20:
            first_element = account_split[0]
            second_element = account_split[1]
            account_card = f"{first_element} ** {second_element[-4:]}"
            operation['to'] = account_card
    return account_operations


def final_function(choice):
    aim_course = []
    for operation in choice:
        from_value = operation.get('from')
        final_result = f"{operation['date']} {operation['description']}\n{from_value} -> {operation['to']}\n{ operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"
        aim_course.append(final_result)
    return aim_course