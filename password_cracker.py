import hashlib
import itertools
import string
import threading
from queue import Queue
import time

def hash_password(password):
    """Hash a password using MD5."""
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def brute_force_worker(queue, target_hash, result):
    while True:
        item = queue.get()
        if item is None:
            break
        length, start, end = item
        for guess in itertools.islice(itertools.product(string.ascii_lowercase + string.digits, repeat=length), start, end):
            guess = ''.join(guess)
            if hash_password(guess) == target_hash:
                result.append(guess)
                return
        queue.task_done()

def threaded_brute_force_attack(target_hash, max_length=8, num_threads=4):
    result = []
    queue = Queue()

    for length in range(1, max_length + 1):
        print(f"Trying length: {length}")
        total_combinations = len(string.ascii_lowercase + string.digits) ** length
        chunk_size = max(1, total_combinations // num_threads)
        
        for i in range(0, total_combinations, chunk_size):
            queue.put((length, i, min(i + chunk_size, total_combinations)))

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=brute_force_worker, args=(queue, target_hash, result))
        t.start()
        threads.append(t)

    for _ in range(num_threads):
        queue.put(None)

    for t in threads:
        t.join()

    return result[0] if result else None

def dictionary_worker(queue, target_hash, result):
    while True:
        password = queue.get()
        if password is None:
            break
        hashed = hash_password(password)
        print(f"Trying password: {password}, Hash: {hashed}")
        if hashed == target_hash:
            result.append(password)
            return
        queue.task_done()

def threaded_dictionary_attack(target_hash, dictionary_file='common_passwords.txt', num_threads=4):
    result = []
    queue = Queue()

    try:
        with open(dictionary_file, 'r', encoding='utf-8') as file:
            for line in file:
                queue.put(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {dictionary_file} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=dictionary_worker, args=(queue, target_hash, result))
        t.start()
        threads.append(t)

    for _ in range(num_threads):
        queue.put(None)

    for t in threads:
        t.join()

    return result[0] if result else None

def main():
    target_hash = input("Enter the MD5 hash to crack: ").strip().lower()
    print(f"Hash of 'password123': {hash_password('password123')}")
    
    test_password = "password123"
    test_hash = hash_password(test_password)
    print(f"Test: Password '{test_password}' hashes to {test_hash}")
    print(f"Target hash: {target_hash}")
    print(f"Do they match? {test_hash == target_hash}")
    
    attack_type = input("Choose attack type (1 for brute force, 2 for dictionary): ")

    start_time = time.time()

    if attack_type == '1':
        result = threaded_brute_force_attack(target_hash)
    elif attack_type == '2':
        result = threaded_dictionary_attack(target_hash)
    else:
        print("Invalid attack type.")
        return

    end_time = time.time()

    if result:
        print(f"Password cracked! The password is: {result}")
    else:
        print("Password not found.")

    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()