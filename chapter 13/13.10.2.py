def replace_all(old, new, source_path, dest_path):
    reader = open(source_path)                      # read the contents of the source file
    content = reader.read()
    reader.close()


    if old in content:                              # Check if the old string exists in the content
        new_content = content.replace(old, new)     # replace the old string with the new

        writer = open(dest_path, 'w')               # write the result into the destination file
        writer.write(new_content)
        writer.close()

        print(f"Replaced '{old}' with '{new}' in the file.")
    else:
        writer = open(dest_path, 'w')               # write the result into the destination file
        writer.write(content)
        writer.close()

        print(f"Pattern '{old}' not found. File copied without changes.")



source = r'C:\Users\desib\IPV\chapter 13\data\photos\notes.txt'
dest = r'C:\Users\desib\IPV\chapter 13\data\photos\new_notes.txt'

replace_all('photos', 'images', source, dest)



# 'w' - overwrites everything
#open('file.txt', 'w').write('Hello')  # file.txt now contains only: "Hello"

# 'a' - adds to the end
#open('file.txt', 'a').write(' World') # file.txt now contains: "Hello World"
