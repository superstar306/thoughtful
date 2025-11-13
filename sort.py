def sort(width, height, length, mass):
    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Example tests
print(sort(100, 100, 100, 10))  # STANDARD
print(sort(200, 50, 50, 10))    # SPECIAL
print(sort(100, 100, 100, 25))  # SPECIAL
print(sort(200, 200, 200, 25))  # REJECTED
