from conversor import api

print("💱 Conversor de Moedas")
print("----------------------")
print()

def get_amount() -> float:
    amount = input("Digite o valor a ser convertido: ")
    return float(amount)

def get_destiny_currency() -> str:
    destiny_currency = input("Moeda de destino (ex: BRL): ")
    return destiny_currency.upper()

def calculate_live_change(amount: float, destiny_currency: str) -> float:
    live_change = api.get_live_change_by_currency(destiny_currency)
    
    return amount * live_change

if __name__ == "__main__":

    amount = get_amount()
    destiny_currency = get_destiny_currency()

    result = calculate_live_change(amount, destiny_currency)
    
    print()
    print(f'💵 Resultado: {amount} USD = {result} {destiny_currency}')