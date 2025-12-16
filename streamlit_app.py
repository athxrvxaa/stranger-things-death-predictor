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
    layout="wide"
)

st.title("☠️ Stranger Things: Death Probability Predictor")
st.caption("⚠️ Entertainment-only ML model (Logistic Regression)")

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

model = LogisticRegression()
model.fit(X, y)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.header("🎛️ Fan Voting Controls")

fan_bias = st.sidebar.slider(
    "Fan protection bias (← safer | danger →)",
    -0.30, 0.30, 0.0, 0.05
)

st.sidebar.markdown("""
**Model Info**
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
for idx, c in enumerate(results, start=1):
    col1, col2 = st.columns([1, 3])

    with col1:
        img = Image.open(c["image"])
        st.image(img, use_container_width=True)

    with col2:
        st.subheader(f"#{idx} — {c['name']}")

        bar = st.progress(0)
        for i in range(int(c["probability"] * 100)):
            time.sleep(0.008)
            bar.progress(i + 1)

        st.write(f"**Predicted Death Probability:** `{int(c['probability'] * 100)}%`")

    st.divider()
