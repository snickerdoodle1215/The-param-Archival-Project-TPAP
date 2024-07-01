import os

def extract_jpegs_from_aboot_mbn(file_path):
    with open(file_path, 'rb') as f:
        aboot_data = f.read()
    
    jpeg_headers = b'\xFF\xD8\xFF\xE0'
    start = 0
    count = 0

    while True:
        # Find the next occurrence of JPEG header
        offset = aboot_data.find(jpeg_headers, start)
        if offset == -1:
            break
        
        # Found a JPEG header, locate the end of the JPEG image
        end_offset = aboot_data.find(b'\xFF\xD9', offset)
        if end_offset == -1:
            break
        
        # Extract the JPEG data
        jpeg_data = aboot_data[offset:end_offset + 2]
        
        # Write the JPEG data to a file
        output_filename = f"{count}.jpg"
        with open(output_filename, 'wb') as jpeg_file:
            jpeg_file.write(jpeg_data)
        
        print(f"Extracted {output_filename}")
        
        # Move start position forward
        start = end_offset + 2
        count += 1

    print(f"Total JPEG images extracted: {count}")

# Usage example
if __name__ == "__main__":
    aboot_mbn_file = "param.lfs"
    if os.path.exists(aboot_mbn_file):
        extract_jpegs_from_aboot_mbn(aboot_mbn_file)
    else:
        print(f"File '{aboot_mbn_file}' not found.")
