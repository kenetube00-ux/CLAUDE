"""
Pure Python PDF Generator - No external dependencies
Correct xref offset tracking for proper rendering
"""

class PDFDoc:
    def __init__(self, width=612, height=792):
        self.width = width
        self.height = height
        self.pages = []
        self.current_stream = ""

    def new_page(self):
        if self.current_stream:
            self.pages.append(self.current_stream)
        self.current_stream = ""

    def add_text(self, x, y, text, font='F1', size=12, gray=0):
        escaped = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        self.current_stream += f"BT {gray} g /{font} {size} Tf {x} {y} Td ({escaped}) Tj ET\n"

    def add_centered_text(self, y, text, font='F1', size=12, gray=0):
        width = len(text) * size * 0.48
        x = (self.width - width) / 2
        self.add_text(x, y, text, font, size, gray)

    def add_line(self, x1, y1, x2, y2, width=1, gray=0):
        self.current_stream += f"q {gray} G {width} w {x1} {y1} m {x2} {y2} l S Q\n"

    def add_rect(self, x, y, w, h, line_width=1, gray=0):
        self.current_stream += f"q {gray} G {line_width} w {x} {y} {w} {h} re S Q\n"

    def add_filled_rect(self, x, y, w, h, gray=0.9):
        self.current_stream += f"q {gray} g {x} {y} {w} {h} re f Q\n"

    def save(self, filename):
        if self.current_stream:
            self.pages.append(self.current_stream)
            self.current_stream = ""

        # Build PDF with correct byte offsets
        objects = []  # list of (obj_number, bytes)

        # Object 1: Catalog
        objects.append(b"1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n")

        # Object 2: Pages
        page_obj_start = 8  # pages start at obj 8 (after catalog, pages, 5 fonts)
        kid_refs = " ".join([f"{page_obj_start + i*2} 0 R" for i in range(len(self.pages))])
        objects.append(f"2 0 obj\n<< /Type /Pages /Kids [{kid_refs}] /Count {len(self.pages)} >>\nendobj\n".encode())

        # Font objects (3-7)
        objects.append(b"3 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n")
        objects.append(b"4 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>\nendobj\n")
        objects.append(b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Courier >>\nendobj\n")
        objects.append(b"6 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Times-Roman >>\nendobj\n")
        objects.append(b"7 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Times-Bold >>\nendobj\n")

        # Page objects and their content streams
        for page_content in self.pages:
            page_obj_num = len(objects) + 1
            stream_obj_num = page_obj_num + 1
            content_bytes = page_content.encode('latin-1', errors='replace')

            # Page object - reference all fonts
            page_obj = (f"{page_obj_num} 0 obj\n"
                       f"<< /Type /Page /Parent 2 0 R "
                       f"/MediaBox [0 0 {self.width} {self.height}] "
                       f"/Contents {stream_obj_num} 0 R "
                       f"/Resources << /Font << /F1 3 0 R /F2 4 0 R /F3 5 0 R /F4 6 0 R /F5 7 0 R >> >> "
                       f">>\nendobj\n").encode()
            objects.append(page_obj)

            # Content stream object
            stream_obj = (f"{stream_obj_num} 0 obj\n"
                         f"<< /Length {len(content_bytes)} >>\n"
                         f"stream\n").encode()
            stream_obj += content_bytes
            stream_obj += b"\nendstream\nendobj\n"
            objects.append(stream_obj)

        # Write PDF
        output = b"%PDF-1.4\n"

        # Track offsets
        offsets = []
        for obj_bytes in objects:
            offsets.append(len(output))
            output += obj_bytes

        # Cross-reference table
        xref_offset = len(output)
        num_objects = len(objects) + 1  # +1 for object 0
        output += f"xref\n0 {num_objects}\n".encode()
        output += b"0000000000 65535 f \n"
        for offset in offsets:
            output += f"{offset:010d} 00000 n \n".encode()

        # Trailer
        output += f"trailer\n<< /Size {num_objects} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode()

        with open(filename, 'wb') as f:
            f.write(output)
