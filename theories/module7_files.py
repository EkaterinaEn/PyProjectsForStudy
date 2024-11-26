file_name = "module7_files.txt"
text="""
text_in_file
text_in_file
text_in_file
text_in_file
text_in_file
"""
with open(file_name, 'w', encoding="utf-8") as file:
    file.write(text)