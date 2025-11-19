#opgave 1
source_path = "notes.txt"
dest_path = "notes_new.txt"

def replace_all(old, new, source_path, dest_path):
    # læser alt content i source_path
    with open(source_path, "r") as f:
        content = f.read()

    # ændrer den gamle string med den nye
    updated = content.replace(old, new)

    # skriver det nye resultat ind i filen
    with open(dest_path, "w") as writer:
        writer.write(updated)

# test kald
replace_all("photos","images", source_path, dest_path)
print(open(source_path).read())
print(open(dest_path).read())



