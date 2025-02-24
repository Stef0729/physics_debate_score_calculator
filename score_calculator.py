import streamlit as st

# Streamlit UI
st.title("Physics Fight Score Calculator")

# Function to calculate the final score for each section
def calculate_final_score(scores, credit):
    try:
        scores = list(map(int, scores.split()))
        if len(scores) < 5:
            return "Enter at least 5 scores"
        maxin = (max(scores) + min(scores)) / 2
        scores.remove(max(scores))
        scores.remove(min(scores))
        sum_scores = maxin + sum(scores[:3])  # Take first 3 after removing min/max
        final_score = (sum_scores / 4) * credit
        return round(final_score, 1)
    except ValueError:
        return "Invalid input"

# Reporter Section
st.header("Reporter")
reporter_scores = st.text_input("Enter 5 scores for the Reporter (space-separated):")
reporter_final = calculate_final_score(reporter_scores, 3)

# Opponent Section
st.header("Opponent")
opponent_scores = st.text_input("Enter 5 scores for the Opponent (space-separated):")
opponent_final = calculate_final_score(opponent_scores, 2)

# Reviewer Section
st.header("Reviewer")
reviewer_scores = st.text_input("Enter 5 scores for the Reviewer (space-separated):")
reviewer_final = calculate_final_score(reviewer_scores, 1)

# Calculate total final score
if st.button("Calculate Final Score"):
    if isinstance(reporter_final, float) and isinstance(opponent_final, float) and isinstance(reviewer_final, float):
        total_score = round(reporter_final + opponent_final + reviewer_final, 1)
        st.success(f"Total Physics Fight Score: {total_score}")
    else:
        st.error("Please enter valid scores for all sections.")
