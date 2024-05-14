#Створення набору унікальних літер для комбінацій
def unique_letters(string1, string2, string3):
    unique_letters = set()

    for string in [string1, string2, string3]:
        unique_letters.update(set(string))

    return unique_letters

#Підрахунок суми значень для певного слова
def transfer(list_in: list, conform_dict: dict ):
    transfer = 0
    for i in range(len(list_in)):
        if list_in[i] in conform_dict:
            transfer += int(conform_dict[list_in[i]])
        else:
            return False
    return transfer


def generate_permutations(string1, string2, string3, unique_chars):
    #Перевірка, чи літери позначаються цифрами від 0 до 9.
    if len(unique_chars) > 10:
        print("Sorry, there are a lot of unique characters.")
        return []

    list_1 = list(string1)
    list_2 = list(string2)
    list_3 = list(string3)

    digits = '0123456789'
    used_digits = set()
    permutations_list = []

    #Заповнення всіх можливих комбінацій через backtracking:
    # 1. Функція зупиняється при умові, що довжина комбінації рівна довжині кількості унікальних букв.
    # 2. За допомогою set() рекурсивно формуємо унікальний набір до п.1.
    # 3. При формуванні permutations_list додаємо умову розв'язку кросфорду

    def backtrack(current_permutation):
        if len(current_permutation) == len(unique_chars):
            conform_dict = dict(zip(unique_chars, current_permutation))

            term_1 = transfer(list_1, conform_dict)
            term_2 = transfer(list_2, conform_dict)
            total = transfer(list_3, conform_dict)
            if term_1 + term_2 == total:
                permutations_list.append(tuple(current_permutation))
                print(term_1, term_2, total)
            return

        for digit in digits:
            if digit not in used_digits:
                used_digits.add(digit)
                backtrack(current_permutation + [digit])
                used_digits.remove(digit)

    backtrack([])

    return permutations_list

string1 = 'more'
string2 = 'send'
string3 = 'money'
print(list(string1))
unique_chars = unique_letters(string1,string2,string3)
print(generate_permutations(string1,string2,string3, unique_chars))

