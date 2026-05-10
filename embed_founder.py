#!/usr/bin/env python3
import base64
import os

# Path to founder image
founder_img_path = r'c:\Users\ayan\Desktop\ACI\founder.jpg'

# Check if file exists
if not os.path.exists(founder_img_path):
    print(f"Error: {founder_img_path} not found!")
    print("Please save the founder picture as 'founder.jpg' in the ACI folder")
    exit(1)

# Read and encode the image
with open(founder_img_path, 'rb') as img_file:
    img_data = img_file.read()
    base64_img = base64.b64encode(img_data).decode('utf-8')

# Create data URI
data_uri = f'data:image/jpeg;base64,{base64_img}'

# Read HTML file
html_path = r'c:\Users\ayan\Desktop\ACI\aayan-cotton.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the founder image src
old_src = 'src="" alt="Founder" id="founder-img"'
new_src = f'src="{data_uri}" alt="Founder" id="founder-img"'

if old_src in html_content:
    html_content = html_content.replace(old_src, new_src)
    print("✓ Founder image successfully embedded!")
else:
    print("Error: Could not find image placeholder in HTML")
    exit(1)

# Write updated HTML
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✓ HTML file updated successfully!")
print(f"✓ Image size: {len(img_data)} bytes")
print(f"✓ Base64 size: {len(base64_img)} characters")
