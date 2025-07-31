import random
import string

# генерируем уникальные данные
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))