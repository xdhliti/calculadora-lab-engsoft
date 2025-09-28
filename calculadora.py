def calculadora(valor1, valor2, operacao):
    try:
        num1 = float(valor1)
        num2 = float(valor2)
    except (ValueError, TypeError):
        return None

    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        if num2 == 0:
            return None
        return num1 / num2
    elif operacao == '^':
        return num1 ** num2
    else:
        return None