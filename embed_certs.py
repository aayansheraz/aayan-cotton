#!/usr/bin/env python3
import base64
import os

html_path = r'c:\Users\ayan\Desktop\ACI\aayan-cotton.html'
aci_folder = r'c:\Users\ayan\Desktop\ACI'

# Read HTML file
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Convert all certificates to base64 and replace
for i in range(1, 5):
    cert_file = os.path.join(aci_folder, f'cert{i}.jpg')
    
    if not os.path.exists(cert_file):
        print(f"⚠ Warning: {cert_file} not found!")
        continue
    
    # Read and encode
    with open(cert_file, 'rb') as f:
        cert_data = f.read()
        base64_cert = base64.b64encode(cert_data).decode('utf-8')
    
    data_uri = f'data:image/jpeg;base64,{base64_cert}'
    
    # Replace in HTML
    old_src = f'src="cert{i}.jpg"'
    new_src = f'src="{data_uri}"'
    
    if old_src in html_content:
        html_content = html_content.replace(old_src, new_src)
        print(f"✓ cert{i}.jpg embedded successfully!")
    
    # Also replace in the lightbox href
    old_href = f'href="cert{i}.jpg"'
    new_href = f'href="{data_uri}"'
    
    if old_href in html_content:
        html_content = html_content.replace(old_href, new_href)
        print(f"✓ cert{i}.jpg lightbox link updated!")

# Write back
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("\n✓ All certificates embedded successfully!")
print("✓ Your HTML will now work on all devices!")
