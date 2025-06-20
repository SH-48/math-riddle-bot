#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import random

# ---- Data ----
questions = [
    {
        "question": "Which quadratic equation represents the area of a square with side length x, if the area is 289 m²?",
        "choices": ["x² - 17x = 289", "x² + 17² = 0", "(x + 17)² = 0", "x² - 289 = 0"],
        "answer": "x² - 289 = 0",
        "hint": "Area of square is x². Rearranged to standard form.",
        "explanation": "Area = x² → x² = 289 → x² - 289 = 0 is the correct form."
    },
    {
        "question": "Solve the quadratic: (x + 1)(x + 2) = -2x(x + 2)",
        "choices": ["x = 1, x = -2/3", "x = -1, x = -2/3", "x = -1, x = 2/3", "x = 1, x = 2/3"],
        "answer": "x = 1, x = -2/3",
        "hint": "Expand both sides and simplify before solving.",
        "explanation": "Simplifying both sides gives a quadratic: x² + 3x + 2 = -2x² - 4x → solve it to get x = 1 and -2/3."
    },
    {
        "question": "Convert binary number 1101₂ to base 10.",
        "choices": ["14", "11", "13", "15"],
        "answer": "13",
        "hint": "Use place values: 1×8 + 1×4 + 0×2 + 1×1.",
        "explanation": "1×8 + 1×4 + 0×2 + 1×1 = 13."
    },
    {
        "question": "Given P = {1,3,5,7,9} and R = {1,4,9}, what is P ∩ R?",
        "choices": ["1, 4", "3, 7", "1, 9", "4, 9"],
        "answer": "1, 9",
        "hint": "Intersection = common elements.",
        "explanation": "Elements in both sets: {1, 9}."
    },
    {
        "question": "In a graph, a vertex has a loop. What is the degree of that vertex?",
        "choices": ["1", "2", "3", "0"],
        "answer": "2",
        "hint": "A loop adds 2 to the degree.",
        "explanation": "In graph theory, a loop contributes two to the degree of a vertex."
    },
    {
        "question": "What is the range of this data set: 10, 5, 8, 18, 22, 12?",
        "choices": ["15", "17", "13", "12"],
        "answer": "17",
        "hint": "Range = Max - Min.",
        "explanation": "Range = 22 - 5 = 17."
    },
    {
        "question": "A fair coin and a die are tossed. How many total outcomes are there?",
        "choices": ["6", "10", "12", "14"],
        "answer": "12",
        "hint": "2 outcomes × 6 outcomes.",
        "explanation": "2 outcomes from coin × 6 outcomes from die = 12 total outcomes."
    },
    {
        "question": "Find the roots of the equation x² + x - 6 = 0",
        "choices": ["x = 3, x = -2", "x = 2, x = -3", "x = -3, x = -2", "x = 1, x = -6"],
        "answer": "x = 2, x = -3",
        "hint": "Factor: (x + 3)(x - 2).",
        "explanation": "x² + x - 6 factors into (x + 3)(x - 2), so x = -3 or x = 2."
    },
    {
        "question": "Express 2(64) + 24 + 6 in base 7.",
        "choices": ["10423", "7044", "5066", "3524"],
        "answer": "5066",
        "hint": "Convert total from base 10 to base 7.",
        "explanation": "2×64 + 24 + 6 = 158 in base 10 → 5066 in base 7."
    },
    {
        "question": "The arrow follows a quadratic path: f(x) = -13/200 x² + 39/20 x. What is its maximum height?",
        "choices": ["1.6", "2.1", "1.95", "2.5"],
        "answer": "1.95",
        "hint": "Find vertex: x = -b/2a, then compute f(x).",
        "explanation": "x = -b/2a = 1.5 → f(1.5) = 1.95 (max height)."
    }
]

# ---- App State ----
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.q_index = 0
    st.session_state.score = 0
    st.session_state.hints_used = 0
    st.session_state.correct_streak = 0
    st.session_state.used_hint_this_round = False
    st.session_state.questions = random.sample(questions, len(questions))
    st.session_state.show_feedback = False
    st.session_state.feedback_msg = ""
    st.session_state.feedback_color = "black"

# ---- Start Page ----
if not st.session_state.started:
    st.title("🧠 Math Riddle Bot")
    st.markdown("Welcome! Test your mind with fun math challenges.")
    st.button("▶️ Start Quiz", on_click=lambda: st.session_state.update({"started": True}))
    st.stop()

# ---- Progress ----
st.markdown(f"### Question {st.session_state.q_index + 1} of {len(st.session_state.questions)}")
st.progress(st.session_state.q_index / len(st.session_state.questions))
st.markdown(f"**Score:** {st.session_state.score} &nbsp;&nbsp; | &nbsp;&nbsp; **Hints left:** {3 - st.session_state.hints_used}")

# ---- Current Question ----
q = st.session_state.questions[st.session_state.q_index]
st.subheader(q["question"])
selected = st.radio("Choose your answer:", q["choices"], key=f"q{st.session_state.q_index}")

# ---- Buttons ----
cols = st.columns([1, 1, 1])
with cols[0]:
    if st.button("✅ Submit Answer"):
        if selected == q["answer"]:
            points = 5 if st.session_state.used_hint_this_round else 10
            st.session_state.correct_streak += 1

            # Add streak bonus
            if st.session_state.correct_streak == 3:
                points += 5
                st.session_state.correct_streak = 0
                msg = f"🔥 Streak Bonus! +{points} points"
                color = "green"
            else:
                msg = f"✅ Correct! +{points} points"
                color = "green"

            st.session_state.score += points
        else:
            st.session_state.correct_streak = 0
            msg = f"❌ Wrong! Correct answer: **{q['answer']}**\n\n📘 {q['explanation']}"
            color = "red"

        st.session_state.show_feedback = True
        st.session_state.feedback_msg = msg
        st.session_state.feedback_color = color

with cols[1]:
    if st.button("💡 Hint"):
        if st.session_state.hints_used < 3:
            st.info(f"Hint: {q['hint']}")
            st.session_state.hints_used += 1
            st.session_state.used_hint_this_round = True
        else:
            st.warning("No more hints!")

with cols[2]:
    if st.button("⏭️ Next Question"):
        if st.session_state.q_index < len(st.session_state.questions) - 1:
            st.session_state.q_index += 1
            st.session_state.used_hint_this_round = False
            st.session_state.show_feedback = False
        else:
            st.session_state.started = False
            st.session_state.show_feedback = False
        st.experimental_rerun()

# ---- Feedback ----
if st.session_state.show_feedback:
    st.markdown(f"<span style='color:{st.session_state.feedback_color}; font-weight:bold'>{st.session_state.feedback_msg}</span>", unsafe_allow_html=True)

# ---- End of Quiz ----
if st.session_state.q_index == len(st.session_state.questions) - 1 and not st.session_state.started:
    st.subheader(f"🎉 Game Over! Your total score: **{st.session_state.score}**")

    st.markdown("### How was your experience?")
    cols = st.columns([1, 1, 1])
    with cols[0]:
        if st.button("😊 Good"):
            st.success("Thanks for your feedback: Good!")
    with cols[1]:
        if st.button("😐 Neutral"):
            st.info("Thanks for your feedback: Neutral")
    with cols[2]:
        if st.button("😞 Bad"):
            st.error("Thanks for your feedback: Bad")

    st.button("🔁 Restart Quiz", on_click=lambda: st.session_state.clear())



# In[ ]:




