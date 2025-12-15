#!/usr/bin/env python3
from pdf2image import convert_from_path
import os

# Convert PDFs to PNG images
pdf_files = ['static/images/fgattn_overview.pdf', 'static/images/flashattn_overview.pdf']

for pdf_file in pdf_files:
    if os.path.exists(pdf_file):
        print(f"Converting {pdf_file}...")
        # Convert PDF to images (one image per page)
        images = convert_from_path(pdf_file, dpi=300)
        
        # Get the base name without extension
        base_name = os.path.splitext(pdf_file)[0]
        
        # Save the first page as PNG
        if images:
            output_file = f"{base_name}.png"
            images[0].save(output_file, 'PNG')
            print(f"Saved to {output_file}")
    else:
        print(f"File not found: {pdf_file}")

print("Conversion complete!")
