def find_32nd_occurrence(file_path, output_path)
    # Define the hexadecimal sequence to search for
    hex_sequence = bytes.fromhex(FFD8FFE0)
    
    # Initialize counters
    occurrence_count = 0
    position = -1
    
    try
        # Read the file in binary mode
        with open(file_path, 'rb') as file
            data = file.read()
            
            # Search for the 32nd occurrence
            for i in range(len(data) - len(hex_sequence) + 1)
                if data[ii + len(hex_sequence)] == hex_sequence
                    occurrence_count += 1
                    if occurrence_count == 32
                        position = i
                        break
        
        # Write the result to the output file
        with open(output_path, 'w') as output_file
            if position != -1
                output_file.write(fThe 32nd occurrence of the hex sequence 'FFD8FFE0' is at byte position {position}n)
            else
                output_file.write(The hex sequence 'FFD8FFE0' does not occur 32 times in the file.n)
                
        print(fResults saved to {output_path})
        
    except Exception as e
        print(fAn error occurred {e})

# Usage
input_file = aboot.mbn  # Change this to the path of your input file
output_file = pathtoyouroutput_file.txt  # Change this to the desired output file path
find_32nd_occurrence(input_file, output_file)
