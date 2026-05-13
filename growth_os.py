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
### AI Sales & Marketing Operating System

Generate ICP, positioning, cold outreach, ad angles, objection handling, and a mini go-to-market strategy.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    product = st.text_input("Product / Business", placeholder="e.g. AI study assistant for university students")
    audience = st.text_input("Target Customer", placeholder="e.g. university students, startup founders, restaurant owners")
    problem = st.text_area("Customer Problem", placeholder="What painful problem do they have?")
    offer = st.text_input("Main Offer", placeholder="e.g. save 5 hours per week, increase leads, reduce manual work")

with col2:
    price = st.text_input("Price / Offer Model", placeholder="e.g. $29/month, free trial, custom B2B pricing")
    channel = st.selectbox(
        "Main Growth Channel",
        ["LinkedIn", "Cold Email", "Instagram", "Landing Page", "Sales Call", "Paid Ads"]
    )
    tone = st.selectbox(
        "Brand Voice",
        ["Premium", "Founder-style", "Direct", "Luxury", "High-converting", "Professional"]
    )
    stage = st.selectbox(
        "Business Stage",
        ["Idea", "Prototype", "MVP", "Early Users", "Revenue", "Scaling"]
    )

st.divider()

if st.button("Generate Revenue System"):
    if product and audience and problem and offer:
        with st.spinner("Building your AI sales system..."):

            prompt = f"""
You are a world-class B2B SaaS growth strategist and sales copywriter.

Product:
{product}

Target Customer:
{audience}

Customer Problem:
{problem}

Main Offer:
{offer}

Price / Offer Model:
{price}

Growth Channel:
{channel}

Brand Voice:
{tone}

Business Stage:
{stage}

Create a premium AI Sales SaaS output with:

## 1. Positioning
Write a sharp positioning statement.

## 2. Ideal Customer Profile
Describe the best-fit customer.

## 3. Pain Points
List the strongest buying pains.

## 4. Value Proposition
Explain why this product matters.

## 5. Offer Angle
Create one strong offer angle.

## 6. Cold Outreach Message
Write a short high-converting outreach message for {channel}.

## 7. Follow-up Message
Write one follow-up message.

## 8. Objection Handling
Handle 3 common objections.

## 9. Landing Page Hero Section
Write:
- Headline
- Subheadline
- CTA button text

## 10. 3 Ad Angles
Create 3 marketing angles.

## 11. Sales Script
Write a short discovery call script.

## 12. Growth Experiments
Give 3 practical experiments to get first users.

Make it specific, premium, and startup-grade.
Avoid generic advice.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            result = response.choices[0].message.content

            st.markdown("## 🚀 Your Revenue System")
            st.markdown(result)

    else:
        st.warning("Please fill in product, target customer, problem, and offer.")
