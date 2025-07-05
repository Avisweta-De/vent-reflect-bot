import streamlit as st
import datetime
import os

# App setup
st.set_page_config(page_title="Vent and Reflect Bot", layout="centered")
st.title("🧠 Vent and Reflect Bot")
st.markdown("Welcome to your private space to express and reflect. Your words are safe here.")

# Ask for username first
username = st.text_input("👤 Enter your name or nickname (used to store your journal):")

if username:
    filename = f"{username.strip().lower()}_log.txt"

    vent = st.text_area("💬 What’s on your mind today?", height=200)

    if vent:
        reflect = st.checkbox("✨ Would you like to reflect on what you shared?")

        reflect_answers = {}
        if reflect:
            st.subheader("🔍 Let's Reflect")
            q1 = st.text_input("1. What triggered this feeling?")
            q2 = st.text_input("2. How do you usually cope with it?")
            q3 = st.text_input("3. What’s one thing that could help you right now?")
            reflect_answers = {
                "What triggered this feeling?": q1,
                "How do you usually cope with it?": q2,
                "What could help now?": q3,
            }

        if st.button("💾 Save Entry"):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log = f"\n[{timestamp}]\nVENT: {vent}\n"
            if reflect and any(reflect_answers.values()):
                log += "REFLECTION:\n"
                for q, a in reflect_answers.items():
                    log += f"- {q} {a}\n"
            else:
                log += "REFLECTION: Skipped or Empty\n"
            log += "-"*40 + "\n"

            with open(filename, "a", encoding="utf-8") as f:
                f.write(log)

            st.success("✅ Your entry has been saved.")

    if st.checkbox("📚 View Your Past Entries"):
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                st.text(f.read())
        else:
            st.warning("You don't have any past entries yet.")
else:
    st.info("Please enter your name to begin.")
