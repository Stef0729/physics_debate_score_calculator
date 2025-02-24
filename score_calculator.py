import streamlit as st

# Streamlit UI
st.title("Final Score Calculator")

# Input fields
credit = st.number_input("Enter credit:", min_value=0.0, step=0.1)
scores_input = st.text_input("Enter scores (separated by spaces):")

if st.button("Calculate Final Score"):
    try:
        scores = list(map(int, scores_input.split()))
        if len(scores) < 5:
            st.error("Please enter at least 5 scores.")
        else:
            maxin = (max(scores) + min(scores)) / 2
            scores.remove(max(scores))
            scores.remove(min(scores))
            sum_scores = maxin + sum(scores[:3])  # Take first 3 after removing min/max
            final_score = (sum_scores / 4) * credit
            st.success(f"The final score is: {final_score:.2f}")
    except ValueError:
        st.error("Please enter valid numeric scores.")
