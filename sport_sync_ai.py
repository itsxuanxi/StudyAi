import streamlit as st
from openai import OpenAI
import random

st.set_page_config(
    page_title="PulsePlay AI",
    page_icon="⚡",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ---------- STYLE ----------
st.markdown("""
<style>
.block-container {
    max-width: 1300px;
    padding-top: 1.5rem;
}

.hero {
    padding: 40px 0px;
}

.hero-title {
    font-size: 64px;
    font-weight: 800;
    line-height: 1;
}

.hero-sub {
    font-size: 22px;
    color: #6b7280;
    margin-top: 12px;
}

.card {
    background: white;
    padding: 24px;
    border-radius: 24px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    margin-bottom: 20px;
}

.metric-card {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    color: white;
    padding: 24px;
    border-radius: 22px;
}

.metric-number {
    font-size: 42px;
    font-weight: 800;
}

.metric-label {
    opacity: 0.9;
}

.section-title {
    font-size: 38px;
    font-weight: 700;
    margin-top: 20px;
    margin-bottom: 10px;
}

.small {
    color: #6b7280;
}

.game-title {
    font-size: 26px;
    font-weight: 700;
}

.player-name {
    font-size: 24px;
    font-weight: 700;
}

.ai-box {
    background: linear-gradient(135deg,#111827,#1f2937);
    color: white;
    padding: 30px;
    border-radius: 28px;
}

.tag {
    display:inline-block;
    padding:6px 14px;
    border-radius:999px;
    background:#eff6ff;
    color:#2563eb;
    font-weight:600;
    margin-right:8px;
    margin-top:8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
<div class="hero-title">
⚡ PulsePlay AI
</div>

<div class="hero-sub">
AI-powered sports social network for finding games, teammates, and active communities nearby.
</div>
</div>
""", unsafe_allow_html=True)

# ---------- TOP METRICS ----------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">12k+</div>
    <div class="metric-label">Active Players</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">840+</div>
    <div class="metric-label">Games This Week</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">92%</div>
    <div class="metric-label">Match Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
    <div class="metric-number">4.9★</div>
    <div class="metric-label">Community Rating</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# ---------- FILTERS ----------
st.markdown('<div class="section-title">Find Your Next Game</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    sport = st.selectbox(
        "Sport",
        ["Basketball", "Soccer", "Volleyball", "Tennis", "Running", "Gym"]
    )

    skill = st.selectbox(
        "Skill Level",
        ["Beginner", "Casual", "Intermediate", "Advanced", "Competitive"]
    )

with f2:
    location = st.text_input(
        "Location",
        placeholder="e.g. Downtown Montreal"
    )

    vibe = st.selectbox(
        "Game Vibe",
        ["Casual", "Competitive", "Social", "Training"]
    )

with f3:
    availability = st.selectbox(
        "Availability",
        ["Tonight", "Tomorrow", "Weekend", "Weekday Evenings"]
    )

    goal = st.selectbox(
        "Goal",
        ["Find Games", "Meet People", "Train", "Find Teammates"]
    )

# ---------- AI SECTION ----------
st.write("")
st.markdown("""
<div class="ai-box">
<h2>🤖 AI Matchmaking Engine</h2>

PulsePlay AI analyzes:
- skill compatibility
- game vibe
- location proximity
- activity level
- player reliability
- social compatibility

to recommend your best sports matches.
</div>
""", unsafe_allow_html=True)

st.write("")

if st.button("Generate AI Match Recommendations"):
    with st.spinner("Analyzing sports compatibility..."):

        prompt = f"""
You are an elite AI sports matchmaking system.

User:
Sport: {sport}
Skill: {skill}
Location: {location}
Vibe: {vibe}
Availability: {availability}
Goal: {goal}

Generate:

1. Best game recommendation
2. Best type of teammate
3. Ideal sports environment
4. One suggested message
5. One smart social tip
6. One growth idea for building a recurring sports community

Make it premium, modern, and startup-quality.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.markdown(response.choices[0].message.content)

# ---------- GAMES ----------
st.write("")
st.markdown('<div class="section-title">🔥 Trending Games Nearby</div>', unsafe_allow_html=True)

games = [
    {
        "title": "McGill Basketball Run",
        "location": "McGill Gym",
        "players": "12/15",
        "skill": "Intermediate",
        "vibe": "Competitive"
    },
    {
        "title": "Downtown Soccer 5v5",
        "location": "Montreal Downtown",
        "players": "8/10",
        "skill": "Casual",
        "vibe": "Social"
    },
    {
        "title": "Concordia Volleyball Night",
        "location": "Concordia Gym",
        "players": "14/18",
        "skill": "Beginner",
        "vibe": "Training"
    }
]

g1, g2, g3 = st.columns(3)

for col, game in zip([g1, g2, g3], games):
    with col:
        st.markdown(f"""
        <div class="card">
        <div class="game-title">{game['title']}</div>

        <div class="tag">{game['skill']}</div>
        <div class="tag">{game['vibe']}</div>

        <p class="small">
        📍 {game['location']}<br>
        👥 {game['players']} players joined
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Join Game", key=game["title"])

# ---------- PLAYERS ----------
st.write("")
st.markdown('<div class="section-title">👥 Suggested Players</div>', unsafe_allow_html=True)

players = [
    {
        "name": "Alex",
        "sport": "Basketball",
        "skill": "Intermediate",
        "rating": "4.9"
    },
    {
        "name": "Maya",
        "sport": "Soccer",
        "skill": "Casual",
        "rating": "4.8"
    },
    {
        "name": "Ryan",
        "sport": "Gym",
        "skill": "Advanced",
        "rating": "5.0"
    }
]

p1, p2, p3 = st.columns(3)

for col, player in zip([p1, p2, p3], players):
    with col:
        compatibility = random.randint(82, 98)

        st.markdown(f"""
        <div class="card">
        <div class="player-name">{player['name']}</div>

        <div class="tag">{player['sport']}</div>
        <div class="tag">{player['skill']}</div>

        <p class="small">
        ⭐ Rating: {player['rating']}<br>
        🤝 Compatibility: {compatibility}%
        </p>
        </div>
        """, unsafe_allow_html=True)

        st.button("Connect", key=player["name"])

# ---------- CREATE GAME ----------
st.write("")
st.markdown('<div class="section-title">➕ Create a Game</div>', unsafe_allow_html=True)

with st.form("create_game"):
    title = st.text_input("Game Title")
    place = st.text_input("Location")
    time = st.text_input("Time")
    description = st.text_area("Description")

    submit = st.form_submit_button("Create Game")

    if submit:
        st.success("Game created successfully.")

# ---------- FOOTER ----------
st.write("")
st.write("")
st.markdown("""
---
### 🚀 PulsePlay AI Vision

PulsePlay AI is building the future of:
- sports matchmaking
- active social networking
- local sports communities
- AI-powered teammate discovery
- real-world social experiences

Built as an AI SaaS prototype.
""")
