"""
Build a clean STT training phrases list for Monica.
- Cleans existing phrases.json (removes garbled/corrupted entries)
- Adds 100 curated high-quality STT phrases
- Generates additional synthetic phrases
- Outputs cleaned docs/phrases.json
"""

import json
import random
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PHRASES_JSON = os.path.join(SCRIPT_DIR, "..", "docs", "phrases.json")

# ── Curated 100 high-quality STT phrases ──────────────────────────────────────
CURATED = [
    # Phonetically Balanced (Harvard Sentences)
    "The birch canoe slid on the smooth planks.",
    "Glue the sheet to the dark blue background.",
    "It's easy to tell the depth of a well.",
    "These days a chicken leg is a rare dish.",
    "Rice is often served in round bowls.",
    "The juice of lemons makes fine punch.",
    "The box was thrown beside the parked truck.",
    "The hogs were fed chopped corn and garbage.",
    "Four hours of steady work faced us.",
    "A large size in stockings is hard to sell.",
    "The boy was there when the sun rose.",
    "A rod is used to catch pink salmon.",
    "The source of the huge river is the clear spring.",
    "Kick the ball straight and follow through.",
    "Help the woman get back to her feet.",
    "A pot of tea helps to pass the evening.",
    "Smoky fires lack flame and heat.",
    "The soft cushion broke the man's fall.",
    "The salt breeze came across from the sea.",
    "The girl at the booth sold fifty bonds.",
    # Voice Assistant & Device Commands
    "Turn off the living room lights.",
    "Set a timer for fifteen minutes.",
    "What is the weather like in Chicago tomorrow?",
    "Play my driving playlist on Spotify.",
    "Remind me to call John at three o'clock.",
    "Lower the thermostat to sixty-eight degrees.",
    "Add paper towels to the grocery list.",
    "Snooze the alarm for ten minutes.",
    "Call mom on speakerphone.",
    "Navigate to the nearest gas station.",
    "Read my unread text messages.",
    "Lock the front door and arm the security system.",
    "What is fifteen percent of eighty-five dollars?",
    "Turn the volume up to seventy-five percent.",
    "Skip to the next track.",
    "How long will it take to drive to the airport?",
    "Turn on the coffee maker at six a.m.",
    "Mute the television.",
    "What's on my calendar for Tuesday?",
    "Pause the podcast.",
    # Professional Dictation
    "The patient presented with a mild fever and a persistent cough.",
    "Please review the attached quarterly earnings report by Friday.",
    "We need to schedule a follow-up meeting with the stakeholders.",
    "Blood pressure is one twenty over eighty, pulse is resting at seventy-two.",
    "The defendant pleaded not guilty to all charges.",
    "The new software update will be deployed at midnight.",
    "Forward this email to the human resources department.",
    "The x-ray results showed a minor fracture in the distal radius.",
    "Let's pivot our strategy to focus on user retention.",
    "I have prescribed a ten-day course of amoxicillin.",
    "Please sign and date the non-disclosure agreement.",
    "The client requested a revision to section four of the contract.",
    "Patient denies any history of cardiovascular disease.",
    "Please approve the pending vacation requests in the portal.",
    "Open a new ticket for the IT department regarding the server outage.",
    "The medication should be taken twice daily with food.",
    "We are waiting on legal approval before proceeding.",
    "End of dictation.",
    # Conversational & Spontaneous Speech
    "Um, I think we should probably just, like, go to the store first.",
    "Yeah, absolutely, I'll be there around, oh, maybe six-thirty?",
    "No way, that's literally exactly what I was thinking!",
    "So, basically, the whole thing was kind of a disaster.",
    "I mean, sure, we could do that, but it might take a while.",
    "Well, you know, it's not really up to me anyway.",
    "Uh, could you repeat that last part? I didn't quite catch it.",
    "Right, right, exactly. That makes total sense.",
    "Honestly, I'm just so tired today, I can't even focus.",
    "Oh, wow, I had no idea that was happening.",
    "Let's just, you know, play it by ear and see what happens.",
    "Yeah, but, like, what if it rains tomorrow?",
    "I guess I could try to fix it, but I'm not making any promises.",
    "Wait, hold on a second. Are you serious?",
    "Um, excuse me, do you happen to know what time it is?",
    "Anyway, long story short, we missed the flight.",
    "I completely forgot to tell you, but she called yesterday.",
    "Yeah, that sounds good to me. Let's do it.",
    "Oh, shoot, I left my wallet in the car.",
    "Well, I suppose we'll just have to wait and see.",
    # Alphanumeric, Dates, Times & Currency
    "The serial number is Alpha Bravo seven niner two.",
    "The meeting is scheduled for Wednesday, October twelfth at two p.m.",
    "Your total comes to forty-seven dollars and eighty-two cents.",
    "My email is j dot smith at example dot com.",
    "The flight number is Delta one eight five six.",
    "Please enter your zip code: nine zero two one zero.",
    "The password is capital T, lowercase h, three, exclamation point.",
    "I was born on January first, nineteen ninety-five.",
    "The coordinates are thirty-four degrees north, one eighteen degrees west.",
    "Call one eight hundred five five five zero one nine nine.",
    "The invoice amount is two thousand five hundred dollars flat.",
    "My license plate is Charlie Kilo X-ray eight four two.",
    "We expect a temperature of minus five degrees Celsius.",
    "The IP address is one ninety-two dot one sixty-eight dot one dot one.",
    "The promotion runs from Black Friday until Cyber Monday.",
    "Room three zero four is located on the third floor.",
    "The recipe calls for one and a half cups of flour.",
    "I need to withdraw five hundred euros from my account.",
    "Track my package with ID number Z as in Zulu, four five nine.",
    "The train leaves at exactly fourteen hundred hours.",
]

# ── Synthetic phrase generator ─────────────────────────────────────────────────
def generate_synthetic(count=2000):
    wake_words = ["Hey Monica", "Okay computer", "Please", "Could you"]
    actions = ["turn on", "turn off", "dim", "increase", "decrease", "play", "pause",
               "navigate to", "call", "text", "set a reminder for", "add to the list"]
    objects = ["the lights", "the thermostat", "the music", "the television",
               "the fan", "the coffee maker", "the alarm", "the volume"]
    contexts = ["in the living room", "to fifty percent", "on Spotify", "right away",
                "in ten minutes", "on speakerphone", "for tomorrow morning",
                "in the bedroom", "please", "when I get home"]
    filler_starts = ["Um, ", "Yeah, ", "So basically, ", "I mean, ",
                     "Honestly, ", "Well, ", "You know, ", "Actually, "]
    statements = [
        "I think we should leave early", "it's going to rain tonight",
        "the meeting got cancelled", "I left my keys inside",
        "the food is getting cold", "I don't know what to do next",
        "she said she'd be here by now", "we need to talk about that later",
        "I totally forgot about the appointment", "the car needs an oil change",
    ]
    filler_ends = [", you know?", ", right?", ", I guess.", ".",
                   " honestly.", " I think.", ", don't you think?"]
    time_words = ["one", "two", "three", "four", "five", "six", "seven", "eight",
                  "nine", "ten", "eleven", "twelve", "fifteen", "thirty", "forty-five"]
    currencies = ["dollars", "euros", "pounds"]
    items = ["a gallon of milk", "some bread", "eggs", "coffee", "orange juice",
             "bananas", "chicken", "pasta", "rice", "soap", "shampoo"]
    questions = [
        "What time does the pharmacy close?",
        "How far is the nearest hospital?",
        "Can you tell me today's top news?",
        "What's the fastest route home?",
        "How do you spell necessary?",
        "What's the capital of Australia?",
        "How many ounces are in a pound?",
        "What's the score of the game?",
        "Who won the election?",
        "What movies are playing tonight?",
        "How do I get to the freeway from here?",
        "What's a good recipe for chicken soup?",
        "How long does it take to hard boil an egg?",
        "What's the exchange rate for the euro today?",
        "Is it going to snow this weekend?",
    ]

    phrases = set()
    while len(phrases) < count:
        t = random.choice(["command", "conversational", "number", "question", "shopping"])
        if t == "command":
            p = f"{random.choice(wake_words)}, {random.choice(actions)} {random.choice(objects)} {random.choice(contexts)}."
        elif t == "conversational":
            p = f"{random.choice(filler_starts)}{random.choice(statements)}{random.choice(filler_ends)}"
        elif t == "number":
            n = random.choice(time_words)
            c = random.choice(currencies)
            p = f"The total comes to {n} {c}."
        elif t == "question":
            p = random.choice(questions)
        else:
            p = f"Could you add {random.choice(items)} to my shopping list?"
        p = re.sub(r' +', ' ', p).strip()
        if p:
            p = p[0].upper() + p[1:]
            phrases.add(p)
    return list(phrases)


# ── Phrase cleaner ─────────────────────────────────────────────────────────────
def is_clean(phrase):
    p = phrase.strip()
    if len(p) < 10 or len(p) > 250:
        return False
    if re.search(r'\(\s*\)', p): return False           # empty brackets
    if re.search(r'\d+x\s*[\+\-]', p): return False    # math like 4x + 12
    if re.search(r'\\[a-zA-Z]', p): return False        # LaTeX
    if re.search(r'\d{4,}', p): return False            # 4+ digit numbers
    if re.search(r'\(\w+,\s*\d{4}\)', p): return False  # citations like (Smith, 2000)
    if re.search(r'\d+\.\d+\.\d+', p): return False    # section numbers
    if re.search(r'[a-z]-\s[a-z]', p): return False    # broken hyphenation
    if re.search(r'\s{2,}', p): return False            # double spaces
    if re.search(r'[A-Z]{5,}', p): return False        # ALL CAPS blocks
    if 'andthen' in p.lower(): return False
    if re.search(r'[a-z]s\s+in\b', p): return False    # OCR: "yourselve s"
    if not p[0].isalpha(): return False
    if p[-1] not in '.?!': return False
    return True


def main():
    print("Loading existing phrases...")
    with open(PHRASES_JSON, "r", encoding="utf-8") as f:
        existing = json.load(f)
    print(f"  Loaded {len(existing):,} phrases")

    print("Cleaning phrases...")
    cleaned = [p for p in existing if is_clean(p)]
    print(f"  Kept {len(cleaned):,} clean phrases ({len(existing)-len(cleaned):,} removed)")

    print("Adding 100 curated phrases...")
    all_phrases = set(cleaned)
    added_curated = sum(1 for p in CURATED if p not in all_phrases)
    all_phrases.update(CURATED)
    print(f"  Added {added_curated} new curated phrases")

    print("Generating 2,000 synthetic phrases...")
    synthetic = generate_synthetic(2000)
    added_synthetic = sum(1 for p in synthetic if p not in all_phrases)
    all_phrases.update(synthetic)
    print(f"  Added {added_synthetic} synthetic phrases")

    final = sorted(all_phrases)
    print(f"\nFinal phrase count: {len(final):,}")

    print(f"Writing {PHRASES_JSON}...")
    with open(PHRASES_JSON, "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    print("Done!")


if __name__ == "__main__":
    main()
