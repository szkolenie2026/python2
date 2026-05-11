from prettytable import PrettyTable

# Tworzenie obiektu tabeli i nagłówków
tabela = PrettyTable()
tabela.field_names = ["Produkt", "Cena", "Ilość"]

# Dodawanie danych
tabela.add_row(["Chleb", 4.50, 10])
tabela.add_row(["Mleko", 3.20, 5])
tabela.add_row(["Kawa", 25.00, 2])

print(tabela)