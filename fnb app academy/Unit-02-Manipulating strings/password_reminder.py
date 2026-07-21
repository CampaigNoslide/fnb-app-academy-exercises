Username = input("Enter your username: " )
password = input("Enter your password: " ).strip()

print(f"Hello {Username}, your password is hint starts with {(password[0]).upper()} and ends with an {(password[-1]).upper()} " )

