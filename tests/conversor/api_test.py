from unittest.mock import patch
from conversor.api import get_live_change_by_currency
import pytest

@patch('requests.api.get')
def test_get_live_change_by_currency_success(mock_get):
    mock_get.return_value.json.return_value = {
        "quotes": {
            "USDUSD": 1.0,
            "USDBRL": 5.0,
        }
    }
    currency = "BRL"
    result = get_live_change_by_currency(currency)
    assert result == 5.0

@patch('requests.api.get')
def test_get_live_change_by_currency_error(mock_get):
    mock_get.return_value.json.return_value = {
        "quotes": {
            "USDUSD": 1.0,
        }
    }
    currency = "BRL"
    
    with pytest.raises(ValueError) as excinfo:
        result = get_live_change_by_currency(currency)
        assert result is None
        
    assert "Ocorreu um erro ao buscar a cotação: 'USDBRL'" in str(excinfo.value)