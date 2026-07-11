"""
Book 168: Write Your Wedding Vows - A Guided Workbook
Trim size: 6x9 inches (432x648 points), 25 pages
Author: Daniel Tesfamariam
"""

from pdf_utils import PDFDoc

pdf = PDFDoc(432, 648)

# Helper functions
def add_lined_area(pdf, start_y, num_lines, left_margin=50, right_margin=382):
    """Add horizontal lines for writing space."""
    for i in range(num_lines):
        y = start_y - (i * 24)
        pdf.add_line(left_margin, y, right_margin, y, 0.5, 0.7)

def wrap_text(text, font_size, max_width, chars_per_point=0.48):
    """Simple word-wrap that returns list of lines."""
    max_chars = int(max_width / (font_size * chars_per_point))
    words = text.split()
    lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 <= max_chars:
            current = current + " " + word if current else word
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


# ============ PAGE 1: Title Page ============
pdf.new_page()
pdf.add_filled_rect(0, 0, 432, 648, 0.95)
pdf.add_filled_rect(40, 280, 352, 200, 1.0)
pdf.add_rect(40, 280, 352, 200, 2, 0.3)
pdf.add_centered_text(445, "WRITE YOUR", 'F2', 28, 0.1)
pdf.add_centered_text(410, "WEDDING VOWS", 'F2', 32, 0.1)
pdf.add_line(130, 395, 302, 395, 1.5, 0.4)
pdf.add_centered_text(365, "A Guided Workbook for", 'F4', 16, 0.3)
pdf.add_centered_text(340, "Personal & Meaningful Vows", 'F4', 16, 0.3)
pdf.add_centered_text(180, "Daniel Tesfamariam", 'F4', 14, 0.4)
# Decorative elements
pdf.add_line(50, 560, 382, 560, 0.5, 0.6)
pdf.add_line(50, 130, 382, 130, 0.5, 0.6)


# ============ PAGE 2: Copyright Page ============
pdf.new_page()
pdf.add_centered_text(400, "Write Your Wedding Vows", 'F2', 14, 0.2)
pdf.add_centered_text(375, "A Guided Workbook for Personal & Meaningful Vows", 'F1', 10, 0.3)
pdf.add_centered_text(340, "Copyright (c) 2025 Daniel Tesfamariam", 'F1', 10, 0.3)
pdf.add_centered_text(320, "All rights reserved.", 'F1', 10, 0.3)
pdf.add_centered_text(295, "No part of this publication may be reproduced, distributed,", 'F1', 9, 0.4)
pdf.add_centered_text(280, "or transmitted in any form without prior written permission.", 'F1', 9, 0.4)
pdf.add_centered_text(250, "Published by Daniel Tesfamariam", 'F1', 10, 0.3)
pdf.add_centered_text(230, "First Edition, 2025", 'F1', 10, 0.3)
pdf.add_centered_text(200, "This workbook is designed to help couples write", 'F1', 9, 0.4)
pdf.add_centered_text(185, "heartfelt, personal wedding vows.", 'F1', 9, 0.4)


# ============ PAGE 3: Why Personal Vows Matter ============
pdf.new_page()
pdf.add_centered_text(600, "Why Personal Vows Matter", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)

# Emotional Impact
pdf.add_text(50, 555, "Emotional Impact", 'F2', 13, 0.2)
pdf.add_text(50, 535, "Personal vows create an emotional connection that resonates", 'F4', 11, 0.3)
pdf.add_text(50, 520, "deeply with your partner, your guests, and yourself. They", 'F4', 11, 0.3)
pdf.add_text(50, 505, "transform a ceremony from a formality into a moment of", 'F4', 11, 0.3)
pdf.add_text(50, 490, "genuine vulnerability and love.", 'F4', 11, 0.3)

# Memory Creation
pdf.add_text(50, 455, "Memory Creation", 'F2', 13, 0.2)
pdf.add_text(50, 435, "Your vows become a treasured memory - words you can return", 'F4', 11, 0.3)
pdf.add_text(50, 420, "to throughout your marriage. They serve as a reminder of", 'F4', 11, 0.3)
pdf.add_text(50, 405, "what you promised and why you chose each other.", 'F4', 11, 0.3)

# Authenticity vs Generic
pdf.add_text(50, 370, "Authenticity vs. Generic Vows", 'F2', 13, 0.2)
pdf.add_text(50, 350, "Generic vows are beautiful, but personal vows tell YOUR", 'F4', 11, 0.3)
pdf.add_text(50, 335, "story. They reflect your unique relationship, your shared", 'F4', 11, 0.3)
pdf.add_text(50, 320, "experiences, and the specific promises that matter most", 'F4', 11, 0.3)
pdf.add_text(50, 305, "to the two of you.", 'F4', 11, 0.3)

pdf.add_filled_rect(60, 200, 312, 70, 0.92)
pdf.add_text(75, 250, "Remember: There is no wrong way to write your vows.", 'F5', 11, 0.2)
pdf.add_text(75, 232, "The best vows come from the heart and speak", 'F4', 11, 0.3)
pdf.add_text(75, 214, "honestly about your love and commitment.", 'F4', 11, 0.3)


# ============ PAGE 4: Traditional vs Personal Vows ============
pdf.new_page()
pdf.add_centered_text(600, "Traditional vs. Personal Vows", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)

# Traditional side
pdf.add_filled_rect(40, 430, 165, 140, 0.93)
pdf.add_text(55, 555, "Traditional Vows", 'F2', 12, 0.2)
pdf.add_text(55, 535, "- Time-honored words", 'F1', 9, 0.3)
pdf.add_text(55, 520, "- Religious significance", 'F1', 9, 0.3)
pdf.add_text(55, 505, "- Familiar to guests", 'F1', 9, 0.3)
pdf.add_text(55, 490, "- Less pressure", 'F1', 9, 0.3)
pdf.add_text(55, 475, "- Universally understood", 'F1', 9, 0.3)
pdf.add_text(55, 460, "- Symbolic weight", 'F1', 9, 0.3)
pdf.add_text(55, 445, "- Officiant-led option", 'F1', 9, 0.3)

# Personal side
pdf.add_filled_rect(227, 430, 165, 140, 0.93)
pdf.add_text(242, 555, "Personal Vows", 'F2', 12, 0.2)
pdf.add_text(242, 535, "- Unique to you", 'F1', 9, 0.3)
pdf.add_text(242, 520, "- Deeply personal", 'F1', 9, 0.3)
pdf.add_text(242, 505, "- Tell your story", 'F1', 9, 0.3)
pdf.add_text(242, 490, "- Emotional depth", 'F1', 9, 0.3)
pdf.add_text(242, 475, "- Memorable moments", 'F1', 9, 0.3)
pdf.add_text(242, 460, "- Creative freedom", 'F1', 9, 0.3)
pdf.add_text(242, 445, "- Specific promises", 'F1', 9, 0.3)

# When to use each
pdf.add_text(50, 400, "When to Use Each:", 'F2', 12, 0.2)
pdf.add_text(50, 380, "Traditional: Religious ceremonies, family expectations,", 'F1', 10, 0.3)
pdf.add_text(50, 365, "comfort with formality, shorter ceremonies.", 'F1', 10, 0.3)
pdf.add_text(50, 340, "Personal: Intimate weddings, creative couples, when you", 'F1', 10, 0.3)
pdf.add_text(50, 325, "want guests to truly know your relationship.", 'F1', 10, 0.3)

# Hybrid approach
pdf.add_text(50, 290, "The Hybrid Approach:", 'F2', 12, 0.2)
pdf.add_text(50, 270, "Many couples combine both - using traditional vows for the", 'F1', 10, 0.3)
pdf.add_text(50, 255, "official exchange and adding personal words before or after.", 'F1', 10, 0.3)
pdf.add_text(50, 235, "This honors tradition while still sharing your unique story.", 'F1', 10, 0.3)
pdf.add_text(50, 215, "You might also weave personal elements into traditional", 'F1', 10, 0.3)
pdf.add_text(50, 200, "frameworks, keeping the structure but making it yours.", 'F1', 10, 0.3)


# ============ PAGE 5: Brainstorming Prompts (Part 1) ============
pdf.new_page()
pdf.add_centered_text(600, "Brainstorming Prompts", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Use these prompts to spark ideas. Write freely - don't edit yet!", 'F4', 10, 0.3)

prompts_p5 = [
    ("When I first knew I loved you...", 550),
    ("What I promise to you...", 430),
    ("How you changed me...", 310),
    ("What marriage means to me...", 190),
]

for prompt, base_y in prompts_p5:
    pdf.add_text(50, base_y - 5, prompt, 'F2', 11, 0.2)
    add_lined_area(pdf, base_y - 25, 4, 50, 382)


# ============ PAGE 6: Brainstorming Prompts (Part 2) ============
pdf.new_page()
pdf.add_centered_text(600, "Brainstorming Prompts (continued)", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)

prompts_p6 = [
    ("My favorite thing about us...", 560),
    ("Our story in 3 moments...", 440),
    ("What I admire most about you...", 320),
    ("Our inside jokes & references...", 200),
]

for prompt, base_y in prompts_p6:
    pdf.add_text(50, base_y - 5, prompt, 'F2', 11, 0.2)
    add_lined_area(pdf, base_y - 25, 4, 50, 382)


# ============ PAGE 7: Vow Structure Template ============
pdf.new_page()
pdf.add_centered_text(600, "Vow Structure Template", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "A strong vow has three parts. Use this framework as a guide:", 'F4', 10, 0.3)

# Opening section
pdf.add_filled_rect(50, 475, 332, 75, 0.93)
pdf.add_text(60, 540, "1. THE OPENING - Set the tone", 'F2', 12, 0.2)
pdf.add_text(60, 520, "Address your partner and establish context.", 'F4', 10, 0.3)
pdf.add_text(60, 502, "Example: \"[Name], from the moment we met at that", 'F4', 10, 0.4)
pdf.add_text(60, 487, "coffee shop, I knew my life was about to change...\"", 'F4', 10, 0.4)

# Promises section
pdf.add_filled_rect(50, 355, 332, 100, 0.93)
pdf.add_text(60, 445, "2. THE PROMISES - The heart of your vows", 'F2', 12, 0.2)
pdf.add_text(60, 425, "Share specific, meaningful commitments.", 'F4', 10, 0.3)
pdf.add_text(60, 407, "Example: \"I promise to be your biggest fan, to", 'F4', 10, 0.4)
pdf.add_text(60, 392, "always save you the last slice of pizza, and to", 'F4', 10, 0.4)
pdf.add_text(60, 377, "hold your hand through every storm life sends.\"", 'F4', 10, 0.4)

# Closing section
pdf.add_filled_rect(50, 250, 332, 80, 0.93)
pdf.add_text(60, 320, "3. THE CLOSING - End with impact", 'F2', 12, 0.2)
pdf.add_text(60, 300, "Wrap up with a powerful declaration of love.", 'F4', 10, 0.3)
pdf.add_text(60, 282, "Example: \"Today I choose you, and I will choose", 'F4', 10, 0.4)
pdf.add_text(60, 267, "you every single day for the rest of our lives.\"", 'F4', 10, 0.4)

pdf.add_text(50, 210, "Tips:", 'F2', 11, 0.2)
pdf.add_text(50, 192, "- Keep each section roughly equal in length", 'F1', 10, 0.3)
pdf.add_text(50, 175, "- Balance humor with sincerity", 'F1', 10, 0.3)
pdf.add_text(50, 158, "- Use specific details over generic statements", 'F1', 10, 0.3)
pdf.add_text(50, 141, "- Read aloud as you write to test the flow", 'F1', 10, 0.3)


# ============ PAGE 8: Word Bank ============
pdf.new_page()
pdf.add_centered_text(600, "Word Bank", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 568, "Choose words that reflect your tone. Mix and match!", 'F4', 10, 0.3)

# Romantic tone
pdf.add_filled_rect(50, 490, 155, 65, 0.93)
pdf.add_text(60, 545, "ROMANTIC", 'F2', 10, 0.2)
pdf.add_text(60, 528, "cherish, adore, forever", 'F1', 9, 0.3)
pdf.add_text(60, 514, "devotion, soulmate, eternal", 'F1', 9, 0.3)
pdf.add_text(60, 500, "beloved, treasure, embrace", 'F1', 9, 0.3)

# Funny tone
pdf.add_filled_rect(227, 490, 155, 65, 0.93)
pdf.add_text(237, 545, "FUNNY", 'F2', 10, 0.2)
pdf.add_text(237, 528, "adventure, shenanigans", 'F1', 9, 0.3)
pdf.add_text(237, 514, "partner-in-crime, tolerate", 'F1', 9, 0.3)
pdf.add_text(237, 500, "weird, chaos, sidekick", 'F1', 9, 0.3)

# Poetic tone
pdf.add_filled_rect(50, 380, 155, 65, 0.93)
pdf.add_text(60, 435, "POETIC", 'F2', 10, 0.2)
pdf.add_text(60, 418, "illuminate, journey, infinite", 'F1', 9, 0.3)
pdf.add_text(60, 404, "intertwine, destiny, bloom", 'F1', 9, 0.3)
pdf.add_text(60, 390, "anchor, constellation, dawn", 'F1', 9, 0.3)

# Simple tone
pdf.add_filled_rect(227, 380, 155, 65, 0.93)
pdf.add_text(237, 435, "SIMPLE", 'F2', 10, 0.2)
pdf.add_text(237, 418, "love, home, partner, best", 'F1', 9, 0.3)
pdf.add_text(237, 404, "friend, team, always, true", 'F1', 9, 0.3)
pdf.add_text(237, 390, "choose, grow, build, stay", 'F1', 9, 0.3)

# Meaningful verbs
pdf.add_text(50, 345, "Meaningful Verbs:", 'F2', 11, 0.2)
pdf.add_text(50, 327, "promise, vow, pledge, commit, dedicate, honor, support,", 'F1', 10, 0.3)
pdf.add_text(50, 312, "uplift, encourage, celebrate, protect, nurture, inspire", 'F1', 10, 0.3)

# Adjectives
pdf.add_text(50, 282, "Adjectives:", 'F2', 11, 0.2)
pdf.add_text(50, 264, "unwavering, steadfast, boundless, genuine, fierce,", 'F1', 10, 0.3)
pdf.add_text(50, 249, "tender, patient, joyful, grateful, courageous, whole", 'F1', 10, 0.3)

# Phrases
pdf.add_text(50, 219, "Useful Phrases:", 'F2', 11, 0.2)
pdf.add_text(50, 201, "\"in this life and the next\" / \"through every season\"", 'F1', 10, 0.3)
pdf.add_text(50, 186, "\"with all that I am\" / \"as long as I breathe\"", 'F1', 10, 0.3)
pdf.add_text(50, 171, "\"you are my home\" / \"I choose you, always\"", 'F1', 10, 0.3)


# ============ PAGES 9-13: Draft Writing Pages ============
draft_pages = [
    ("Draft 1 - Let It Flow", "Write freely without editing. Get your thoughts on paper."),
    ("Draft 2 - Refine Your Ideas", "Rework your favorite parts from Draft 1. Shape them."),
    ("Draft 3 - Find Your Voice", "Read aloud. Does it sound like you? Adjust the tone."),
    ("Edit & Refine", "Cut what doesn't serve the vows. Polish each sentence."),
    ("Final Version", "Your finished vows. Practice reading these aloud."),
]

for title, subtitle in draft_pages:
    pdf.new_page()
    pdf.add_centered_text(600, title, 'F2', 18, 0.1)
    pdf.add_line(100, 590, 332, 590, 1, 0.4)
    pdf.add_centered_text(570, subtitle, 'F4', 10, 0.4)
    add_lined_area(pdf, 540, 20, 50, 382)


# ============ PAGE 14: Tips for Delivery ============
pdf.new_page()
pdf.add_centered_text(600, "Tips for Delivery", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)

# Managing Nervousness
pdf.add_text(50, 560, "Managing Nervousness", 'F2', 13, 0.2)
pdf.add_text(50, 540, "- Take deep breaths before you begin speaking", 'F1', 10, 0.3)
pdf.add_text(50, 523, "- Look at your partner - their face will calm you", 'F1', 10, 0.3)
pdf.add_text(50, 506, "- Pause between sentences - silence is powerful", 'F1', 10, 0.3)
pdf.add_text(50, 489, "- It's okay to cry - your guests expect emotion", 'F1', 10, 0.3)
pdf.add_text(50, 472, "- Remember: everyone is rooting for you", 'F1', 10, 0.3)

# Memorization vs Cue Cards
pdf.add_text(50, 440, "Memorization vs. Cue Cards", 'F2', 13, 0.2)
pdf.add_text(50, 420, "- Cue cards are perfectly acceptable and recommended", 'F1', 10, 0.3)
pdf.add_text(50, 403, "- Write key phrases on a small card, not full text", 'F1', 10, 0.3)
pdf.add_text(50, 386, "- Have your officiant hold a backup copy", 'F1', 10, 0.3)
pdf.add_text(50, 369, "- Memorizing creates pressure - allow yourself grace", 'F1', 10, 0.3)

# Practice Tips
pdf.add_text(50, 337, "Practice Tips", 'F2', 13, 0.2)
pdf.add_text(50, 317, "- Read aloud daily for at least one week before", 'F1', 10, 0.3)
pdf.add_text(50, 300, "- Practice in front of a mirror to see your expressions", 'F1', 10, 0.3)
pdf.add_text(50, 283, "- Record yourself and listen back for pacing", 'F1', 10, 0.3)
pdf.add_text(50, 266, "- Practice with a trusted friend for feedback", 'F1', 10, 0.3)

# Voice Projection
pdf.add_text(50, 234, "Voice Projection", 'F2', 13, 0.2)
pdf.add_text(50, 214, "- Speak slowly - nerves make us rush", 'F1', 10, 0.3)
pdf.add_text(50, 197, "- Project to the back row, not just your partner", 'F1', 10, 0.3)
pdf.add_text(50, 180, "- Ask about microphone options at your venue", 'F1', 10, 0.3)
pdf.add_text(50, 163, "- Vary your tone - don't read in a monotone", 'F1', 10, 0.3)


# ============ PAGE 15: Vow Length Guide ============
pdf.new_page()
pdf.add_centered_text(600, "Vow Length Guide", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)

pdf.add_text(50, 560, "The Ideal Length: 60-90 Seconds", 'F2', 14, 0.2)
pdf.add_text(50, 535, "Most wedding planners and officiants recommend keeping", 'F4', 11, 0.3)
pdf.add_text(50, 518, "your vows between 60 and 90 seconds when spoken aloud.", 'F4', 11, 0.3)

# Word count box
pdf.add_filled_rect(50, 420, 332, 80, 0.93)
pdf.add_text(60, 490, "Word Count Guidance:", 'F2', 12, 0.2)
pdf.add_text(60, 470, "- 30 seconds = approx. 75 words (too short)", 'F1', 10, 0.3)
pdf.add_text(60, 453, "- 60 seconds = approx. 150 words (minimum)", 'F1', 10, 0.3)
pdf.add_text(60, 436, "- 90 seconds = approx. 225 words (ideal max)", 'F1', 10, 0.3)

pdf.add_text(50, 395, "Why This Length Works:", 'F2', 12, 0.2)
pdf.add_text(50, 375, "- Long enough to say something meaningful", 'F1', 10, 0.3)
pdf.add_text(50, 358, "- Short enough to hold everyone's attention", 'F1', 10, 0.3)
pdf.add_text(50, 341, "- Easier to memorize or deliver confidently", 'F1', 10, 0.3)
pdf.add_text(50, 324, "- Both partners' vows stay balanced in length", 'F1', 10, 0.3)

pdf.add_text(50, 290, "Timing Yourself:", 'F2', 12, 0.2)
pdf.add_text(50, 270, "1. Set a timer on your phone", 'F1', 10, 0.3)
pdf.add_text(50, 253, "2. Read at a slow, ceremonial pace (not your normal speed)", 'F1', 10, 0.3)
pdf.add_text(50, 236, "3. Add 10-15 seconds for pauses and emotion on the day", 'F1', 10, 0.3)
pdf.add_text(50, 219, "4. Aim for both partners to be within 30 seconds of each other", 'F1', 10, 0.3)

pdf.add_filled_rect(50, 150, 332, 50, 0.93)
pdf.add_text(60, 185, "Pro tip: Coordinate with your partner on length -", 'F5', 10, 0.2)
pdf.add_text(60, 168, "you don't want a 30-second vow following a 3-minute one!", 'F4', 10, 0.3)


# ============ PAGE 16: Sample Vows - Funny ============
pdf.new_page()
pdf.add_centered_text(600, "Sample Vows: Funny & Lighthearted", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Style: Humorous with a heartfelt ending", 'F4', 10, 0.4)

pdf.add_filled_rect(40, 310, 352, 240, 0.95)
pdf.add_text(55, 535, "[Name], I love you. And I promise to keep loving you", 'F4', 11, 0.3)
pdf.add_text(55, 518, "even when you steal all the blankets. Even when you", 'F4', 11, 0.3)
pdf.add_text(55, 501, "leave your socks everywhere. Even when you insist on", 'F4', 11, 0.3)
pdf.add_text(55, 484, "watching that terrible show for the fifth time.", 'F4', 11, 0.3)
pdf.add_text(55, 460, "I promise to laugh at your jokes - even the bad ones -", 'F4', 11, 0.3)
pdf.add_text(55, 443, "and to always be your partner in every adventure and", 'F4', 11, 0.3)
pdf.add_text(55, 426, "misadventure. I promise to let you pick the restaurant", 'F4', 11, 0.3)
pdf.add_text(55, 409, "at least half the time, and to never go to bed angry -", 'F4', 11, 0.3)
pdf.add_text(55, 392, "mostly because I know you'll want to talk it out anyway.", 'F4', 11, 0.3)
pdf.add_text(55, 368, "But seriously - you are my favorite person on this", 'F4', 11, 0.3)
pdf.add_text(55, 351, "planet. You make ordinary days extraordinary. I choose", 'F4', 11, 0.3)
pdf.add_text(55, 334, "you today, tomorrow, and for all my tomorrows.", 'F4', 11, 0.3)

pdf.add_text(50, 280, "Why it works:", 'F2', 11, 0.2)
pdf.add_text(50, 262, "- Opens with humor that guests relate to", 'F1', 10, 0.3)
pdf.add_text(50, 245, "- Uses specific, personal details (customize yours!)", 'F1', 10, 0.3)
pdf.add_text(50, 228, "- Shifts to sincerity at the end for emotional impact", 'F1', 10, 0.3)
pdf.add_text(50, 211, "- Approx. 150 words = about 60 seconds", 'F1', 10, 0.3)


# ============ PAGE 17: Sample Vows - Emotional ============
pdf.new_page()
pdf.add_centered_text(600, "Sample Vows: Deeply Emotional", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Style: Heartfelt, vulnerable, and intimate", 'F4', 10, 0.4)

pdf.add_filled_rect(40, 320, 352, 230, 0.95)
pdf.add_text(55, 535, "[Name], standing here today, I am overwhelmed by the", 'F4', 11, 0.3)
pdf.add_text(55, 518, "depth of what I feel for you. You came into my life", 'F4', 11, 0.3)
pdf.add_text(55, 501, "when I wasn't looking, and you changed everything.", 'F4', 11, 0.3)
pdf.add_text(55, 477, "You taught me that love isn't just a feeling - it's", 'F4', 11, 0.3)
pdf.add_text(55, 460, "a choice you make every morning. It's patience when", 'F4', 11, 0.3)
pdf.add_text(55, 443, "I'm difficult, grace when I fall short, and joy in", 'F4', 11, 0.3)
pdf.add_text(55, 426, "the smallest moments we share together.", 'F4', 11, 0.3)
pdf.add_text(55, 402, "I vow to be your safe place, your greatest champion,", 'F4', 11, 0.3)
pdf.add_text(55, 385, "and your constant. I promise to hold your hand through", 'F4', 11, 0.3)
pdf.add_text(55, 368, "the storms and dance with you in the sunshine. You are", 'F4', 11, 0.3)
pdf.add_text(55, 351, "my home, my heart, and my forever. I love you beyond", 'F4', 11, 0.3)
pdf.add_text(55, 334, "words - but I will spend my life trying to show you.", 'F4', 11, 0.3)

pdf.add_text(50, 290, "Why it works:", 'F2', 11, 0.2)
pdf.add_text(50, 272, "- Opens with genuine vulnerability", 'F1', 10, 0.3)
pdf.add_text(50, 255, "- Acknowledges what the partner brings to the relationship", 'F1', 10, 0.3)
pdf.add_text(50, 238, "- Makes specific, heartfelt promises", 'F1', 10, 0.3)
pdf.add_text(50, 221, "- Closes with a powerful declaration", 'F1', 10, 0.3)


# ============ PAGE 18: Sample Vows - Religious ============
pdf.new_page()
pdf.add_centered_text(600, "Sample Vows: Faith-Based", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Style: Rooted in faith with personal touches", 'F4', 10, 0.4)

pdf.add_filled_rect(40, 320, 352, 230, 0.95)
pdf.add_text(55, 535, "[Name], I believe God brought us together for a", 'F4', 11, 0.3)
pdf.add_text(55, 518, "purpose. In you, I see His grace, His love, and His", 'F4', 11, 0.3)
pdf.add_text(55, 501, "plan for my life made beautifully clear.", 'F4', 11, 0.3)
pdf.add_text(55, 477, "Before God and our loved ones, I vow to love you as", 'F4', 11, 0.3)
pdf.add_text(55, 460, "Scripture calls me to - with patience, kindness, and", 'F4', 11, 0.3)
pdf.add_text(55, 443, "selflessness. I promise to pray with you, grow with", 'F4', 11, 0.3)
pdf.add_text(55, 426, "you, and build a home rooted in faith.", 'F4', 11, 0.3)
pdf.add_text(55, 402, "I promise to seek God first in our marriage, to forgive", 'F4', 11, 0.3)
pdf.add_text(55, 385, "as we are forgiven, and to trust in His plan when the", 'F4', 11, 0.3)
pdf.add_text(55, 368, "path is uncertain. You are my answered prayer, my", 'F4', 11, 0.3)
pdf.add_text(55, 351, "blessing, and my partner in this beautiful journey", 'F4', 11, 0.3)
pdf.add_text(55, 334, "of faith. I love you today and for all eternity.", 'F4', 11, 0.3)

pdf.add_text(50, 290, "Why it works:", 'F2', 11, 0.2)
pdf.add_text(50, 272, "- Acknowledges faith as the foundation", 'F1', 10, 0.3)
pdf.add_text(50, 255, "- Incorporates scripture themes naturally", 'F1', 10, 0.3)
pdf.add_text(50, 238, "- Balances spiritual commitment with personal promises", 'F1', 10, 0.3)
pdf.add_text(50, 221, "- Appropriate for religious ceremonies", 'F1', 10, 0.3)


# ============ PAGE 19: Sample Vows - Simple ============
pdf.new_page()
pdf.add_centered_text(600, "Sample Vows: Simple & Direct", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Style: Clear, honest, and unpretentious", 'F4', 10, 0.4)

pdf.add_filled_rect(40, 350, 352, 200, 0.95)
pdf.add_text(55, 535, "[Name], I love you. It's that simple and that", 'F4', 11, 0.3)
pdf.add_text(55, 518, "complicated all at once.", 'F4', 11, 0.3)
pdf.add_text(55, 494, "I promise to be honest with you, always. I promise", 'F4', 11, 0.3)
pdf.add_text(55, 477, "to listen when you need to talk and to hold you when", 'F4', 11, 0.3)
pdf.add_text(55, 460, "words aren't enough. I promise to build a life with", 'F4', 11, 0.3)
pdf.add_text(55, 443, "you that we're both proud of.", 'F4', 11, 0.3)
pdf.add_text(55, 419, "I will be your partner, your teammate, and your best", 'F4', 11, 0.3)
pdf.add_text(55, 402, "friend. Today, I give you my whole heart. You are", 'F4', 11, 0.3)
pdf.add_text(55, 385, "enough, and we are enough. I choose you.", 'F4', 11, 0.3)

pdf.add_text(50, 320, "Why it works:", 'F2', 11, 0.2)
pdf.add_text(50, 302, "- Every word carries weight - nothing extra", 'F1', 10, 0.3)
pdf.add_text(50, 285, "- Feels genuine and unscripted", 'F1', 10, 0.3)
pdf.add_text(50, 268, "- Easy to deliver without getting emotional", 'F1', 10, 0.3)
pdf.add_text(50, 251, "- Short length (about 45 seconds) - perfect for nervous speakers", 'F1', 10, 0.3)


# ============ PAGE 20: Sample Vows - Poetic ============
pdf.new_page()
pdf.add_centered_text(600, "Sample Vows: Poetic & Literary", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Style: Lyrical, metaphorical, and artistic", 'F4', 10, 0.4)

pdf.add_filled_rect(40, 310, 352, 240, 0.95)
pdf.add_text(55, 535, "[Name], you are the dawn after my longest night, the", 'F4', 11, 0.3)
pdf.add_text(55, 518, "shore my restless heart finally found. In you, I have", 'F4', 11, 0.3)
pdf.add_text(55, 501, "discovered what poets have tried to capture for", 'F4', 11, 0.3)
pdf.add_text(55, 484, "centuries - a love that is both quiet and infinite.", 'F4', 11, 0.3)
pdf.add_text(55, 460, "I vow to tend the garden of our love with gentle hands.", 'F4', 11, 0.3)
pdf.add_text(55, 443, "I vow to be the lighthouse when the fog rolls in, and", 'F4', 11, 0.3)
pdf.add_text(55, 426, "the soft place to land when the world is too much.", 'F4', 11, 0.3)
pdf.add_text(55, 402, "Our story is not written in grand gestures but in the", 'F4', 11, 0.3)
pdf.add_text(55, 385, "thousand small moments - morning coffee, tangled feet,", 'F4', 11, 0.3)
pdf.add_text(55, 368, "quiet evenings. These are the verses of our life.", 'F4', 11, 0.3)
pdf.add_text(55, 344, "Today I give you my words, my heart, and every chapter", 'F4', 11, 0.3)
pdf.add_text(55, 327, "yet to be written. You are my poem, my song, my story.", 'F4', 11, 0.3)

pdf.add_text(50, 280, "Why it works:", 'F2', 11, 0.2)
pdf.add_text(50, 262, "- Rich imagery creates an emotional experience", 'F1', 10, 0.3)
pdf.add_text(50, 245, "- Metaphors make abstract feelings tangible", 'F1', 10, 0.3)
pdf.add_text(50, 228, "- Rhythmic language is beautiful spoken aloud", 'F1', 10, 0.3)
pdf.add_text(50, 211, "- Ideal for literary-minded couples", 'F1', 10, 0.3)


# ============ PAGES 21-23: Partner's Vow Writing Section ============
# Page 21: Partner's Brainstorm
pdf.new_page()
pdf.add_centered_text(600, "Partner's Section: Brainstorm", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "This section is for your partner to brainstorm their vows.", 'F4', 10, 0.4)

partner_prompts = [
    "When I first knew I loved you...",
    "What I promise to you...",
    "My favorite memory of us...",
    "What our future looks like to me...",
]

y_pos = 535
for prompt in partner_prompts:
    pdf.add_text(50, y_pos, prompt, 'F2', 11, 0.2)
    add_lined_area(pdf, y_pos - 20, 4, 50, 382)
    y_pos -= 120


# Page 22: Partner's Draft
pdf.new_page()
pdf.add_centered_text(600, "Partner's Section: Draft", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Write your draft vows here. Let your heart lead.", 'F4', 10, 0.4)
add_lined_area(pdf, 540, 20, 50, 382)

# Page 23: Partner's Final Version
pdf.new_page()
pdf.add_centered_text(600, "Partner's Section: Final Version", 'F2', 18, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Your polished, final vows. Practice reading these aloud.", 'F4', 10, 0.4)
add_lined_area(pdf, 540, 20, 50, 382)


# ============ PAGE 24: Day-of Vow Card Template ============
pdf.new_page()
pdf.add_centered_text(600, "Day-of Vow Card", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Write your vows on this card-sized template. Cut along the border", 'F4', 10, 0.3)
pdf.add_text(50, 550, "and carry it with you on your wedding day.", 'F4', 10, 0.3)

# Card outline (roughly 4x6 inches = 288x432 but scaled to fit)
card_x = 66
card_y = 140
card_w = 300
card_h = 380
pdf.add_rect(card_x, card_y, card_w, card_h, 1.5, 0.3)
pdf.add_rect(card_x + 5, card_y + 5, card_w - 10, card_h - 10, 0.5, 0.5)

# Header inside card
pdf.add_centered_text(497, "My Vows to You", 'F5', 14, 0.2)
pdf.add_line(card_x + 20, 490, card_x + card_w - 20, 490, 0.5, 0.5)

# Lined writing space inside card
for i in range(14):
    line_y = 465 - (i * 22)
    pdf.add_line(card_x + 20, line_y, card_x + card_w - 20, line_y, 0.3, 0.7)

# Date line at bottom of card
pdf.add_text(card_x + 20, 160, "Date: _______________", 'F4', 10, 0.4)


# ============ PAGE 25: Our Vows Keepsake Page ============
pdf.new_page()
pdf.add_centered_text(600, "Our Vows Keepsake", 'F2', 20, 0.1)
pdf.add_line(100, 590, 332, 590, 1, 0.4)
pdf.add_text(50, 565, "Record both of your final vows here as a lasting keepsake.", 'F4', 10, 0.3)

# Partner 1 section
pdf.add_filled_rect(40, 345, 352, 200, 0.95)
pdf.add_text(55, 535, "Partner 1:", 'F2', 12, 0.2)
pdf.add_text(55, 518, "Name: _______________________________", 'F4', 10, 0.4)
for i in range(6):
    line_y = 490 - (i * 22)
    pdf.add_line(55, line_y, 377, line_y, 0.3, 0.6)

# Partner 2 section
pdf.add_filled_rect(40, 105, 352, 200, 0.95)
pdf.add_text(55, 295, "Partner 2:", 'F2', 12, 0.2)
pdf.add_text(55, 278, "Name: _______________________________", 'F4', 10, 0.4)
for i in range(6):
    line_y = 250 - (i * 22)
    pdf.add_line(55, line_y, 377, line_y, 0.3, 0.6)

# Wedding date
pdf.add_centered_text(75, "Wedding Date: _______________________", 'F4', 11, 0.3)


# ============ SAVE PDF ============
pdf.save('/projects/sandbox/CLAUDE/kdp_books/Book168_Wedding_Vow_Writing.pdf')
print("SUCCESS: Book168_Wedding_Vow_Writing.pdf created successfully!")
print("  - 25 pages, 6x9 inches (432x648 points)")
print("  - Wedding Vow Writing Workbook by Daniel Tesfamariam")
