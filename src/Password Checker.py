name = input("Enter your name: ")
password = input("Enter Your Password: ")

password_starts_length = "*" * len(password)

print(f"Hello {name}, your password {password_starts_length}"
      f" is {len(password)} letters long")
