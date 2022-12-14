import os
import sys


def clean_asm(input_file, output_file):
    input_lines = input_file.read().splitlines()
    input_lines = [line
    .replace(" ","")
    .replace("\n","")
    .split("//")[0]
    .split("\t")[0]
    for line in input_lines]

    
    output_file.write("\n"
    .join((line
        .replace("FRAME","frame")
        # .replace("RET","return_address")
        .replace("RETURN_LABEL","Sys.init$ret.") 
    for line in input_lines if 
    line)))





if __name__ == '__main__':
    argument_path = os.path.abspath(sys.argv[1])
    files_to_translate = argument_path
    output_path, extension = os.path.splitext(argument_path)
    output_path += "_clean.asm"
    with open(output_path, 'w') as output_file:
        filename, extension = os.path.splitext(files_to_translate)
        with open(files_to_translate, 'r') as input_file:
            clean_asm(input_file, output_file)
