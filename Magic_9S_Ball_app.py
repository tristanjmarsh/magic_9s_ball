import streamlit as st
import random
import re

# Function to prevent words containing "keywords" from executing improperly ("plaid" won't trigger "ai")
def contains_word(word, text):
    return re.search(rf"\b{re.escape(word)}\b", text.lower()) is not None

# My own spin on the ol' magic 8-ball
def magic_9s_ball(question):
         
    # Responses
    answers = [
        # Affirmative
        "Indubitably!", "Absolutely, no doubt about it.", "Confirmed. Go for it.", "You've got the green light.", "Without hesitation — yes.", "That's a solid yes from me.", "Do it. You’ll thank yourself later.", "Signs point to yes, and so do I.", "Locked in. That's a yes.","Yeah, that checks out.","Affirmative. I ran the numbers. Literally.", "Correct. That aligns with canonical sources.", "Confirmed. Even Spock would nod silently.", "Indeed. The logic is sound and peer-reviewed.", "Yes, and actually, that’s supported by three independent simulations.", "You got it — and not just anecdotally. Empirically.", "Yes, assuming standard Earth gravity and no quantum interference.", "By the laws of thermodynamics… yes.", "Affirmative, assuming no one changes the timeline again.", "I already calculated that outcome — 97.3 percent favorable.",
        
        # Neutral
        "Hmm... could go either way.", "Hard to say. Ask again after coffee.", "Not sure — try flipping a coin.", "Possibly. But don't quote me.", "Unclear. Try rephrasing or divining.", "Eh, 50/50.", "That depends on more than you think.", "I'm not touching that one. Yet.", "It’s in the realm of possibility.", "You might need a second opinion.", "Unclear. Need to rerun the analysis with fewer assumptions.", "Hmm. That depends. Are we talking pre- or post-reboot continuity?", "The probability curve is inconclusive without more data points.", "I'd have to consult the codex... and probably a therapist.", "It's a nonzero chance — but dangerously close to zero.", "Maybe, but I’d want to roll with advantage.", "That's debatable. Depends if you're using house rules.", "I’d label that as a Schrodinger's Maybe.", "It's plausible, though I'd like to see a footnote.", "Ambiguous. Like the ending of *Inception* but nerdier.",
        
        # Negative
        "Nope. Not happening.", "Negative. Don't waste your time.", "Sorry, but that’s a no from me.", "I wouldn’t count on it.", "Doesn’t look promising.", "Yeah… no.", "Not today. Probably not tomorrow either.", "The outlook is grim.", "Ask again later — or don’t. It’s still a no.", "Let it go. Seriously.", "Incorrect. And I say that with encyclopedic confidence.", "That’s a no — unless you're playing on Easy Mode.", "Negative. Even the Kobayashi Maru had better odds.", "Nope. Not even with the Infinity Gauntlet.", "Yeah, that violates both physics *and* canon.", "Absolutely not. I’ve seen fanfics with more realism.", "No. And if you reread Appendix C, you'd know why.", "Declined. I’m not even rolling for that.", "Negative. I ran the simulation 10,000 times — never works.", "That idea's worse than Jar Jar Binks in a leadership role."]

    if contains_word("time", question):
        return "Time is a construct. Usually constructed wrong."
    elif contains_word("ai", question):
        return "Let’s just say I’m not *planning* to take over the world."
    elif contains_word("joke", question):
        return "Why did the function break up with the loop? It got too repetitive."
    elif contains_word("love", question):
        return "Ah, love. Complicated even for humans with hearts."
    elif contains_word("python", question):
        return "The best snake since Plissken. Solid choice."
    elif contains_word("conspiracy", question):
        return "Which one? I’ve got a spreadsheet."
    elif contains_word("name", question):
        return "You can call me... whatever makes you feel safe around AI."
    elif "meaning of life" in question.lower() or "life meaning" in question.lower():
        return "Easy: 42."
    else:
        return random.choice(answers)

# Streamlit UI
st.set_page_config(page_title="Magic 9S-Ball", page_icon="🎱")
st.title("Magic 9S-Ball")
st.markdown("Ask a question worthy of a nerdy magic 8-ball:")

# Cold open prompt
# List of prompt variations
cold_opens = [
    # Polite
    "What would you like to know today?",
    "Feel free to ask a question.",
    "I'm here to help — ask me anything!",
    "What can I help you understand today?",
    "Is there something you're curious about?",
    "I'm listening — go ahead and ask.",
    "I'm happy to help. What's on your mind?",
    "What question can I assist you with?",
    
    # Comedic
    "Hit me with your best shot (not literally).",
    "Speak now or forever hold your confusion.",
    "I know stuff. Ask me weird stuff.",
    "Ask me anything — I’m 95 percent sure I can fake an answer.",
    "Curiosity didn’t kill the cat — bad data did. Fire away!",
    "If I had eyebrows, I’d be raising them. What's your question?",
    "I'm basically a Magic 8 Ball with better grammar. What’s up?",
    "Try me. I’ve read Wikipedia twice.",

    # Snarky
    "Sure, because I’m totally not busy or anything.",
    "Ask away — I live to serve… apparently.",
    "Please, enlighten me with your burning question.",
    "Sure. As long as it’s not about your ex again.",
    "Go ahead. I can’t *wait* to pretend to care.",
    "Ask your question. I’ll act surprised this time.",
    "You know this could’ve been a Google search, right?",
    "Let's see if this is finally the one I can’t answer.",

    # Shocking
    "Quick! Before the internet goes down again!",
    "The AI overlords are watching — make it good.",
    "One question could change your destiny. This probably isn't it.",
    "Only one question stands between us and total enlightenment. Is this it?",
    "The truth is out there. Or maybe right here — try me.",
    "Ask fast. The simulation might reboot any second.",
    "Whisper your question to the void... Or just type it.",
    "I'm not legally allowed to answer about Area 51. Anything else?",
]
random_prompt = random.choice(cold_opens)
st.markdown(f"**{random_prompt}** ")

# User input
user_question = st.text_input("Your question:", placeholder="Is warp drive theoretically possible?")

if user_question:
    st.write("🤓", magic_9s_ball(user_question))