import streamlit as st
from utils import predict
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Eye Disease AI", page_icon="👁️", layout="wide")

# --- UI Styling (Advanced Glassmorphism) ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(145deg, #e0eafc 0%, #cfdef3 100%); }
    .main-card {
        background: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.15);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin-bottom: 20px;
    }
    .disease-tag {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 15px;
        background: #e1f5fe;
        color: #01579b;
        font-size: 0.8rem;
        font-weight: bold;
        margin: 5px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background: linear-gradient(45deg, #2193b0, #6dd5ed);
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #1a2a6c; font-family: sans-serif;'>✨ Eye Disease AI Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #555;'>Smart Screening for a Clearer Vision</p>", unsafe_allow_html=True)

# --- Sidebar: Pyari Identification Guide ---
with st.sidebar:
    st.markdown("### 📚 Disease Guide")
    
    # Disease 1
    st.markdown("---")
    st.image("https://cdn-icons-png.flaticon.com/512/822/822102.png", width=50) # Cute icon
    st.markdown("**Cataract (मोतियाबिंद)**")
    st.caption("Clouding of the lens. It's like looking through a frosty window.")
    
    # Disease 2
    st.markdown("---")
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063205.png", width=50)
    st.markdown("**Glaucoma (काला मोतिया)**")
    st.caption("Damage to the optic nerve, often due to high eye pressure.")
    
    # Disease 3
    st.markdown("---")
    st.image("https://cdn-icons-png.flaticon.com/512/10059/10059345.png", width=50)
    st.markdown("**Diabetic Retinopathy**")
    st.caption("Caused by high blood sugar levels damaging retinal blood vessels.")
    
    st.divider()
    st.success("Normal: Eye is healthy! ✨")

# --- Main Layout ---
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown("### 📤 Step 1: Upload Scan")
    uploaded_file = st.file_uploader("Drop your retinal image here", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Retinal Scan", use_column_width=True)
    else:
        st.info("Awaiting file upload...")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown("### 🧠 Step 2: AI Diagnosis")
    
    if uploaded_file:
        if st.button("RUN DEEP ANALYSIS ✨"):
            with st.spinner('Neural Network is scanning layers...'):
                result, confidence = predict(image)
                
                if "Error" in result:
                    st.error(result)
                else:
                    # ✅ FIXED: Simple IF condition for balloons
                    if result == "Normal":
                        st.balloons()
                    
                    st.markdown(f"""
                        <div style="text-align: center; padding: 20px; border-radius: 15px; background: white; border: 1px solid #ddd;">
                            <p style="color: #666; margin-bottom: 5px;">Primary Identification</p>
                            <h1 style="color: #1a2a6c; margin-top: 0;">{result}</h1>
                            <div style="background: #f0f0f0; border-radius: 10px; padding: 10px;">
                                <span style="font-weight: bold; color: #2193b0;">Accuracy Score: {confidence * 100:.1f}%</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    st.progress(confidence)
                    
                    if result != "Normal":
                        st.warning(f"**Recommendation:** High risk of {result} detected. Please schedule an appointment with an Ophthalmologist.")
                    else:
                        st.success("Great! Your scan appears to be within normal parameters.")
    else:
        st.write("Upload an image to unlock AI analysis.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- Interactive Footer ---
st.markdown("<br><center><p style='color: #888;'>Designed with ❤️ for Eye_Disease_Detection| v3.0 Pro</p></center>", unsafe_allow_html=True)