import random
secret = random.randint(1, 50)
attempt = 1
while True:
  guess = int(input("Guess the number:"))
  if guess == secret:
    print("Your guess is right")
    break
  else:
    print("Your guess is wrong")
    if guess>secret:
      print(f"Your guess is {guess - secret} large")
    else:
      print(f"Your guess is {secret - guess} small")
  attempt += 1

print(f"Total attempt: {attempt}")