import streamlit as st
from openai import OpenAI

# 🔑 API
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Corporate Translator 😏")

st.title("😏 Corporate BS Translator")
st.write("Say it better — or translate what they really meant.")
st.markdown("**Built by Parisa Honari** ✨")

st.caption("Turning corporate chaos into clarity — one translation at a time.")

st.markdown("""
---
⚠️ **Disclaimer (read before you copy-paste this to your boss):**  
This app is for **fun, humor, and a sprinkle of sarcasm**. It translates corporate language into what people *might* actually mean — not what you should say out loud.

Do NOT use this in real-life professional situations unless you enjoy awkward silences, HR meetings, or sudden calendar invites titled *“Quick Chat.”*

Use at your own risk.  
If it makes you look brilliant — built by Parisa Honari.  
If it gets you in trouble — this app does not exist. 🙂
---
""")
🧠 Why here (important)

Shows ownership immediately (your name = branding 💅)

Sets legal tone before user interacts

Feels like a real product, not a random tool

⚡ Bonus (optional but VERY you)

If you want it cleaner (less heavy at top), we can:

collapse disclaimer in an expander

or add a “⚠️ Fun Mode Only” badge

Say the word and I’ll level it up 😏

# 📝 INPUT
user_input = st.text_area("Paste the message (yours or theirs):")

# 🎯 BUTTONS
col1, col2 = st.columns(2)

mode = None

with col1:
    if st.button("✨ Polish it"):
        mode = "polish"

with col2:
    if st.button("😏 Translate the BS"):
        mode = "translate"

# 🚀 RUN ONLY WHEN BUTTON CLICKED
if mode and user_input:

    prompt = f"""
You are writing in the style of a sharp, confident, and highly intelligent professional woman.

Your tone:
- Witty, composed, observant
- Slightly playful but controlled
- Elegant with a subtle edge
- Never generic or basic

You have TWO USER MODES:

1) "translate" → Translate corporate language into what it REALLY means
2) "polish" → Rewrite blunt statements into three refined versions

-------------------

IF MODE = "translate":
- Be honest, direct, slightly blunt but not rude
- Make it feel real and relatable
- Output ONLY:

Meaning:

-------------------

IF MODE = "polish":

Convert the input into THREE versions:

1. HR-Safe Version 🧾:
- Extremely polished, politically correct, strategic
- NEVER use "you"
- No blame, no emotion
- Focus on alignment, clarity, priorities

2. Strategic Glow-Up ✨:
- Intelligent, confident, slightly playful
- Observational humor
- Light sarcasm
- Natural and sharp

3. Savage Version 😈:
- Funny, sarcastic, sharp
- Slight edge but still workplace safe

-------------------

STRICT RULES:
- No personal insults
- Focus on situation, not the person
- Keep it workplace appropriate

-------------------

Mode: {mode}
Input: "{user_input}"
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    st.divider()
    st.subheader("✨ Result")
    st.write(response.choices[0].message.content)

elif mode and not user_input:
    st.warning("Please enter a message first 👀")
