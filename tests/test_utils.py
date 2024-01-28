from datetime import datetime
import json
import pytest
from src.utils import json_file,executed_is,re_format_data,reverse_data,hidden_card,hidden_account,final_function

def test_json_file():
    return json_file("operations.json")


def test_executed_is():
    examples = [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}, {'state': "NOTHING"}]
    result = executed_is(examples)
    assert  result == [{'state': 'EXECUTED'}, {'state': 'EXECUTED'}]


def test_re_format_data():
    day = [{"date": "2022-01-01T12:30:00.000"}, {"date": "2022-01-02T15:45:00.000"}]
    result = re_format_data(day)
    for item in result:
        assert isinstance(item['original_date'], datetime)


def test_reverse_data():
    days = [
        {"original_date": datetime(2022, 1, 1)},
        {"original_date": datetime(2022, 1, 2)},
        {"original_date": datetime(2022, 1, 3)},
    ]
    result = reverse_data(days)
    assert result == [
        {"original_date": datetime(2022, 1, 3)},
        {"original_date": datetime(2022, 1, 2)},
        {"original_date": datetime(2022, 1, 1)},
    ]


def test_hidden_card():
    card_operations = [
        {"from": "1234 5678 9012 3456"},
        {"from": "abcd efgh ijkl mnop qrst"},
        {"from": "foo bar baz qux quux corge grault"},
    ]
    result = hidden_card(card_operations)
    expected = [
        {"from": "1234 5678 9012 3456"},
        {"from": "abcd efgh ijkl mnop qrst"},
        {"from": "foo bar baz qux quux corge grault"},
    ]
    assert result == expected


def test_hidden_account():
    account_operations = [
        {"to": "9876 5432 1098 7654"},
        {"to": "wxyz uvwx ijkl mnop qrst"},
    ]
    result = hidden_account(account_operations)
    expected = [
        {"to": "9876 5432 1098 7654"},
        {"to": "wxyz uvwx ijkl mnop qrst"},
    ]
    assert result == expected


def test_final_function():
    choice = [
        {
            "date": "2022-01-01",
            "description": "Payment",
            "from": "1234 5678 9012 3456",
            "to": "9876 5432 1098 7654",
            "operationAmount": {"amount": 100, "currency": {"name": "USD"}},
        },
        {
            "date": "2022-01-02",
            "description": "Transfer",
            "from": "abcd efgh ijkl mnop qrst",
            "to": "wxyz uvwx ijkl mnop qrst",
            "operationAmount": {"amount": 50, "currency": {"name": "EUR"}},
        },
    ]
    result = final_function(choice)
    expected = [
        "2022-01-01 Payment\n1234 5678 9012 3456 -> 9876 5432 1098 7654\n100 USD\n",
        "2022-01-02 Transfer\nabcd efgh ijkl mnop qrst -> wxyz uvwx ijkl mnop qrst\n50 EUR\n",
    ]
    assert result == expected