import mammoth
import os
import glob
from pathlib import Path
import shutil

def doc_to_markdown(input_file,directory,out_directory):
    dirpath = Path(out_directory)
    if (dirpath.exists()==False):
        os.makedirs(dirpath)
    print(dirpath)
    output_file = out_directory +"\\"+ input_file[:len(input_file)-4]
    with open(directory+"\\"+input_file, "rb") as docx_file:
        result = mammoth.convert_to_markdown(docx_file)
    with open(output_file, "w",encoding='utf-8') as markdown_file:
        markdown_file.write(result.value)

def choose_directory(directory):
    os.chdir(directory)
    for root, dirs, files in os.walk(".", topdown = False):
            for name in files:
                doc_to_markdown(name,root,"md/"+root) 