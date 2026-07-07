"""Book 76: AI Tools for Caregivers - Technology to Help You Care for Aging Parents"""
from pdf_utils import PDFDoc

doc = PDFDoc(432, 648)

# Title page
doc.new_page()
doc.add_filled_rect(0, 0, 432, 648, 0.94)
doc.add_centered_text(530, "AI TOOLS FOR", 'F2', 22)
doc.add_centered_text(498, "CAREGIVERS", 'F2', 22)
doc.add_centered_text(455, "Technology to Help You Care", 'F5', 15)
doc.add_centered_text(433, "for Aging Parents", 'F5', 15)
doc.add_line(110, 415, 322, 415, 2, 0.3)
doc.add_centered_text(380, "Modern Solutions for the", 'F1', 12)
doc.add_centered_text(358, "Sandwich Generation", 'F1', 12)
doc.add_centered_text(200, "Daniel Tesfamariam", 'F2', 14)
doc.add_centered_text(175, "2024", 'F1', 11)

# Copyright page
doc.new_page()
doc.add_centered_text(500, "AI TOOLS FOR CAREGIVERS", 'F2', 14)
doc.add_centered_text(475, "Technology to Help You Care for Aging Parents", 'F4', 10)
doc.add_centered_text(440, "Copyright 2024 Daniel Tesfamariam", 'F1', 10)
doc.add_centered_text(420, "All rights reserved.", 'F1', 10)
doc.add_centered_text(390, "No part of this publication may be reproduced without permission.", 'F1', 9)
doc.add_centered_text(360, "Published independently via KDP.", 'F1', 10)
doc.add_centered_text(330, "This book is informational only. Consult professionals for medical and legal advice.", 'F1', 9)

chapters = [
    ("Chapter 1: The Caregiver Challenge Today", [
        "Over 53 million Americans serve as unpaid caregivers for aging family members.",
        "The average caregiver spends 24 hours per week providing care while juggling their own life.",
        "Caregiver burnout affects 40-70 percent of family caregivers leading to health problems.",
        "Geographic distance makes caregiving even harder when parents live far away.",
        "AI technology offers solutions that reduce stress while improving care quality.",
        "These tools do not replace your love and attention - they amplify your ability to help.",
        "Technology handles monitoring, reminders, and coordination so you can focus on connection.",
        "This book covers practical AI tools you can implement immediately.",
        "Each chapter addresses a specific caregiving challenge with technology-based solutions.",
        "You will learn to choose the right tools for your parent's specific needs.",
        "Caring for your parents is noble work - AI helps you do it without sacrificing yourself.",
    ]),
    ("Chapter 2: AI Monitoring Systems Overview", [
        "AI monitoring creates a safety net around your parent without requiring your constant presence.",
        "Systems range from simple motion sensors to comprehensive AI-powered monitoring platforms.",
        "CarePredict, Alarm.com, and Lively are popular AI monitoring solutions for seniors.",
        "These systems learn normal daily patterns and alert you only when something seems wrong.",
        "Unlike cameras, many systems monitor activity without recording video for privacy.",
        "AI distinguishes between normal variations and genuinely concerning behavior changes.",
        "Cloud-based dashboards let you check on activity patterns from your phone anywhere.",
        "Multiple caregivers (siblings, aides) can share access to the same monitoring system.",
        "Systems typically cost $30-100 per month after initial equipment purchase.",
        "Most install in under an hour with no technical modifications to the home required.",
        "Start with one or two sensors in key areas and expand based on what you learn.",
    ]),
    ("Chapter 3: Smart Sensors for Safety", [
        "Smart sensors detect movement, door openings, temperature, and water usage passively.",
        "Motion sensors in hallways confirm your parent is moving around during the day.",
        "Door sensors alert you if your parent leaves the house at unusual times.",
        "Bed sensors track sleep patterns and detect if your parent does not get up by morning.",
        "Stove sensors detect heat and shut off burners if left unattended too long.",
        "Water sensors detect leaks and floods before major damage occurs.",
        "Temperature sensors ensure the home stays comfortable and safe in extreme weather.",
        "Smoke and carbon monoxide AI detectors send alerts directly to your phone.",
        "Refrigerator sensors confirm your parent is eating meals at regular times.",
        "All data combines into daily reports showing overall activity and wellness patterns.",
        "Sensors are small, discreet, and do not make your parent feel watched or controlled.",
    ]),
    ("Chapter 4: AI Medication Management Tools", [
        "Medication errors are the leading preventable cause of harm in elderly patients.",
        "AI pill dispensers (MedMinder, Hero, TabSafe) dispense the right pills at the right time.",
        "Locked dispensers prevent double-dosing even when memory is significantly impaired.",
        "AI alerts go to you if your parent misses a dose so you can remind them.",
        "Some systems call your parent directly with an automated voice reminder.",
        "AI checks for dangerous drug interactions when new medications are added.",
        "Refill tracking ensures prescriptions are reordered before running out.",
        "Photo verification confirms the correct pills were taken (some advanced systems).",
        "AI correlates medication adherence with health outcomes over time.",
        "These systems connect with pharmacies for automated prescription management.",
        "Monthly costs range from $30-80, often cheaper than the consequences of missed doses.",
    ]),
    ("Chapter 5: GPS Tracking for Wandering Prevention", [
        "Wandering affects 60 percent of people with dementia and can be life-threatening.",
        "GPS tracking devices worn as watches, pendants, or shoe inserts provide real-time location.",
        "AI geofencing sends immediate alerts if your parent leaves a defined safe area.",
        "Location history shows movement patterns that might indicate confusion or distress.",
        "Many devices include a one-button SOS that your parent can press in an emergency.",
        "AI learns normal travel patterns and only alerts for truly unusual movements.",
        "Two-way communication allows you to speak with your parent through the device.",
        "Battery life on modern trackers extends days or weeks between charges.",
        "Waterproof designs stay on during bathing when many wandering incidents occur.",
        "Some devices hide discreetly in shoes for parents who resist wearing visible trackers.",
        "These devices provide peace of mind and can literally save lives during wandering events.",
    ]),
    ("Chapter 6: AI-Powered Health Alerts", [
        "AI health monitoring detects problems before they become emergencies.",
        "Continuous vital sign monitoring tracks heart rate, oxygen, and temperature trends.",
        "AI distinguishes normal fluctuations from patterns that predict hospitalization.",
        "Blood pressure cuffs with AI track readings over time and predict dangerous spikes.",
        "Weight monitoring detects sudden changes that indicate fluid retention or malnutrition.",
        "AI analyzes trends across multiple health indicators for a complete picture.",
        "Alerts are prioritized: urgent notifications versus general wellness updates.",
        "You receive weekly summary reports showing overall health trajectory.",
        "AI reduces false alarms that cause unnecessary worry and emergency room visits.",
        "These systems can notify your parent's doctor directly with concerning data.",
        "Early intervention based on AI alerts has been shown to reduce hospitalizations by 30 percent.",
    ]),
    ("Chapter 7: Remote Health Monitoring Explained", [
        "Remote patient monitoring (RPM) brings hospital-level tracking into your parent's home.",
        "Medicare now covers RPM for many chronic conditions, making it free or low-cost.",
        "Connected devices automatically send health data to your parent's healthcare provider.",
        "Blood glucose monitors with AI predict dangerous sugar levels hours in advance.",
        "Heart monitors detect arrhythmias and alert cardiologists in real time.",
        "Pulse oximeters track oxygen levels crucial for COPD and heart failure patients.",
        "AI analyzes all this data together, finding correlations humans would miss.",
        "Your parent's doctor receives alerts when intervention is needed, not just at appointments.",
        "Many RPM programs include a care coordinator who calls to check on your parent.",
        "This bridges the gap between quarterly doctor visits with continuous oversight.",
        "Ask your parent's primary care physician if they offer RPM services.",
    ]),
    ("Chapter 8: AI Scheduling for Care Coordination", [
        "Coordinating care among multiple providers, family members, and aides is complex.",
        "AI scheduling tools like CareZone and Lotsa Helping Hands organize everything.",
        "Shared calendars show all appointments, medication times, and caregiver shifts.",
        "AI detects scheduling conflicts and suggests solutions before they cause problems.",
        "Automatic reminders go to the right person (sibling, aide, or you) for each task.",
        "Task lists can be divided fairly among family members based on availability.",
        "AI tracks what has been completed and follows up on missed responsibilities.",
        "Communication logs ensure all caregivers know what happened during previous shifts.",
        "Meal planning, transportation, and household tasks are all coordinated in one place.",
        "Transition notes between caregivers prevent important information from being lost.",
        "This reduces the mental load of being the primary coordinator for your parent's care.",
    ]),
    ("Chapter 9: AI Communication Tools for Dementia Patients", [
        "Communication becomes increasingly difficult as dementia progresses.",
        "AI-powered picture communication boards help when verbal expression fails.",
        "Voice AI can interpret unclear speech and translate it into understandable messages.",
        "Simple tablet interfaces let your parent express needs with one-touch icons.",
        "AI learns your parent's speech patterns and becomes better at understanding them over time.",
        "Music and familiar songs triggered by AI can facilitate emotional communication.",
        "AI photo slideshows prompt conversation by displaying familiar faces and places.",
        "Simplified video calling interfaces require only one button press to connect.",
        "AI companions provide patient, repeated conversation without frustration.",
        "These tools preserve dignity by maximizing your parent's ability to communicate.",
        "Even in advanced stages, AI helps maintain some level of meaningful interaction.",
    ]),
    ("Chapter 10: Voice AI for Non-Verbal Communication", [
        "When speech becomes impossible, AI offers alternative communication pathways.",
        "Eye-tracking AI allows your parent to select words and phrases by looking at them.",
        "Gesture recognition AI interprets hand movements and facial expressions into words.",
        "AI-powered speech generation creates a voice for those who have lost theirs.",
        "Emotion detection AI helps caregivers understand pain, discomfort, or distress signals.",
        "Breathing pattern AI can indicate if your parent is in pain even without verbal reports.",
        "Touch-based communication tablets respond to simple taps for yes, no, and common needs.",
        "AI learns your parent's unique non-verbal cues and translates them for caregivers.",
        "These tools reduce the frustration both patient and caregiver feel during communication gaps.",
        "Some systems can be trained with recordings of your parent's voice from earlier in life.",
        "Communication, in any form, preserves connection and reduces agitation.",
    ]),
    ("Chapter 11: AI-Powered Meal Planning for Elderly", [
        "Proper nutrition is crucial but challenging when appetite, ability, and needs change.",
        "AI meal planning considers dietary restrictions, medications, and nutritional needs.",
        "Apps generate meal plans accounting for dysphagia (swallowing difficulty) and texture needs.",
        "AI grocery delivery integration ensures food arrives without your parent needing to shop.",
        "Meal kits designed for seniors with AI-selected recipes simplify cooking for aides.",
        "Nutrition tracking AI ensures your parent gets adequate protein, calcium, and hydration.",
        "AI suggests finger foods and easy-to-eat options when utensil use becomes challenging.",
        "Calorie monitoring detects dangerous weight loss that indicates nutritional decline.",
        "AI medication timing coordinates meals with drugs that must be taken with or without food.",
        "Shared meal planning lets distant family members contribute to nutrition decisions.",
        "Simple slow-cooker and one-pot recipes reduce kitchen complexity and safety risks.",
    ]),
    ("Chapter 12: AI Exercise Programs for Limited Mobility", [
        "Physical activity prevents decline even when mobility is significantly limited.",
        "AI creates gentle exercise programs tailored to specific physical capabilities.",
        "Chair-based exercises maintain strength without fall risk during movement.",
        "AI watches via camera and adjusts exercises if your parent shows strain or discomfort.",
        "Range-of-motion exercises prevent joint stiffness and contractures in sedentary patients.",
        "AI breathing exercises improve lung capacity and reduce anxiety simultaneously.",
        "Progress is tracked at tiny increments to show improvement even when changes are small.",
        "Programs adapt daily based on energy levels, pain reports, and observed movement.",
        "AI exercise timing works around medication schedules and energy peak periods.",
        "Short sessions (5-10 minutes) multiple times daily are more effective than one long session.",
        "Family members can participate remotely, exercising together through video.",
    ]),
    ("Chapter 13: AI Financial Management for Elderly Parents", [
        "Financial exploitation is the most common form of elder abuse affecting millions yearly.",
        "AI banking alerts detect unusual transactions that may indicate scams or exploitation.",
        "Simplified banking interfaces with AI prevent costly errors in bill payment.",
        "AI monitors spending patterns and flags sudden changes that suggest problems.",
        "Automatic bill payment ensures essential services are never interrupted.",
        "AI scam detection warns your parent about suspicious calls, emails, and messages.",
        "Power of attorney combined with AI monitoring lets you oversee without controlling.",
        "Subscription tracking AI identifies forgotten recurring charges draining accounts.",
        "AI budgeting tools ensure funds last throughout the month for all necessities.",
        "Shared financial dashboards keep all authorized family members informed transparently.",
        "These tools protect your parent's finances while respecting their independence.",
    ]),
    ("Chapter 14: Legal Document AI Assistants", [
        "Essential legal documents must be in place before cognitive decline makes them invalid.",
        "AI legal services help create advance directives, living wills, and healthcare proxies.",
        "Power of attorney documents should be completed while your parent can still consent.",
        "AI explains complex legal terminology in simple, understandable language.",
        "Document storage AI keeps all important papers organized and accessible to authorized people.",
        "AI reminds you when legal documents need updating due to life changes or law revisions.",
        "Trust and estate planning AI helps you understand options without expensive attorney consultations.",
        "HIPAA authorization forms allow you to communicate with your parent's medical providers.",
        "AI generates checklists of all documents needed for comprehensive elder care planning.",
        "Digital copies stored securely in the cloud prevent loss of critical paperwork.",
        "Start these conversations early - waiting until crisis makes everything harder.",
    ]),
    ("Chapter 15: AI Respite Care Resources", [
        "Caregiver burnout is not selfish to acknowledge - it is a medical reality to address.",
        "AI helps you find and schedule respite care when you need a break.",
        "Care.com and other platforms use AI to match your parent with qualified temporary caregivers.",
        "AI vetting systems check backgrounds, qualifications, and reviews of potential providers.",
        "Adult day programs found through AI search give your parent socialization while you rest.",
        "In-home respite AI coordinates schedules between regular care and relief periods.",
        "AI monitors your stress indicators and suggests respite before you reach crisis.",
        "Virtual support groups for caregivers provide peer connection any time of day.",
        "AI self-care apps remind you to eat, sleep, exercise, and take breaks.",
        "Planned respite (regular, scheduled breaks) prevents burnout better than emergency breaks.",
        "You cannot pour from an empty cup - taking care of yourself enables better caregiving.",
    ]),
    ("Chapter 16: AI Support Groups for Caregivers", [
        "Connecting with other caregivers who truly understand your experience is invaluable.",
        "AI matches you with support groups based on your specific caregiving situation.",
        "Virtual groups meet at convenient times so you do not need to leave your parent alone.",
        "AI-facilitated discussions ensure everyone gets to speak and share experiences.",
        "Condition-specific groups (Alzheimer's, Parkinson's, stroke) offer targeted advice.",
        "Anonymous options let you share vulnerable feelings without judgment from people you know.",
        "AI resources within groups share relevant articles, tips, and local services.",
        "Mentor matching connects you with experienced caregivers who have navigated your challenges.",
        "Text-based groups let you participate during quiet moments throughout the day.",
        "The shared understanding in these groups reduces the isolation caregiving creates.",
        "Finding your people - those who get it - is one of the most important steps you can take.",
    ]),
    ("Chapter 17: Using ChatGPT for Caregiver Questions", [
        "ChatGPT is available 24/7 to answer your caregiving questions without judgment.",
        "Ask it to explain medical terminology from your parent's diagnosis or treatment plan.",
        "Get suggestions for activities appropriate to your parent's cognitive and physical level.",
        "Request help writing letters to insurance companies, doctors, or care facilities.",
        "Ask for meal ideas that meet specific dietary restrictions and texture requirements.",
        "Get help researching local resources, programs, and services for seniors.",
        "Use it to practice difficult conversations before having them with family members.",
        "Ask for coping strategies when you feel overwhelmed, frustrated, or guilty.",
        "Request templates for care logs, medication tracking, and communication with providers.",
        "Important: AI provides information, not medical advice. Always verify with professionals.",
        "Think of it as a knowledgeable friend available any time you need guidance or support.",
    ]),
    ("Chapter 18: AI and End-of-Life Planning Tools", [
        "End-of-life planning is an act of love that reduces burden on everyone involved.",
        "AI guides difficult conversations with frameworks that make discussing wishes easier.",
        "Advance care planning AI ensures your parent's preferences are documented clearly.",
        "AI creates comprehensive checklists covering medical, legal, financial, and personal wishes.",
        "Five Wishes and similar AI-guided documents address values, not just medical decisions.",
        "Digital legacy planning helps organize online accounts, passwords, and subscriptions.",
        "Memorial planning AI helps document preferences for services, music, and readings.",
        "AI organizes all important contacts, documents, and information in one accessible place.",
        "Family communication AI helps share decisions with siblings who may not all agree.",
        "These tools make the inevitable less overwhelming when the time eventually comes.",
        "Having these conversations now, while possible, is a gift to your entire family.",
    ]),
    ("Chapter 19: The Future of AI Caregiving", [
        "AI caregiving technology is advancing faster than any other health sector currently.",
        "Humanoid robots will soon assist with physical tasks like lifting and bathing.",
        "AI diagnostic tools will detect health changes days or weeks before symptoms appear.",
        "Natural language AI will communicate naturally with even severely impaired patients.",
        "Autonomous vehicles will restore transportation independence for elderly individuals.",
        "AI-powered smart homes will anticipate needs and provide assistance proactively.",
        "Emotional AI will detect pain, depression, and anxiety through subtle behavioral cues.",
        "Personalized medicine AI will optimize treatments for each individual's unique biology.",
        "Caregiver training AI will teach techniques through interactive simulation.",
        "These advances will make aging in place feasible for far more people than today.",
        "The future is one where technology supports both caregiver and care recipient equally.",
    ]),
    ("Chapter 20: Caregiver Self-Care with AI Tools", [
        "Your health and well-being directly affect the quality of care you provide.",
        "AI fitness apps create quick workouts you can do during brief breaks from caregiving.",
        "Meditation apps provide 3-5 minute stress relief sessions for overwhelmed moments.",
        "Sleep tracking AI helps you maximize rest quality when sleep quantity is limited.",
        "AI meal planning ensures you eat well even when focused entirely on your parent's needs.",
        "Mood tracking AI identifies patterns and triggers in your emotional well-being.",
        "AI scheduling blocks protected time for yourself that cannot be given away.",
        "Virtual therapy with AI matching finds counselors who specialize in caregiver issues.",
        "AI reminds you of your own medical appointments that caregivers often postpone.",
        "Social connection AI helps you maintain friendships despite your demanding schedule.",
        "You matter too. AI tools help you remember and act on that essential truth.",
    ]),
]

for title, lines in chapters:
    doc.new_page()
    doc.add_text(36, 608, title, 'F2', 11.5)
    doc.add_line(36, 600, 396, 600, 1, 0.4)
    y = 575
    for line in lines:
        doc.add_text(36, y, line, 'F4', 9.8)
        y -= 21

doc.save("/projects/sandbox/CLAUDE/kdp_books/Book76_AI_Guide_Caregivers.pdf")
print("Created Book76_AI_Guide_Caregivers.pdf")
