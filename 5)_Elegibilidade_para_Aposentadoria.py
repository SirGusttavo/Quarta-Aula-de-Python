idade = int(input('Digite sua idade: '))
tempo = int(input('Digite seu tempo de contribuição em anos: '))
if idade >= 65 or tempo >= 30:
    print("Você pode se aposentar!")
else:
    print("Você ainda não pode se aposentar!")