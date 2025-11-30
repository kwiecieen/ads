#dana tablica n liczb, chcemy znalezc tą która byłaby na pozycji k po posortowaniu
#1. Podziel dane na n/5(sufit) grup po 5 elementow. W kazdej grupie znajdz mediane.
#2. Znajdź medianę median, oznaczamy ją x. - rekurencyjnie
#3. Wykonujemy operację partition(z quick sorta) względem x
#4. Kontynuujemy tak jak w zwykłym selectcie.
# ZLOZONOSC CZASOWA:
#O(1), jesli n <= stala
#T(sufit n/5) + T(7n/10 + 6) + an, jesli n > stala (an to czas dzialania partition)
