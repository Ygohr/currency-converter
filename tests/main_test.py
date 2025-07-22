import pytest
from unittest.mock import patch
from main import get_amount, get_destiny_currency, calculate_live_change

@patch('builtins.input', side_effect=['abc', '10.5'])
def test_get_amount_valid_and_invalid(mock_input):
    result = get_amount()
    assert result == 10.5

@patch('builtins.input', side_effect=['123', 'brl'])
def test_get_destiny_currency_valid_and_invalid(mock_input):
    result = get_destiny_currency()
    assert result == 'BRL'

@patch('conversor.api.get_live_change_by_currency', return_value=5.0)
def test_calculate_live_change_success(mock_api):
    result = calculate_live_change(2, 'BRL')
    assert result == 10.0

@patch('conversor.api.get_live_change_by_currency', side_effect=Exception('Erro de API'))
def test_calculate_live_change_error(mock_api, capsys):
    result = calculate_live_change(2, 'BRL')
    assert result is None
    captured = capsys.readouterr()
    assert 'Erro ao obter cotação' in captured.out or captured.err
