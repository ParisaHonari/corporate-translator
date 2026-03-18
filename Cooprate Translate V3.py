import streamlit as st
import os
from openai import OpenAI

# 🔑 API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ⚙️ Page Config
st.set_page_config(page_title="Corporate Translator 😏", layout="wide")

# 🎨 STYLE (width + polish)
st.markdown("""
<style>

/* Layout width */
.block-container {
    max-width: 1100px;
    padding-top: 1.2rem;
    margin: auto;
}

/* Text area */
textarea {
    width: 100% !important;
    border-radius: 12px !important;
    border: 1px solid #ddd !important;
    padding: 12px !important;
    font-size: 16px !important;
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    background-color: #7B1E3A;
    color: white;
    font-weight: 600;
}

.stButton>button:hover {
    background-color: #5a162b;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# 🧠 HEADER
st.markdown("""
<h1 style='text-align: center; color:#7B1E3A;'>😏 Corporate BS Translator</h1>
<p style='text-align: center; font-size:18px; color:#444;'>
Say it better — or translate what they really meant.
</p>
<p style='text-align: center; font-weight:600; color:#7B1E3A;'>
Built by Parisa Honari ✨
</p>
""", unsafe_allow_html=True)

# 📝 INPUT (CENTER FEEL)
st.markdown("### ✍️ Paste your message below")
user_input = st.text_area("", height=150)

# 🎯 BUTTONS
col1, col2 = st.columns(2)

mode = None

with col1:
    if st.button("✨ Polish it"):
        mode = "polish"

with col2:
    if st.button("😏 Translate the BS"):
        mode = "translate"

# 🚀 RUN
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

    st.markdown(f"""
    <div style="
        background-color:#F7F7F7;
        padding:20px;
        border-radius:12px;
        border-left:5px solid #7B1E3A;
    ">
    {response.choices[0].message.content}
    </div>
    """, unsafe_allow_html=True)

elif mode and not user_input:
    st.warning("Please enter a message first 👀")

# ⚠️ DISCLAIMER (MOVED TO BOTTOM)
st.markdown("""
<br><br>
<hr>

<p style='font-size:13px; color:gray; text-align:center;'>
⚠️ This tool is for fun, humor, and a bit of sarcasm.  
Use at your own risk — especially before sending emails to your boss 😏
</p>
""", unsafe_allow_html=True)
