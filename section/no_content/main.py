users_db = []

def register_user(___):
    if ___:
        ___ "Registration failed: age must be 18 or older."
    
    user = {"username": ___, "email": ___, "age": ___}
    users_db.___(___)
    
    ___ f"User {username} registered successfully!"

# Pass the parameters in any way to register a user
result1 = register_user(___)

# Testing the result
print(result1)
print(users_db)  # List of registered users
