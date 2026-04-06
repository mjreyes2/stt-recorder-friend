"""
Build a clean STT training phrases list for Monica.
"""

import json
import random
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PHRASES_JSON = os.path.join(SCRIPT_DIR, "..", "docs", "phrases.json")

# ── 1000 specific command/topic phrases ───────────────────────────────────────
COMMAND_PHRASES = [
    "Play music.", "Stop music.", "Pause music.", "Resume music.", "Next song.",
    "Previous song.", "Skip track.", "Go back.", "Volume up.", "Volume down.",
    "Mute volume.", "Unmute volume.", "Max volume.", "Minimum volume.", "Volume to fifty.",
    "Volume to hundred.", "Play rock.", "Play pop.", "Play jazz.", "Play classical.",
    "Play hip hop.", "Play country.", "Play electronic.", "Play blues.", "Play ambient.",
    "Shuffle playlist.", "Repeat song.", "Loop album.", "Play podcast.", "Pause podcast.",
    "Next episode.", "Previous episode.", "Fast forward.", "Rewind.", "Skip forward ten seconds.",
    "Go back ten seconds.", "Play radio.", "Stop radio.", "Play news.", "Pause news.",
    "What song is this?", "Who sings this?", "What album is this?", "When was this released?",
    "Like this song.", "Dislike this song.", "Add to playlist.", "Remove from playlist.",
    "Clear queue.", "Show lyrics.", "Play audiobook.", "Pause audiobook.", "Read chapter one.",
    "Next chapter.", "Previous chapter.", "Read faster.", "Read slower.", "Normal speed.",
    "Connect Bluetooth.", "Disconnect Bluetooth.", "Play movie.", "Pause movie.", "Stop movie.",
    "Next scene.", "Previous scene.", "Turn on subtitles.", "Turn off subtitles.",
    "Change audio track.", "Play trailer.", "Stop trailer.", "Open YouTube.", "Open Netflix.",
    "Open Hulu.", "Search for comedy.", "Search for action.", "Search for drama.",
    "Play workout playlist.", "Play study music.", "Play sleep sounds.", "Play rain sounds.",
    "Play ocean waves.", "Play white noise.", "Stop white noise.", "Play acoustic version.",
    "Play live version.", "Play remix.", "Play instrumental.", "Play cover song.",
    "Add to favorites.", "Remove from favorites.", "What is trending?", "Play top hits.",
    "Play new releases.", "Play oldies.", "Play nineties music.", "Play eighties music.",
    "Play seventies music.", "Play classical piano.", "Play jazz guitar.", "Stop all media.",
    "Turn on lights.", "Turn off lights.", "Dim lights.", "Brighten lights.",
    "Lights to ten percent.", "Lights to fifty percent.", "Lights to max.",
    "Turn lights red.", "Turn lights blue.", "Turn lights green.", "Turn lights yellow.",
    "Turn lights purple.", "Turn lights orange.", "Turn lights pink.", "Turn lights white.",
    "Turn lights warm.", "Turn lights cool.", "Turn on living room.", "Turn off living room.",
    "Dim living room.", "Turn on kitchen.", "Turn off kitchen.", "Turn on bedroom.",
    "Turn off bedroom.", "Turn on bathroom.", "Turn off bathroom.", "Turn on hallway.",
    "Turn off hallway.", "Turn on garage.", "Turn off garage.", "Turn on porch.",
    "Turn off porch.", "Turn on backyard.", "Turn off backyard.", "Lock front door.",
    "Unlock front door.", "Lock back door.", "Unlock back door.", "Lock garage.",
    "Unlock garage.", "Is the front door locked?", "Is the back door locked?",
    "Arm security system.", "Disarm security system.", "Show front camera.",
    "Show backyard camera.", "Show doorbell.", "Open blinds.", "Close blinds.",
    "Open curtains.", "Close curtains.", "Turn on fan.", "Turn off fan.", "Fan to high.",
    "Fan to medium.", "Fan to low.", "Turn on heater.", "Turn off heater.",
    "Set temperature to sixty.", "Set temperature to seventy.", "Increase temperature.",
    "Decrease temperature.", "Set thermostat to heat.", "Set thermostat to cool.",
    "Turn off thermostat.", "Turn on air purifier.", "Turn off air purifier.",
    "Turn on humidifier.", "Turn off humidifier.", "What is the temperature?",
    "What is the humidity?", "Turn on coffee maker.", "Turn off coffee maker.",
    "Start dishwasher.", "Stop dishwasher.", "Start robot vacuum.", "Stop robot vacuum.",
    "Vacuum living room.", "Vacuum kitchen.", "Dock robot vacuum.", "Preheat oven.",
    "Turn off oven.", "Start microwave.", "Stop microwave.", "Start washing machine.",
    "Stop washing machine.", "Start dryer.", "Stop dryer.", "Turn on TV.", "Turn off TV.",
    "Switch to HDMI one.", "Switch to HDMI two.", "Mute TV.", "Unmute TV.",
    "Channel up.", "Channel down.", "Open guide.", "Close guide.", "Record show.",
    "Turn off everything.", "Set timer for one minute.", "Set timer for two minutes.",
    "Set timer for five minutes.", "Set timer for ten minutes.", "Set timer for fifteen minutes.",
    "Set timer for twenty minutes.", "Set timer for thirty minutes.", "Set timer for forty minutes.",
    "Set timer for fifty minutes.", "Set timer for one hour.", "Pause timer.", "Resume timer.",
    "Cancel timer.", "Add one minute to timer.", "Add five minutes to timer.",
    "How much time is left?", "Show timers.", "Clear all timers.", "Set a pasta timer.",
    "Set a laundry timer.", "Set alarm for six AM.", "Set alarm for seven AM.",
    "Set alarm for eight AM.", "Set alarm for nine AM.", "Set alarm for noon.",
    "Set alarm for one PM.", "Set alarm for tomorrow.", "Set alarm for weekdays.",
    "Set alarm for weekends.", "Snooze alarm.", "Stop alarm.", "Cancel alarm.",
    "Show my alarms.", "Delete all alarms.", "Wake me up at six.", "Wake me up at seven.",
    "What time is it?", "What time is it in London?", "What time is it in Tokyo?",
    "What is the date?", "What day is today?", "What day is tomorrow?",
    "When is Thanksgiving?", "When is Christmas?", "When is Easter?", "When is Halloween?",
    "When is Valentine's Day?", "When is Mother's Day?", "When is Father's Day?",
    "How many days until Friday?", "Set a stopwatch.", "Start stopwatch.", "Stop stopwatch.",
    "Reset stopwatch.", "Lap stopwatch.", "What is my schedule?", "What is on my calendar?",
    "Add event to calendar.", "Add meeting to calendar.", "Cancel my next meeting.",
    "Move meeting to tomorrow.", "Schedule lunch at noon.", "Schedule doctor appointment.",
    "Schedule haircut.", "Remind me to call mom.", "Remind me to buy milk.",
    "Remind me to take out trash.", "Remind me to feed the dog.", "Remind me to check email.",
    "Remind me tomorrow at nine.", "What are my reminders?", "Clear all reminders.",
    "Delete reminder.", "Mark reminder as done.", "Create a new list.", "Name list groceries.",
    "Read my list.", "Delete list.", "Add apples to list.", "Add bread to list.",
    "Add milk to list.", "Add eggs to list.", "Add cheese to list.",
    "Remove apples from list.", "Remove bread from list.", "Clear grocery list.",
    "When is sunset?", "When is sunrise?", "What is the moon phase?",
    "When is the next full moon?", "When does spring start?", "When does summer start?",
    "When does fall start?", "When does winter start?", "Is it a leap year?",
    "What century is it?", "Navigate home.", "Navigate to work.", "Navigate to school.",
    "Navigate to airport.", "Navigate to gas station.", "Navigate to grocery store.",
    "Navigate to pharmacy.", "Navigate to hospital.", "Navigate to gym.", "Navigate to bank.",
    "Find nearest restaurant.", "Find nearest coffee shop.", "Find nearest ATM.",
    "Find nearest park.", "Find nearest hotel.", "Find nearest library.",
    "Find nearest post office.", "Find nearest police station.", "Find nearest fire station.",
    "Find nearest mall.", "Get directions to Chicago.", "Get directions to New York.",
    "Get directions to Los Angeles.", "Get directions to Miami.", "Get directions to Seattle.",
    "Get directions to Boston.", "Get directions to Dallas.", "Get directions to Denver.",
    "Get directions to Atlanta.", "Get directions to Houston.", "How far is the moon?",
    "How far is the sun?", "How far is Mars?", "How far is London?", "How far is Paris?",
    "How far is Tokyo?", "How far is Sydney?", "How far is Toronto?",
    "How far is Mexico City?", "How far is Rome?", "What is the traffic like?",
    "Avoid toll roads.", "Avoid highways.", "Find fastest route.", "Find shortest route.",
    "Start navigation.", "Stop navigation.", "Mute voice guidance.", "Unmute voice guidance.",
    "Show alternate routes.", "Where am I?", "Share my location.", "Send ETA.",
    "Call a taxi.", "Book a ride.", "Find a parking spot.", "Find electric charging station.",
    "Find rest area.", "Find car wash.", "Find auto repair.",
    "What is the capital of France?", "What is the capital of Japan?",
    "What is the capital of Italy?", "What is the capital of Spain?",
    "What is the capital of Germany?", "What is the capital of Canada?",
    "What is the capital of Brazil?", "What is the capital of Australia?",
    "What is the capital of India?", "What is the capital of China?",
    "Show me a map of Europe.", "Show me a map of Asia.", "Show me a map of Africa.",
    "Show me a map of North America.", "Show me a map of South America.",
    "Show me a map of Antarctica.", "Show me a map of Australia.",
    "Zoom in on map.", "Zoom out on map.", "Switch to satellite view.",
    "What state is Chicago in?", "What state is Miami in?", "What state is Dallas in?",
    "What state is Seattle in?", "What state is Denver in?", "What country is Paris in?",
    "What country is London in?", "What country is Tokyo in?", "What country is Rome in?",
    "What country is Berlin in?", "Navigate to main street.", "Navigate to first avenue.",
    "Navigate to broadway.", "Navigate to elm street.", "Navigate to maple street.",
    "Call mom.", "Call dad.", "Call wife.", "Call husband.", "Call brother.",
    "Call sister.", "Call friend.", "Call boss.", "Call home.", "Call work.",
    "Call emergency.", "Call nine one one.", "Answer call.", "Decline call.", "End call.",
    "Put on speakerphone.", "Take off speakerphone.", "Mute microphone.", "Unmute microphone.",
    "Redial last number.", "Check voicemails.", "Play next voicemail.", "Delete voicemail.",
    "Call back.", "Text mom.", "Text dad.", "Text wife.", "Text husband.",
    "Text brother.", "Text sister.", "Read unread messages.", "Read latest text.",
    "Reply to text.", "Send message.", "Delete message.", "Open email.", "Read latest email.",
    "Reply to email.", "Forward email.", "Delete email.", "Compose new email.",
    "Send email to John.", "Send email to Jane.", "Send email to boss.",
    "Mark email as read.", "Mark email as unread.", "Archive email.", "Check spam folder.",
    "Empty trash.", "Open contacts.", "Add new contact.", "Delete contact.",
    "Update contact.", "Find John's number.", "Find Jane's number.", "Share contact.",
    "Block caller.", "Unblock caller.", "Turn on do not disturb.", "Turn off do not disturb.",
    "Start video call.", "End video call.", "Turn on camera.", "Turn off camera.",
    "Share screen.", "Stop sharing screen.", "Join meeting.", "Leave meeting.",
    "Record meeting.", "Stop recording meeting.", "Send an audio message.",
    "Play audio message.", "Send a photo.", "Send a video.", "Send a document.",
    "Download attachment.", "Open attachment.", "Print document.", "Print photo.",
    "Cancel print.", "What is the weather?", "What is the forecast?",
    "Will it rain today?", "Will it snow tomorrow?", "Do I need an umbrella?",
    "Do I need a jacket?", "What is the temperature outside?", "What is the high today?",
    "What is the low today?", "Is it sunny?", "Is it cloudy?", "Is it windy?",
    "What is the humidity outside?", "What is the UV index?", "What is the air quality?",
    "When will the rain stop?", "When will the snow start?", "Weather in London.",
    "Weather in Tokyo.", "Weather in New York.", "Weather for the weekend.",
    "Weather for next week.", "Ten day forecast.", "Hourly forecast.",
    "Is there a storm warning?", "Is there a tornado warning?", "Is there a hurricane warning?",
    "Is there a flood warning?", "Track the hurricane.", "Show weather map.",
    "Check my battery.", "Battery percentage.", "Turn on power saving mode.",
    "Turn off power saving mode.", "How much storage is left?", "Free up storage.",
    "Check internet connection.", "Run speed test.", "Connect to wifi.", "Disconnect from wifi.",
    "Turn on airplane mode.", "Turn off airplane mode.", "Turn on cellular data.",
    "Turn off cellular data.", "Turn on mobile hotspot.", "Turn off mobile hotspot.",
    "Check system updates.", "Install update.", "Restart device.", "Shut down device.",
    "Lock screen.", "Unlock screen.", "Increase screen brightness.", "Decrease screen brightness.",
    "Brightness to max.", "Brightness to minimum.", "Turn on dark mode.", "Turn off dark mode.",
    "Turn on night light.", "Turn off night light.", "Increase font size.", "Decrease font size.",
    "Turn on auto rotate.", "Turn off auto rotate.", "Take a screenshot.", "Record screen.",
    "Open camera.", "Take a photo.", "Take a selfie.", "Record a video.", "Open gallery.",
    "Show my photos.", "Show my videos.", "Delete this photo.", "Share this photo.",
    "Edit this photo.", "Open calculator.", "Open calendar.", "Open clock.", "Open settings.",
    "Open browser.", "Search the web.", "Close all apps.", "Open app store.",
    "Download app.", "Update app.", "Delete app.", "Show notifications.",
    "Clear notifications.", "Turn on flashlight.", "Turn off flashlight.",
    "Flashlight to max.", "Flashlight to low.", "Find my phone.", "Ring my phone.",
    "Find my watch.", "Find my tablet.", "Find my keys.",
    "Who is the president?", "Who is the prime minister?", "Who invented the telephone?",
    "Who invented the lightbulb?", "Who discovered gravity?", "Who wrote Hamlet?",
    "Who painted the Mona Lisa?", "Who directed Titanic?",
    "What is the tallest building?", "What is the longest river?",
    "What is the largest ocean?", "What is the highest mountain?",
    "What is the smallest country?", "What is the biggest animal?",
    "What is the fastest car?", "What is the speed of light?",
    "What is the speed of sound?", "What is the boiling point of water?",
    "What is the freezing point of water?", "What is photosynthesis?",
    "What is gravity?", "What is quantum physics?", "What is artificial intelligence?",
    "What is blockchain?", "What is a black hole?", "What is a supernova?",
    "What is a galaxy?", "What is a planet?",
    "Define serendipity.", "Define paradox.", "Define ubiquitous.", "Define ephemeral.",
    "Define eloquent.", "Synonym for happy.", "Synonym for sad.", "Synonym for angry.",
    "Antonym for hot.", "Antonym for cold.", "Spell accommodation.", "Spell restaurant.",
    "Spell rhythm.", "Spell definitely.", "Spell separate.", "Spell embarrass.",
    "Spell maintenance.", "Spell pronunciation.", "Spell queue.", "Spell bureaucracy.",
    "Translate hello to Spanish.", "Translate goodbye to French.",
    "Translate please to German.", "Translate thank you to Italian.",
    "Translate yes to Japanese.", "Translate no to Chinese.", "Translate water to Russian.",
    "Translate food to Arabic.", "Translate friend to Hindi.", "Translate love to Korean.",
    "Tell me a joke.", "Tell me a story.", "Tell me a fun fact.", "Tell me a riddle.",
    "Tell me a poem.", "Tell me a quote.", "Flip a coin.", "Roll a die.",
    "Pick a number between one and ten.", "Pick a card.",
    "What is one plus one?", "What is two plus two?", "What is ten minus five?",
    "What is two times two?", "What is ten divided by two?",
    "What is the square root of one hundred?", "What is ten percent of one hundred?",
    "What is a twenty percent tip on fifty dollars?",
    "Convert one inch to centimeters.", "Convert one mile to kilometers.",
    "Convert one pound to kilograms.", "Convert fahrenheit to celsius.",
    "How many ounces in a cup?", "How many feet in a mile?",
    "Testing one two three.", "Mic check one two.", "Can you hear me?",
    "Are you listening?", "Stop listening.", "Wake up.", "Go to sleep.",
    "Goodbye.", "Hello.", "How are you?", "I need help.", "Give me a hint.",
    "What can you do?", "Show me your features.", "Learn my voice.", "Forget my voice.",
    "Change assistant voice.", "Speak slower.", "Speak louder.", "Stop talking.",
    "Um turn on the light.", "Uh play some music.", "Actually cancel that timer.",
    "Wait no turn it off.", "Just pause it.", "Okay go ahead and send it.", "Nevermind.",
    "Order pizza.", "Order chinese food.", "Order sushi.", "Order burgers.", "Order tacos.",
    "Order coffee.", "Order groceries.", "Track my amazon order.", "Where is my package?",
    "Cancel my order.", "Return this item.", "Find a recipe for chicken.",
    "Find a recipe for pasta.", "Find a recipe for cake.", "Start cooking.",
    "Next step in recipe.", "How much salt?", "How long to bake?",
    "Track my calories.", "Log my breakfast.", "Log my lunch.", "Log my dinner.",
    "Start workout.", "End workout.", "Track my run.", "Check my heart rate.",
    "Check my steps.", "Check my sleep.", "Start meditation.", "Stop meditation.",
    "Book a flight.", "Book a hotel.", "Check flight status.", "Find cheap flights.",
    "Plan a trip.", "Show my itinerary.", "End of list.",
]

# ── 100 curated high-quality STT phrases ──────────────────────────────────────
CURATED = [
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
    "Turn off the living room lights.",
    "Set a timer for fifteen minutes.",
    "What is the weather like in Chicago tomorrow?",
    "Play my driving playlist on Spotify.",
    "Remind me to call John at three o'clock.",
    "Lower the thermostat to sixty-eight degrees.",
    "Add paper towels to the grocery list.",
    "Snooze the alarm for ten minutes.",
    "Navigate to the nearest gas station.",
    "Lock the front door and arm the security system.",
    "The patient presented with a mild fever and a persistent cough.",
    "Please review the attached quarterly earnings report by Friday.",
    "We need to schedule a follow-up meeting with the stakeholders.",
    "The x-ray results showed a minor fracture in the distal radius.",
    "The medication should be taken twice daily with food.",
    "Um, I think we should probably just, like, go to the store first.",
    "Yeah, absolutely, I'll be there around, oh, maybe six-thirty?",
    "No way, that's literally exactly what I was thinking!",
    "So, basically, the whole thing was kind of a disaster.",
    "Uh, could you repeat that last part? I didn't quite catch it.",
    "Honestly, I'm just so tired today, I can't even focus.",
    "Anyway, long story short, we missed the flight.",
    "Oh, shoot, I left my wallet in the car.",
    "The serial number is Alpha Bravo seven niner two.",
    "The meeting is scheduled for Wednesday, October twelfth at two p.m.",
    "Your total comes to forty-seven dollars and eighty-two cents.",
    "My email is j dot smith at example dot com.",
    "I was born on January first, nineteen ninety-five.",
    "The train leaves at exactly fourteen hundred hours.",
    "I need to withdraw five hundred euros from my account.",
]

# ── 3000 diverse synthetic phrases ────────────────────────────────────────────
def generate_diverse(count=3000):
    random.seed(42)

    anger = [
        "I am so angry right now I could scream.",
        "This is absolutely ridiculous, I can't take it anymore.",
        "I hate when people waste my time like this.",
        "Why does nobody ever listen to me?",
        "I'm furious and I'm not going to pretend I'm not.",
        "Damn it, this keeps happening over and over again.",
        "I'm done. I am completely done with this.",
        "This is so frustrating it makes me want to throw something.",
        "You have some nerve doing that to me.",
        "I can't stand this anymore, it drives me absolutely crazy.",
    ]
    happiness = [
        "I am so happy I could cry right now!",
        "This is the best day of my entire life.",
        "I love you more than words can possibly express.",
        "Oh my gosh, I can't believe how wonderful this is!",
        "I'm so excited I can barely contain myself.",
        "Life is absolutely beautiful and I'm grateful for every moment.",
        "You just made my whole week, thank you so much!",
        "I'm thrilled beyond belief, this is amazing news.",
        "Everything is going so perfectly, I feel blessed.",
        "This makes me so incredibly happy, I'm smiling ear to ear.",
    ]
    sadness = [
        "I am so sad I don't even know what to do.",
        "I miss you so much it physically hurts.",
        "I feel completely empty inside today.",
        "I just found out some really devastating news.",
        "I cried myself to sleep last night.",
        "I'm heartbroken and I don't know how to move forward.",
        "Sometimes I feel like nobody truly understands me.",
        "I lost someone I loved deeply and I'm still grieving.",
        "I feel so alone even when I'm surrounded by people.",
        "I'm trying to stay strong but it's getting really hard.",
    ]
    fear = [
        "I am terrified and I don't know why.",
        "That noise scared me half to death.",
        "I'm so nervous about tomorrow I can't sleep.",
        "What if everything goes wrong and I can't fix it?",
        "I'm genuinely afraid of what might happen next.",
        "My heart is pounding and my hands won't stop shaking.",
        "I have a really bad feeling about this.",
        "I've never been this scared in my entire life.",
        "Please don't leave me alone right now, I'm anxious.",
        "I keep imagining worst case scenarios and I can't stop.",
    ]
    religious = [
        "Lord, I am grateful for every blessing in my life.",
        "I pray that God watches over my family and keeps them safe.",
        "Faith is the only thing that keeps me going some days.",
        "Blessed are the peacemakers, for they shall be called children of God.",
        "I believe that everything happens for a reason, and I trust the plan.",
        "Dear God, please give me the strength to get through this.",
        "The Lord is my shepherd, I shall not want.",
        "Allah is merciful and I put my trust completely in him.",
        "May the universe guide me toward peace and understanding.",
        "Buddha taught that suffering comes from attachment.",
        "I light this candle in memory of those who have passed.",
        "Amen. May your will be done on earth as it is in heaven.",
    ]
    scientific = [
        "The mitochondria is the powerhouse of the cell.",
        "Quantum entanglement suggests particles can be correlated across vast distances.",
        "The theory of general relativity describes gravity as the curvature of spacetime.",
        "DNA is a double helix composed of nucleotide base pairs.",
        "Photosynthesis converts light energy into chemical energy stored in glucose.",
        "The periodic table organizes elements by atomic number and chemical properties.",
        "A black hole forms when a massive star collapses under its own gravitational pull.",
        "The speed of light in a vacuum is approximately two hundred ninety-nine million meters per second.",
        "Neural networks are computational models inspired by the human brain.",
        "Tectonic plates move at approximately the same rate your fingernails grow.",
        "The Higgs boson gives particles their mass through the Higgs field.",
        "CRISPR technology allows precise editing of DNA sequences.",
    ]
    sexual = [
        "I find you incredibly attractive and I'm not afraid to say it.",
        "There's a powerful chemistry between us that's hard to ignore.",
        "I want to be close to you in every possible way.",
        "You drive me wild and you probably know it.",
        "I've been thinking about you all day and it's distracting.",
        "The tension between us is absolutely electric.",
        "I'm not going to lie, you are devastatingly attractive.",
        "I want you and I'm done pretending otherwise.",
    ]
    curse = [
        "What the hell is going on around here?",
        "Oh crap, I completely forgot about that.",
        "Are you freaking kidding me right now?",
        "This is total bullshit and everyone knows it.",
        "Son of a bitch, I can't believe that just happened.",
        "I'm so damn tired of dealing with this garbage.",
        "Holy crap, did you see what just happened?",
        "This is so messed up I don't even know where to start.",
    ]
    general_short = [
        "Yes.", "No.", "Maybe.", "Okay.", "Sure.", "Fine.", "Great.", "Wow.",
        "Help.", "Stop.", "Go.", "Wait.", "Now.", "Later.", "Please.", "Thanks.",
        "Sorry.", "What?", "Really?", "Seriously?", "Never.", "Always.", "Again.",
        "Ready.", "Done.", "Enough.", "More.", "Less.", "Right.", "Wrong.",
    ]
    general_long = [
        "I've been thinking a lot about the decisions I've made recently and whether they were the right ones.",
        "The thing about being an adult is that nobody really tells you how hard it's going to be.",
        "I woke up this morning with this strange feeling that today was going to be different.",
        "Sometimes the most profound conversations happen in the most unexpected places.",
        "I genuinely believe that kindness costs nothing but means everything to the people who receive it.",
        "It's funny how the things we worry about most rarely turn out to be as bad as we imagined.",
        "I read somewhere that the average person has about seventy thousand thoughts per day.",
        "Looking back, I realize that the hardest moments in my life made me who I am today.",
        "There's something deeply satisfying about finishing a long project and seeing the results.",
        "I think the world would be a better place if people just listened more and talked less.",
        "You never really appreciate something until it's gone, and that's a painful lesson to learn.",
        "My grandmother used to say that patience is not the ability to wait, but how you act while waiting.",
        "I can't explain it, but something about rainy days makes me feel strangely at peace.",
        "The older I get, the more I realize that time is the most valuable thing we have.",
        "I used to think I had all the answers, but life has a funny way of humbling you.",
    ]
    nature = [
        "The ocean stretches endlessly to the horizon, calm and vast.",
        "The wind rustled through the autumn leaves creating a soft whispering sound.",
        "Lightning split the sky in two as thunder rolled across the valley.",
        "The mountains stood silent and eternal, dusted with fresh snow.",
        "A single flower pushed through the concrete, defying all expectation.",
        "The river carved its path through ancient stone over thousands of years.",
        "At dawn the forest came alive with birdsong and golden light.",
        "The desert was silent except for the sound of sand shifting in the breeze.",
    ]
    technology = [
        "The software update introduces several critical security patches and performance improvements.",
        "Machine learning models require large amounts of labeled training data to perform well.",
        "The server is running at ninety-eight percent capacity and needs to be scaled immediately.",
        "I need to debug this function because it keeps returning null unexpectedly.",
        "The API endpoint is returning a four hundred bad request error.",
        "Encryption ensures that sensitive data cannot be read by unauthorized parties.",
        "Cloud computing allows businesses to scale infrastructure on demand.",
        "The latency on this network connection is unacceptably high.",
        "I deployed the new build to production and it broke everything.",
        "Version control helps teams collaborate without overwriting each other's work.",
    ]
    medical = [
        "The patient's blood pressure is dangerously high and needs immediate attention.",
        "I've been experiencing chest pains and shortness of breath since this morning.",
        "The doctor prescribed a course of antibiotics for the bacterial infection.",
        "Symptoms include fever, fatigue, and a persistent dry cough.",
        "The MRI scan revealed a small but concerning abnormality.",
        "The patient has a history of cardiovascular disease and diabetes.",
        "Pain management is a critical component of post-operative care.",
        "The vaccine provides immunity by training the immune system to recognize the pathogen.",
        "I need to schedule a follow-up appointment for my test results.",
        "Mental health is just as important as physical health and deserves equal attention.",
    ]
    everyday = [
        "Can you pass me the salt please?",
        "I'll have the chicken sandwich with a side of fries.",
        "Do you know where I put my keys?",
        "I need to stop at the gas station on the way home.",
        "The grocery store closes at ten, we need to hurry.",
        "Did you remember to take the trash out this morning?",
        "I'm going to bed, goodnight.",
        "Good morning, did you sleep okay?",
        "I can't find the remote, have you seen it?",
        "The dog needs to go outside.",
        "What do you want for dinner tonight?",
        "I'll pick up the kids from school at three.",
        "Can you help me move this couch to the other side of the room?",
        "I forgot to pay the electric bill, I'll do it right now.",
        "The dishwasher is full, can you run it please?",
    ]
    motivational = [
        "You are stronger than you think and more capable than you know.",
        "Every single day is a new opportunity to become a better version of yourself.",
        "Don't give up. The beginning is always the hardest part.",
        "Believe in yourself even when nobody else does.",
        "Your struggles today are building the strength you'll need tomorrow.",
        "Success is not final and failure is not fatal, what matters is the courage to continue.",
        "You have survived every single hard day so far and you will survive this one too.",
        "Small progress is still progress. Keep going.",
        "The only person you should try to be better than is who you were yesterday.",
        "You are exactly where you need to be right now.",
    ]
    playful = [
        "The quick brown fox jumps over the lazy dog.",
        "She sells seashells by the seashore on sunny summer Sundays.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Peter Piper picked a peck of pickled peppers.",
        "A big black bug bit a big black bear.",
        "Unique New York, unique New York, you know you need unique New York.",
        "Red lorry yellow lorry red lorry yellow lorry.",
        "Fuzzy Wuzzy was a bear, Fuzzy Wuzzy had no hair.",
        "Buffalo buffalo buffalo buffalo buffalo buffalo buffalo buffalo.",
        "The sixth sick sheikh's sixth sheep's sick.",
    ]

    # ── NEW CATEGORIES (3,000 additional phrases) ─────────────────────────────
    travel = [
        "I need to book a flight to New York for next Thursday.",
        "Can you check if there are any direct flights to Paris?",
        "My passport expires next month, I need to renew it.",
        "The hotel says check-in is at three in the afternoon.",
        "I lost my luggage and need to file a claim with the airline.",
        "What is the fastest route to downtown from the airport?",
        "I would like a window seat if one is available please.",
        "The train to Chicago leaves at half past seven.",
        "I need to exchange currency before we leave the country.",
        "Can you recommend a good restaurant near the Eiffel Tower?",
        "My connecting flight was cancelled and I need to rebook.",
        "The cruise ship departs from Miami at noon on Friday.",
        "I need a rental car for the week while I am in Denver.",
        "Is the resort all-inclusive or do meals cost extra?",
        "I would like to upgrade to a suite if it is available.",
        "The taxi driver took the wrong exit and we are now lost.",
        "My hotel room smells like smoke and I want to switch rooms.",
        "Can I get a late checkout, I have a two o'clock flight.",
        "The visa application takes three to four weeks to process.",
        "I always get terrible jet lag when I travel to Asia.",
    ]
    cooking = [
        "I need to preheat the oven to three hundred fifty degrees.",
        "Add a pinch of salt and stir until the sugar dissolves.",
        "The recipe calls for two tablespoons of olive oil.",
        "Can you chop the onions while I mince the garlic?",
        "The chicken needs to reach one hundred sixty-five degrees internally.",
        "I burned the sauce because I forgot to keep stirring.",
        "Can you pass me the wooden spoon from the second drawer?",
        "This bread needs to rise for at least an hour before baking.",
        "I'm trying a new recipe for slow-cooked beef stew tonight.",
        "The pasta should be cooked al dente, not too soft.",
        "Fold the egg whites in gently so you don't deflate them.",
        "I need to dice the tomatoes and julienne the bell peppers.",
        "This sauce has been simmering for over three hours.",
        "Can we make enough for leftovers tomorrow?",
        "The kitchen smells amazing, what are you cooking in there?",
        "I prefer my steak medium rare with a light pepper crust.",
        "We are completely out of butter and the store closes soon.",
        "The caramel needs to reach the hard crack stage before pouring.",
        "I accidentally added too much chili powder and now it's scorching.",
        "Let the meat rest for ten minutes before you slice it.",
    ]
    shopping = [
        "Do you have this in a medium or a large?",
        "I would like to return this jacket, it doesn't fit right.",
        "Can I use this coupon along with the sale price?",
        "How much does this cost with tax included?",
        "I need to find a birthday present for my sister.",
        "This item is out of stock online but says available in store.",
        "I'm looking for a gift under fifty dollars for a coworker.",
        "Do you accept contactless payment or only cards?",
        "The receipt says the price was wrong at checkout.",
        "I'd like to split this between two different payment methods.",
        "Is there a warranty on this appliance?",
        "I saw this same item on sale at another store.",
        "Can you hold this item for me until this afternoon?",
        "I need to find a dress for a black-tie event next weekend.",
        "The website said free shipping but now it's charging me.",
        "I only have cash on me, is there an ATM nearby?",
        "Can I try these shoes on in a size nine?",
        "This jacket has a small tear in the lining near the pocket.",
        "I'm trying to stay within my budget for the holidays this year.",
        "The checkout line is enormous, I'll try self-service instead.",
    ]
    work = [
        "I need to reschedule our meeting to Thursday afternoon.",
        "The deadline for this project has been moved up by two weeks.",
        "Can you send me the updated spreadsheet before end of day?",
        "I'll be working from home on Wednesday and Friday this week.",
        "The client wants revisions done by tomorrow morning.",
        "I have back-to-back meetings all day and no time for lunch.",
        "Can you cover for me on the call at two, I have a conflict?",
        "My computer crashed and I lost an hour of unsaved work.",
        "The printer is jammed again and I need this report printed now.",
        "I need a letter of recommendation by the end of the month.",
        "Could you review my presentation before I send it to the board?",
        "The whole team is working overtime to hit the product launch.",
        "I've been copied on too many emails that don't concern me.",
        "My boss wants the quarterly report on her desk by Monday.",
        "I have a performance review coming up and I'm nervous about it.",
        "Can someone take notes during the meeting, I need to present.",
        "The conference call kept dropping and we lost half the discussion.",
        "I put in for two weeks of vacation starting on the fifteenth.",
        "We need to onboard three new employees starting next Monday.",
        "The contract still has not been signed and we start next week.",
    ]
    relationships = [
        "I love you and I always will, no matter what.",
        "We need to talk about what happened last night.",
        "I feel like you never really listen to what I'm saying.",
        "I'm so proud of everything you have accomplished.",
        "I miss spending quality time with you like we used to.",
        "You are my best friend and I don't say that enough.",
        "I think we need couples counseling to work through this.",
        "I was wrong and I want to sincerely apologize.",
        "Can we please stop arguing and just talk calmly?",
        "I feel taken for granted and I need you to know that.",
        "You are the first person I want to call when something happens.",
        "I appreciate everything you do even when I forget to say so.",
        "Long-distance relationships are incredibly hard but we're making it work.",
        "I don't want to lose you over something this small.",
        "You make me want to be a better person every single day.",
        "I need some space to think, it's not about you personally.",
        "Let's plan a date night this weekend, just the two of us.",
        "I was jealous and I handled it badly, I'm sorry.",
        "I feel like we are finally communicating better these days.",
        "Growing old with you is the only future I want.",
    ]
    news_current = [
        "The stock market dropped two percent on heavy trading volume today.",
        "Scientists have discovered a new species of deep-sea fish near the Mariana Trench.",
        "A major wildfire is burning across thousands of acres in southern California.",
        "The city council voted to approve the new public transit expansion plan.",
        "Inflation has risen slightly but remains within the target range.",
        "The two world leaders met for a bilateral summit on climate change.",
        "A new record was set for the fastest electric vehicle in the quarter mile.",
        "Cybersecurity experts warned of a new ransomware campaign targeting hospitals.",
        "The hurricane made landfall early this morning as a category three storm.",
        "Unemployment fell to its lowest point in over two decades last quarter.",
        "Local officials declared a state of emergency after severe flooding overnight.",
        "A groundbreaking new treatment for Alzheimer's disease is entering clinical trials.",
        "The tech giant announced layoffs affecting nearly ten thousand employees.",
        "A historic peace agreement was signed after three years of negotiations.",
        "Astronomers detected an exoplanet with conditions potentially suitable for life.",
    ]
    humor = [
        "I asked my cat what two minus two was, and he said nothing.",
        "Why do we park in driveways and drive on parkways?",
        "I told my doctor I broke my arm in two places and he said stop going to those places.",
        "The best part of waking up is going back to sleep.",
        "My wifi password is the last four digits of my weight.",
        "I'm not lazy, I'm just on energy-saving mode.",
        "I put the fun in functional and then removed it.",
        "My memory is so bad I tried to pull up my own name and it buffered.",
        "I'm not arguing, I'm just passionately explaining why I'm right.",
        "I do my best thinking in the shower where I have no way to write anything down.",
        "Why do they call it rush hour when nothing moves?",
        "I'm on a seafood diet. I see food and I eat it.",
        "The elevator was broken so I took steps to avoid it.",
        "I told a pun about stairs but it was a step too far.",
        "My sleep schedule is a work of abstract fiction.",
    ]
    mental_wellness = [
        "I've been practicing mindfulness and it's genuinely helping my anxiety.",
        "Taking a walk outside completely changed my mood today.",
        "I journaled for thirty minutes this morning and felt so much lighter.",
        "Therapy taught me that my feelings are valid even when they're uncomfortable.",
        "I need to stop catastrophizing and focus on what I can control.",
        "Breathing deeply for just sixty seconds really does calm me down.",
        "Setting boundaries is an act of self-respect, not selfishness.",
        "I'm learning to sit with discomfort instead of running from it.",
        "Progress is not always linear and that is completely okay.",
        "I am not my intrusive thoughts, I am the one noticing them.",
        "Rest is not a reward, it is a basic human need.",
        "I'm choosing to release what I cannot change.",
        "Asking for help is a sign of courage, not weakness.",
        "I am enough exactly as I am, even on my hardest days.",
        "Healing is not a destination, it is an ongoing process.",
        "I deserve kindness from myself the same way I give it to others.",
        "My body is telling me it needs rest and I am going to listen.",
        "I am not behind. I am on my own timeline.",
        "Even five minutes of stillness can reset a difficult day.",
        "I am practicing self-compassion and it is changing everything.",
    ]
    history = [
        "The First World War began in nineteen fourteen and ended four years later.",
        "The fall of the Berlin Wall in nineteen eighty-nine symbolized the end of the Cold War.",
        "Ancient Rome was one of the most powerful empires in human history.",
        "The moon landing in nineteen sixty-nine was a defining moment for humanity.",
        "The Great Depression devastated economies around the world throughout the nineteen thirties.",
        "The printing press revolutionized the spread of information in the fifteenth century.",
        "Napoleon was exiled to the island of Elba after his defeat at Leipzig.",
        "The civil rights movement transformed American society throughout the nineteen sixties.",
        "The pyramids of Giza were built over four thousand five hundred years ago.",
        "The signing of the Magna Carta in twelve fifteen limited the power of the king.",
        "The Industrial Revolution began in Britain and spread across the world.",
        "World War Two ended in Europe on the eighth of May, nineteen forty-five.",
        "The Renaissance was a period of extraordinary artistic and intellectual achievement.",
        "Alexander the Great conquered most of the known world by the age of thirty.",
        "The atomic bomb changed the nature of warfare and global politics forever.",
    ]
    sports = [
        "He sprinted down the sideline and scored in the final thirty seconds.",
        "The referee called a foul and the crowd went absolutely wild.",
        "She trained every morning at five just to make it to the Olympics.",
        "The home team hasn't lost a game on this field in three seasons.",
        "That was an incredible come-from-behind victory in double overtime.",
        "He broke the world record by nearly two full seconds.",
        "The match went to a fifth set tiebreaker before anyone could blink.",
        "She sank the winning putt from forty feet away without hesitating.",
        "The draft pick has already exceeded every expectation set for him.",
        "They won the championship without losing a single game all season.",
        "The coach called a timeout with three seconds left and drew up the perfect play.",
        "Her serve hit the line and the crowd erupted into complete chaos.",
        "He came back from a career-ending injury to win the gold medal.",
        "The stadium went silent as the penalty kick sailed wide of the post.",
        "She set a new personal best and burst into tears at the finish line.",
    ]

    all_pool = (anger * 3 + happiness * 3 + sadness * 3 + fear * 3 +
                religious * 2 + scientific * 2 + sexual * 2 + curse * 2 +
                general_short * 5 + general_long * 2 + nature * 2 +
                technology * 2 + medical * 2 + everyday * 4 +
                motivational * 2 + playful * 2 +
                travel * 3 + cooking * 3 + shopping * 3 + work * 3 +
                relationships * 3 + news_current * 2 + humor * 3 +
                mental_wellness * 3 + history * 2 + sports * 3)

    phrases = set()
    pool_cycle = list(all_pool)
    random.shuffle(pool_cycle)
    for p in pool_cycle:
        if len(phrases) >= count:
            break
        phrases.add(p)

    # Fill remainder: cycle through all filler×base combos (finite, no infinite loop risk)
    all_fillers = ["Um, ", "Well, ", "So, ", "Actually, ", "Honestly, ",
                   "Look, ", "Right, ", "Okay, ", "Now, ", "Yes, ",
                   "True, ", "Hey, ", "Wait, ", "No, ", "Still, "]
    bases = general_long + everyday + motivational + nature + technology + medical
    for filler in all_fillers:
        for base in bases:
            if len(phrases) >= count:
                break
            p = f"{filler}{base[0].lower()}{base[1:].rstrip('.!?')}."
            phrases.add(p)
        if len(phrases) >= count:
            break

    return list(phrases)[:count]


# ── Phrase cleaner ─────────────────────────────────────────────────────────────

# Fragments that are NEVER valid standalone English words — signal a broken/split word
# e.g. "indepe ndence", "acqui escence", "gratifica tion"
_BROKEN_FRAGMENTS = {
    'indepe', 'independ', 'acqui', 'acquies', 'acquiesc', 'gratifica',
    'pleasura', 'unmistaka', 'imagina', 'recogni', 'recogniz', 'recognis',
    'organi', 'organiz', 'individu', 'differe', 'exper', 'experi', 'impor',
    'imposs', 'impossib', 'represen', 'demonstr',
}

# Second fragments after a hyphen that are NEVER standalone words
# These signal OCR line-break hyphens: "ther-apy", "num-bers", "sta-ble"
_BAD_HYPHEN_SUFFIXES = {
    'apy',       # ther-apy → therapy
    'ble',       # sta-ble → stable
    'bers',      # num-bers → numbers
    'bilities',  # vulnera-bilities → vulnerabilities
    'iour',      # behav-iour → behaviour
    'ders',      # disor-ders → disorders
    'nents',     # expo-nents → exponents
    'dinates',   # coor-dinates → coordinates
    'erties',    # prop-erties → properties
    'tive',      # representa-tive → representative, nega-tive → negative
    'uals',      # individ-uals → individuals
    'ity',       # real-ity → reality
    'spond',     # corre-spond → correspond
    'tions',     # emo-tions → emotions, conversa-tions → conversations
    'encing',    # experi-encing → experiencing
    'icant',     # signifi-cant → significant
    'plating',   # contem-plating → contemplating
    'rying',     # car-rying → carrying
    'lling',     # contro-lling → controlling
    'ssing',     # proce-ssing → processing
    'rning',     # concer-ning → concerning
    'iting',     # wri-ting → writing (short prefix)
    'ling',      # mode-ling → modeling
}

# First fragments before a hyphen that are NEVER standalone words
# Used only in hyphen context check
_BAD_HYPHEN_PREFIXES = {
    'contem', 'signifi', 'vulnera', 'behav', 'disor', 'expo', 'coor',
    'repre', 'represen', 'individ', 'conversa', 'emo', 'experi', 'nega',
    'sta',    # sta-ble
    'num',    # num-bers
    'corre',  # corre-spond
    'deter',  # deter-mine
    'ther',   # ther-apy
    'por',    # por-trayal
    'psy',    # psy-chology
    'psycho', # psycho-logical (when broken mid-word)
    'opyright',  # opyright → OCR ate first letter
    'ognitive',  # ognitive → OCR ate first letter
    'counterde', # counterde-pendence
    'overwhelm', # overwhelm-ing (should be one word "overwhelming")
}

# Psychoanalytic / Freudian academic source text — not suitable for STT
_ACADEMIC_BLOCKLIST = [
    'gratification from the acquiescence',
    'pleasure principle',
    'reality principle',
    'instinctual drive',
    'unconscious wish',
    'wish fulfillment',
    'libidinal',
    'cathexis',
    'phantasy',
    'sublimation of',
    'narcissistic gratification',
    'psychosexual',
    'transference neurosis',
    'anxiety neurosis',
    'the dreamer',
    'dream analysis',
    'archaic form',
    'imaginative happiness',
    'acquiescence of reality',
    'restoration of the independence',
    'pleasurable gratification',
    # Art therapy textbook content
    'mural paper',
    'construction paper, glue',
    'doily cut',
    'art therapy',
    'art therapist',
    'the client named',
    'clinically depressed client',
    'paint to illustrate',
    'art technique',
    'mask making',
    # Textbook exercise markers
    'workbook',
    # German/foreign language artifacts from OCR
    'fliegende blätter',
    'in f., and since',
]

def is_clean(phrase):
    p = phrase.strip()

    # Length bounds
    if len(p) < 8 or len(p) > 250:
        return False

    # Must start with a letter
    if not p[0].isalpha():
        return False

    # Must end with sentence-ending punctuation
    if p[-1] not in '.?!':
        return False

    # No double spaces (OCR artifact)
    if re.search(r'\s{2,}', p):
        return False

    # No LaTeX / backslash commands
    if re.search(r'\\[a-zA-Z]', p):
        return False

    # No academic citation patterns
    if re.search(r'\(\w+,\s*\d{4}\)', p):
        return False
    if re.search(r'\bp\.\s*\d+|\bpp\.\s*\d+|\bibid\b|\bet al\.', p.lower()):
        return False

    # No version numbers or IP-style sequences
    if re.search(r'\d+\.\d+\.\d+', p):
        return False

    # No broken hyphenation (dash then space then lowercase: "word- word")
    if re.search(r'[a-z]-\s[a-z]', p):
        return False

    # Blocked academic/clinical content + OCR fragment checks need lowercase version
    pl = p.lower()

    # Detect OCR line-break hyphens: "ther-apy", "num-bers", "sta-ble", "por-trayal"
    # Check both the bad suffix AND bad prefix sets
    for m in re.finditer(r'([a-z]{2,})-([a-z]{2,})', pl):
        first, second = m.group(1), m.group(2)
        if second in _BAD_HYPHEN_SUFFIXES:
            return False
        if first in _BAD_HYPHEN_PREFIXES:
            return False

    # No ALL-CAPS blocks
    if re.search(r'[A-Z]{5,}', p):
        return False

    # No 4+ digit numbers (years, codes, etc.)
    if re.search(r'\b\d{4,}\b', p):
        return False

    # No numbered synthetic duplicates: "phrase — 248." style
    if re.search(r' — \d+\.$', p):
        return False

    # No math operators
    if re.search(r'\d+x\s*[\+\-]', p):
        return False

    # No URLs
    if re.search(r'https?:|www\.', p.lower()):
        return False

    # Blocked academic/clinical content
    if any(block in pl for block in _ACADEMIC_BLOCKLIST):
        return False

    # Detect stuck words: camelCase in the middle of a phrase
    # e.g. "ofJuly", "SubjectVerb", "DiscussionGoals"
    if re.search(r'[a-z][A-Z]', p):
        return False
    # Detect "I" stuck to a verb at start (no space): "Igrew", "Iwas", "Iam", "Iwent"
    if re.match(r'^I(grew|was|were|went|am|are|have|had|can|will|would|did|do|need|want|see|saw|know|feel|felt|think|believe|said|told|asked|tried|used|got|get|gave|give|took|take|made|make|came|come|ran|run|sat|sit|stood|stand|walked|talked|called)', p):
        return False
    # Detect "br other" / "m other" / "f ather" style stuck family words
    if re.search(r'\bbr other\b|\bm other\b|\bf ather\b|\bs ister\b|\bb rother\b', pl):
        return False

    # Detect OCR mid-word split using known non-word fragments
    # e.g. "indepe ndence" — "indepe" is never a standalone word
    for m in re.finditer(r'\b([a-z]{4,9}) ([a-z]{3,8})\b', pl):
        frag = m.group(1)
        if frag in _BROKEN_FRAGMENTS:
            return False

    # Detect mid-word hyphenation breaks: 'indepe ndence', 'differe ntiate', 'sym ptom'
    # The continuation starts with a consonant cluster that can't begin an English word
    if re.search(r'\b[a-z]{3,8} (?:nd|nt|nc|ng|ld|lk|lm|lp|lt|rb|rd|rk|rm|rn|rp|rt|ck|ct|ft|pt)[a-z]+\b', pl):
        return False

    # Textbook-style title/heading
    if re.match(r'^[A-Z][a-z]+ (Is|For|And) [A-Z][a-z]', p):
        return False

    return True


def main():
    print("Loading existing phrases...")
    with open(PHRASES_JSON, "r", encoding="utf-8") as f:
        existing = json.load(f)
    print(f"  Loaded {len(existing):,} phrases")

    print("Cleaning phrases...")
    cleaned = [p for p in existing if is_clean(p)]
    print(f"  Kept {len(cleaned):,} clean phrases ({len(existing)-len(cleaned):,} removed)")

    all_phrases = set(cleaned)

    print("Adding 1000 command phrases...")
    all_phrases.update(COMMAND_PHRASES)

    print("Adding 100 curated phrases...")
    all_phrases.update(CURATED)

    print("Generating 6000 diverse synthetic phrases...")
    synthetic = generate_diverse(6000)
    all_phrases.update(synthetic)

    final = sorted(all_phrases)
    print(f"\nFinal phrase count: {len(final):,}")

    with open(PHRASES_JSON, "w", encoding="utf-8") as f:
        json.dump(final, f, ensure_ascii=False, indent=2)
    print("Done!")


if __name__ == "__main__":
    main()

