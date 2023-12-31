def finding_symmetry(word):
# Usunięcie białych znaków i zmiana na małe litery
    word = word.replace(" ", "").lower()
    return word == word[::-1]

# Lista do sprawdzenia
words = ["kajak", "potop", "hello", "radar", "python", "level"]
sentences = ["No lemon, no melon", "Stressed desserts", "Nobody's perfect", "Never odd or even", "Some men interpret nine memos", "Sad but true"]

# Sprawdzenie każdego wyrazu
for word in words:
    result = finding_symmetry(word)
    print(f'Czy "{word}" to palindrom? {result}')

# Sprawdzenie każdego zdania
for sentence in sentences:
    result = finding_symmetry(sentence)
    print(f'Czy "{sentence}" to palindrom? {result}')