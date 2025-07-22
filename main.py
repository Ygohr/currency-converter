from conversor import api

print("💱 Conversor de Moedas")
print("----------------------")
print()

def get_amount() -> float:
    while True:
        amount = input("Digite o valor a ser convertido: ")
        try:
            return float(amount)
        except ValueError:
            print("Por favor, digite um número válido.")

def get_destiny_currency() -> str:
    while True:
        destiny_currency = input("Digite a moeda de destino (ex: BRL): ")
        if destiny_currency.isalpha():
            return destiny_currency.upper()
        else:
            print("Por favor, digite uma moeda válida (apenas letras).")

def calculate_live_change(amount: float, destiny_currency: str) -> float:
    try:
        live_change = api.get_live_change_by_currency(destiny_currency)
        return amount * live_change
    except Exception as e:
        print(f"Erro ao obter cotação: {e}")
        return None

if __name__ == "__main__":
    amount = get_amount()
    destiny_currency = get_destiny_currency()
    result = calculate_live_change(amount, destiny_currency)

    if result is not None:
        print()
        print(f'💵 Resultado: {amount} USD = {result} {destiny_currency}')
    else:
        print("Conversão não realizada.")