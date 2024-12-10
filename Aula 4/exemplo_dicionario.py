produto_01: dict = {
    'nome':'sapato',
    'quantidade': 39,
    'preco':10.38,
    'disponibilidade': True
}

produto_02: dict = {
    'nome':'televisao',
    'quantidade': 10,
    'preco':70.38,
    'disponibilidade': False
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)
print(carrinho)