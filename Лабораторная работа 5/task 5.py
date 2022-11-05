from random import sample
import string


def get_random_password(n=8) -> str:
    generate_password = []
    final_password = []
    while len(generate_password) < n:
        generate_password.append(sample(string.ascii_uppercase, 1))
        generate_password.append(sample(string.ascii_lowercase, 1))
        generate_password.append(sample(string.digits, 1))
    generate_password = sample(generate_password, n)
    for i in generate_password:
        for m in i:
            final_password.append(m)
    final_password = ''.join(final_password)
    return final_password

    ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())
