# definiujemy macierz cyfr "1" i "0"
digits = [
    "111111101101101111111",  # 0
    "001001001001001001001",  # 1
    "111001111100111100111",  # 2
    "111001111001111001111",  # 3
    "101101111001001001001",  # 4
    "111100111001111001111",  # 5
    "111100111101101111111",  # 6
    "111001001001001001001",  # 7
    "111111111101111111111",  # 8
    "111101111001111001111"   # 9
]

# funkcja wyświetlająca liczbę binarną na ekranie
function display_binary(num::Int)
    # zamieniamy liczbę na napis i dodajemy wiodące zera
    binary_str = string(num, base=2)
    while length(binary_str) < 4
        binary_str = "0" * binary_str
    end
    
    # wyświetlamy cyfry
    for i in 1:7  # każda cyfra ma 7 rzędów
        for digit in binary_str
            index = parse(Int, digit) + 1  # indeks cyfry 0-9
            row = digits[index][((i - 1) * 3 + 1):(i * 3)]  # wybieramy odpowiedni rząd
            for bit in row
                if bit == '1'
                    print("██")
                else
                    print("  ")
                end
            end
            print("  ")  # odstęp między cyframi
        end
        println()
    end
end

# testujemy funkcję wyświetlając liczby od 0 do 15
for i in 0:15
    display_binary(i)
    sleep(0.5)
    # czyszczenie ekranu
    print("\033[2J\033[H")
end
