# ============================================================
# Stranger Things — Season 5 Volume 2 Survival Predictor
# Fan-theory ML simulation using Logistic Regression
# ============================================================

import streamlit as st
import numpy as np
import random
from PIL import Image
from sklearn.linear_model import LogisticRegression

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="Stranger Things S5 Vol. 2 Predictor",
    layout="wide"
)

st.title("☠️ Stranger Things — Season 5 Volume 2 Survival Predictor")

st.caption(
    "⚠️ Fan-theory based ML simulation for Season 5 Volume 2. "
    "Not official, not canon, purely for entertainment."
)

st.info(
    "This app simulates *possible* Season 5 Volume 2 outcomes using "
    "narrative risk factors like plot armor, danger exposure, and "
    "villain proximity. It does NOT use real scripts, leaks, or Netflix data."
)

# ------------------------------------------------------------
# EXPLANATION FUNCTION (FINAL SEASON LOGIC)
# ------------------------------------------------------------
def generate_reasons(c):
    reasons = []

    if c["powers"]:
        reasons.append("• Carries a major supernatural burden going into the final arc.")

    if c["danger_level"] >= 3:
        reasons.append("• Frequently placed on the frontline during Season 5 conflicts.")

    if c["villain_proximity"] >= 3:
        reasons.append("• Closely tied to Vecna / Upside Down endgame events.")

    if c["plot_armor"] >= 3:
        reasons.append("• Strong narrative protection for the series finale.")
    else:
        reasons.append("• Limited plot armor in a finale season raises fatal stakes.")

    return reasons[:3]

# ------------------------------------------------------------
# CHARACTER DATA (SEASON 5 CONTEXT)
# scale: 1 = low, 3 = high
# ------------------------------------------------------------
characters = [
    {
        "name": "Eleven",
        "powers": 1,
        "screen_time": 1,
        "fan_favorite": 1,
        "danger_level": 3,
        "plot_armor": 3,
        "villain_proximity": 3,
        "image": "images/eleven.jpg",
    },
    {
        "name": "Max Mayfield",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 0,
        "danger_level": 2,
        "plot_armor": 1,
        "villain_proximity": 3,
        "image": "images/max_mayfield.jpg",
    },
    {
        "name": "Steve Harrington",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 1,
        "danger_level": 2,
        "plot_armor": 2,
        "villain_proximity": 2,
        "image": "images/steve_harrington.jpg",
    },
    {
        "name": "Dustin Henderson",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 1,
        "danger_level": 1,
        "plot_armor": 3,
        "villain_proximity": 1,
        "image": "images/dustin_henderson.jpg",
    },
    {
        "name": "Jim Hopper",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 1,
        "danger_level": 3,
        "plot_armor": 2,
        "villain_proximity": 3,
        "image": "images/jim_hopper.jpg",
    },
    {
        "name": "Mike Wheeler",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 0,
        "danger_level": 1,
        "plot_armor": 2,
        "villain_proximity": 1,
        "image": "images/mike_wheeler.jpg",
    },
    {
        "name": "Lucas Sinclair",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 0,
        "danger_level": 2,
        "plot_armor": 1,
        "villain_proximity": 2,
        "image": "images/lucas_sinclair.jpg",
    },
    {
        "name": "Will Byers",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 1,
        "danger_level": 2,
        "plot_armor": 2,
        "villain_proximity": 3,
        "image": "images/will_byers.jpg",
    },
    {
        "name": "Robin Buckley",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 1,
        "danger_level": 1,
        "plot_armor": 2,
        "villain_proximity": 1,
        "image": "images/robin_buckley.jpg",
    },
    {
        "name": "Nancy Wheeler",
        "powers": 0,
        "screen_time": 1,
        "fan_favorite": 1,
        "danger_level": 2,
        "plot_armor": 2,
        "villain_proximity": 2,
        "image": "images/nancy_wheeler.jpg",
    },
]

# ------------------------------------------------------------
# TRAIN LOGISTIC REGRESSION (SYNTHETIC DATA)
# ------------------------------------------------------------
X, y = [], []

for _ in range(3000):
    powers = random.randint(0, 1)
    screen = random.randint(0, 1)
    fan = random.randint(0, 1)
    danger = random.randint(1, 3)
    armor = random.randint(1, 3)
    villain = random.randint(1, 3)

    risk_score = (
        powers * 0.6
        + danger * 0.8
        + villain * 0.9
        - armor * 1.0
        - fan * 0.5
        + random.uniform(-0.3, 0.3)
    )

    X.append([powers, screen, fan, danger, armor, villain])
    y.append(1 if risk_score > 1.5 else 0)

model = LogisticRegression()
model.fit(X, y)

# ------------------------------------------------------------
# SIDEBAR CONTROLS
# ------------------------------------------------------------
st.sidebar.header("🎛️ Finale Scenario Controls")

fan_bias = st.sidebar.slider(
    "Fan protection bias (← safer | darker ending →)",
    -0.30,
    0.30,
    0.0,
    0.05,
)

dark_ending = st.sidebar.checkbox("Enable Dark Ending Scenario", False)

if dark_ending:
    fan_bias -= 0.15

st.sidebar.caption(
    "Dark Ending = higher fatality risk, minimal plot armor."
)

# ------------------------------------------------------------
# PREDICTIONS
# ------------------------------------------------------------
results = []

for c in characters:
    features = np.array([[ 
        c["powers"],
        c["screen_time"],
        c["fan_favorite"],
        c["danger_level"],
        c["plot_armor"],
        c["villain_proximity"],
    ]])

    prob = model.predict_proba(features)[0][1]
    prob = max(0.05, min(prob + fan_bias, 0.95))

    results.append({**c, "probability": prob})

results.sort(key=lambda x: x["probability"], reverse=True)

# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------
st.header("📺 Season 5 Volume 2 — Predicted Risk Ranking")
st.markdown(
    "Final-season survival simulation based on character arcs, narrative stakes, "
    "and Upside Down endgame proximity."
)

for idx, c in enumerate(results, start=1):
    col1, col2 = st.columns([1, 3])

    with col1:
        try:
            img = Image.open(c["image"])
            st.image(img, use_container_width=True)
        except Exception:
            st.warning("Image not available")

    with col2:
        st.subheader(f"#{idx} — {c['name']}")

        st.progress(int(c["probability"] * 100))

        st.write(
            f"**Season 5 Vol. 2 Death Risk:** "
            f"`{int(c['probability'] * 100)}%`"
        )

        st.markdown("**Why this prediction:**")
        for reason in generate_reasons(c):
            st.write(reason)

    st.divider()
