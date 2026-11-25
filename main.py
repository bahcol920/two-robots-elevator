import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write("I calculated a 97% chance this elevator ride would be awkward. I did not calculate what to do about it.")
