"""
Pure Python PDF Generator - No external dependencies
Generates KDP-ready PDF interiors using raw PDF specification
"""

class PDFDoc:
    def __init__(self, width=612, height=792):
        # Default Letter size: 612x792 points (8.5x11 inches)
        self.width = width
        self.height = height
        self.objects = []
        self.pages = []
        self.current_page_streams = []
        self.fonts = {}
        self._setup_fonts()

    def _setup_fonts(self):
        self.fonts = {
            'Helvetica': 'Helvetica',
            'Helvetica-Bold': 'Helvetica-Bold',
            'Courier': 'Courier',
            'Times': 'Times-Roman',
            'Times-Bold': 'Times-Bold',
        }

    def new_page(self):
        if self.current_page_streams:
            self.pages.append(self.current_page_streams)
        self.current_page_streams = []
        # Always start each page with black fill and stroke
        self.current_page_streams.append("0 g 0 G\n")

    def _finish_last_page(self):
        if self.current_page_streams:
            self.pages.append(self.current_page_streams)
            self.current_page_streams = []

    def add_text(self, x, y, text, font='Helvetica', size=12, gray=0):
        """Add text at position. gray=0 is black, gray=1 is white."""
        escaped = text.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
        # Explicitly set text color before rendering
        stream = f"BT {gray} g /{font} {size} Tf {x} {y} Td ({escaped}) Tj ET\n"
        self.current_page_streams.append(stream)

    def add_centered_text(self, y, text, font='Helvetica', size=12, gray=0):
        """Add centered text. gray=0 is black, gray=1 is white."""
        char_width = size * 0.5
        text_width = len(text) * char_width
        x = (self.width - text_width) / 2
        self.add_text(x, y, text, font, size, gray)

    def add_line(self, x1, y1, x2, y2, width=1, gray=0):
        """Draw a line. gray=0 is black."""
        stream = f"{gray} G {width} w {x1} {y1} m {x2} {y2} l S\n"
        self.current_page_streams.append(stream)

    def add_rect(self, x, y, w, h, fill=False, stroke=True, line_width=1, gray=0):
        """Draw a rectangle outline. gray=0 is black."""
        stream = f"{gray} G {line_width} w {x} {y} {w} {h} re S\n"
        self.current_page_streams.append(stream)

    def set_gray(self, gray_level):
        """Set both fill and stroke color."""
        stream = f"{gray_level} g {gray_level} G\n"
        self.current_page_streams.append(stream)

    def reset_color(self):
        """Reset to black fill and stroke."""
        stream = "0 g 0 G\n"
        self.current_page_streams.append(stream)

    def add_filled_rect(self, x, y, w, h, gray=0.9):
        """Draw a filled rectangle, then reset to black."""
        stream = f"q {gray} g {x} {y} {w} {h} re f Q\n"
        self.current_page_streams.append(stream)

    def save(self, filename):
        self._finish_last_page()
        pdf_bytes = self._build_pdf()
        with open(filename, 'wb') as f:
            f.write(pdf_bytes)

    def _build_pdf(self):
        out = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
        offsets = []
        obj_num = 1

        # Catalog
        offsets.append(len(out))
        out += f"{obj_num} 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n".encode()
        obj_num += 1

        # Pages object
        offsets.append(len(out))
        page_refs = " ".join([f"{i} 0 R" for i in range(3, 3 + len(self.pages) * 2, 2)])
        out += (f"{obj_num} 0 obj\n<< /Type /Pages /Kids [{page_refs}] "
                f"/Count {len(self.pages)} >>\nendobj\n").encode()
        obj_num += 1

        # Font objects
        font_obj_start = obj_num
        font_names = ['Helvetica', 'Helvetica-Bold', 'Courier', 'Times-Roman', 'Times-Bold']
        for fname in font_names:
            offsets.append(len(out))
            out += (f"{obj_num} 0 obj\n<< /Type /Font /Subtype /Type1 "
                    f"/BaseFont /{fname} >>\nendobj\n").encode()
            obj_num += 1

        # Build font resource dict
        font_dict_parts = []
        font_keys = ['Helvetica', 'Helvetica-Bold', 'Courier', 'Times-Roman', 'Times-Bold']
        for i, fk in enumerate(font_keys):
            font_dict_parts.append(f"/{fk.replace('-', '')} {font_obj_start + i} 0 R")
        font_dict_parts.append(f"/Helvetica {font_obj_start} 0 R")
        font_dict_parts.append(f"/HelveticaBold {font_obj_start + 1} 0 R")
        font_dict_parts.append(f"/Courier {font_obj_start + 2} 0 R")
        font_dict_parts.append(f"/TimesRoman {font_obj_start + 3} 0 R")
        font_dict_parts.append(f"/TimesBold {font_obj_start + 4} 0 R")
        font_res = " ".join(font_dict_parts)

        # Pages and content streams
        for page_streams in self.pages:
            content_str = "".join(page_streams)
            content_bytes = content_str.encode('latin-1', errors='replace')

            # Page object
            offsets.append(len(out))
            content_obj = obj_num + 1
            out += (f"{obj_num} 0 obj\n<< /Type /Page /Parent 2 0 R "
                    f"/MediaBox [0 0 {self.width} {self.height}] "
                    f"/Contents {content_obj} 0 R "
                    f"/Resources << /Font << {font_res} >> >> "
                    f">>\nendobj\n").encode()
            obj_num += 1

            # Content stream
            offsets.append(len(out))
            out += (f"{obj_num} 0 obj\n<< /Length {len(content_bytes)} >>\n"
                    f"stream\n").encode()
            out += content_bytes
            out += b"\nendstream\nendobj\n"
            obj_num += 1

        # Cross-reference table
        xref_offset = len(out)
        out += b"xref\n"
        out += f"0 {obj_num}\n".encode()
        out += b"0000000000 65535 f \n"
        for offset in offsets:
            out += f"{offset:010d} 00000 n \n".encode()

        # Trailer
        out += (f"trailer\n<< /Size {obj_num} /Root 1 0 R >>\n"
                f"startxref\n{xref_offset}\n%%EOF\n").encode()
        return out
