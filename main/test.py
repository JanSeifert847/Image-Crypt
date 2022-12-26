import base64

# Open the PNG file in binary mode
with open('test.png', 'rb') as file:
    # Read the contents of the file
    png_data = file.read()

# Encode the binary data into a base64 string
png_string = base64.b64encode(png_data).decode('utf-8')

# Print the resulting string
print(png_string)
