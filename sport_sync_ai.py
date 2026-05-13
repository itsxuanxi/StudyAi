import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="SportSync AI",
    page_icon="⚡",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------- STYLE ----------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    max-width: 1200px;
}
.card {
    background: #ffffff;
    padding: 24px;
    border-radius: 20px;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.04);
}
.highlight {
    color: #2563eb;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
# ⚡ SportSync AI
### AI-powered social sports network for finding games, teammates, and active communities near you.

Stop asking random group chats.  
Get matched with the right people, right sport, right location, and right skill level.
""")

st.divider()

# ---------- USER INPUT ----------
col1, col2, col3 = st.columns(3)

with col1:
    sport = st.selectbox(
        "Sport",
        ["Basketball", "Soccer", "Tennis", "Volleyball", "Badminton", "Running", "Gym"]
    )

    skill = st.selectbox(
        "Skill Level",
        ["Beginner", "Casual", "Intermediate", "Advanced", "Competitive"]
    )

with col2:
    location = st.text_input(
        "Location",
        placeholder="e.g. McGill, Concordia, Downtown Montreal"
    )

    time = st.selectbox(
        "Availability",
        ["Today", "Tomorrow", "This weekend", "Weekday evenings", "Weekend mornings"]
    )

with col3:
    vibe = st.selectbox(
        "Game Vibe",
        ["Casual", "Competitive", "Social", "Training", "Beginner-friendly"]
    )

    goal = st.selectbox(
        "Your Goal",
        ["Find a game", "Find teammates", "Create a group", "Meet sporty friends", "Train consistently"]
    )

st.divider()

# ---------- FAKE DATABASE ----------
players = [
    {"name": "Alex", "sport": "Basketball", "skill": "Intermediate", "location": "McGill", "rating": "4.8", "vibe": "Competitive"},
    {"name": "Maya", "sport": "Basketball", "skill": "Casual", "location": "Concordia", "rating": "4.7", "vibe": "Social"},
    {"name": "Daniel", "sport": "Soccer", "skill": "Advanced", "location": "Downtown Montreal", "rating": "4.9", "vibe": "Competitive"},
    {"name": "Sophie", "sport": "Tennis", "skill": "Beginner", "location": "Parc Jeanne-Mance", "rating": "4.6", "vibe": "Beginner-friendly"},
    {"name": "Ryan", "sport": "Gym", "skill": "Intermediate", "location": "Concordia", "rating": "4.8", "vibe": "Training"},
]

games = [
    {"title": "McGill Basketball Run", "sport": "Basketball", "skill": "Intermediate", "location": "McGill Gym", "time": "Tomorrow", "spots": "3 spots left", "vibe": "Competitive"},
    {"title": "Concordia Casual Hoops", "sport": "Basketball", "skill": "Casual", "location": "Concordia Gym", "time": "Today", "spots": "4 spots left", "vibe": "Social"},
    {"title": "Downtown Soccer 5v5", "sport": "Soccer", "skill": "Advanced", "location": "McGill Lower Field", "time": "This weekend", "spots": "5 spots left", "vibe": "Competitive"},
    {"title": "Beginner Tennis Match", "sport": "Tennis", "skill": "Beginner", "location": "Parc Jeanne-Mance", "time": "This weekend", "spots": "1 spot left", "vibe": "Beginner-friendly"},
    {"title": "Evening Gym Partner Session", "sport": "Gym", "skill": "Intermediate", "location": "Concordia Fitness Centre", "time": "Weekday evenings", "spots": "2 spots left", "vibe": "Training"},
]

# ---------- FILTER ----------
matched_games = [
    g for g in games
    if g["sport"] == sport
    and (location == "" or location.lower() in g["location"].lower())
]

matched_players = [
    p for p in players
    if p["sport"] == sport
    and (location == "" or location.lower() in p["location"].lower())
]

# ---------- DASHBOARD ----------
m1, m2, m3, m4 = st.columns(4)
m1.metric("Matched Games", len(matched_games))
m2.metric("Matched Players", len(matched_players))
m3.metric("Avg Match Score", "87%")
m4.metric("Active Area", location if location else "Montreal")

st.divider()

# ---------- AI MATCHMAKING ----------
st.header("🤖 AI Matchmaking Recommendation")

if st.button("Generate AI Match Plan"):
    if location:
        with st.spinner("Finding your best sports matches..."):
            prompt = f"""
You are an AI matchmaking assistant for a social sports app.

User profile:
Sport: {sport}
Skill level: {skill}
Location: {location}
Availability: {time}
Game vibe: {vibe}
Goal: {goal}

Available games:
{games}

Available players:
{players}

Create a smart sports matchmaking plan with:

1. Best Game Recommendation
2. Best Player Type to Match With
3. Suggested Message to Join or Invite
4. Why this match makes sense
5. Safety / social advice
6. How to make this into a recurring sports group

Make it practical, premium, and startup-app style.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            st.markdown(response.choices[0].message.content)
    else:
        st.warning("Enter a location first.")

st.divider()

# ---------- GAME CARDS ----------
st.header("🔥 Recommended Games")

if matched_games:
    cols = st.columns(2)

    for i, game in enumerate(matched_games):
        with cols[i % 2]:
            st.markdown(f"""
<div class="card">
<h3>{game['title']}</h3>
<p><b>Sport:</b> {game['sport']}</p>
<p><b>Skill:</b> {game['skill']}</p>
<p><b>Location:</b> {game['location']}</p>
<p><b>Time:</b> {game['time']}</p>
<p><b>Vibe:</b> {game['vibe']}</p>
<p><span class="highlight">{game['spots']}</span></p>
</div>
""", unsafe_allow_html=True)
            st.button(f"Join {game['title']}", key=f"join_{i}")
else:
    st.warning("No matching games found. Try a broader location or different sport.")

st.divider()

# ---------- PLAYER CARDS ----------
st.header("👥 Matched Players")

if matched_players:
    cols = st.columns(3)

    for i, player in enumerate(matched_players):
        with cols[i % 3]:
            st.markdown(f"""
<div class="card">
<h3>{player['name']}</h3>
<p><b>Sport:</b> {player['sport']}</p>
<p><b>Skill:</b> {player['skill']}</p>
<p><b>Area:</b> {player['location']}</p>
<p><b>Vibe:</b> {player['vibe']}</p>
<p><b>Rating:</b> ⭐ {player['rating']}</p>
</div>
""", unsafe_allow_html=True)
            st.button(f"Invite {player['name']}", key=f"invite_{i}")
else:
    st.info("No matched players yet.")

st.divider()

# ---------- CREATE GAME ----------
st.header("➕ Create a New Game")

with st.form("create_game"):
    c1, c2 = st.columns(2)

    with c1:
        new_title = st.text_input("Game Title", placeholder="e.g. Friday Night Basketball Run")
        new_sport = st.selectbox("Sport Type", ["Basketball", "Soccer", "Tennis", "Volleyball", "Badminton", "Running", "Gym"])
        new_location = st.text_input("Game Location", placeholder="e.g. Concordia Gym")

    with c2:
        new_skill = st.selectbox("Required Skill Level", ["Beginner", "Casual", "Intermediate", "Advanced", "Competitive"])
        new_time = st.text_input("Game Time", placeholder="e.g. Friday 7 PM")
        new_spots = st.number_input("Players Needed", min_value=1, max_value=30, value=5)

    description = st.text_area("Game Description", placeholder="Describe the vibe, rules, and who should join.")

    submitted = st.form_submit_button("Create Game")

    if submitted:
        st.success("Game created! In a real product, this would be saved to a database.")

st.divider()

# ---------- STARTUP POSITIONING ----------
st.header("🚀 Product Vision")

st.markdown("""
SportSync AI is not just a sports meetup app.

It is an **AI-powered sports social network** that can evolve into:

- Player matching
- Recurring sports groups
- Campus sports communities
- Paid premium groups
- Court discovery
- Team formation
- Local sports marketplace
- Brand sponsorships
""")
