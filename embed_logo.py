# Read the base64 logo
with open(r'c:\Users\ayan\Desktop\ACI\logo_base64.txt', 'r') as f:
    base64_logo = f.read().strip()

# Create the data URI
data_uri = f'data:image/png;base64,{base64_logo}'

# Read the HTML file
with open(r'c:\Users\ayan\Desktop\ACI\aayan-cotton.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace the old img src with the data URI
old_img = '<img src="Logo.png" alt="Aayan Cotton Logo" class="logo-img">'
new_img = f'<img src="{data_uri}" alt="Aayan Cotton Logo" class="logo-img">'

html_content = html_content.replace(old_img, new_img)

# Write the updated HTML back
with open(r'c:\Users\ayan\Desktop\ACI\aayan-cotton.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Logo embedded successfully!")
