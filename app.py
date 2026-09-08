import streamlit as st

# ---------------------------------------------------------
# Page Configuration & Design System
# ---------------------------------------------------------
st.set_page_config(
    page_title="UDYAMPRAGYA — Rural Business Advisory Portal",
    page_icon="🌾",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, high-contrast, official theme
st.markdown(
    """
    <style>
    /* Hide Streamlit default chrome elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Container & Background */
    .stApp {
        background-color: #F4F6F8 !important;
        color: #1A1A1A !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    .main .block-container {
        max-width: 600px;
        padding-top: 1rem;
        padding-bottom: 3rem;
    }
    
    /* All headings force #0B2E59 */
    h1, h2, h3, h4, h5, h6, .step-heading {
        color: #0B2E59 !important;
        font-weight: 700 !important;
    }
    
    /* All body text force #1A1A1A */
    p, span, div, .stMarkdown, .stText {
        color: #1A1A1A;
    }
    
    /* Tricolor Top Accent Bar */
    .tricolor-bar {
        height: 6px;
        width: 100%;
        background: linear-gradient(to right, #E67E22 0%, #E67E22 33.3%, #FFFFFF 33.3%, #FFFFFF 66.6%, #1E8449 66.6%, #1E8449 100%);
        border-radius: 4px;
        margin-bottom: 18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Header Component (#0B3D91 background, #FFFFFF header text) */
    .official-header {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 14px;
        padding: 14px 18px;
        background: #0B3D91 !important;
        color: #FFFFFF !important;
        border-radius: 12px;
        border: 1px solid #0B2E59;
        box-shadow: 0 4px 12px rgba(11, 61, 145, 0.15);
        margin-bottom: 24px;
    }
    .emblem-icon {
        width: 48px;
        height: 48px;
        border-radius: 50%;
        background: #FFFFFF;
        color: #0B3D91;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        border: 2px solid #E6A817;
        flex-shrink: 0;
    }
    .header-titles {
        text-align: left;
    }
    .header-main-title {
        font-size: 22px !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        letter-spacing: 1px;
        margin: 0 !important;
        line-height: 1.1 !important;
    }
    .header-tagline {
        font-size: 13px !important;
        font-weight: 600 !important;
        color: #FFFFFF !important;
        margin-top: 2px !important;
        margin-bottom: 0 !important;
        opacity: 0.95;
    }
    
    /* Card Container (#FFFFFF background, #D0D5DA border) */
    .step-card {
        background-color: #FFFFFF !important;
        border-radius: 14px;
        padding: 24px 20px;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
        border: 1px solid #D0D5DA !important;
        margin-bottom: 20px;
    }
    
    /* Step Badge (#E6A817 background, #0B2E59 text) */
    .step-badge {
        display: inline-block;
        background-color: #E6A817 !important;
        color: #0B2E59 !important;
        font-weight: 800 !important;
        font-size: 12px;
        padding: 6px 12px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
    }
    
    /* Headings (#0B2E59) & Subtitles (#4A4A4A) */
    .step-heading {
        color: #0B2E59 !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        margin-top: 0;
        margin-bottom: 6px;
    }
    .step-description {
        color: #4A4A4A !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    
    /* Greeting Banner */
    .greeting-banner {
        background: #EBF3FA !important;
        border-left: 4px solid #0B3D91 !important;
        padding: 14px 18px;
        border-radius: 8px;
        color: #0B2E59 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        margin-bottom: 20px;
        border-top: 1px solid #D0D5DA;
        border-right: 1px solid #D0D5DA;
        border-bottom: 1px solid #D0D5DA;
    }
    
    /* Summary Box */
    .summary-card {
        background: #FFFFFF !important;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #D0D5DA !important;
        margin-bottom: 20px;
    }
    .summary-title {
        font-size: 13px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #4A4A4A !important;
        font-weight: 700 !important;
        margin-bottom: 8px;
    }
    .summary-content {
        font-size: 18px !important;
        font-weight: 700 !important;
        color: #0B2E59 !important;
        line-height: 1.4;
    }
    .feasibility-badge {
        background: #FFF8E7 !important;
        border: 1px solid #E6A817 !important;
        color: #0B2E59 !important;
        padding: 14px 18px;
        border-radius: 10px;
        font-size: 15px !important;
        font-weight: 700 !important;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Helper styling for category note (#4A4A4A) */
    .category-note {
        font-size: 13px !important;
        color: #4A4A4A !important;
        margin-top: -8px;
        margin-bottom: 14px;
        font-weight: 500 !important;
    }
    
    /* Buttons (#C0392B background, #FFFFFF text) */
    div.stButton > button {
        background-color: #C0392B !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        transition: all 0.2s ease-in-out !important;
        box-shadow: 0 2px 5px rgba(192, 57, 43, 0.2) !important;
    }
    div.stButton > button:hover {
        background-color: #A93226 !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 10px rgba(169, 50, 38, 0.3) !important;
    }
    div.stButton > button[kind="secondary"] {
        background-color: #FFFFFF !important;
        color: #0B2E59 !important;
        border: 2px solid #D0D5DA !important;
        font-weight: 700 !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        background-color: #F4F6F8 !important;
        color: #0B3D91 !important;
        border-color: #0B3D91 !important;
    }

    /* Form Input & Selectbox Label Styling (#0B2E59) */
    .stTextInput label, .stNumberInput label, .stSelectbox label, label {
        color: #0B2E59 !important;
        font-weight: 700 !important;
        font-size: 15px !important;
    }
    
    /* Input Fields (Text & Number Input) */
    div[data-baseweb="input"] input {
        color: #1A1A1A !important;
        background-color: #FFFFFF !important;
    }

    /* Closed Selectbox Box (Input State) */
    div[data-baseweb="select"],
    div[data-baseweb="select"] > div,
    select {
        background-color: #FFFFFF !important;
        color: #1A1A1A !important;
        border-color: #D0D5DA !important;
    }

    div[data-baseweb="select"] span,
    div[data-baseweb="select"] div,
    div[data-baseweb="select"] svg {
        color: #1A1A1A !important;
        fill: #1A1A1A !important;
    }

    /* Open Dropdown Container (Listbox / Popover / Menu) */
    div[data-baseweb="popover"],
    div[data-baseweb="popover"] > div,
    div[data-baseweb="menu"],
    ul[role="listbox"] {
        background-color: #FFFFFF !important;
        border: 1px solid #D0D5DA !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12) !important;
    }

    /* Option Items in List (Unselected & Default State) */
    li[role="option"],
    div[role="option"],
    ul[role="listbox"] li,
    div[data-baseweb="menu"] div,
    div[data-baseweb="menu"] span,
    select option,
    option {
        background-color: #FFFFFF !important;
        color: #0B2E59 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }

    /* Selected / Hovered Option Items */
    li[role="option"]:hover,
    li[role="option"][aria-selected="true"],
    div[role="option"]:hover,
    div[role="option"][aria-selected="true"],
    ul[role="listbox"] li:hover,
    div[data-baseweb="menu"] div:hover,
    div[data-baseweb="menu"] [aria-selected="true"],
    select option:hover,
    select option:focus,
    select option:checked,
    option:hover,
    option:focus,
    option:checked {
        background-color: #E6A817 !important;
        color: #0B2E59 !important;
        font-weight: 700 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# Translations Data Structure
# ---------------------------------------------------------
TRANSLATIONS = {
    "en": {
        "step3_title": "Personal Details",
        "step3_subtitle": "Please share your basic details to get started",
        "name_label": "Full Name",
        "name_placeholder": "e.g., Ramesh Patil",
        "age_label": "Age (Years)",
        "category_label": "Category / Caste Section",
        "category_purpose": "(used only to check government scheme eligibility)",
        "category_options": ["-- Select Category --", "General", "OBC", "SC", "ST", "Other"],
        "greeting_fmt": "Welcome, {name}! 🙏",
        "step4_title": "Capital & Location Details",
        "step4_subtitle": "Specify your available capital and business location",
        "capital_label": "Capital Amount (₹)",
        "district_label": "District",
        "taluk_label": "Taluk",
        "hobli_label": "Hobli",
        "village_label": "Village",
        "step5_title": "Confirmation & Review",
        "step5_subtitle": "Review your onboarding information below",
        "summary_heading": "Location & Investment Summary",
        "summary_fmt": "{village}, {taluk} taluk, Kalaburagi — capital ₹{capital}",
        "feasibility_msg": "Generating your feasibility report next...",
        "btn_continue": "Continue ➔",
        "btn_back": "⬅ Back",
        "btn_get_started": "Get Started ➔",
        "err_fill_all": "Please complete all required fields before continuing.",
        "err_lang": "Please select a language before proceeding.",
        "err_capital": "Please enter a valid capital amount greater than ₹0."
    },
    "hi": {
        "step3_title": "व्यक्तिगत विवरण",
        "step3_subtitle": "شروع करने के लिए कृपया अपना मूल विवरण दर्ज करें",
        "name_label": "पूरा नाम",
        "name_placeholder": "जैसे: रमेश पाटिल",
        "age_label": "आयु (वर्ष)",
        "category_label": "वर्ग / जाति अनुभाग",
        "category_purpose": "(केवल सरकारी योजना पात्रता जांचने के लिए उपयोग किया जाता है)",
        "category_options": ["-- वर्ग चुनें --", "सामान्य (General)", "अन्य पिछड़ा वर्ग (OBC)", "अनुसूचित जाति (SC)", "अनुसूचित जनजाति (ST)", "अन्य (Other)"],
        "greeting_fmt": "स्वागत है, {name}! 🙏",
        "step4_title": "पूंजी और स्थान विवरण",
        "step4_subtitle": "अपनी उपलब्ध पूंजी और व्यावसायिक स्थान का चयन करें",
        "capital_label": "पूंजी राशि (₹)",
        "district_label": "जिला",
        "taluk_label": "तालुका",
        "hobli_label": "होबली",
        "village_label": "गाँव",
        "step5_title": "पुष्टि और समीक्षा",
        "step5_subtitle": "नीचे दिए गए अपने ऑनबोर्डिंग विवरण की जांच करें",
        "summary_heading": "स्थान और निवेश सारांश",
        "summary_fmt": "{village}, {taluk} तालुका, कलबुर्गी — पूंजी ₹{capital}",
        "feasibility_msg": "आपकी व्यवहार्यता रिपोर्ट आगे तैयार की जा रही है...",
        "btn_continue": "आगे बढ़ें ➔",
        "btn_back": "⬅ पीछे",
        "btn_get_started": "शुरू करें ➔",
        "err_fill_all": "कृपया आगे बढ़ने से पहले सभी आवश्यक फ़ील्ड भरें।",
        "err_lang": "कृपया आगे बढ़ने से पहले एक भाषा का चयन करें।",
        "err_capital": "कृपया ₹0 से अधिक की मान्य पूंजी राशि दर्ज करें।"
    },
    "kn": {
        "step3_title": "ವೈಯಕ್ತಿಕ ವಿವರಗಳು",
        "step3_subtitle": "ಪ್ರಾರಂಭಿಸಲು ದಯವಿಟ್ಟು ನಿಮ್ಮ ಮೂಲ ವಿವರಗಳನ್ನು ನೀಡಿ",
        "name_label": "ಪೂರ್ಣ ಹೆಸರು",
        "name_placeholder": "ಉದಾ: ರಮೇಶ್ ಪಾಟೀಲ್",
        "age_label": "ವಯಸ್ಸು (ವರ್ಷಗಳು)",
        "category_label": "ವರ್ಗ / ಜಾತಿ ವಿಭಾಗ",
        "category_purpose": "(ಸರ್ಕಾರಿ ಯೋಜನೆಯ ಅರ್ಹತೆಯನ್ನು ಪರಿಶೀಲಿಸಲು ಮಾತ್ರ ಬಳಸಲಾಗುತ್ತದೆ)",
        "category_options": ["-- ವರ್ಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ --", "ಸಾಮಾನ್ಯ (General)", "ಒಬಿಸಿ (OBC)", "ಎಸ್‌ಸಿ (SC)", "ಎಸ್‌ಟಿ (ST)", "ಇತರೆ (Other)"],
        "greeting_fmt": "ಸ್ವಾಗತ, {name}! 🙏",
        "step4_title": "ಬಂಡವಾಳ ಮತ್ತು ಸ್ಥಳದ ವಿವರಗಳು",
        "step4_subtitle": "ನಿಮ್ಮ ಲಭ್ಯವಿರುವ ಬಂಡವಾಳ ಮತ್ತು ವ್ಯವಹಾರದ ಸ್ಥಳವನ್ನು ನಮೂದಿಸಿ",
        "capital_label": "ಬಂಡವಾಳದ ಮೊತ್ತ (₹)",
        "district_label": "ಜಿಲ್ಲೆ",
        "taluk_label": "ತಾಲೂಕು",
        "hobli_label": "ಹೋಬಳಿ",
        "village_label": "ಗ್ರಾಮ",
        "step5_title": "ದೃಢೀಕರಣ ಮತ್ತು ಪರಿಶೀಲನೆ",
        "step5_subtitle": "ನಿಮ್ಮ ವಿವರಗಳನ್ನು ಕೆಳಗೆ ಪರಿಶೀಲಿಸಿ",
        "summary_heading": "ಸ್ಥಳ ಮತ್ತು ಹೂಡಿಕೆ ಸಾರಾಂಶ",
        "summary_fmt": "{village}, {taluk} ತಾಲೂಕು, ಕಲಬುರಗಿ — ಬಂಡವಾಳ ₹{capital}",
        "feasibility_msg": "ನಿಮ್ಮ ಸಾಧ್ಯತಾ ವರದಿಯನ್ನು ಮುಂದೆ ರಚಿಸಲಾಗುತ್ತಿದೆ...",
        "btn_continue": "ಮುಂದುವರಿಸಿ ➔",
        "btn_back": "⬅ ಹಿಂತಿರುಗಿ",
        "btn_get_started": "ಪ್ರಾರ೦ಭಿಸಿ ➔",
        "err_fill_all": "ದಯವಿಟ್ಟು ಮುಂದುವರಿಯುವ ಮೊದಲು ಎಲ್ಲಾ ಅಗತ್ಯ ಕ್ಷೇತ್ರಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ.",
        "err_lang": "ಮುಂದುವರಿಯಲು ದಯವಿಟ್ಟು ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "err_capital": "ದಯವಿಟ್ಟು ₹0 ಗಿಂತ ಹೆಚ್ಚಿನ ಸಿಂಧುವಾದ ಬಂಡವಾಳದ ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ."
    },
    "te": {
        "step3_title": "వ్యక్తిగత వివరాలు",
        "step3_subtitle": "ప్రారంభించడానికి దయచేసి మీ ప్రాథమిక వివరాలను తెలియజేయండి",
        "name_label": "పూర్తి పేరు",
        "name_placeholder": "ఉదా: రమేష్ పాటిల్",
        "age_label": "వయస్సు (సంవత్సరాలు)",
        "category_label": "వర్గం / కుల విభాగం",
        "category_purpose": "(ప్రభుత్వ పథకం అర్హతను తనిఖీ చేయడానికి మాత్రమే ఉపయోగించబడుతుంది)",
        "category_options": ["-- వర్గాన్ని ఎంచుకోండి --", "జనరల్ (General)", "ఒబిసి (OBC)", "ఎస్సీ (SC)", "ఎస్టీ (ST)", "ఇతర (Other)"],
        "greeting_fmt": "స్వాగతం, {name}! 🙏",
        "step4_title": "మూలధనం మరియు ప్రాంతం వివరాలు",
        "step4_subtitle": "మీ పెట్టుబడి మూలధనం మరియు వ్యాపార ప్రాంతాన్ని పేర్కొనండి",
        "capital_label": "మూలధన మొత్తం (₹)",
        "district_label": "జిల్లా",
        "taluk_label": "తాలూకా",
        "hobli_label": "హోబ్లి",
        "village_label": "గ్రామం",
        "step5_title": "నిర్ధారణ మరియు సమీక్ష",
        "step5_subtitle": "కింద మీ వివరాలను సమీక్షించండి",
        "summary_heading": "ప్రాంతం మరియు పెట్టుబడి సారాంశం",
        "summary_fmt": "{village}, {taluk} తాలూకా, కలబురగి — మూలధనం ₹{capital}",
        "feasibility_msg": "మీ సాధ్యత నివేదిక తర్వాత రూపొందించబడుతోంది...",
        "btn_continue": "కొనసాగించండి ➔",
        "btn_back": "⬅ వెనుకకు",
        "btn_get_started": "ప్రారంభించండి ➔",
        "err_fill_all": "దయచేసి ముందుకు వెళ్లే ముందు అన్ని అవసరమైన ఫీల్డ్‌లను పూరించండి.",
        "err_lang": "కొనసాగడానికి దయచేసి ఒక భాషను ఎంచుకోండి.",
        "err_capital": "దయచేసి ₹0 కంటే ఎక్కువ చెల్లుబాటు అయ్యే మూలధన మొత్తాన్ని నమోదు చేయండి."
    },
    "ur": {
        "step3_title": "ذاتی تفصیلات",
        "step3_subtitle": "شروع کرنے کے لیے براہ کرم اپنی بنیادی تفصیلات درج کریں",
        "name_label": "پورا نام",
        "name_placeholder": "مثال: رمیش پاٹل",
        "age_label": "عمر (سال)",
        "category_label": "زمرہ / ذات کا شعبہ",
        "category_purpose": "(صرف سرکاری اسکیم کی اہلیت کی جانچ کے لیے)",
        "category_options": ["-- زمرہ منتخب کریں --", "جنرل (General)", "او بی سی (OBC)", "ایس سی (SC)", "ایس ٹی (ST)", "دیگر (Other)"],
        "greeting_fmt": "خوش آمدید، {name}! 🙏",
        "step4_title": "سرمایہ اور مقام کی تفصیلات",
        "step4_subtitle": "اپنی دستیاب سرمایہ کاری اور کاروباری مقام کا تعین کریں",
        "capital_label": "سرمائے کی رقم (₹)",
        "district_label": "ضلع",
        "taluk_label": "تعلقہ",
        "hobli_label": "ہوبلی",
        "village_label": "گاؤں",
        "step5_title": "تصدیق اور جائزہ",
        "step5_subtitle": "نیچے اپنی اون بورڈنگ تفصیلات کا جائزہ لیں",
        "summary_heading": "مقام اور سرمایہ کاری کا خلاصہ",
        "summary_fmt": "{village}، {taluk} تعلقہ، کلبورگی — سرمایہ ₹{capital}",
        "feasibility_msg": "آپ کی فزیبلٹی رپورٹ تیار کی جا رہی ہے...",
        "btn_continue": "آگے بڑھیں ➔",
        "btn_back": "⬅ پیچھے",
        "btn_get_started": "شروع کریں ➔",
        "err_fill_all": "براہ کرم آگے بڑھنے سے پہلے تمام ضروری خانے پر کریں۔",
        "err_lang": "آگے بڑھنے کے لیے براہ کرم ایک زبان منتخب کریں۔",
        "err_capital": "براہ کرم ₹0 سے زیادہ کی درست رقم درج کریں۔"
    }
}

# ---------------------------------------------------------
# Dynamic Location Dropdown Mappings
# ---------------------------------------------------------
TALUK_HOBLI_MAP = {
    "Aland": ["Aland Hobli", "Nimbarga Hobli"],
    "Chincholi": ["Chincholi Hobli", "Wadi Hobli"]
}

HOBLI_VILLAGE_MAP = {
    "Aland Hobli": ["Nimbarga", "Kadganchi", "Nalegaon"],
    "Nimbarga Hobli": ["Nimbarga", "Kadechur", "Halsur"],
    "Chincholi Hobli": ["Chincholi", "Chandapur", "Wadi"],
    "Wadi Hobli": ["Wadi", "Sultanpur", "Bhusanoor"]
}

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "step" not in st.session_state:
    st.session_state["step"] = 1

if "lang" not in st.session_state:
    st.session_state["lang"] = None

if "name" not in st.session_state:
    st.session_state["name"] = ""

if "age" not in st.session_state:
    st.session_state["age"] = 25

if "category" not in st.session_state:
    st.session_state["category"] = ""

if "greeting" not in st.session_state:
    st.session_state["greeting"] = ""

if "capital" not in st.session_state:
    st.session_state["capital"] = 50000

if "district" not in st.session_state:
    st.session_state["district"] = "Kalaburagi"

if "taluk" not in st.session_state:
    st.session_state["taluk"] = "Aland"

if "hobli_options" not in st.session_state:
    st.session_state["hobli_options"] = TALUK_HOBLI_MAP["Aland"]

if "hobli" not in st.session_state:
    st.session_state["hobli"] = st.session_state["hobli_options"][0]

if "village_options" not in st.session_state:
    st.session_state["village_options"] = HOBLI_VILLAGE_MAP[st.session_state["hobli"]]

if "village" not in st.session_state:
    st.session_state["village"] = st.session_state["village_options"][0]


# Callbacks for dependent dropdowns
def on_taluk_change():
    selected_taluk = st.session_state["taluk_select"]
    st.session_state["taluk"] = selected_taluk
    new_hoblis = TALUK_HOBLI_MAP.get(selected_taluk, [])
    st.session_state["hobli_options"] = new_hoblis
    st.session_state["hobli"] = new_hoblis[0] if new_hoblis else ""
    
    new_villages = HOBLI_VILLAGE_MAP.get(st.session_state["hobli"], [])
    st.session_state["village_options"] = new_villages
    st.session_state["village"] = new_villages[0] if new_villages else ""


def on_hobli_change():
    selected_hobli = st.session_state["hobli_select"]
    st.session_state["hobli"] = selected_hobli
    new_villages = HOBLI_VILLAGE_MAP.get(selected_hobli, [])
    st.session_state["village_options"] = new_villages
    st.session_state["village"] = new_villages[0] if new_villages else ""


# Helper to get current translation dictionary
def get_trans():
    lang = st.session_state.get("lang") or "en"
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"])


# ---------------------------------------------------------
# UI Rendering Functions (Only ONE screen active at any run)
# ---------------------------------------------------------
def render_common_header():
    """Renders the top tricolor bar and official portal header."""
    st.markdown('<div class="tricolor-bar"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="official-header">
            <div class="emblem-icon">🌾</div>
            <div class="header-titles">
                <h1 class="header-main-title">UDYAMPRAGYA</h1>
                <p class="header-tagline">Rural Business Advisory Portal</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# STEP 1 — Welcome
def render_step_1():
    render_common_header()
    
    st.markdown(
        """
        <div class="step-card">
            <div class="step-badge">STEP 1 OF 5 — WELCOME</div>
            <h2 class="step-heading">Welcome to UDYAMPRAGYA</h2>
            <p class="step-description">Empowering rural entrepreneurs with personalized business guidance, scheme eligibility checks, and market feasibility insights.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    if st.button("Get Started ➔", use_container_width=True, type="primary"):
        st.session_state["step"] = 2
        st.rerun()


# STEP 2 — Language Selection
def render_step_2():
    render_common_header()
    
    st.markdown(
        """
        <div class="step-card" style="margin-bottom: 15px;">
            <div class="step-badge">STEP 2 OF 5 — LANGUAGE</div>
            <h2 class="step-heading">Choose Your Language / ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ</h2>
            <p class="step-description">Select your preferred language to proceed with the portal onboarding.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    languages = [
        ("English", "en", "🇬🇧"),
        ("हिंदी (Hindi)", "hi", "🇮🇳"),
        ("ಕನ್ನಡ (Kannada)", "kn", "🇮🇳"),
        ("తెలుగు (Telugu)", "te", "🇮🇳"),
        ("اردو (Urdu)", "ur", "🇮🇳")
    ]
    
    # Render 5 language choice buttons
    for name, code, flag in languages:
        is_selected = (st.session_state["lang"] == code)
        label = f"{flag}  {name} {'✓ (Selected)' if is_selected else ''}"
        btn_type = "primary" if is_selected else "secondary"
        if st.button(label, key=f"lang_btn_{code}", use_container_width=True, type=btn_type):
            st.session_state["lang"] = code
            st.rerun()
            
    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    
    col_back, col_next = st.columns([1, 2])
    with col_back:
        if st.button("⬅ Back", use_container_width=True):
            st.session_state["step"] = 1
            st.rerun()
            
    with col_next:
        if st.button("Continue ➔", use_container_width=True, type="primary"):
            if not st.session_state["lang"]:
                st.error("Please select a language before proceeding. / ಮುಂದುವರಿಯಲು ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.")
            else:
                st.session_state["step"] = 3
                st.rerun()


# STEP 3 — Personal Details
def render_step_3():
    render_common_header()
    t = get_trans()
    
    st.markdown(
        f"""
        <div class="step-card" style="margin-bottom: 15px;">
            <div class="step-badge">STEP 3 OF 5 — PERSONAL DETAILS</div>
            <h2 class="step-heading">{t['step3_title']}</h2>
            <p class="step-description">{t['step3_subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Input fields
    name_val = st.text_input(
        t["name_label"],
        value=st.session_state.get("name", ""),
        placeholder=t["name_placeholder"],
        key="input_name"
    )
    
    age_val = st.number_input(
        t["age_label"],
        min_value=18,
        max_value=100,
        value=int(st.session_state.get("age", 25)),
        step=1,
        key="input_age"
    )
    
    cat_options = t["category_options"]
    curr_cat = st.session_state.get("category", "")
    default_idx = cat_options.index(curr_cat) if curr_cat in cat_options else 0
    
    category_val = st.selectbox(
        t["category_label"],
        options=cat_options,
        index=default_idx,
        key="input_category"
    )
    st.markdown(f'<div class="category-note">{t["category_purpose"]}</div>', unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    
    col_back, col_next = st.columns([1, 2])
    with col_back:
        if st.button(t["btn_back"], use_container_width=True):
            st.session_state["step"] = 2
            st.rerun()
            
    with col_next:
        if st.button(t["btn_continue"], use_container_width=True, type="primary"):
            # Validation
            if not name_val.strip() or category_val == cat_options[0]:
                st.error(t["err_fill_all"])
            else:
                st.session_state["name"] = name_val.strip()
                st.session_state["age"] = age_val
                st.session_state["category"] = category_val
                st.session_state["greeting"] = t["greeting_fmt"].format(name=name_val.strip())
                st.session_state["step"] = 4
                st.rerun()


# STEP 4 — Capital & Location
def render_step_4():
    render_common_header()
    t = get_trans()
    
    # Show greeting banner
    if st.session_state.get("greeting"):
        st.markdown(f'<div class="greeting-banner">{st.session_state["greeting"]}</div>', unsafe_allow_html=True)
        
    st.markdown(
        f"""
        <div class="step-card" style="margin-bottom: 15px;">
            <div class="step-badge">STEP 4 OF 5 — LOCATION & CAPITAL</div>
            <h2 class="step-heading">{t['step4_title']}</h2>
            <p class="step-description">{t['step4_subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    capital_val = st.number_input(
        t["capital_label"],
        min_value=0,
        max_value=10000000,
        value=int(st.session_state.get("capital", 50000)),
        step=5000,
        key="input_capital"
    )
    
    # District read-only
    st.text_input(
        t["district_label"],
        value=st.session_state["district"],
        disabled=True,
        key="input_district"
    )
    
    # Taluk dropdown
    taluk_opts = ["Aland", "Chincholi"]
    t_idx = taluk_opts.index(st.session_state["taluk"]) if st.session_state["taluk"] in taluk_opts else 0
    st.selectbox(
        t["taluk_label"],
        options=taluk_opts,
        index=t_idx,
        key="taluk_select",
        on_change=on_taluk_change
    )
    
    # Hobli dropdown
    h_opts = st.session_state["hobli_options"]
    h_idx = h_opts.index(st.session_state["hobli"]) if st.session_state["hobli"] in h_opts else 0
    st.selectbox(
        t["hobli_label"],
        options=h_opts,
        index=h_idx,
        key="hobli_select",
        on_change=on_hobli_change
    )
    
    # Village dropdown
    v_opts = st.session_state["village_options"]
    v_idx = v_opts.index(st.session_state["village"]) if st.session_state["village"] in v_opts else 0
    selected_village = st.selectbox(
        t["village_label"],
        options=v_opts,
        index=v_idx,
        key="village_select"
    )
    
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    
    col_back, col_next = st.columns([1, 2])
    with col_back:
        if st.button(t["btn_back"], use_container_width=True):
            st.session_state["step"] = 3
            st.rerun()
            
    with col_next:
        if st.button(t["btn_continue"], use_container_width=True, type="primary"):
            if capital_val <= 0:
                st.error(t["err_capital"])
            else:
                st.session_state["capital"] = capital_val
                st.session_state["village"] = selected_village
                st.session_state["step"] = 5
                st.rerun()


# STEP 5 — Confirmation
def render_step_5():
    render_common_header()
    t = get_trans()
    
    st.markdown(
        f"""
        <div class="step-card" style="margin-bottom: 15px;">
            <div class="step-badge">STEP 5 OF 5 — CONFIRMATION</div>
            <h2 class="step-heading">{t['step5_title']}</h2>
            <p class="step-description">{t['step5_subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    village = st.session_state.get("village", "")
    taluk = st.session_state.get("taluk", "")
    capital_fmt = f"{st.session_state.get('capital', 0):,}"
    
    summary_text = t["summary_fmt"].format(
        village=village,
        taluk=taluk,
        capital=capital_fmt
    )
    
    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-title">📋 {t['summary_heading']}</div>
            <div class="summary-content">{summary_text}</div>
        </div>
        
        <div class="feasibility-badge">
            <span>⚙️</span>
            <span>{t['feasibility_msg']}</span>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    
    if st.button(t["btn_back"], use_container_width=True):
        st.session_state["step"] = 4
        st.rerun()


# ---------------------------------------------------------
# Control Flow — Strict If/Elif Dispatcher for Single Screen
# ---------------------------------------------------------
current_step = st.session_state.get("step", 1)

if current_step == 1:
    render_step_1()
elif current_step == 2:
    render_step_2()
elif current_step == 3:
    render_step_3()
elif current_step == 4:
    render_step_4()
elif current_step == 5:
    render_step_5()
else:
    st.session_state["step"] = 1
    st.rerun()
