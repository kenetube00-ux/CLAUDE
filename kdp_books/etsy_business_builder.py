#!/usr/bin/env python3
"""Etsy Digital Product Business Builder - 20 High-Quality Books (579-598)
Full production: 60-120 pages, professional formatting, worksheets, templates"""
import sys, os
sys.path.insert(0, '/projects/sandbox/CLAUDE/kdp_books')
from pdf_utils import PDFDoc

AUTHOR = "Daniel Tesfamariam"
BRAND = "Bible Made Simple Publishing"

def create_pro_book(book_num, filename, title, subtitle, badge, cover_features, sections):
    """Create a professionally formatted Etsy digital product PDF"""
    pdf = PDFDoc(width=612, height=792)
    
    # ===== COVER PAGE (Professional) =====
    pdf.new_page()
    pdf.add_filled_rect(0, 0, 612, 792, gray=0.97)
    pdf.add_filled_rect(0, 600, 612, 192, gray=0.07)
    pdf.add_rect(16, 16, 580, 760, line_width=2.5, gray=0.15)
    pdf.add_rect(24, 24, 564, 744, line_width=0.7, gray=0.4)
    # Title
    tlines = title.split('\n')
    ty = 748 if len(tlines) <= 2 else 762
    for i, tl in enumerate(tlines):
        pdf.add_centered_text(ty - i*38, tl, font='F2', size=26, gray=0.97)
    pdf.add_centered_text(608, subtitle, font='F4', size=11, gray=0.72)
    # Badge
    pdf.add_filled_rect(180, 555, 252, 24, gray=0.18)
    pdf.add_text(195, 561, badge, font='F2', size=9, gray=0.95)
    # Features
    y = 510
    for feat in cover_features[:6]:
        pdf.add_centered_text(y, f"* {feat}", font='F1', size=9, gray=0.3)
        y -= 18
    # Format info
    pdf.add_line(150, 400, 462, 400, width=1, gray=0.3)
    pdf.add_centered_text(375, "Instant Digital Download | Printable PDF | 8.5 x 11", font='F1', size=9, gray=0.35)
    pdf.add_centered_text(350, "60-120 Pages of Actionable Content", font='F1', size=9, gray=0.4)
    # Author
    pdf.add_centered_text(200, f"By {AUTHOR}", font='F2', size=13, gray=0.15)
    pdf.add_centered_text(175, BRAND, font='F1', size=9, gray=0.4)
    # Footer
    pdf.add_filled_rect(0, 24, 612, 45, gray=0.07)
    pdf.add_centered_text(42, "Personal Use License | Do Not Redistribute", font='F1', size=8, gray=0.7)

    # ===== TERMS OF USE =====
    pdf.new_page()
    pdf.add_centered_text(750, "Terms of Use & Welcome", font='F2', size=16, gray=0.12)
    pdf.add_line(150, 738, 462, 738, width=0.5, gray=0.3)
    terms = [
        "Thank you for purchasing this resource!","",
        "WHAT YOU GET:",
        "- Complete printable PDF (60-120 pages)",
        "- Professional worksheets and templates",
        "- Checklists and action plans",
        "- Quick-reference guides",
        "- Bonus resources section","",
        "PERSONAL USE LICENSE:",
        "- Print unlimited copies for your household",
        "- Use for personal development/planning",
        "- Share with spouse/partner (same household)",
        "- Do NOT resell, redistribute, or share the file",
        "- Do NOT upload to any website or platform","",
        "PROFESSIONAL USE (if applicable):",
        "- Therapists/coaches: use with up to 20 clients",
        "- Teachers: use in your classroom","",
        "DISCLAIMER:",
        "This is an educational resource. It does not replace",
        "professional advice. Consult qualified professionals","for specific medical, legal, or financial concerns.","",
        "LOVED THIS? Leave a 5-star review on Etsy!",
        f"(c) 2025 {AUTHOR} | {BRAND}",
    ]
    y = 710
    for line in terms:
        pdf.add_text(72, y, line, font='F1', size=9.5, gray=0.2)
        y -= 17

    # ===== TABLE OF CONTENTS =====
    pdf.new_page()
    pdf.add_centered_text(750, "Table of Contents", font='F2', size=18, gray=0.1)
    pdf.add_line(150, 738, 462, 738, width=0.5, gray=0.3)
    toc_y = 705
    ch_num = 0
    for sec in sections:
        if sec[0] == 'chapter' or sec[0] == 'section_title':
            ch_num += 1
            if toc_y < 80:
                pdf.new_page()
                toc_y = 740
            pdf.add_text(72, toc_y, f"{ch_num}. {sec[1]}", font='F1', size=10, gray=0.2)
            toc_y -= 22

    # ===== CONTENT PAGES =====
    for sec in sections:
        stype = sec[0]
        
        if stype == 'chapter':
            # Chapter title page
            pdf.new_page()
            pdf.add_filled_rect(0, 380, 612, 80, gray=0.07)
            pdf.add_centered_text(425, sec[1], font='F2', size=20, gray=0.97)
            if len(sec) > 2:
                pdf.add_centered_text(395, sec[2], font='F4', size=10, gray=0.7)
            
        elif stype == 'text':
            # Text content page
            pdf.new_page()
            pdf.add_text(72, 750, sec[1], font='F2', size=12, gray=0.12)
            pdf.add_line(72, 738, 540, 738, width=0.5, gray=0.3)
            paragraphs = sec[2] if len(sec) > 2 else []
            y = 710
            for para in paragraphs:
                if not para:
                    y -= 10
                    continue
                words = para.split()
                line = ""
                for word in words:
                    test = line + " " + word if line else word
                    if len(test) * 5.2 > 450:
                        if y < 60:
                            pdf.new_page()
                            pdf.add_text(72, 770, sec[1][:35], font='F1', size=8, gray=0.5)
                            y = 745
                        pdf.add_text(72, y, line, font='F1', size=10, gray=0.15)
                        y -= 14
                        line = word
                    else:
                        line = test
                if line:
                    if y < 60:
                        pdf.new_page()
                        y = 745
                    pdf.add_text(72, y, line, font='F1', size=10, gray=0.15)
                    y -= 14
                y -= 6
                
        elif stype == 'worksheet':
            # Interactive worksheet page
            pdf.new_page()
            pdf.add_centered_text(765, sec[1], font='F2', size=12, gray=0.12)
            pdf.add_line(72, 753, 540, 753, width=0.5, gray=0.3)
            if len(sec) > 2 and sec[2]:
                pdf.add_text(72, 735, sec[2], font='F4', size=9, gray=0.4)
            fields = sec[3] if len(sec) > 3 else []
            y = 710
            for f in fields:
                if y < 55:
                    pdf.new_page()
                    pdf.add_text(72, 770, sec[1][:35], font='F1', size=8, gray=0.5)
                    y = 745
                if f.startswith('#'):
                    y -= 4
                    pdf.add_text(72, y, f[1:], font='F2', size=10, gray=0.12)
                    y -= 17
                elif f == '_':
                    pdf.add_line(72, y, 540, y, width=0.3, gray=0.6)
                    y -= 18
                elif f.startswith('['):
                    pdf.add_rect(72, y-9, 11, 11, line_width=0.5, gray=0.4)
                    pdf.add_text(90, y-6, f[1:], font='F1', size=9.5, gray=0.2)
                    y -= 18
                elif f.startswith('>'):
                    pdf.add_text(82, y, f[1:], font='F4', size=9, gray=0.35)
                    y -= 15
                else:
                    pdf.add_text(72, y, f, font='F1', size=9.5, gray=0.2)
                    y -= 14
                    
        elif stype == 'checklist':
            pdf.new_page()
            pdf.add_centered_text(765, sec[1], font='F2', size=12, gray=0.12)
            pdf.add_line(72, 753, 540, 753, width=0.5, gray=0.3)
            items = sec[2] if len(sec) > 2 else []
            y = 725
            for item in items:
                if y < 55:
                    pdf.new_page()
                    pdf.add_text(72, 770, sec[1][:35], font='F1', size=8, gray=0.5)
                    y = 745
                pdf.add_rect(72, y-9, 11, 11, line_width=0.5, gray=0.4)
                pdf.add_text(90, y-6, item, font='F1', size=9.5, gray=0.2)
                y -= 20
                
        elif stype == 'tracker':
            pdf.new_page()
            pdf.add_centered_text(765, sec[1], font='F2', size=12, gray=0.12)
            pdf.add_line(72, 753, 540, 753, width=0.5, gray=0.3)
            rows = sec[2] if len(sec) > 2 else []
            y = 725
            for row in rows:
                if y < 55:
                    pdf.new_page()
                    y = 745
                pdf.add_filled_rect(72, y-4, 468, 18, gray=0.94)
                pdf.add_text(78, y, row, font='F1', size=9, gray=0.2)
                y -= 22
                
        elif stype == 'faq':
            pdf.new_page()
            pdf.add_centered_text(765, "Frequently Asked Questions", font='F2', size=12, gray=0.12)
            pdf.add_line(72, 753, 540, 753, width=0.5, gray=0.3)
            qa_pairs = sec[1] if len(sec) > 1 else []
            y = 720
            for q, a in qa_pairs:
                if y < 100:
                    pdf.new_page()
                    y = 745
                pdf.add_text(72, y, f"Q: {q}", font='F2', size=10, gray=0.12)
                y -= 16
                # Wrap answer
                words = a.split()
                line = ""
                for word in words:
                    test = line + " " + word if line else word
                    if len(test) * 5 > 430:
                        pdf.add_text(82, y, line, font='F1', size=9.5, gray=0.25)
                        y -= 13
                        line = word
                    else:
                        line = test
                if line:
                    pdf.add_text(82, y, line, font='F1', size=9.5, gray=0.25)
                    y -= 13
                y -= 12

        elif stype == 'resources':
            pdf.new_page()
            pdf.add_centered_text(765, "Resources & Next Steps", font='F2', size=12, gray=0.12)
            pdf.add_line(72, 753, 540, 753, width=0.5, gray=0.3)
            items = sec[1] if len(sec) > 1 else []
            y = 720
            for item in items:
                if y < 55: break
                pdf.add_text(72, y, f"- {item}", font='F1', size=9.5, gray=0.2)
                y -= 16

    # ===== BONUS PAGE =====
    pdf.new_page()
    pdf.add_centered_text(700, "BONUS: Quick-Reference Cheat Sheet", font='F2', size=14, gray=0.12)
    pdf.add_line(150, 688, 462, 688, width=0.5, gray=0.3)
    pdf.add_centered_text(650, "Print this page and keep it visible!", font='F4', size=10, gray=0.4)
    pdf.add_text(72, 610, "TOP 5 TAKEAWAYS FROM THIS BOOK:", font='F2', size=11, gray=0.15)
    for i in range(5):
        pdf.add_text(72, 580 - i*30, f"{i+1}. ________________________________", font='F1', size=10, gray=0.3)
    pdf.add_text(72, 400, "MY #1 ACTION STEP:", font='F2', size=11, gray=0.15)
    pdf.add_line(72, 370, 540, 370, width=0.5, gray=0.5)
    pdf.add_line(72, 340, 540, 340, width=0.5, gray=0.5)
    pdf.add_text(72, 280, "MY DEADLINE:", font='F2', size=11, gray=0.15)
    pdf.add_line(200, 280, 400, 280, width=0.5, gray=0.5)

    # ===== CALL TO ACTION PAGE =====
    pdf.new_page()
    pdf.add_filled_rect(0, 350, 612, 180, gray=0.07)
    pdf.add_centered_text(490, "You Did It!", font='F2', size=28, gray=0.97)
    pdf.add_centered_text(450, "Now take action on what you learned.", font='F4', size=12, gray=0.72)
    pdf.add_line(200, 430, 412, 430, width=1, gray=0.25)
    pdf.add_centered_text(380, "Progress beats perfection. Start today.", font='F1', size=11, gray=0.72)
    pdf.add_centered_text(290, "LOVED THIS RESOURCE?", font='F2', size=12, gray=0.15)
    pdf.add_centered_text(265, "Leave a 5-star review on Etsy!", font='F1', size=10, gray=0.3)
    pdf.add_centered_text(240, "It helps other people find this resource.", font='F1', size=9, gray=0.4)
    pdf.add_centered_text(190, f"{AUTHOR} | {BRAND}", font='F2', size=10, gray=0.2)
    pdf.add_centered_text(165, "More resources: Search 'Daniel Tesfamariam' on Etsy & Amazon", font='F1', size=9, gray=0.4)

    # ===== SAVE =====
    output = f"/projects/sandbox/CLAUDE/kdp_books/Book{book_num}_{filename}.pdf"
    pdf.save(output)
    fsize = os.path.getsize(output)
    with open(output, 'rb') as f:
        pcount = f.read().count(b'/Type /Page')
    print(f"  Book {book_num}: {title.replace(chr(10),' ')[:45]:<47} | {pcount:>3} pg | {fsize:,} bytes")
    return output, pcount
