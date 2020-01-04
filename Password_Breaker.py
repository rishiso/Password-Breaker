import time

start_time = time.time()
characters = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#recursive function for finding passwords
def generate(arr, i):
    if i == len(arr[0]):
        return arr
    else:
        res = []
        for password in arr:
            for char in characters:
                new_password = password[:i] + char + password[i + 1:]
                res.append(new_password)
        return generate(res, i + 1)

count = 0
max_length = 5

#finds passwords of every length
for length in range(1, max_length + 1):
    starting_pw = ["A" * length]
    for i in generate(starting_pw, 0):
        print(i)
        count += 1

print("\nExecution Time: ", int(time.time() - start_time), " seconds")
print(count, " passwords generated.")
