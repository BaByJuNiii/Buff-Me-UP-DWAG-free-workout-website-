import streamlit as st

# Set up page config
st.set_page_config(page_title="LET'S BUFF UP DAWG", page_icon="💪", layout="wide")

# ==========================================
# 🌌 STYLING ENGINE (CSS & Anime Magic)
# ==========================================

st.markdown(
    """
    <style>
    /* Main app container styling */
    .stApp {
        background-image: linear-gradient(rgba(10, 10, 30, 0.75), rgba(10, 10, 30, 0.75)), url("https://w.wallhaven.cc/full/8o/wallhaven-8ozmzo.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Center title header styling */
    .main-title {
        text-align: center;
        color: #FFFFFF;
        font-family: 'Impact', 'Arial Black', sans-serif;
        text-transform: uppercase;
        letter-spacing: 3px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.9);
        background-color: rgba(20, 20, 40, 0.85);
        padding: 25px;
        border-radius: 15px;
        border: 3px solid #5C19EB;
        margin-bottom: 25px;
        font-size: 2.5rem;
    }
    
    /* Welcome Note Banner Box */
    .welcome-banner {
        background-color: rgba(92, 25, 235, 0.2);
        border-left: 5px solid #33FF77;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 25px;
        color: #FFFFFF;
    }
    .welcome-banner h3 {
        color: #33FF77 !important;
        margin-top: 0;
    }
    .profile-links a {
        color: #33FF77 !important;
        text-decoration: none;
        font-weight: bold;
        margin-right: 15px;
    }
    .profile-links a:hover {
        text-decoration: underline;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(20, 20, 40, 0.95) !important;
        border-right: 2px solid #5C19EB;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    
    /* Neon green numbers for metrics */
    [data-testid="stMetricValue"] {
        color: #33FF77 !important;
        font-size: 2.2rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }
    [data-testid="stMetricLabel"] {
        color: #A0A0A0 !important;
    }
    
    /* Transparent aesthetic tab lists */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(20, 20, 40, 0.8) !important;
        border-radius: 10px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 📊 THE OPEN FITNESS MATH ENGINE
# ==========================================

def calculate_fitness_metrics(weight, height, age, gender, activity, deficit):
    # 1. BMI Calculation
    height_m = height / 100
    bmi = round(weight / (height_m ** 2), 1)
    if bmi < 18.5:
        bmi_cat = "Underweight"
    elif 18.5 <= bmi < 25:
        bmi_cat = "Normal weight"
    elif 25 <= bmi < 30:
        bmi_cat = "Overweight"
    else:
        bmi_cat = "Obese"
    
    # 2. Target Weight Calculation
    inches_over_5_ft = max(0, (height / 2.54) - 60)
    if gender == "Male":
        base_w = 50.0
    elif gender == "Female":
        base_w = 45.5
    else:
        base_w = 47.75
        
    ideal_w = round(base_w + (2.3 * inches_over_5_ft), 1)
    
    # 3. Calorie Deficit
    if gender == "Male":
        gender_offset = 5
    elif gender == "Female":
        gender_offset = -161
    else:
        gender_offset = -78
        
    bmr = (10 * weight) + (6.25 * height) - (5 * age) + gender_offset
    
    activity_multipliers = {
        "Sedentary (Little/no exercise)": 1.2,
        "Lightly Active (1-3 days/week)": 1.375,
        "Moderately Active (3-5 days/week)": 1.55,
        "Very Active (6-7 days/week)": 1.725
    }
    tdee = round(bmr * activity_multipliers[activity])
    target_calories = tdee - deficit
    
    # 4. Fat Intake Target
    target_fat_grams = round((target_calories * 0.25) / 9)
    
    # 5. Hydration Target
    water_liters = round((weight * 35) / 1000, 1)
    
    return bmi, bmi_cat, ideal_w, tdee, target_calories, target_fat_grams, water_liters


# ==========================================
# 🖥️ USER INTERFACE
# ==========================================

# --- Sidebar Inputs ---
st.sidebar.header("👋 Getting Started")
username_input = st.sidebar.text_input("What should we call you?", placeholder="Type your name here...")
username = username_input.strip() if username_input.strip() else "Dawg"

st.sidebar.markdown("---")
st.sidebar.header("👤 Personal Metrics")
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Intersex"])
age = st.sidebar.slider("Age (Years)", 1, 110, 25, step=1)
weight = st.sidebar.slider("Weight (kg)", 30.0, 300.0, 70.0, step=0.1, format="%.1f")
height = st.sidebar.slider("Height (cm)", 100, 250, 170, step=1)

st.sidebar.markdown("---")
st.sidebar.header("🎯 Goals & Routine")
activity = st.sidebar.selectbox("Your Activity Level", [
    "Sedentary (Little/no exercise)", 
    "Lightly Active (1-3 days/week)", 
    "Moderately Active (3-5 days/week)", 
    "Very Active (6-7 days/week)"
])
deficit_target = st.sidebar.slider("Target Calorie Deficit", 200, 1000, 500, step=50)


# Main Header
st.markdown('<div class="main-title">🔥 LET\'S BUFF UP DAWG 🔥</div>', unsafe_allow_html=True)

# Your Custom Welcome Note Block (LINKS UPDATED!)
st.markdown(
    f"""
    <div class="welcome-banner">
        <h3>HELLLLOOO CHINGUS!! 👋</h3>
        <p><strong>WELCOME TO THE DOJO, {username.upper()}!</strong> Junii here! Okay, I made this open source so everyone can enjoy it without paying anything and have a personal trainer in their devices! 🔥</p>
        <p>So enjoy this and follow me up for more projects:</p>
        <div class="profile-links">
            <a href="https://github.com/BaByJuNiii" target="_blank">🐙 GitHub</a>
            <a href="https://www.linkedin.com/in/junaydmsheikh" target="_blank">💼 LinkedIn</a>
        </div>
        <p style="margin-top: 15px; font-style: italic; color: #A0A0A0;">SIGNING OFF FOR NOW!</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# Calculate Results
bmi, bmi_cat, ideal_w, tdee, target_cal, target_fat, water = calculate_fitness_metrics(
    weight, height, age, gender, activity, deficit_target
)

# App Navigation Layout
tab1, tab2, tab3, tab4 = st.tabs(["📊 Body Composition", "🍎 Nutrition & Deficit", "⏳ Intermittent Fasting", "⚔️ Workout Splits"])

with tab1:
    st.header("Body Metrics & Composition")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Body Mass Index")
        st.metric("Your BMI", f"{bmi:.1f}")
        st.info(f"Classification: **{bmi_cat}**")
    with col2:
        st.subheader("Target Weight")
        st.metric("Target Weight", f"{ideal_w:.1f} kg")

with tab2:
    st.header("Energy & Macronutrient Engine")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("🔥 Calorie Strategy")
        st.metric("Maintenance (TDEE)", f"{tdee} kcal")
        st.metric("Weight Loss Target", f"{target_cal} kcal", delta=f"-{deficit_target} kcal")
    with col2:
        st.subheader("🥑 Macronutrients")
        st.metric("Daily Fat Target", f"{target_fat} g")
    with col3:
        st.subheader("💧 Hydration Targets")
        st.metric("Water Needed", f"{water:.1f} Liters")

with tab3:
    st.header("Intermittent Fasting Scheduler")
    fasting_style = st.selectbox("Select Your Fasting Window Schedule", [
        "16:8 (Lean Gains Protocol)", 
        "18:6 (Advanced Fasting Window)", 
        "20:4 (The Warrior Diet)", 
        "24-Hour Fast (Circadian Reset)"
    ])
    st.success(f"Active Routine Configured: **{fasting_style}**")

with tab4:
    st.header("⚔️ Anime Hypertrophy Workout Splits")
    st.write("Pick your program strategy and alternate weeks below to rotate variations and dodge growth plateaus.")
    
    # 1. Base Strategy Selection
    split_choice = st.selectbox("Choose Your Split Architecture", [
        "Push / Pull / Legs (PPL) - Hypertrophy King",
        "Upper / Lower - The Balanced Athlete",
        "The Arnold Split - Golden Era Volume",
        "Aesthetic Bodybuilding - Golden Ratio Symmetry ✨"
    ])
    
    # 2. Monthly Periodization Selector
    current_week = st.radio(
        "📆 Select Training Rotation Phase (Monthly Chart)",
        ["Weeks 1 & 3: Barbell & Strength Focus", "Weeks 2 & 4: Dumbbell & Deep Stretch Focus"],
        horizontal=True
    )
    
    st.markdown("---")
    
    # ==========================================
    # ROUTINE 1: PUSH / PULL / LEGS (PPL)
    # ==========================================
    if "Push / Pull / Legs" in split_choice:
        c1, c2, c3 = st.columns(3)
        if "Weeks 1 & 3" in current_week:
            with c1:
                st.markdown("### 🔥 Day 1: Push (Barbell Heavy)")
                st.write("1. **Incline Barbell Press:** 4 sets x 6-8 reps")
                st.write("2. **Flat Barbell Bench:** 3 sets x 8-10 reps")
                st.write("3. **Standing Overhead Press:** 3 sets x 8 reps")
                st.write("4. **Barbell Skullcrushers:** 3 sets x 10 reps")
                st.write("5. **Lateral Cable Raises:** 4 sets x 12 reps")
            with c2:
                st.markdown("### 🧬 Day 2: Pull (Width & Density)")
                st.write("1. **Conventional Deadlift:** 3 sets x 5 reps")
                st.write("2. **Weighted Pull-Ups:** 4 sets x 6-8 reps")
                st.write("3. **Barbell Bent-Over Rows:** 3 sets x 8-10 reps")
                st.write("4. **Barbell Bicep Curls:** 3 sets x 10 reps")
                st.write("5. **Rear Delt Face Pulls:** 4 sets x 15 reps")
            with c3:
                st.markdown("### 🦵 Day 3: Legs (Absolute Power)")
                st.write("1. **Barbell Back Squats:** 4 sets x 6-8 reps")
                st.write("2. **Romanian Deadlifts:** 3 sets x 8-10 reps")
                st.write("3. **Leg Press (Heavy Width):** 3 sets x 10-12 reps")
                st.write("4. **Lying Leg Curls:** 3 sets x 12 reps")
                st.write("5. **Standing Calf Raises:** 4 sets x 15 reps")
        else:
            with c1:
                st.markdown("### 🔥 Day 1: Push (Dumbbell & Stretch)")
                st.write("1. **Incline Dumbbell Press:** 4 sets x 8-10 reps")
                st.write("2. **Flat Dumbbell Flyes:** 3 sets x 10-12 reps")
                st.write("3. **Seated Dumbbell Shoulder Press:** 3 sets x 8-10 reps")
                st.write("4. **Overhead Dumbbell Extensions:** 3 sets x 12 reps")
                st.write("5. **Dumbbell Lateral Raises:** 4 sets x 15 reps")
            with c2:
                st.markdown("### 🧬 Day 2: Pull (Isolation & Squeeze)")
                st.write("1. **Chest-Supported Dumbbell Rows:** 4 sets x 8-10 reps")
                st.write("2. **Lat Pulldowns (Wide Grip):** 3 sets x 10-12 reps")
                st.write("3. **Single-Arm Dumbbell Rows:** 3 sets x 10 reps")
                st.write("4. **Incline Dumbbell Curls:** 3 sets x 10-12 reps")
                st.write("5. **Dumbbell Rear Delt Flyes:** 4 sets x 15 reps")
            with c3:
                st.markdown("### 🦵 Day 3: Legs (Quads & Deep Range)")
                st.write("1. **Bulgarian Split Squats (Dumbbell):** 3 sets x 8-10 reps each")
                st.write("2. **Dumbbell Romanian Deadlifts:** 3 sets x 10-12 reps")
                st.write("3. **Leg Extensions (Peak Squeeze):** 4 sets x 12-15 reps")
                st.write("4. **Seated Leg Curls:** 3 sets x 12 reps")
                st.write("5. **Seated Calf Raises:** 4 sets x 15 reps")

    # ==========================================
    # ROUTINE 2: UPPER / LOWER
    # ==========================================
    elif "Upper / Lower" in split_choice:
        c1, c2 = st.columns(2)
        if "Weeks 1 & 3" in current_week:
            with c1:
                st.markdown("### 🦾 Days 1 & 3: Upper Body (Barbell Foundations)")
                st.write("1. **Flat Barbell Bench Press:** 4 sets x 6-8 reps")
                st.write("2. **Barbell Pendlay Rows:** 4 sets x 6-8 reps")
                st.write("3. **Seated Barbell Overhead Press:** 3 sets x 8 reps")
                st.write("4. **Close-Grip Barbell Press:** 3 sets x 10 reps")
                st.write("5. **EZ-Bar Bicep Curls:** 3 sets x 10 reps")
            with c2:
                st.markdown("### 🦿 Days 2 & 4: Lower Body (Posterior Load)")
                st.write("1. **Barbell Back Squats:** 4 sets x 6-8 reps")
                st.write("2. **Barbell Romanian Deadlifts:** 4 sets x 8-10 reps")
                st.write("3. **Leg Press:** 3 sets x 10 reps")
                st.write("4. **Standing Calf Raises:** 4 sets x 12 reps")
                st.write("5. **Hanging Knee Raises:** 3 sets x Failure")
        else:
            with c1:
                st.markdown("### 🦾 Days 1 & 3: Upper Body (Dumbbell Hypertrophy)")
                st.write("1. **Incline Dumbbell Bench Press:** 4 sets x 8-10 reps")
                st.write("2. **One-Arm Dumbbell Rows:** 4 sets x 8-10 reps")
                st.write("3. **Dumbbell Lateral Raises:** 4 sets x 12-15 reps")
                st.write("4. **Incline Dumbbell Hammer Curls:** 3 sets x 10-12 reps")
                st.write("5. **Overhead Cable Tricep Extensions:** 3 sets x 12 reps")
            with c2:
                st.markdown("### 🦿 Days 2 & 4: Lower Body (Quad Isolation focus)")
                st.write("1. **Goblet Squats (Deep Depth):** 4 sets x 10-12 reps")
                st.write("2. **Lying Leg Curls:** 4 sets x 10-12 reps")
                st.write("3. **Dumbbell Walking Lunges:** 3 sets x 12 steps total")
                st.write("4. **Seated Calf Raises:** 4 sets x 15 reps")
                st.write("5. **Abdominal Cable Crunches:** 3 sets x 15 reps")

    # ==========================================
    # ROUTINE 3: THE ARNOLD SPLIT
    # ==========================================
    elif "Arnold Split" in split_choice:
        c1, c2, c3 = st.columns(3)
        if "Weeks 1 & 3" in current_week:
            with c1:
                st.markdown("### 🦁 Day 1: Chest & Back (Compound Supersets)")
                st.write("1. **Barbell Bench Press:** 4 sets x 6-8 reps")
                st.write("2. **Barbell Rows (Overhand):** 4 sets x 6-8 reps")
                st.write("3. **Incline Barbell Bench:** 3 sets x 8-10 reps")
                st.write("4. **Lat Pulldowns (Close Grip):** 3 sets x 10 reps")
                st.write("5. **Weighted Chest Dips:** 3 sets x 8-10 reps")
            with c2:
                st.markdown("### 🦅 Day 2: Shoulders & Arms (Mass Blocks)")
                st.write("1. **Standing Barbell OHP:** 4 sets x 6-8 reps")
                st.write("2. **Barbell Curls (Heavy):** 3 sets x 8 reps")
                st.write("3. **Lying EZ-Bar Extensions:** 3 sets x 10 reps")
                st.write("4. **Seated Dumbbell Lateral Raises:** 4 sets x 12 reps")
                st.write("5. **Hammer Cable Curls:** 3 sets x 12 reps")
            with c3:
                st.markdown("### 🪵 Day 3: Legs (Heavy Core)")
                st.write("1. **Barbell Back Squats:** 4 sets x 6-8 reps")
                st.write("2. **Conventional Deadlifts:** 3 sets x 5 reps")
                st.write("3. **Leg Press:** 3 sets x 10 reps")
                st.write("4. **Lying Leg Curls:** 3 sets x 12 reps")
                st.write("5. **Standing Calf Raises:** 4 sets x 15 reps")
        else:
            with c1:
                st.markdown("### 🦁 Day 1: Chest & Back (Dumbbell Pump Volume)")
                st.write("1. **Flat Dumbbell Press:** 4 sets x 8-10 reps")
                st.write("2. **Chest-Supported Dumbbell Rows:** 4 sets x 8-10 reps")
                st.write("3. **Incline Dumbbell Flyes:** 3 sets x 10-12 reps")
                st.write("4. **Straight-Arm Cable Pull-overs:** 3 sets x 12 reps")
                st.write("5. **Dumbbell Pullovers:** 3 sets x 10 reps")
            with c2:
                st.markdown("### 🦅 Day 2: Shoulders & Arms (Isolation Caps)")
                st.write("1. **Seated Dumbbell Shoulder Press:** 4 sets x 8-10 reps")
                st.write("2. **Incline Dumbbell Curls:** 3 sets x 10-12 reps")
                st.write("3. **Dumbbell Overhead Extensions:** 3 sets x 10-12 reps")
                st.write("4. **Cable Lateral Raises:** 4 sets x 15 reps")
                st.write("5. **Concentration Curls:** 3 sets x 12 reps")
            with c3:
                st.markdown("### 🪵 Day 3: Legs (Dumbbell Unilateral Load)")
                st.write("1. **Dumbbell Bulgarian Split Squats:** 3 sets x 10 reps each")
                st.write("2. **Dumbbell Romanian Deadlifts:** 3 sets x 10-12 reps")
                st.write("3. **Dumbbell Goblet Squats:** 3 sets x 12 reps")
                st.write("4. **Leg Extensions:** 4 sets x 15 reps")
                st.write("5. **Seated Calf Raises:** 4 sets x 15 reps")

    # ==========================================
    # ROUTINE 4: AESTHETIC BODYBUILDING
    # ==========================================
    elif "Aesthetic Bodybuilding" in split_choice:
        c1, c2, c3 = st.columns(3)
        st.info("✨ Golden Ratio Architecture: Prioritizing the V-Taper, deep muscle separations, and capped lateral delts.")
        if "Weeks 1 & 3" in current_week:
            with c1:
                st.markdown("### 📐 Day 1: Shoulders & Arms (V-Taper Framing)")
                st.write("1. **Seated Barbell Overhead Press:** 4 sets x 6-8 reps")
                st.write("2. **Leaning Cable Lateral Raises:** 4 sets x 12-15 reps")
                st.write("3. **EZ-Bar 21s (Bicep Shock):** 3 sets x 21 reps total")
                st.write("4. **Rope Tricep Pushdowns:** 4 sets x 12 reps")
                st.write("5. **Dumbbell Hammer Curls:** 3 sets x 10 reps")
            with c2:
                st.markdown("### 🔱 Day 2: Chest & Back (Upper Chest Illusion)")
                st.write("1. **Incline Barbell Bench Press:** 4 sets x 6-8 reps")
                st.write("2. **Wide-Grip Lat Pulldowns:** 4 sets x 8-10 reps")
                st.write("3. **Low-To-High Cable Flies:** 3 sets x 12 reps")
                st.write("4. **T-Bar Rows (Chest Supported):** 3 sets x 10 reps")
                st.write("5. **Straight-Arm Lat Pulldown:** 3 sets x 15 reps")
            with c3:
                st.markdown("### 🏛️ Day 3: Legs & Abs (Teardrop Sweep)")
                st.write("1. **Barbell Hack Squats:** 4 sets x 8-10 reps")
                st.write("2. **Romanian Deadlifts:** 3 sets x 8-10 reps")
                st.write("3. **Leg Extensions (3s peak pause):** 4 sets x 12 reps")
                st.write("4. **Seated Calf Raises:** 4 sets x 20 reps")
                st.write("5. **Hanging Leg Raises:** 4 sets x 15 reps")
        else:
            with c1:
                st.markdown("### 📐 Day 1: Shoulders & Arms (3D Caps & Peak)")
                st.write("1. **Dumbbell Arnold Press:** 4 sets x 8-10 reps")
                st.write("2. **Incline Dumbbell Lateral Raises:** 4 sets x 12 reps")
                st.write("3. **Incline Dumbbell Curls (Deep stretch):** 3 sets x 10-12 reps")
                st.write("4. **Overhead Single-Arm Cable Extension:** 4 sets x 12 reps")
                st.write("5. **Reverse Grip Cable Curls:** 3 sets x 15 reps")
            with c2:
                st.markdown("### 🔱 Day 2: Chest & Back (Symmetry & Striations)")
                st.write("1. **Incline Dumbbell Press (30° Angle):** 4 sets x 8-10 reps")
                st.write("2. **Close-Grip Seated Cable Rows:** 4 sets x 10 reps")
                st.write("3. **Flat Dumbbell Flyes:** 3 sets x 12 reps")
                st.write("4. **Single-Arm Lat Pulldown:** 3 sets x 10-12 reps")
                st.write("5. **Incline Dumbbell Pullovers:** 3 sets x 12 reps")
            with c3:
                st.markdown("### 🏛️ Day 3: Legs & Abs (Definition & Core)")
                st.write("1. **Leg Press (High & Narrow Foot Placement):** 4 sets x 10-12 reps")
                st.write("2. **Lying Leg Curls:** 4 sets x 12-15 reps")
                st.write("3. **Dumbbell Goblet Squats (Heels Elevated):** 3 sets x 12-15 reps")
                st.write("4. **Donkey Calf Raises:** 4 sets x 15 reps")
                st.write("5. **Ab Roller Wheels:** 3 sets x Failure")