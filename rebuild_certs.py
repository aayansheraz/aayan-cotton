#!/usr/bin/env python3
import base64
import os

# Directory containing certificate images
cert_dir = r"C:\Users\ayan\Desktop\ACI"

# Certificate metadata
certs = [
    {
        "id": 1,
        "file": "cert1.jpg",
        "title": "ISO 9001:2015",
        "description": "Global standard certification ensuring consistent excellence and quality management across our entire manufacturing process."
    },
    {
        "id": 2,
        "file": "cert2.jpg",
        "title": "ISO 13485:2016",
        "description": "Medical device quality management system standard certifying our adherence to international health and safety regulations."
    },
    {
        "id": 3,
        "file": "cert3.jpg",
        "title": "CE Certification",
        "description": "European conformity mark confirming that our products meet all applicable EU directives and quality standards for medical devices."
    },
    {
        "id": 4,
        "file": "cert4.jpg",
        "title": "CE Certified Scope",
        "description": "The official approved product list (Annex 1) detailing the specific surgical dressings we are authorized to manufacture and export."
    },
    {
        "id": 5,
        "file": "cert5.jpg",
        "title": "International Compliance",
        "description": "Full compliance certification meeting all international standards and regulatory requirements for medical device manufacturing and distribution."
    }
]

# Generate certificate cards HTML with embedded base64
html_output = []

for cert in certs:
    cert_path = os.path.join(cert_dir, cert["file"])
    
    # Read and encode certificate image
    with open(cert_path, "rb") as f:
        cert_data = f.read()
        base64_data = base64.b64encode(cert_data).decode('utf-8')
    
    # Create card HTML
    card_html = f'''  <!-- CARD {cert["id"]} -->
  <div class="cert-card reveal" style="height:260px; perspective:1000px; background:none; border:none; padding:0;">
    <div style="position:relative; width:100%; height:100%; transform-style:preserve-3d; transition:transform 0.7s ease;">
      <div style="position:absolute; width:100%; height:100%; backface-visibility:hidden; background:white; border:2px solid #c8f0d8; border-radius:16px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:24px;">
        <h4 style="font-family:'Playfair Display',serif; color:#1a6b3c; margin:12px 0 6px;">{cert["title"]}</h4>
        <p style="font-size:12px; color:#5a8a6e; text-align:center;">{cert["description"]}</p>
        <p style="font-size:11px; color:#2d9b57; margin-top:10px;">Click on the Certificate to see</p>
      </div>
      <div style="position:absolute; width:100%; height:100%; backface-visibility:hidden; transform:rotateY(180deg); border-radius:16px; overflow:hidden;">
        <img src="data:image/jpeg;base64,{base64_data}" alt="{cert["title"]}" style="width:100%; height:100%; object-fit:cover;">
      </div>
    </div>
  </div>
'''
    html_output.append(card_html)

# Write combined HTML to file
output_html = ''.join(html_output)
with open(os.path.join(cert_dir, "certs_html.txt"), "w") as f:
    f.write(output_html)

print("✓ Certificate cards HTML generated")
print(f"✓ Total cards: {len(html_output)}")
print(f"✓ Output saved to: {os.path.join(cert_dir, 'certs_html.txt')}")
