import streamlit as st
import sentiment_extract.get_sentiment as gs

st.markdown("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢄⡲⠖⠛⠉⠉⠉⠉⠉⠙⠛⠿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⣡⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⣡⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⢡⣶⠏⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣶⣶⣶⣶⣦⣄⣸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠌⢀⣿⠏⠀⠀⠀⠀⠀⠀⠸⠿⠋⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⡼⢿⣦⣄⠠⠤⠐⠒⠒⠒⠢⠤⣄⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⣸⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⠠⠇⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠙⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣴⣁⠀⣀⣤⣴⣾⣿⣿⣿⣿⡿⢿⣿⣶⣄⠀⠀⠀⠀⠀⣿⣷⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡇⠘⠟⣻⣿⣧⠀⠀⠀⠀⢿⣿⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡿⠀⠀⠸⣿⠿⠋⠉⠁⠛⠻⠿⢿⣧⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠋⠁⠀⢀⣄⡀⠀⠀⠀⢀⣀⣤⣴⣿⣿⣧⠀⢀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⣿⠏⢀⠀⢀⡴⠿⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣇⠀⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⣿⣤⣿⣷⡈⠀⠀⠀⠙⠻⣿⣿⣿⣿⠿⠛⠛⣻⣿⣿⡄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠈⠋⢉⣠⣴⣾⣿⣿⣿⣿⣷⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⣿⣿⢻⡏⢹⠙⡆⠀⠀⠀⠒⠚⢛⣉⣉⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⡞⠁⠉⠀⠁⠀⣄⣀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣈⡛⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠛⠋⠉⠉⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣻⠿⠿⢿⣿⠿⠿⠋⠁⠀⠙⣿⡁⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠋⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣹⣦⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⣀⣼⣿⣄⣀⣀⡄⠀⣀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀
    ⠀⠀⠀⠀⠀⢰⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀
    ⠀⠀⠀⢀⣤⣤⣤⣶⣿⣿⣿⣿⠿⠿⠟⠋⢹⠇⠀⠀⢀⣼⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⢀⡏⠀⠀⢀⣾⠋⣹⣿⣿⣿⡟⠀⠀⣸⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
    ⢠⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⡼⠀⠀⢀⣾⠏⢀⣿⣿⣿⠋⠀⠀⣰⣿⣧⡀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
""")
st.title("VADER Sentiment Analysis")
st.write("(Valence Aware Dictionary and sEntiment Reasoner) model to analyze the sentiment of input text.")

st.subheader("Input a sentence to analyze sentiment")
text_input = st.text_area("Enter your text here:")

options = ["Subreddit", "Title", "Body"]
selected_option = st.selectbox("Select an option:", options)

if not text_input.strip():
    st.stop() 

# averages 1
if selected_option == "Subreddit":
    result = gs.main(selection=1, value=text_input)
    st.text(result)

# title_average 2
if selected_option == "Title":
    result = gs.main(selection=2, value=text_input)
    st.text(result)

# body_average 3
if selected_option == "Body(post)":
    result = gs.main(selection=3, value=text_input)
    st.text(result)

# st.write(f"Subreddit: {subreddit}")
