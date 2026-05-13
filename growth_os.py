import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="GrowthOS AI",
    page_icon="⚡",
    layout="wide"
)

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.markdown("""
# ⚡ GrowthOS AI
### AI Revenue Command Center for startup founders

Build your positioning, ICP, offer, outreach, landing page, sales script, pricing strategy, and go-to-market plan in one click.
""")

st.divider()

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ Control Panel")

mode = st.sidebar.selectbox(
    "Revenue Mode",
    [
        "Full Revenue System",
        "Cold Outreach Engine",
        "Landing Page Generator",
        "Sales Call Coach",
        "GTM Strategy",
        "Investor-style Business Review"
    ]
)

depth = st.sidebar.selectbox(
    "Output Depth",
    ["Fast", "Detailed", "Founder-Level", "Investor-Level"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Built as an AI SaaS Prototype")

# ---------- INPUT ----------
st.markdown("## 1. Business Input")

col1, col2, col3 = st.columns(3)

with col1:
    product = st.text_input(
        "Product / Business",
        placeholder="e.g. AI study assistant for university students"
    )

    customer = st.text_input(
        "Target Customer",
        placeholder="e.g. university students, startup founders, restaurants"
    )

    pain = st.text_area(
        "Customer Pain",
        placeholder="What painful problem do they have?"
    )

with col2:
    outcome = st.text_input(
        "Promised Outcome",
        placeholder="e.g. save 5 hours per week, get more leads, close more sales"
    )

    pricing = st.text_input(
        "Pricing Model",
        placeholder="e.g. $29/month, free trial, B2B custom pricing"
    )

    competitors = st.text_area(
        "Competitors / Alternatives",
        placeholder="e.g. Notion, ChatGPT, Canva, agencies, manual work"
    )

with col3:
    channel = st.selectbox(
        "Main Growth Channel",
        [
            "LinkedIn",
            "Cold Email",
            "Instagram",
            "TikTok",
            "Landing Page",
            "Sales Call",
            "Paid Ads",
            "Campus Ambassador",
            "Partnerships"
        ]
    )

    stage = st.selectbox(
        "Business Stage",
        [
            "Idea",
            "Prototype",
            "MVP",
            "Early Users",
            "First Revenue",
            "Scaling"
        ]
    )

    tone = st.selectbox(
        "Brand Voice",
        [
            "Premium",
            "Founder-style",
            "Direct",
            "Luxury",
            "YC-style",
            "High-converting",
            "Professional"
        ]
    )

st.divider()

# ---------- SCORECARD ----------
st.markdown("## 2. AI Business Scorecard")

if product and customer and pain and outcome:
    score = min(95, 55 + len(product) % 10 + len(customer) % 10 + len(pain) % 15 + len(outcome) % 10)
else:
    score = 0

m1, m2, m3, m4 = st.columns(4)

m1.metric("Market Clarity", f"{score}%")
m2.metric("Offer Strength", f"{max(score - 7, 0)}%")
m3.metric("GTM Readiness", f"{max(score - 12, 0)}%")
m4.metric("Revenue Potential", f"{max(score - 5, 0)}%")

st.divider()

# ---------- AI GENERATION ----------
st.markdown("## 3. Generate Revenue Assets")

if st.button("🚀 Build Full Growth System"):

    if product and customer and pain and outcome:

        with st.spinner("Building your AI revenue command center..."):

            prompt = f"""
You are a world-class AI revenue strategist, SaaS founder, GTM advisor, sales copywriter, and growth operator.

Business:
{product}

Target Customer:
{customer}

Customer Pain:
{pain}

Promised Outcome:
{outcome}

Pricing Model:
{pricing}

Competitors / Alternatives:
{competitors}

Growth Channel:
{channel}

Business Stage:
{stage}

Brand Voice:
{tone}

Selected Mode:
{mode}

Output Depth:
{depth}

Create an elite startup-grade Revenue Command Center.

Return the output with these sections:

# 1. Founder-Level Business Diagnosis
Analyze the business opportunity, weakness, market risk, and strongest angle.

# 2. Sharp Positioning
Give:
- One-line positioning
- Category
- Who it is for
- Who it is NOT for
- Why now

# 3. Ideal Customer Profile
Include:
- Best-fit user
- Buyer persona
- Pain intensity
- Buying trigger
- Where to find them
- What they already use

# 4. Pain Map
Create:
- Surface pain
- Deeper pain
- Emotional pain
- Business pain
- Urgency level

# 5. Offer Architecture
Create:
- Core offer
- Bonus
- Guarantee
- Risk reversal
- Pricing suggestion
- Free trial / demo strategy

# 6. Competitive Differentiation
Compare against existing alternatives.
Explain why someone would switch.

# 7. Landing Page System
Write:
- Hero headline
- Subheadline
- CTA
- 3 feature blocks
- 3 benefit blocks
- Social proof idea
- FAQ section

# 8. Cold Outreach System
Create:
- LinkedIn connection message
- LinkedIn DM
- Cold email
- Follow-up 1
- Follow-up 2
- Follow-up 3
- Breakup message

# 9. Sales Call Script
Create:
- Opening
- Discovery questions
- Pain questions
- Demo transition
- Closing line
- Objection handling

# 10. Objection Handling Matrix
Handle:
- Too expensive
- I need to think
- We already use something
- Not a priority
- Send me more info
- No budget

# 11. Content Strategy
Create:
- 10 LinkedIn post ideas
- 5 short-form video ideas
- 5 founder story angles
- 5 educational content angles

# 12. 14-Day GTM Plan
Day-by-day execution plan to get first users or booked calls.

# 13. Growth Experiments
Give 10 practical experiments ranked by:
- speed
- cost
- difficulty
- expected impact

# 14. KPI Dashboard
List:
- acquisition KPIs
- activation KPIs
- revenue KPIs
- retention KPIs
- sales KPIs

# 15. Investor-Style Verdict
Give:
- Strength score / 100
- Risk score / 100
- Most promising angle
- Biggest weakness
- Next best action

Make it specific, premium, practical, and not generic.
Write like a top 1% startup operator.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content

            st.markdown("## ⚡ AI Revenue Command Center")
            st.markdown(result)

    else:
        st.warning("Please fill in product, target customer, pain, and promised outcome.")

st.divider()

# ---------- EXTRA TOOLS ----------
st.markdown("## 4. Mini Tools")

tool_col1, tool_col2, tool_col3 = st.columns(3)

with tool_col1:
    st.markdown("""
    ### 🎯 ICP Builder
    Identify your best-fit customers and where to find them.
    """)

with tool_col2:
    st.markdown("""
    ### 📩 Outreach Engine
    Generate cold emails, LinkedIn DMs, and follow-ups.
    """)

with tool_col3:
    st.markdown("""
    ### 💰 Offer Optimizer
    Improve pricing, packaging, and conversion angle.
    """)

st.divider()

st.markdown("""
## 🚀 Product Vision

GrowthOS AI can become a real B2B AI SaaS for:

- startup founders
- freelancers
- sales teams
- agencies
- small businesses
- solopreneurs

It is not just a copy generator.  
It is an **AI Revenue Operating System**.
""")
