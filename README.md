💳 Calculadora de Valores

Este é um programa em Python que simula um sistema de pagamento de produtos, aplicando descontos ou juros de acordo com a forma de pagamento escolhida pelo usuário.

📌 Funcionalidades
Entrada segura do valor do produto (com validação)
Menu interativo de formas de pagamento
Cálculo automático de:
Descontos
Juros
Parcelamento
Tratamento de erros para entradas inválidas
💰 Formas de Pagamento
Opção	Forma de Pagamento	Condição
1	À vista (dinheiro/cheque)	10% de desconto
2	À vista no cartão	5% de desconto
3	Em até 2x no cartão	Sem desconto
4	3x ou mais no cartão	20% de juros
⚙️ Como funciona
O usuário informa o valor do produto
O sistema valida se o valor é numérico e maior que zero
Um menu é exibido com as formas de pagamento
O usuário escolhe uma opção
O sistema calcula e exibe:
Valor final
Número de parcelas (se houver)
Valor de cada parcela
🛠️ Tecnologias utilizadas
Python 3
Estruturas de repetição (while)
Estruturas condicionais (if, elif, else)
Tratamento de exceções (try/except)
▶️ Como executar
Certifique-se de ter o Python instalado
Salve o código no arquivo:
calculadora-de-valores.py
Execute no terminal:
python calculadora-de-valores.py
⚠️ Validações implementadas
O valor do produto deve ser:
Numérico
Maior que zero
A forma de pagamento deve ser válida (1 a 4)
Parcelamentos acima de 3x exigem número inteiro válido
🚀 Possíveis melhorias
Transformar o código em funções
Criar interface gráfica
Salvar histórico de compras
Permitir múltiplos produtos (carrinho)
👨‍💻 Autor

Desenvolvido por você 😎
Projeto de prática em lógica de programação com Python.
