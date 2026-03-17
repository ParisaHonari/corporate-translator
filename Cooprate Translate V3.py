import streamlit as st
from openai import OpenAI

# 🔑 API
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Corporate Translator 😏")

st.title("😏 Corporate BS Translator")
st.write("Say it better — or translate what they really meant.")

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