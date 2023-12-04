import random

def generate_lotto_numbers():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)

lotto_numbers = generate_lotto_numbers()
print("추출된 로또 번호:", lotto_numbers)