from pdf_utils import PDFDoc
from book_helpers import *

def create_book():
    doc = PDFDoc(612, 792)
    chapters = [
        ("Every Kid Is a Writer", "Yes, YOU are a writer! If you can think, imagine, and feel, you can write. Writing is not about being perfect - it is about expressing YOUR unique ideas and voice. Every published author started exactly where you are now. Some wrote terrible first drafts! The secret is simply this: writers WRITE. The more you write, the better you get."),
        ("Finding Story Ideas", "Ideas are everywhere! Look at the world around you and ask 'What if?' What if your pet could talk? What if gravity reversed for a day? What if you found a time machine? Keep an idea journal and write down EVERYTHING - overheard conversations, interesting people, weird dreams, news stories. You will never run out of ideas!"),
        ("Building Characters", "Great characters feel REAL. They have wants, fears, flaws, strengths, and secrets. Create a character sheet: name, age, appearance, personality, biggest fear, greatest wish, secret, best friend, worst habit, and special talent. The more you know about your character, the more alive they become on the page."),
        ("Creating Settings", "Settings are not just locations - they create MOOD. A dark forest feels different from a sunny beach. Use all 5 senses to describe settings: what do characters see, hear, smell, touch, and taste? Make settings come alive so readers feel like they are THERE. The best settings almost become characters themselves."),
        ("Plot Structure", "Every great story has a Beginning (introduce characters and world), Middle (problem gets worse, characters struggle), and End (climax and resolution). Think of plot like a roller coaster: it goes up (tension builds), reaches the peak (most exciting moment), then comes down (resolution). Readers need all three parts!"),
        ("Dialogue That Sounds Real", "Good dialogue sounds like how people actually talk - not how they write! Use contractions (don't instead of do not). Keep speeches short. Give each character a unique voice. Use dialogue to reveal personality, advance the plot, and create tension. Read your dialogue out loud - if it sounds stiff, rewrite it."),
        ("Show, Don't Tell", "Instead of telling readers 'Sara was scared,' SHOW it: 'Sara's hands trembled. Her breath came in short gasps. Every shadow looked like a monster.' Showing uses sensory details and actions to make readers FEEL the emotion instead of just being told about it. This is the most powerful writing technique!"),
        ("Writing Poetry", "Poetry is concentrated emotion! You don't need to rhyme (free verse is great!). Poetry types: Haiku (5-7-5 syllables), Acrostic (first letters spell a word), Limerick (funny, AABBA rhyme), Free Verse (no rules!), and Concrete (shaped like the subject). Poetry lets you play with language like an artist plays with paint."),
        ("Writing Funny Stories", "Humor in writing comes from surprise, exaggeration, weird comparisons, timing, and absurd situations. Funny characters often take things too literally, have extreme reactions, or find themselves in ridiculous situations. Read funny books to learn techniques! And remember: comedy is harder than drama - respect the funny writers."),
        ("Writing Mysteries", "Mystery readers love clues! Plant 'breadcrumbs' throughout your story that make sense looking back. Include red herrings (false clues that mislead). Use misdirection - make readers suspect the wrong person. The solution should be surprising yet logical. Give readers a fair chance to solve it themselves!"),
        ("Writing Fantasy & Sci-Fi", "World-building is the key to great fantasy and sci-fi! Create consistent rules for your world. What is possible and impossible? What is the history? What are the cultures? Great speculative fiction uses impossible settings to explore very REAL human emotions and problems. Even dragons need believable motivations!"),
        ("Editing Your Work", "First drafts are supposed to be messy - that is why they are called 'rough' drafts! Editing is where good writing becomes GREAT. Steps: 1) Let it rest 24+ hours. 2) Read out loud. 3) Cut unnecessary words. 4) Check for clarity. 5) Fix grammar/spelling. 6) Get feedback. 7) Revise again. Professional authors often edit 10+ times!"),
        ("Publishing Options for Kids", "You can share your writing with the world TODAY! Options: school literary magazine, online writing communities (Wattpad, FanFiction.net), self-publishing (Amazon KDP), writing contests (Scholastic, Young Authors), starting a blog, making zines, or simply sharing with friends and family. Don't wait for permission to be a writer."),
        ("Author Habits", "Professional writers have habits that help them produce consistently. They write at the same time daily. They set word count goals. They read A LOT. They carry notebooks everywhere. They don't wait for inspiration - they write even when they don't feel like it. Habits beat motivation every time!"),
        ("Your 30-Day Writing Challenge", "For the next 30 days, write something every single day. It does not matter how short or messy. Just write! This challenge will build your writing muscle, fill your notebook with ideas, and prove that you CAN be a consistent writer. Day 1 starts TODAY. Ready?"),
    ]
    
    prompts_20 = ["A door appears in your bedroom wall that wasn't there yesterday...","Write from the perspective of your pet for one day.","Two best friends discover they have the same recurring dream.","A kid finds a phone that can text anyone in history.","The last person on Earth gets a knock on the door.","You wake up and everyone speaks a language you don't know.","A tree in your backyard starts growing unusual fruit.","Write a story that takes place entirely in an elevator.","Your shadow starts acting independently.","A letter arrives addressed to you from the year 2075.","The school bully turns out to have a heartbreaking secret.","You can suddenly hear what animals are thinking.","A kid discovers their boring town has a hidden underground world.","Write a day in the life of your favorite object.","Two kids from enemy schools must work together on a project.","A magic notebook: anything written in it becomes true.","The new kid at school isn't from another city - they're from another dimension.","Write a story using only dialogue (no descriptions).","A kid's imaginary friend turns out to be real.","The weirdest substitute teacher ever walks into your classroom."]

    title_page(doc, "YOUNG AUTHOR'S GUIDE", "How to Write Amazing Stories, Poems & More (Ages 8-14)", "15 Chapters * Techniques * Exercises * 30-Day Writing Challenge")
    copyright_page(doc, "YOUNG AUTHOR'S GUIDE")
    toc_page(doc, [c[0] for c in chapters])

    for idx, (ch_title, content) in enumerate(chapters):
        chapter_header(doc, idx+1, ch_title)
        y = 580
        y = add_wrapped(doc, 72, y, content, 'F1', 11, 0.2)
        doc.new_page()

        # Exercise page
        doc.add_centered_text(720, f"CHAPTER {idx+1}: WRITING EXERCISE", 'F2', 16, 0)
        doc.add_line(180, 710, 432, 710, 1, 0.3)
        
        exercises = [
            "Write for 5 minutes without stopping. Don't erase anything. Don't judge. Just WRITE whatever comes to mind. This is called 'freewriting' and it's how professional authors warm up.",
            f"Choose one of these 'What If' prompts and write the opening paragraph:\n{prompts_20[idx]}",
            "Create a character sheet for a character you invent right now. Name, age, personality trait, fear, desire, secret, flaw, and one quirky habit. Make them feel REAL.",
            "Describe your bedroom using all 5 senses. What do you SEE (colors, light)? HEAR (sounds)? SMELL? FEEL (textures)? Can you TASTE anything? Make a reader feel PRESENT.",
            "Write the plot outline for a short story: Beginning (who + where + normal life), Problem (what goes wrong), Rising Action (3 events making it worse), Climax (biggest moment), Resolution (how it ends).",
            "Write a conversation between two characters who want opposite things. One wants to go to the park, the other wants to stay home. Make each voice sound DIFFERENT.",
            "Rewrite these 'telling' sentences using 'showing': 'It was cold.' 'She was happy.' 'He was tired.' 'The food was delicious.' Use sensory details and actions!",
            "Write a 5-line poem about an emotion without naming the emotion. Can someone guess which feeling you wrote about? Try haiku form (5-7-5 syllables).",
            "Write a short scene where something embarrassing happens to your character. Make the reader laugh! Use exaggeration and surprise.",
            "Write the opening of a mystery: describe a setting with something slightly 'off.' Plant one clue that readers might miss. Hook them in the first paragraph!",
            "Invent a fantasy world in one paragraph: What are the rules? What's different from Earth? What does it look like? Who lives there? What conflict exists?",
            "Take something you wrote before. Cut 20% of the words WITHOUT losing meaning. Which words were unnecessary? How does it read now?",
            "Write a book blurb (back cover summary) for a book YOU would want to read. In 3-4 sentences, hook a reader. Don't give away the ending!",
            "Set a timer for 10 minutes. Write without stopping until it rings. Don't edit, don't cross out, don't stop. How many words did you write? That's your baseline!",
            "Write about TODAY. What happened? How did you feel? What did you notice? A journal entry IS writing! Every day is a story worth telling.",
        ]
        
        y = 685
        y = add_wrapped(doc, 72, y, exercises[idx], 'F4', 11, 0.2)
        y -= 20
        doc.add_text(72, y, "YOUR WRITING SPACE:", 'F2', 12, 0.1)
        y -= 5
        while y > 100:
            y -= 20
            doc.add_text(72, y, "___________________________________________________________", 'F1', 10, 0.4)
        doc.new_page()

    # 20 story prompts page
    doc.add_centered_text(720, "20 STORY STARTER PROMPTS", 'F2', 18, 0)
    doc.add_line(180, 710, 432, 710, 1, 0.3)
    y = 685
    for i, p in enumerate(prompts_20):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "STORY PROMPTS (continued)", 'F2', 16, 0)
            y = 690
        lines = wrap(f"{i+1}. {p}", 72)
        for l in lines:
            doc.add_text(72, y, l, 'F1', 10, 0.2)
            y -= 15
        y -= 8
    doc.new_page()

    # 30-day challenge
    doc.add_centered_text(720, "30-DAY WRITING CHALLENGE", 'F2', 18, 0)
    daily = ["Write about your morning in detail","Describe a stranger you saw today","Write dialogue between you and your future self","Poem: 5 things that are [color]","Rewrite a fairy tale in modern day","Write a letter to yourself 10 years from now","Story: a kid finds something unusual","Describe your favorite food to an alien","Write about your biggest fear","Flash fiction: tell a story in exactly 50 words","Write from the perspective of an old photograph","Describe a place you love without naming it","Write the worst day ever (fiction!)","Poem about a sound you heard today","Write about a time you were brave","Describe your best friend without using their name","Story opening: first line must be a question","Write directions to your house as adventure","What would you do with invisibility for 1 hour?","Write a scene set 100 years in the future","Letter to your favorite author","Describe the view from your window as a painting","Write a story where the last line is the title","Poem: what does silence look like?","Rewrite today as if it were the best day ever","Write about something you're grateful for (in detail!)","Story: two characters are stuck somewhere together","Write your own obituary at age 100 (imaginary life!)","Create a new holiday and describe how it's celebrated","Free write for 15 minutes. No stopping. No judging. Just write!"]
    y = 690
    for i, d in enumerate(daily):
        if y < 80:
            doc.new_page()
            doc.add_centered_text(720, "30-DAY CHALLENGE (continued)", 'F2', 14, 0)
            y = 700
        doc.add_text(72, y, f"Day {i+1:2d}: [ ] {d}", 'F1', 10, 0.3)
        y -= 19
    doc.new_page()

    certificate(doc, "YOUNG AUTHOR CERTIFICATE")
    add_supplemental(doc, 'Writing', 78)
    doc.save('/projects/sandbox/CLAUDE/kdp_books/Book343_Kids_Creative_Writing.pdf')
    print("Book343_Kids_Creative_Writing.pdf created successfully!")

if __name__ == "__main__":
    create_book()
