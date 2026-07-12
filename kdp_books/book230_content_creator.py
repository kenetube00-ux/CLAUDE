"""Book 230: The Content Creator's Empire Builder"""
from pdf_utils import PDFDoc

def create_book():
    doc = PDFDoc(612, 792)
    author = "Daniel Tesfamariam"
    
    doc.new_page()
    doc.add_filled_rect(0, 700, 612, 92, 0.2)
    doc.add_centered_text(755, "THE CONTENT CREATOR'S", 'F2', 22, 1)
    doc.add_centered_text(725, "EMPIRE BUILDER", 'F2', 22, 1)
    doc.add_centered_text(665, "Multi-Platform Strategy & Monetization Planner", 'F4', 13, 0.3)
    doc.add_centered_text(200, author, 'F2', 14, 0.3)

    doc.new_page()
    doc.add_centered_text(700, "THE CONTENT CREATOR'S EMPIRE BUILDER", 'F2', 12)
    doc.add_centered_text(670, f"Copyright {author}. All rights reserved.", 'F1', 10)

    # Personal Brand Definition
    doc.new_page()
    doc.add_centered_text(750, "PERSONAL BRAND DEFINITION", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    lines = ["My expertise: ________________________________",
        "My unique angle: ________________________________",
        "My ideal audience: ________________________________",
        "Their biggest problem: ________________________________",
        "How I solve it differently: ________________________________", "",
        "Brand personality (3 words): ________________________________",
        "Brand colors: ________________________________",
        "Brand voice: [ ] Professional [ ] Casual [ ] Funny [ ] Inspirational",
        "Tagline: ________________________________", "",
        "MY BRAND STATEMENT:",
        "I help [audience] to [transformation] through [method].",
        "________________________________"]
    for line in lines:
        doc.add_text(72, y, line, 'F1', 10)
        y -= 18

    # Content Pillars
    doc.new_page()
    doc.add_centered_text(750, "CONTENT PILLARS - 5 PILLARS x 20 SUB-TOPICS", 'F2', 12)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 715
    for p in range(1, 6):
        doc.add_text(72, y, f"PILLAR {p}: ________________________________", 'F2', 9)
        y -= 14
        for row in range(4):
            start = row * 5 + 1
            doc.add_text(90, y, f"{start}._______ {start+1}._______ {start+2}._______ {start+3}._______ {start+4}._______", 'F1', 7)
            y -= 12
        y -= 10

    # Platform Strategy
    doc.new_page()
    doc.add_centered_text(750, "PLATFORM STRATEGY", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    platforms = [
        ("YOUTUBE", "Long-form authority. Posting: ___/week. Format: ___________"),
        ("INSTAGRAM", "Visual + community. Posting: ___/day. Stories: ___/day"),
        ("TIKTOK", "Discovery + virality. Posting: ___/day. Series: ___________"),
        ("PINTEREST", "Evergreen traffic. Pins: ___/week. Boards: ___"),
        ("NEWSLETTER", "Owned audience. Frequency: ___/week. Platform: ___________"),
    ]
    for name, details in platforms:
        doc.add_text(72, y, name, 'F2', 10)
        y -= 16
        doc.add_text(90, y, details, 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Strength: _________________ Audience size goal: _______", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Best content type: ________________________________", 'F1', 9)
        y -= 25


    # Monetization Ladder
    doc.new_page()
    doc.add_centered_text(750, "MONETIZATION LADDER", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    ladder = [
        ("FREE CONTENT", "Build audience, establish authority", "Followers needed: ___"),
        ("LOW-TICKET ($)", "Digital products, templates, ebooks $7-47", "Target: $___/mo"),
        ("MID-TICKET ($$)", "Courses, memberships, workshops $97-497", "Target: $___/mo"),
        ("HIGH-TICKET ($$$)", "Coaching, consulting, services $997+", "Target: $___/mo"),
        ("PASSIVE", "Ads, affiliates, licensing", "Target: $___/mo"),
    ]
    for name, desc, target in ladder:
        doc.add_text(72, y, name, 'F2', 10)
        y -= 16
        doc.add_text(90, y, desc, 'F1', 9)
        y -= 14
        doc.add_text(90, y, f"My offering: _________________ {target}", 'F1', 9)
        y -= 25

    # Revenue Stream Planner
    doc.new_page()
    doc.add_centered_text(750, "REVENUE STREAM PLANNER", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    streams = ["Ad Revenue (YouTube/Blog)", "Sponsorships/Brand Deals",
               "Digital Products", "Affiliate Marketing", "Services/Coaching"]
    for s in streams:
        doc.add_text(72, y, s, 'F2', 10)
        y -= 16
        doc.add_text(90, y, "Current: $___/mo  Target (6mo): $___/mo  Target (12mo): $___/mo", 'F1', 9)
        y -= 14
        doc.add_text(90, y, "Action to grow: ________________________________", 'F1', 9)
        y -= 25
    doc.add_text(72, y, "TOTAL INCOME TARGET: $______/month by ___/___/___", 'F2', 10)

    # Sponsorship Rate + Media Kit
    doc.new_page()
    doc.add_centered_text(750, "SPONSORSHIP RATES & MEDIA KIT", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "RATE CALCULATOR:", 'F2', 10)
    y -= 18
    rates = ["YouTube integration (30-60s): $___",
        "YouTube dedicated video: $___",
        "Instagram post: $___", "Instagram story set: $___",
        "TikTok video: $___", "Newsletter mention: $___",
        "Bundle deal (multi-platform): $___"]
    for r in rates:
        doc.add_text(90, y, r, 'F1', 9)
        y -= 16
    y -= 15
    doc.add_text(72, y, "MEDIA KIT TEMPLATE:", 'F2', 10)
    y -= 16
    kit = ["Bio (50 words): ________________________________",
        "Niche/audience demo: ________________________________",
        "Platform stats: ________________________________",
        "Past brand partners: ________________________________",
        "Testimonial: ________________________________",
        "Contact: ________________________________"]
    for item in kit:
        doc.add_text(90, y, item, 'F1', 9)
        y -= 16

    # Content Batching Planner
    doc.new_page()
    doc.add_centered_text(750, "CONTENT BATCHING PLANNER", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "WEEKLY BATCH SCHEDULE:", 'F2', 10)
    y -= 18
    days = [("Monday", "Ideation + scripting"), ("Tuesday", "Filming/recording"),
            ("Wednesday", "Editing"), ("Thursday", "Graphics + scheduling"),
            ("Friday", "Engagement + admin")]
    for day, focus in days:
        doc.add_text(90, y, f"{day}: {focus} ________________________________", 'F1', 9)
        y -= 16
    y -= 15
    doc.add_text(72, y, "MONTHLY CONTENT PLAN:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Week 1 theme: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Week 2 theme: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Week 3 theme: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Week 4 theme: ________________________________", 'F1', 9)

    # Analytics Dashboard (track monthly)
    doc.new_page()
    doc.add_centered_text(750, "MONTHLY ANALYTICS DASHBOARD", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 720
    doc.add_text(72, y, "Month: ________", 'F1', 10)
    y -= 22
    doc.add_text(72, y, "Platform", 'F2', 8)
    doc.add_text(170, y, "Followers", 'F2', 8)
    doc.add_text(250, y, "Growth", 'F2', 8)
    doc.add_text(310, y, "Engagement", 'F2', 8)
    doc.add_text(400, y, "Revenue", 'F2', 8)
    doc.add_line(72, y-5, 540, y-5, 0.5, 0.3)
    for plat in ["YouTube", "Instagram", "TikTok", "Pinterest", "Newsletter", "Website"]:
        y -= 20
        doc.add_text(72, y, plat, 'F1', 9)
        doc.add_line(170, y-2, 245, y-2, 0.5, 0.5)
        doc.add_line(250, y-2, 305, y-2, 0.5, 0.5)
        doc.add_line(310, y-2, 395, y-2, 0.5, 0.5)
        doc.add_line(400, y-2, 470, y-2, 0.5, 0.5)
    y -= 25
    doc.add_text(72, y, "TOTAL REVENUE: $______  Best performing content: ________________", 'F2', 9)

    # Email + Product Launch + Collab + 90-day + Annual
    doc.new_page()
    doc.add_centered_text(750, "GROWTH STRATEGY & PLANNING", 'F2', 14)
    doc.add_line(72, 738, 540, 738, 0.5, 0.3)
    y = 710
    doc.add_text(72, y, "EMAIL LIST GROWTH:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Lead magnet: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Current subscribers: ___  Goal: ___  Growth/week: ___", 'F1', 9)
    y -= 20
    doc.add_text(72, y, "PRODUCT LAUNCH CHECKLIST:", 'F2', 10)
    y -= 16
    launch = ["[ ] Validate idea with audience", "[ ] Create product",
        "[ ] Sales page/landing page", "[ ] Email sequence (5-7 emails)",
        "[ ] Social media teasers (2 weeks)", "[ ] Launch day posts all platforms",
        "[ ] Follow-up sequence"]
    for item in launch:
        doc.add_text(90, y, item, 'F1', 8)
        y -= 12
    y -= 15
    doc.add_text(72, y, "COLLABORATION TRACKER:", 'F2', 10)
    y -= 16
    for _ in range(3):
        doc.add_text(90, y, "Creator: _____________ Platform: ___ Status: ___ Result: ___", 'F1', 8)
        y -= 14
    y -= 15
    doc.add_text(72, y, "90-DAY GROWTH PLAN:", 'F2', 10)
    y -= 16
    doc.add_text(90, y, "Month 1 focus: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Month 2 focus: ________________________________", 'F1', 9)
    y -= 14
    doc.add_text(90, y, "Month 3 focus: ________________________________", 'F1', 9)
    y -= 20
    doc.add_text(72, y, "ANNUAL REVENUE PROJECTION: $____________", 'F2', 10)

    doc.save("Book230_Content_Creator_Empire.pdf")
    print("Created: Book230_Content_Creator_Empire.pdf")

if __name__ == "__main__":
    create_book()
