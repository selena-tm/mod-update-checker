file_path = input("Please input the file path for your mod list (path/to/file.txt): ")

with open(file_path, "r") as file:
    not_updated = 0
    old_version_used = 0
    replaced = 0
    no_longer_needed = 0
    total = 0
    for line in file:
        total += 1
        line = line.strip()
        if line[0] == "[":
            if line[1] == "!":
                not_updated += 1
            elif line[1] == "/":
                old_version_used += 1
            elif line[1] == "R":
                replaced += 1
            elif line[1] == "N":
                no_longer_needed += 1
    print(f"Mods not updated: {not_updated}/{total}")
    print(f"Old version of mod used: {old_version_used}/{total}")
    print(f"Replaced mods: {replaced}/{total}")
    print(f"Mods that are no longer needed: {no_longer_needed}/{total}")