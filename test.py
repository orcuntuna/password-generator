import pwg

# generate password 6 character
simple = pwg.generate(6)
print("simple password: ", simple)

# generate password 16 character (default)
medium = pwg.generate()
print("medium password: ", medium)

# generate password 6 character
hard = pwg.generate(32)
print("hard password: ", hard)

