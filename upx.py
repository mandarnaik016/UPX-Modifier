import sys
import random
import os.path

def randhex():
    return str(random.choice("0123456789ABCDEF")) + str(random.choice("0123456789ABCDEF"))

def change_hex(input_file_name, output_file_name):
    hex_to_find = "555058"
    # hex_to_replace = "585055" # https://gchq.github.io/CyberChef/index.html#recipe=Pseudo-Random_Number_Generator(3,'Hex')
    hex_to_replace = randhex() + randhex() + randhex()
    with open(input_file_name, "rb") as input_file, open(
        output_file_name, "wb"
    ) as output_file:
        file_content = input_file.read()
        file_content_hex = file_content.hex()
        new_content_hex = file_content_hex.replace(hex_to_find, hex_to_replace)
        new_content = bytes.fromhex(new_content_hex)
        output_file.write(new_content)
    print("[*] FILE MODIFIED")

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) < 3:
        print("""
 +-+-+-+ +-+-+-+-+-+-+-+-+
 |U|P|X| |M|O|D|I|F|I|E|R|
 +-+-+-+ +-+-+-+-+-+-+-+-+
                                                                                                      
[*] Usage: upx.exe inputFile.exe outputFile.exe""")
    else:
        input_file_name = sys.argv[1]
        output_file_name = sys.argv[2]
        if os.path.exists(input_file_name):
            change_hex(input_file_name, output_file_name)
        else:
            print("[*] INPUT FILE NOT FOUND")
        
