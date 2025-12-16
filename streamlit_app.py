<<<<<<< HEAD
# ============================================================
# Stranger Things: Death Probability Predictor
# Entertainment-only ML demo using Logistic Regression
# ============================================================

import streamlit as st
import numpy as np
import random
import time
from PIL import Image
from sklearn.linear_model import LogisticRegression

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="Stranger Things: Death Probability Predictor",
=======
import streamlit as st
import numpy as np
import time
import random
from sklearn.linear_model import LogisticRegression
from PIL import Image

# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Stranger Things Death Predictor",
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5
    layout="wide"
)

st.title("☠️ Stranger Things: Death Probability Predictor")
st.caption("⚠️ Entertainment-only ML model (Logistic Regression)")

<<<<<<< HEAD
# ------------------------------------------------------------
# GEN-ALPHA EXPLANATION FUNCTION
# ------------------------------------------------------------
def generate_reasons(c):
    reasons = []

    if c["powers"]:
        reasons.append("• Has OP powers, which puts them in danger basically every episode.")

    if c["danger_level"] >= 3:
        reasons.append("• Constantly does risky stuff — survival instincts are kinda questionable.")

    if c["villain_proximity"] >= 3:
        reasons.append("• Always way too close to the main villain. Huge red flag.")

    if c["plot_armor"] >= 3:
        reasons.append("• Heavy plot armor — writers might save them at the last second.")
    else:
        reasons.append("• Plot armor is weak… chances are looking sus.")

    return reasons[:3]

# ------------------------------------------------------------
# CHARACTER DATA (TOP 10 WITH VARIANCE)
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

for _ in range(2500):
    powers = random.randint(0, 1)
    screen = random.randint(0, 1)
    fan = random.randint(0, 1)
    danger = random.randint(1, 3)
    armor = random.randint(1, 3)
    villain = random.randint(1, 3)

    risk_score = (
        powers * 0.5
        + danger * 0.7
        + villain * 0.8
        - armor * 0.9
        - fan * 0.4
        + random.uniform(-0.3, 0.3)
    )

    X.append([powers, screen, fan, danger, armor, villain])
    y.append(1 if risk_score > 1.6 else 0)
=======
# -------------------------------------------------
# TOP 10 CHARACTERS
# -------------------------------------------------
characters = [
    {"name": "Eleven", "powers": 1, "screen_time": 1, "fan_favorite": 1, "image": "images/eleven.jpg"},
    {"name": "Max Mayfield", "powers": 0, "screen_time": 1, "fan_favorite": 0, "image": "images/max_mayfield.jpg"},
    {"name": "Steve Harrington", "powers": 0, "screen_time": 1, "fan_favorite": 1, "image": "images/steve_harrington.jpg"},
    {"name": "Dustin Henderson", "powers": 0, "screen_time": 1, "fan_favorite": 1, "image": "images/dustin_henderson.jpg"},
    {"name": "Jim Hopper", "powers": 0, "screen_time": 1, "fan_favorite": 1, "image": "images/jim_hopper.jpg"},
    {"name": "Mike Wheeler", "powers": 0, "screen_time": 1, "fan_favorite": 0, "image": "images/mike_wheeler.jpg"},
    {"name": "Lucas Sinclair", "powers": 0, "screen_time": 1, "fan_favorite": 0, "image": "images/lucas_sinclair.jpg"},
    {"name": "Will Byers", "powers": 0, "screen_time": 1, "fan_favorite": 1, "image": "images/will_byers.jpg"},
    {"name": "Robin Buckley", "powers": 0, "screen_time": 1, "fan_favorite": 1, "image": "images/robin_buckley.jpg"},
    {"name": "Nancy Wheeler", "powers": 0, "screen_time": 1, "fan_favorite": 1, "image": "images/nancy_wheeler.jpg"},
]

# -------------------------------------------------
# Train ML model (synthetic data)
# -------------------------------------------------
X, y = [], []

for _ in range(1000):
    powers = random.randint(0, 1)
    screen = random.randint(0, 1)
    fan = random.randint(0, 1)

    risk = powers * 0.45 + screen * 0.25 - fan * 0.35 + random.uniform(-0.1, 0.1)
    X.append([powers, screen, fan])
    y.append(1 if risk > 0.4 else 0)
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5

model = LogisticRegression()
model.fit(X, y)

<<<<<<< HEAD
# ------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------
=======
# -------------------------------------------------
# Sidebar
# -------------------------------------------------
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5
st.sidebar.header("🎛️ Fan Voting Controls")

fan_bias = st.sidebar.slider(
    "Fan protection bias (← safer | danger →)",
<<<<<<< HEAD
    -0.30,
    0.30,
    0.0,
    0.05,
=======
    -0.30, 0.30, 0.0, 0.05
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5
)

st.sidebar.markdown("""
**Model Info**
<<<<<<< HEAD
- Logistic Regression  
- Expanded feature space  
- Synthetic training data  
- Animated probabilities  
""")

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
    prob = max(0.03, min(prob + fan_bias, 0.95))

    results.append({**c, "probability": prob})

results.sort(key=lambda x: x["probability"], reverse=True)

# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------
=======
- Logistic Regression
- Animated probabilities
""")

# -------------------------------------------------
# Predictions
# -------------------------------------------------
results = []

for c in characters:
    features = np.array([[c["powers"], c["screen_time"], c["fan_favorite"]]])
    prob = model.predict_proba(features)[0][1]
    prob = max(0.05, min(prob + fan_bias, 0.95))

    results.append({**c, "probability": prob})

results = sorted(results, key=lambda x: x["probability"], reverse=True)

# -------------------------------------------------
# Display
# -------------------------------------------------
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5
for idx, c in enumerate(results, start=1):
    col1, col2 = st.columns([1, 3])

    with col1:
<<<<<<< HEAD
        try:
            img = Image.open(c["image"])
            st.image(img, use_container_width=True)
        except Exception as e:
            st.error(f"Image error: {e}")
=======
        img = Image.open(c["image"])
        st.image(img, use_container_width=True)
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5

    with col2:
        st.subheader(f"#{idx} — {c['name']}")

        bar = st.progress(0)
        for i in range(int(c["probability"] * 100)):
<<<<<<< HEAD
            time.sleep(0.004)
=======
            time.sleep(0.008)
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5
            bar.progress(i + 1)

        st.write(f"**Predicted Death Probability:** `{int(c['probability'] * 100)}%`")

<<<<<<< HEAD
        st.markdown("**Why this prediction:**")
        for reason in generate_reasons(c):
            st.write(reason)

=======
>>>>>>> 03f75abbb2abe17cf6461b01b37d615d3ee336e5
    st.divider()
