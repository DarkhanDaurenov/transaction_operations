from src.utils import json_file, executed_is, re_format_data, reverse_data, hidden_card, hidden_account, final_function

json_open = json_file("../operations.json")
executed = executed_is(json_open)
correct_data = re_format_data(executed)
format_date = reverse_data(correct_data)
number_card = hidden_card(format_date)
number_account = hidden_account(number_card)
result = final_function(number_account)
for item in result:
    print(item)