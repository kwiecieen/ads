'''mamy waluty od nr. 1 do n
K[x][y] = ile waluty y dostaję za 1 x
Czy istnieje seria transakcji gdzie za 1-kę danej waluty dostaję >1 tej waluty?'''

'''1.rozw: zamiast wagi K[x][y] ustawiamy -log K[x][y] '''
'''2.rozw: w momencie gdy nie da sie wymienic kazdej waluty na kazda, to dodajemy wierzcholek ktory jest polaczany
z kazdym innym z wagą 0 '''