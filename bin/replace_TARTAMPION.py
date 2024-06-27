import fileinput
import argparse

# Replace all mentions of TARTAMPION with the clermont_out path 
if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("modif_script", help="Path to the modification script")
    parser.add_argument("clermont_out", help="Path to the clermont_out file")
    args = parser.parse_args()

    modif_script = args.modif_script
    clermont_out = args.clermont_out

    # Replace all mentions of TARTAMPION with the clermont_out path
    lines = [] 
    with fileinput.FileInput(modif_script, inplace=True) as file:
        for line in file:
            line = line.replace('TARTAMPION', clermont_out)
            lines.append(line)
    # overwrite the file with the new content
    with open(modif_script, 'w') as file:
        for line in lines:
            file.write(line)