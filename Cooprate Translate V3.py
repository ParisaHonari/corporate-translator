import streamlit as st
import os
from openai import OpenAI

# 🔑 API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ⚙️ Page Config
st.set_page_config(page_title="Corporate Translator 😏", layout="wide")

# 🎨 STYLE
st.markdown("""
<style>

/* Layout */
.block-container {
    max-width: 1000px;
    padding-top: 0.3rem;
    margin: auto;
}

/* Text area */
textarea {
    width: 100% !important;
    border-radius: 12px !important;
    border: 1px solid #ddd !important;
    padding: 14px !important;
    font-size: 16px !important;
}

/* Buttons */
.stButton>button {
    border-radius: 16px;
    background-color: #E87C72;
    color: white;
    font-weight: 600;
    padding: 14px;
    font-size: 16px;
    white-space: nowrap;
    border: none;
}

.stButton>button:hover {
    background-color: #d96b61;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# 🧠 HEADER
st.markdown("""
<h1 style='text-align: center; color:#E87C72;'>😏 Corporate BS Translator</h1>
<p style='text-align: center; font-size:18px; color:#444;'>
Say it better — or translate what they really meant.
</p>
<p style='text-align: center; font-weight:600; color:#E87C72;'>
Built by Parisa Honari ✨
</p>
""", unsafe_allow_html=True)

# ✍️ INPUT
st.markdown("<h3 style='text-align:center;'>✍️ Paste your message below</h3>", unsafe_allow_html=True)
user_input = st.text_area("", height=150)

# 🎯 PERFECT BUTTONS (FIXED)
mode = None

col_left, col_center, col_right = st.columns([1,2,1])

with col_center:
    b1, b2 = st.columns(2)

    with b1:
        if st.button("✨ Polish it", use_container_width=True):
            mode = "polish"

    with b2:
        if st.button("😏 Translate the BS", use_container_width=True):
            mode = "translate"

# 🚀 RUN
if mode and user_input:

    prompt = f"""
You are writing in the style of a sharp, confident, witty, and highly intelligent professional woman.

Your tone:
- Observant, clever, slightly sarcastic
- Elegant but with personality
- Never boring or generic

You have TWO USER MODES:

1) "translate" → Decode corporate language into what it REALLY means
2) "polish" → Rewrite blunt statements into three refined versions

-------------------

IF MODE = "translate":

Output EXACTLY like this:

💭 What they said:
(optional clean version)

🧠 What they actually mean:
(witty, honest, slightly sarcastic but smart)

💅 Translation:
(short, punchy, memorable line)

-------------------

IF MODE = "polish":

Convert into THREE versions:

1. HR-Safe Version 🧾:
- Polished, strategic, politically correct
- No "you"
- No blame

2. Strategic Glow-Up ✨:
- Smart, confident, slightly playful
- Light sarcasm

3. Savage Version 😈:
- Funny, sharp, a little bold but still workplace safe

-------------------

STRICT RULES:
- No personal insults
- Keep it workplace appropriate
- Make it sound natural and human

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
        background-color:#F9F4F3;
        padding:20px;
        border-radius:12px;
        border-left:5px solid #E87C72;
    ">
    {response.choices[0].message.content}
    </div>
    """, unsafe_allow_html=True)

elif mode and not user_input:
    st.warning("Please enter a message first 👀")

# ⚠️ FOOTER
st.markdown("""
<br><br>
<hr>
<p style='font-size:13px; color:gray; text-align:center;'>
⚠️ This tool is for fun, humor, and sarcasm.  
Use at your own risk 😏
</p>
""", unsafe_allow_html=True)
