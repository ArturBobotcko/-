import random

ru_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def generate_key():
    p = 29
    q = 73

    first_private_key = random.randint(0, p - 1)
    second_private_key = random.randint(0, p - 1)
    first_public_key = pow(q, first_private_key) % p
    second_public_key = pow(q, second_private_key) % p

    first_session_key = pow(second_public_key, first_private_key) % p
    second_session_key = pow(first_public_key, second_private_key) % p

    return first_session_key

def caesar_encrypt(text, key):
    shifted_ru_alphabet = ru_alphabet[key:] + ru_alphabet[:key]
    encrypted_text = ''
    for char in text:
        if char.lower() in ru_alphabet:
            index = ru_alphabet.index(char.lower())
            encrypted_char = shifted_ru_alphabet[index]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, key):
    shifted_ru_alphabet = ru_alphabet[key:] + ru_alphabet[:key]
    decrypted_text = ''
    for char in text:
        if char.lower() in shifted_ru_alphabet:
            index = shifted_ru_alphabet.index(char.lower())
            decrypted_char = ru_alphabet[index]
            if char.isupper():
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

session_key = generate_key()

message_to_alice = 'Привет, как дела? Пошли гулять :)'
encrypted_message = caesar_encrypt(message_to_alice, session_key)
print("Зашифрованное сообщение для Алисы: ", encrypted_message)
decrypted_message = caesar_decrypt(encrypted_message, session_key)
print("Расшифрованное сообщение для Алисы: ", decrypted_message)