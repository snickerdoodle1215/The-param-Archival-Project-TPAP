def find_32nd_occurrence(file_path, output_path):
    hex_sequence = bytes.fromhex("FFD8FFE0")
    occurrence_count = 0
    position = -1

    try:
        with open(file_path, 'rb') as file:
            data = file.read()

            for i in range(len(data) - len(hex_sequence) + 1):
                if data[i:i + len(hex_sequence)] == hex_sequence:
                    occurrence_count += 1
                    if occurrence_count == 32:
                        position = i
                        break

        with open(output_path, 'w') as output_file:
            if position != -1:
                output_file.write(f"The 32nd occurrence of the hex sequence 'FFD8FFE0' is at byte position: {position}\n")
            else:
                output_file.write("The hex sequence 'FFD8FFE0' does not occur 32 times in the file.\n")

        print(f"Results saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
    except IOError as e:
        print(f"IO error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Usage
input_file = "aboot.mbn"  # Change this to the path of your input file
output_file = "whereisit_jpg31.txt"  # Change this to the desired output file path
find_32nd_occurrence(input_file, output_file)
