#jak zaimplementowac kolejkę w zaamortyzowanym czasie O(1) mając dwa stosy?
#mamy dwa stosy, prawy i lewy, jak chcemy dodac to dodajemy na prawy, jak cgcemy sciagnac to przerzucamy wszystko
#na lewy stos żeby go odwrócić do góry nogami i ściągamy już z lewego
#czas staly wynika z tego, ze kazdy element jest raz wkladany na prawy stos, raz przekladany na lewy i raz zdejmowany