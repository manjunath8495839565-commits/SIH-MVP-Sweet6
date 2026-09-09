import streamlit as st
import plotly.graph_objects as go

# ---------------------------------------------------------
# Page Configuration & Full-Width Layout
# ---------------------------------------------------------
st.set_page_config(
    page_title="UDYAMPRAGYA — Rural Business Advisory Portal",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Full-Width Layout & High-Contrast Visual System
st.markdown(
    """
    <style>
    /* Hide Streamlit default chrome elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Global Container & Full Width Background */
    .stApp {
        background-color: #F4F6F8 !important;
        color: #1A1A1A !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Remove narrow centered block container restriction for full-width feel */
    .main .block-container {
        max-width: 100% !important;
        padding-top: 0.5rem !important;
        padding-bottom: 3rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
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
        margin-bottom: 14px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* Full-Width Header Bar (#0B3D91 background, #FFFFFF text) */
    .official-header {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        gap: 16px;
        padding: 16px 24px;
        background: #0B3D91 !important;
        color: #FFFFFF !important;
        border-radius: 12px;
        border: 1px solid #0B2E59;
        box-shadow: 0 4px 12px rgba(11, 61, 145, 0.15);
        margin-bottom: 20px;
        width: 100%;
    }
    .emblem-icon {
        width: 52px;
        height: 52px;
        border-radius: 50%;
        background: #FFFFFF;
        color: #0B3D91;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        border: 2px solid #E6A817;
        flex-shrink: 0;
    }
    .header-titles {
        text-align: left;
    }
    .header-main-title {
        font-size: 24px !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        letter-spacing: 1.2px;
        margin: 0 !important;
        line-height: 1.1 !important;
    }
    .header-tagline {
        font-size: 14px !important;
        font-weight: 600 !important;
        color: #FFFFFF !important;
        margin-top: 2px !important;
        margin-bottom: 0 !important;
        opacity: 0.95;
    }

    /* Analytics Section Header */
    .analytics-section-title {
        font-size: 16px !important;
        font-weight: 800 !important;
        color: #0B2E59 !important;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Stat Cards Styling */
    .stat-card {
        background-color: #FFFFFF !important;
        border-radius: 12px;
        padding: 18px 16px;
        box-shadow: none !important;
        border: 1px solid #D0D5DA !important;
        text-align: center;
        height: 100%;
    }
    .stat-number {
        font-size: 30px !important;
        font-weight: 800 !important;
        color: #0B3D91 !important;
        line-height: 1.2;
        margin-bottom: 4px;
    }
    .stat-label {
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #4A4A4A !important;
        line-height: 1.3;
    }
    .stat-caption {
        font-size: 12px !important;
        color: #4A4A4A !important;
        font-style: italic;
        margin-top: 6px;
        margin-bottom: 16px;
    }
    
    /* Feature Cards Styling (Step 1) */
    .feature-card {
        background-color: #FFFFFF !important;
        border: 1px solid #D0D5DA !important;
        border-radius: 12px;
        padding: 20px 18px;
        box-shadow: none !important;
        height: 100%;
    }
    .feature-icon {
        color: #0B3D91 !important;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
    }
    .feature-title {
        color: #0B2E59 !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        margin-bottom: 6px;
        line-height: 1.3;
    }
    .feature-desc {
        color: #4A4A4A !important;
        font-size: 13px !important;
        font-weight: 400 !important;
        line-height: 1.4;
    }
    
    /* Step Card Container (#FFFFFF background, #D0D5DA border) */
    .step-card {
        background-color: #FFFFFF !important;
        border-radius: 14px;
        padding: 28px 24px;
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
        padding: 6px 14px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 14px;
    }
    
    /* Headings (#0B2E59) & Subtitles (#4A4A4A) */
    .step-heading {
        color: #0B2E59 !important;
        font-size: 24px !important;
        font-weight: 700 !important;
        margin-top: 0;
        margin-bottom: 8px;
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
        padding: 22px;
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
        font-size: 19px !important;
        font-weight: 700 !important;
        color: #0B2E59 !important;
        line-height: 1.4;
    }
    .feasibility-badge {
        background: #FFF8E7 !important;
        border: 1px solid #E6A817 !important;
        color: #0B2E59 !important;
        padding: 16px 20px;
        border-radius: 10px;
        font-size: 16px !important;
        font-weight: 700 !important;
        display: flex;
        align-items: center;
        gap: 12px;
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
        padding: 12px 24px !important;
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
        margin-bottom: 6px !important;
    }
    
    /* Input Fields (Text & Number Input Container & Controls) */
    div[data-baseweb="input"],
    div[data-baseweb="base-input"],
    .stTextInput input,
    .stNumberInput input {
        background-color: #FFFFFF !important;
        color: #1A1A1A !important;
        border: 1px solid #D0D5DA !important;
        border-radius: 8px !important;
    }
    
    div[data-baseweb="input"] input {
        color: #1A1A1A !important;
        background-color: #FFFFFF !important;
        font-size: 15px !important;
        font-weight: 500 !important;
    }

    div[data-baseweb="input"] input::placeholder {
        color: #666666 !important;
        opacity: 1 !important;
    }

    /* Disabled Input Fields */
    input:disabled,
    div[data-baseweb="input"][disabled] input,
    .stTextInput input:disabled {
        background-color: #F4F6F8 !important;
        color: #4A4A4A !important;
        -webkit-text-fill-color: #4A4A4A !important;
        border-color: #D0D5DA !important;
        font-weight: 600 !important;
    }

    /* Closed Selectbox Box (Input State) */
    div[data-baseweb="select"],
    div[data-baseweb="select"] > div,
    select {
        background-color: #FFFFFF !important;
        color: #1A1A1A !important;
        border: 1px solid #D0D5DA !important;
        border-radius: 8px !important;
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
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.12) !important;
        border-radius: 8px !important;
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
# Translations Data Structure (Single-Page App Layout)
# ---------------------------------------------------------
TRANSLATIONS = {
    "en": {
        "welcome_title": "Welcome to UDYAMPRAGYA",
        "welcome_subtitle": "Empowering rural entrepreneurs with personalized business guidance, scheme eligibility checks, and market feasibility insights.",
        "plan_title": "My Business Plan",
        "plan_subtitle": "Enter or edit your business idea and location details to receive instant AI guidance and subsidy eligibility",
        "profile_title": "Profile & Settings",
        "profile_subtitle": "Manage your user profile, change language preferences, or log out of your session",
        "login_title": "Portal Login",
        "login_subtitle": "Enter your credentials to access personalized business advisory",
        "user_id_label": "User ID / Mobile Number",
        "user_id_placeholder": "e.g., 9876543210 or USER123",
        "password_label": "Password",
        "password_placeholder": "Enter password",
        "btn_login": "Login ➔",
        "register_link": "New user? Register here",
        "change_lang_link": "🌐 Change Language",
        "err_login_empty": "Please enter your User ID and Password.",
        "name_label": "Full Name",
        "name_placeholder": "e.g., Ramesh Patil",
        "age_label": "Age (Years)",
        "category_label": "Category / Caste Section",
        "category_purpose": "(used only to check government scheme eligibility)",
        "category_options": ["-- Select Category --", "General", "OBC", "SC", "ST", "Other"],
        "greeting_fmt": "Welcome, {name}! 🙏",
        "capital_label": "Capital Amount (₹)",
        "district_label": "District",
        "taluk_label": "Taluk",
        "hobli_label": "Hobli",
        "village_label": "Village",
        "business_idea_label": "Business Idea / Sector",
        "business_idea_placeholder": "e.g., Agri-processing, Flour Mill, Dairy Farm, Handicrafts",
        "investment_label": "Required Investment (₹)",
        "ai_panel_title": "AI Guidance & Eligibility",
        "nav_dashboard": "Dashboard",
        "nav_data_sources": "Data Sources",
        "nav_business_plan": "My Business Plan",
        "nav_profile": "Profile & Settings",
        "btn_logout": "🚪 Logout",
        "btn_save_plan": "💾 Save Plan",
        "msg_plan_saved": "Business plan saved successfully! / ನಿಮ್ಮ ವ್ಯವಹಾರ ಯೋಜನೆಯನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಉಳಿಸಲಾಗಿದೆ!",
        "btn_continue": "Continue ➔",
        "btn_back": "⬅ Back",
        "err_fill_all": "Please complete all required fields before continuing.",
        "err_lang": "Please select a language before proceeding.",
        "err_capital": "Please enter a valid capital amount greater than ₹0."
    },
    "hi": {
        "welcome_title": "UDYAMPRAGYA में आपका स्वागत है",
        "welcome_subtitle": "ग्रामीण उद्यमियों को व्यक्तिगत व्यावसायिक मार्गदर्शन, योजना पात्रता जांच और बाजार व्यवहार्यता अंतर्दृष्टि के साथ सशक्त बनाना।",
        "plan_title": "मेरी व्यावसायिक योजना",
        "plan_subtitle": "त्वरित एआई मार्गदर्शन और योजना पात्रता जानकारी प्राप्त करने के लिए अपनी व्यावसायिक योजना दर्ज करें या संपादित करें",
        "profile_title": "प्रोफाइल और सेटिंग्स",
        "profile_subtitle": "अपनी प्रोफाइल प्रबंधित करें, भाषा प्राथमिकताएँ बदलें, या लॉग आउट करें",
        "login_title": "पोर्टल लॉगिन",
        "login_subtitle": "व्यक्तिगत व्यावसायिक सलाह तक पहुँचने के लिए अपनी जानकारी दर्ज करें",
        "user_id_label": "यूज़र आईडी / मोबाइल नंबर",
        "user_id_placeholder": "जैसे: 9876543210 या USER123",
        "password_label": "पासवर्ड",
        "password_placeholder": "पासवर्ड दर्ज करें",
        "btn_login": "लॉगिन करें ➔",
        "register_link": "नए उपयोगकर्ता? यहाँ पंजीकरण करें",
        "change_lang_link": "🌐 भाषा बदलें",
        "err_login_empty": "कृपया अपनी यूज़र आईडी और पासवर्ड दर्ज करें।",
        "name_label": "पूरा नाम",
        "name_placeholder": "जैसे: रमेश पाटिल",
        "age_label": "आयु (वर्ष)",
        "category_label": "वर्ग / जाति अनुभाग",
        "category_purpose": "(केवल सरकारी योजना पात्रता जांचने के लिए उपयोग किया जाता है)",
        "category_options": ["-- वर्ग चुनें --", "सामान्य (General)", "अन्य पिछड़ा वर्ग (OBC)", "अनुसूचित जाति (SC)", "अनुसूचित जनजाति (ST)", "अन्य (Other)"],
        "greeting_fmt": "स्वागत है, {name}! 🙏",
        "capital_label": "पूंजी राशि (₹)",
        "district_label": "जिला",
        "taluk_label": "तालुका",
        "hobli_label": "होबली",
        "village_label": "गाँव",
        "business_idea_label": "व्यावसायिक विचार / क्षेत्र",
        "business_idea_placeholder": "जैसे: कृषि-प्रसंस्करण, आटा चक्की, डेयरी फार्म",
        "investment_label": "आवश्यक निवेश (₹)",
        "ai_panel_title": "एआई मार्गदर्शन और पात्रता",
        "nav_dashboard": "डैशबोर्ड",
        "nav_business_plan": "मेरी व्यावसायिक योजना",
        "nav_profile": "प्रोफाइल और सेटिंग्स",
        "btn_logout": "🚪 लॉग आउट",
        "btn_save_plan": "💾 योजना सहेजें",
        "msg_plan_saved": "व्यावसायिक योजना सफलतापूर्वक सहेजी गई!",
        "btn_continue": "आगे बढ़ें ➔",
        "btn_back": "⬅ पीछे",
        "err_fill_all": "कृपया आगे बढ़ने से पहले सभी आवश्यक फ़ील्ड भरें।",
        "err_lang": "कृपया आगे बढ़ने से पहले एक भाषा का चयन करें।",
        "err_capital": "कृपया ₹0 से अधिक की मान्य पूंजी राशि दर्ज करें।"
    },
    "kn": {
        "welcome_title": "UDYAMPRAGYA ಗೆ ಸ್ವಾಗತ",
        "welcome_subtitle": "ವೈಯಕ್ತಿಕಗೊಳಿಸಿದ ವ್ಯವಹಾರ ಮಾರ್ಗದರ್ಶನ, ಯೋಜನೆ ಅರ್ಹತಾ ಪರಿಶೀಲನೆಗಳು ಮತ್ತು ಮಾರುಕಟ್ಟೆ ಸಾಧ್ಯತೆಯ ಒಳನೋಟಗಳೊಂದಿಗೆ ಗ್ರಾಮೀಣ ಉದ್ಯಮಿಗಳನ್ನು ಸಬಲೀಕರಣಗೊಳಿಸುವುದು.",
        "plan_title": "ನನ್ನ ವ್ಯವಹಾರ ಯೋಜನೆ",
        "plan_subtitle": "ತಕ್ಷಣದ AI ಮಾರ್ಗದರ್ಶನ ಮತ್ತು ಯೋಜನೆ ಅರ್ಹತೆಯ ಒಳನೋಟಗಳನ್ನು ಪಡೆಯಲು ನಿಮ್ಮ ವ್ಯವಹಾರದ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ ಅಥವಾ ಸಂಪಾದಿಸಿ",
        "profile_title": "ಪ್ರೊಫೈಲ್ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "profile_subtitle": "ನಿಮ್ಮ ಪ್ರೊಫೈಲ್ ನಿರ್ವಹಿಸಿ, ಭಾಷೆಯ ಆದ್ಯತೆಗಳನ್ನು ಬದಲಾಯಿಸಿ ಅಥವಾ ಲಾಗ್‌ಔಟ್ ಮಾಡಿ",
        "login_title": "ಪೋರ್ಟಲ್ ಲಾಗಿನ್",
        "login_subtitle": "ವೈಯಕ್ತಿಕಗೊಳಿಸಿದ ವ್ಯವಹಾರ ಸಲಹೆಯನ್ನು ಪಡೆಯಲು ನಿಮ್ಮ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ",
        "user_id_label": "ಬಳಕೆದಾರ ಐಡಿ / ಮೊಬೈಲ್ ಸಂಖ್ಯೆ",
        "user_id_placeholder": "ಉದಾ: 9876543210 ಅಥವಾ USER123",
        "password_label": "ಪಾಸ್‌ವರ್ಡ್",
        "password_placeholder": "ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿ",
        "btn_login": "ಲಾಗಿನ್ ಮಾಡಿ ➔",
        "register_link": "ಹೊಸ ಬಳಕೆದಾರರೇ? ಇಲ್ಲಿ ನೋಂದಾಯಿಸಿ",
        "change_lang_link": "🌐 ಭಾಷೆಯನ್ನು ಬದಲಾಯಿಸಿ",
        "err_login_empty": "ದಯವಿಟ್ಟು ನಿಮ್ಮ ಬಳಕೆದಾರ ಐಡಿ ಮತ್ತು ಪಾಸ್‌ವರ್ಡ್ ನಮೂದಿಸಿ.",
        "name_label": "ಪೂರ್ಣ ಹೆಸರು",
        "name_placeholder": "ಉದಾ: ರಮೇಶ್ ಪಾಟೀಲ್",
        "age_label": "ವಯಸ್ಸು (ವರ್ಷಗಳು)",
        "category_label": "ವರ್ಗ / ಜಾತಿ ವಿಭಾಗ",
        "category_purpose": "(ಸರ್ಕಾರಿ ಯೋಜನೆಯ ಅರ್ಹತೆಯನ್ನು ಪರಿಶೀಲಿಸಲು ಮಾತ್ರ ಬಳಸಲಾಗುತ್ತದೆ)",
        "category_options": ["-- ವರ್ಗವನ್ನು ಆಯ್ಕೆಮಾಡಿ --", "ಸಾಮಾನ್ಯ (General)", "ಒಬಿಸಿ (OBC)", "ಎಸ್‌ಸಿ (SC)", "ಎಸ್‌ಟಿ (ST)", "ಇತರೆ (Other)"],
        "greeting_fmt": "ಸ್ವಾಗತ, {name}! 🙏",
        "capital_label": "ಬಂಡವಾಳದ ಮೊತ್ತ (₹)",
        "district_label": "ಜಿಲ್ಲೆ",
        "taluk_label": "ತಾಲೂಕು",
        "hobli_label": "ಹೋಬಳಿ",
        "village_label": "ಗ್ರಾಮ",
        "business_idea_label": "ವ್ಯವಹಾರದ ಕಲ್ಪನೆ / ವಲಯ",
        "business_idea_placeholder": "ಉದಾ: ಕೃಷಿ ಸಂಸ್ಕರಣೆ, ಹಿಟ್ಟಿನ ಗಿರಣಿ, ಹಾಲಿನ ಫಾರ್ಮ್",
        "investment_label": "ಅಗತ್ಯವಿರುವ ಹೂಡಿಕೆ (₹)",
        "ai_panel_title": "AI ಮಾರ್ಗದರ್ಶನ ಮತ್ತು ಅರ್ಹತೆ",
        "nav_dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "nav_business_plan": "ನನ್ನ ವ್ಯವಹಾರ ಯೋಜನೆ",
        "nav_profile": "ಪ್ರೊಫೈಲ್ ಮತ್ತು ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "btn_logout": "🚪 ಲಾಗ್‌ಔಟ್ ಮಾಡಿ",
        "btn_save_plan": "💾 ಯೋಜನೆಯನ್ನು ಉಳಿಸಿ",
        "msg_plan_saved": "ನಿಮ್ಮ ವ್ಯವಹಾರ ಯೋಜನೆಯನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಉಳಿಸಲಾಗಿದೆ!",
        "btn_continue": "ಮುಂದುವರಿಸಿ ➔",
        "btn_back": "⬅ ಹಿಂತಿರುಗಿ",
        "err_fill_all": "ದಯವಿಟ್ಟು ಮುಂದುವರಿಯುವ ಮೊದಲು ಎಲ್ಲಾ ಅಗತ್ಯ ಕ್ಷೇತ್ರಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ.",
        "err_lang": "ಮುಂದುವರಿಯಲು ದಯವಿಟ್ಟು ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "err_capital": "ದಯವಿಟ್ಟು ₹0 ಗಿಂತ ಹೆಚ್ಚಿನ ಸಿಂಧುವಾದ ಬಂಡವಾಳದ ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ."
    },
    "te": {
        "welcome_title": "UDYAMPRAGYA కు స్వాగతం",
        "welcome_subtitle": "వ్యక్తిగతీకరించిన వ్యాపార మార్గదర్శకత్వం, పథకం అర్హత తనిఖీలు మరియు మార్కెట్ సాధ్యత అంతర్దృష్టులతో గ్రామీణ పారిశ్రామికవేత్తలను సాధికారపరచడం.",
        "plan_title": "నా వ్యాపార ప్రణాళిక",
        "plan_subtitle": "తక్షణ AI మార్గదర్శకత్వం మరియు పథకం అర్హత అంతర్దృష్టులను పొందడానికి మీ వ్యాపార వివరాలను నమోదు చేయండి లేదా సవరించండి",
        "profile_title": "ప్రొఫైల్ మరియు సెట్టింగ్‌లు",
        "profile_subtitle": "మీ ప్రొఫైల్‌ను నిర్వహించండి, భాషా ప్రాధాన్యతలను మార్చండి లేదా లాగ్ అవుట్ చేయండి",
        "login_title": "పోర్టల్ లాగిన్",
        "login_subtitle": "వ్యక్తిగతీకరించిన వ్యాపార సలహాలను పొందడానికి మీ వివరాలను నమోదు చేయండి",
        "user_id_label": "యూజర్ ఐడీ / మొబైల్ నంబర్",
        "user_id_placeholder": "ఉదా: 9876543210 లేదా USER123",
        "password_label": "పాస్‌వర్డ్",
        "password_placeholder": "పాస్‌వర్డ్ నమోదు చేయండి",
        "btn_login": "లాగిన్ చేయండి ➔",
        "register_link": "కొత్త వినియోగదారులా? ఇక్కడ నమోదు చేసుకోండి",
        "change_lang_link": "🌐 భాషను మార్చండి",
        "err_login_empty": "దయచేసి మీ యూజర్ ఐడీ మరియు పాస్‌వర్డ్ నమోదు చేయండి.",
        "name_label": "పూర్తి పేరు",
        "name_placeholder": "ఉదా: రమేష్ పాటిల్",
        "age_label": "వయస్సు (సంవత్సరాలు)",
        "category_label": "వర్గం / కుల విభాగం",
        "category_purpose": "(ప్రభుత్వ పథకం అర్హతను తనిఖీ చేయడానికి మాత్రమే ఉపయోగించబడుతుంది)",
        "category_options": ["-- వర్గాన్ని ఎంచుకోండి --", "జనరల్ (General)", "ఒబిసి (OBC)", "ఎస్సీ (SC)", "ఎస్టీ (ST)", "ఇతర (Other)"],
        "greeting_fmt": "స్వాగతం, {name}! 🙏",
        "capital_label": "మూలధన మొత్తం (₹)",
        "district_label": "జిల్లా",
        "taluk_label": "తాలూకా",
        "hobli_label": "హోబ్లి",
        "village_label": "గ్రామం",
        "business_idea_label": "వ్యాపార ఆలోచన / రంగం",
        "business_idea_placeholder": "ఉదా: వ్యవసాయ ప్రాసెసింగ్, పిండి మిల్లు, డైరీ ఫార్మ్",
        "investment_label": "అవసరమైన పెట్టుబడి (₹)",
        "ai_panel_title": "AI మార్గదర్శకత్వం మరియు అర్హత",
        "nav_dashboard": "డాష్‌బోర్డ్",
        "nav_business_plan": "నా వ్యాపార ప్రణాళిక",
        "nav_profile": "ప్రొఫైల్ మరియు సెట్టింగ్‌లు",
        "btn_logout": "🚪 లాగ్ అవుట్",
        "btn_go_to_plan": "నా వ్యాపార ప్రణాళికకు వెళ్లండి ➔",
        "btn_go_to_profile": "ప్రొఫైల్ మరియు సెట్టింగ్‌లకు వెళ్లండి ➔",
        "btn_back_to_dashboard": "⬅ డాష్‌బోర్డ్‌కు తిరిగి వెళ్లండి",
        "summary_heading": "ప్రాంతం మరియు పెట్టుబడి సారాంశం",
        "summary_fmt": "{village}, {taluk} తాలూకా, కలబురగి — మూలధనం ₹{capital}",
        "feasibility_msg": "మీ సాధ్యత నివేదిక తర్వాత రూపొందించబడుతోంది...",
        "btn_continue": "కొనసాగించండి ➔",
        "btn_back": "⬅ వెనుకకు",
        "err_fill_all": "దయచేసి ముందుకు వెళ్లే ముందు అన్ని అవసరమైన ఫీల్డ్‌లను పూరించండి.",
        "err_lang": "కొనసాగడానికి దయచేసి ఒక భాషను ఎంచుకోండి.",
        "err_capital": "దయచేసి ₹0 కంటే ఎక్కువ చెల్లుబాటు అయ్యే మూలధన మొత్తాన్ని నమోదు చేయండి."
    },
    "ur": {
        "step1_title": "UDYAMPRAGYA میں آپ کا استقبال ہے",
        "step1_subtitle": "دیہی تاجروں کو ذاتی کاروباری رہنمائی، اسکیم کی اہلیت کی جانچ، اور مارکیٹ فزیبلٹی بصیرت کے ساتھ بااختیار بنانا۔",
        "step1_badge": "مرحلہ 1 کا 3 — ڈیش بورڈ",
        "step2_title": "میرا کاروباری منصوبہ",
        "step2_subtitle": "فوری AI رہنمائی اور اسکیم کی اہلیت کی بصیرت حاصل کرنے کے لیے اپنی کاروباری تفصیلات درج کریں",
        "step2_badge": "مرحلہ 2 کا 3 — میرا کاروباری منصوبہ",
        "step3_title": "پروفائل اور ترتیبات",
        "step3_subtitle": "اپنا پروفائل منظم کریں، زبان کی ترجیحات تبدیل کریں، یا لاگ آؤٹ کریں",
        "step3_badge": "مرحلہ 3 کا 3 — پروفائل اور ترتیبات",
        "login_title": "پورٹل لاگ ان",
        "login_subtitle": "ذاتی کاروباری مشاورت تک رسائی کے لیے اپنی تفصیلات درج کریں",
        "user_id_label": "یوزر آئی ڈی / موبائل نمبر",
        "user_id_placeholder": "مثال: 9876543210 یا USER123",
        "password_label": "پاس ورڈ",
        "password_placeholder": "پاس ورڈ درج کریں",
        "btn_login": "لاگ ان کریں ➔",
        "register_link": "نئے صارف؟ یہاں رجسٹر کریں",
        "change_lang_link": "🌐 زبان تبدیل کریں",
        "err_login_empty": "براہ کرم اپنا یوزر آئی ڈی اور پاس ورڈ درج کریں۔",
        "name_label": "پورا نام",
        "name_placeholder": "مثال: رمیش پاٹل",
        "age_label": "عمر (سال)",
        "category_label": "زمرہ / ذات کا شعبہ",
        "category_purpose": "(صرف سرکاری اسکیم کی اہلیت کی جانچ کے لیے)",
        "category_options": ["-- زمرہ منتخب کریں --", "جنرل (General)", "او بی سی (OBC)", "ایس سی (SC)", "ایس ٹی (ST)", "دیگر (Other)"],
        "greeting_fmt": "خوش آمدید، {name}! 🙏",
        "capital_label": "سرمائے کی رقم (₹)",
        "district_label": "ضلع",
        "taluk_label": "تعلقہ",
        "hobli_label": "ہوبلی",
        "village_label": "گاؤں",
        "business_idea_label": "کاروباری خیال / شعبہ",
        "business_idea_placeholder": "مثال: زرعی پروسیسنگ، آٹا مل، ڈیری فارم",
        "investment_label": "مطلوبہ سرمایہ کاری (₹)",
        "ai_panel_title": "AI رہنمائی اور اہلیت",
        "nav_dashboard": "ڈیش بورڈ",
        "nav_business_plan": "میرا کاروباری منصوبہ",
        "nav_profile": "پروفائل اور ترتیبات",
        "btn_logout": "🚪 لاگ آؤٹ",
        "btn_go_to_plan": "کاروباری منصوبے پر جائیں ➔",
        "btn_go_to_profile": "پروفائل اور ترتیبات پر جائیں ➔",
        "btn_back_to_dashboard": "⬅ ڈیش بورڈ پر واپس جائیں",
        "summary_heading": "مقام اور سرمایہ کاری کا خلاصہ",
        "summary_fmt": "{village}، {taluk} تعلقہ، کلبورگی — سرمایہ ₹{capital}",
        "feasibility_msg": "آپ کی فزیبلٹی رپورٹ تیار کی جا رہی ہے...",
        "btn_continue": "آگے بڑھیں ➔",
        "btn_back": "⬅ پیچھے",
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
    "Chincholi": ["Chincholi Hobli", "Wadi Hobli"],
    "Afzalpur": [],
    "Jevargi": [],
    "Kalaburagi": []
}

HOBLI_VILLAGE_MAP = {
    "Aland Hobli": ["Nimbarga", "Kadganchi", "Nalegaon"],
    "Nimbarga Hobli": ["Nimbarga", "Kadechur", "Halsur"],
    "Chincholi Hobli": ["Chincholi", "Chandapur", "Wadi"],
    "Wadi Hobli": ["Wadi", "Sultanpur", "Bhusanoor"]
}

# ---------------------------------------------------------
# Data Sources & Official Government Portals Dataset
# ---------------------------------------------------------
DATA_SOURCES = {
    "Agriculture & Crop Data": [
        {"name": "Directorate of Economics & Statistics (DES), Karnataka", "desc": "Crop area, production, and yield data by district", "url": "https://des.karnataka.gov.in/"},
        {"name": "Karnataka APMC Portal (Krishi Marata Vahini)", "desc": "Daily mandi/APMC commodity prices", "url": "https://krishimaratavahini.kar.nic.in/"},
        {"name": "Department of Horticulture, Karnataka", "desc": "Fruit, vegetable, and spice production data", "url": "https://horticulture.kar.nic.in/"},
        {"name": "Agricultural Census", "desc": "Land holding size and cultivator classification", "url": "https://agcensus.nic.in/"},
        {"name": "Karnataka Millet Mission", "desc": "Millet production policy and support data", "url": "https://rfrk.karnataka.gov.in/"},
        {"name": "National Food Security Mission (NFSM)", "desc": "Nutri-cereal and millet promotion schemes", "url": "https://nfsm.gov.in/"},
    ],
    "Livestock & Dairy": [
        {"name": "20th Livestock Census, DAHD", "desc": "District-wise cattle, sheep, goat, poultry population", "url": "https://dahd.nic.in/division/statistics"},
        {"name": "DAHD Karnataka (Animal Husbandry & Veterinary Services)", "desc": "Veterinary infrastructure and meat/milk pricing", "url": "https://ahvs.karnataka.gov.in/"},
        {"name": "Karnataka Milk Federation (KMF / Nandini)", "desc": "Milk procurement price and cooperative network", "url": "https://www.kmfnandini.coop/"},
        {"name": "National Dairy Development Board (NDDB)", "desc": "National milk production benchmarks", "url": "https://www.nddb.coop/"},
        {"name": "National Egg Coordination Committee (NECC)", "desc": "Daily egg and broiler price data", "url": "https://necc.in/"},
    ],
    "Fisheries": [
        {"name": "Karnataka Department of Fisheries", "desc": "Inland water area and fish production data", "url": "https://fisheries.karnataka.gov.in/"},
        {"name": "PMMSY (Blue Revolution Scheme)", "desc": "Fisheries subsidy scheme details", "url": "https://pmmsy.dof.gov.in/"},
    ],
    "Government Schemes & Subsidies": [
        {"name": "PMEGP (KVIC)", "desc": "Micro-enterprise subsidy scheme project profiles", "url": "https://www.kviconline.gov.in/pmegp/pmegpweb/"},
        {"name": "SMAM (Farm Mechanization Mission)", "desc": "Custom Hiring Center subsidy guidelines", "url": "https://agrimachinery.nic.in/"},
        {"name": "Agriculture Infrastructure Fund (AIF/AMI)", "desc": "Warehouse and storage subsidy scheme", "url": "https://agriinfra.dac.gov.in/"},
        {"name": "PM-KUSUM", "desc": "Solar irrigation pump subsidy scheme", "url": "https://pmkusum.mnre.gov.in/"},
        {"name": "KREDL (Karnataka Renewable Energy)", "desc": "State solar/renewable energy scheme data", "url": "https://kredl.karnataka.gov.in/"},
        {"name": "PKVY / Natural Farming (NCOF)", "desc": "Organic farming policy support", "url": "https://pgsindia-ncof.gov.in/"},
        {"name": "DAY-NRLM / KSRLM", "desc": "Self-Help Group (SHG) enterprise data", "url": "https://nrlm.gov.in/"},
    ],
    "Financial & Project Models": [
        {"name": "NABARD Model Project Reports", "desc": "Standard project cost templates across sectors", "url": "https://www.nabard.org/"},
        {"name": "Udyam Registration (MSME)", "desc": "Registered micro-enterprise data by district", "url": "https://udyamregistration.gov.in/"},
    ],
    "Market Prices & Consumer Data": [
        {"name": "Department of Consumer Affairs", "desc": "Retail price monitoring dashboard", "url": "https://fcainfoweb.nic.in/reports/report_menu_web.aspx"},
        {"name": "FSSAI / FoSCoS", "desc": "Food safety registration for processing units", "url": "https://foscos.fssai.gov.in/"},
    ],
    "Infrastructure & Storage": [
        {"name": "NCCD (Cold Chain Development)", "desc": "Cold storage infrastructure gap analysis", "url": "https://nccd.gov.in/"},
        {"name": "CWC (Central Warehousing Corporation)", "desc": "Government godown/warehouse capacity", "url": "https://cewacor.nic.in/"},
        {"name": "WDRA (Warehousing Regulatory Authority)", "desc": "Electronic Negotiable Warehouse Receipt system", "url": "https://wdra.gov.in/"},
        {"name": "KIADB (Industrial Areas Development Board)", "desc": "Industrial land and infrastructure data", "url": "https://kiadb.karnataka.gov.in/"},
    ],
    "Population & Census": [
        {"name": "Census of India 2011", "desc": "Population, literacy, and workforce data", "url": "https://censusindia.gov.in/"},
    ],
    "Research Institutions": [
        {"name": "ICAR-CIRG / ICAR-NIANP / UAS Raichur", "desc": "Livestock breed and agro-climatic research", "url": "https://icar.org.in/"},
        {"name": "MNRE (Solar Resource Assessment)", "desc": "Solar irradiance and renewable potential data", "url": "https://mnre.gov.in/"},
    ],
}

# ---------------------------------------------------------
# Session State Initialization (Entry Flow: Step 0 Lang -> Login -> Step 1 Welcome)
# ---------------------------------------------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = None

if "step" not in st.session_state or st.session_state["lang"] is None:
    st.session_state["step"] = "lang"

if "name" not in st.session_state:
    st.session_state["name"] = "Ramesh Patil"

if "age" not in st.session_state:
    st.session_state["age"] = 25

if "category" not in st.session_state:
    st.session_state["category"] = "OBC"

if "greeting" not in st.session_state:
    st.session_state["greeting"] = ""

if "capital" not in st.session_state:
    st.session_state["capital"] = 50000

if "district" not in st.session_state:
    st.session_state["district"] = "Kalaburagi"

if "business_idea" not in st.session_state:
    st.session_state["business_idea"] = "Agri-processing & Flour Mill"

if "investment_needed" not in st.session_state:
    st.session_state["investment_needed"] = 200000

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
    if new_hoblis:
        st.session_state["hobli"] = new_hoblis[0]
    else:
        st.session_state["hobli"] = ""
        st.session_state["village_options"] = []
        st.session_state["village"] = ""
        return
    
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
# UI Header, Analytics Banner & Growth Chart
# ---------------------------------------------------------
def render_common_header():
    """Renders the top tricolor bar and full-width official header."""
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


def render_growth_chart():
    """Renders the year-over-year micro-enterprises growth chart in Plotly."""
    years = ['2022', '2023', '2024', '2025', '2026']
    assisted = [450, 1120, 2300, 3400, 4820]
    
    fig = go.Figure(data=[
        go.Bar(
            x=years,
            y=assisted,
            marker_color='#0B3D91',
            text=[f"{v:,}" for v in assisted],
            textposition='outside',
            textfont=dict(color='#0B2E59', size=13, family='sans-serif'),
            hovertemplate='<b>Year %{x}</b><br>Enterprises: %{y:,}<extra></extra>'
        )
    ])
    fig.update_layout(
        title=dict(
            text="<b>📈 Micro-enterprises assisted, year over year</b>",
            font=dict(size=17, color="#0B2E59", family="sans-serif")
        ),
        margin=dict(l=20, r=20, t=50, b=20),
        height=280,
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#FFFFFF",
        xaxis=dict(
            title=dict(text="Year", font=dict(color="#4A4A4A", size=13)),
            tickfont=dict(color="#4A4A4A", size=12),
            showgrid=False
        ),
        yaxis=dict(
            title=dict(text="Number of Enterprises", font=dict(color="#4A4A4A", size=13)),
            tickfont=dict(color="#4A4A4A", size=12),
            showgrid=True,
            gridcolor="#E0E0E0"
        )
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def render_analytics_banner():
    """Renders data.gov.in style 4-stat cards analytics banner and growth chart near top of every screen."""
    st.markdown('<div class="analytics-section-title">📊 UDYAMPRAGYA Portal Analytics</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">12,450+</div>
                <div class="stat-label">Rural entrepreneurs assisted</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">3,820+</div>
                <div class="stat-label">Micro-enterprises evaluated</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">2</div>
                <div class="stat-label">Districts covered<br><span style="font-size: 11px; color: #4A4A4A;">(Kalaburagi, Shivamogga)</span></div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col4:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">₹18.6 Cr+</div>
                <div class="stat-label">Total loan eligibility calculated</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    st.markdown('<div class="stat-caption">Figures shown are illustrative for this prototype.</div>', unsafe_allow_html=True)
    
    # Growth Chart
    render_growth_chart()
    st.markdown('<div class="stat-caption" style="margin-top: -15px; margin-bottom: 24px;">Figures shown are illustrative for this prototype.</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# Step Renderers (4 Steps Total)
# ---------------------------------------------------------

# ---------------------------------------------------------
# Sidebar Component (Post-Login Single Page Navigation)
# ---------------------------------------------------------
def render_sidebar():
    """Renders persistent 3-item sidebar with active-state highlighting."""
    st.sidebar.markdown(
        """
        <div style="text-align: center; padding: 12px 0 16px 0;">
            <div style="font-size: 34px; margin-bottom: 4px;">🌾</div>
            <div style="font-size: 18px; font-weight: 800; color: #0B2E59; letter-spacing: 0.8px;">UDYAMPRAGYA</div>
            <div style="font-size: 11px; font-weight: 600; color: #4A4A4A;">Rural Business Advisory Portal</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    t = get_trans()
    step = st.session_state.get("step", "dashboard")
    if step in ["dashboard"]:
        active_key = "dashboard"
    elif step == "data_sources":
        active_key = "data_sources"
    elif step in [1, 2, 3, "business_plan"]:
        active_key = "business_plan"
    elif step == "profile":
        active_key = "profile"
    else:
        active_key = "dashboard"
        
    st.sidebar.markdown('<div style="font-size: 12px; font-weight: 700; color: #4A4A4A; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 10px;">NAVIGATION</div>', unsafe_allow_html=True)
    
    nav_items = [
        ("dashboard", "📊", t.get("nav_dashboard", "Dashboard")),
        ("data_sources", "🗂️", t.get("nav_data_sources", "Data Sources")),
        ("business_plan", "💼", t.get("nav_business_plan", "My Business Plan")),
        ("profile", "⚙️", t.get("nav_profile", "Profile & Settings"))
    ]
    
    for s_key, icon, label in nav_items:
        is_active = (active_key == s_key)
        btn_type = "primary" if is_active else "secondary"
        if st.sidebar.button(f"{icon}  {label}", key=f"sidebar_nav_{s_key}", use_container_width=True, type=btn_type):
            if s_key == "business_plan":
                st.session_state["step"] = 1
            else:
                st.session_state["step"] = s_key
            st.rerun()
            
    st.sidebar.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)
    
    # Bottom Left Profile Badge & Logout
    user_display = st.session_state.get("name") or st.session_state.get("login_user_id") or "Ramesh Patil"
    st.sidebar.markdown(
        f"""
        <div style="background: #FFFFFF; border: 1px solid #D0D5DA; border-radius: 10px; padding: 12px; margin-bottom: 12px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="font-size: 26px;">👤</div>
                <div>
                    <div style="font-size: 14px; font-weight: 700; color: #0B2E59;">{user_display}</div>
                    <div style="font-size: 11px; color: #4A4A4A;">Active Entrepreneur</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    if st.sidebar.button(t.get("btn_logout", "🚪 Logout"), key="sidebar_logout", use_container_width=True, type="secondary"):
        st.session_state["login_user_id"] = ""
        st.session_state["login_password"] = ""
        st.session_state["step"] = "lang"
        st.rerun()


# ---------------------------------------------------------
# Pre-Step & Section Component Renderers
# ---------------------------------------------------------

def render_wizard_stepper(current_step):
    """Renders a modern horizontal wizard stepper with 3 steps."""
    steps = [
        (1, "Personal Details", "👤"),
        (2, "Capital & Location", "📍"),
        (3, "Confirmation", "✅")
    ]
    
    html = '<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 24px; background: #FFFFFF; padding: 18px 24px; border-radius: 14px; border: 1px solid #D0D5DA; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">'
    
    for idx, (step_num, title, icon) in enumerate(steps):
        is_active = (current_step == step_num)
        is_completed = (current_step > step_num)
        
        if is_active:
            badge_bg = "#0B3D91"
            badge_color = "#FFFFFF"
            text_color = "#0B2E59"
            font_weight = "800"
            border_style = "2px solid #E6A817"
        elif is_completed:
            badge_bg = "#1E8449"
            badge_color = "#FFFFFF"
            text_color = "#1E8449"
            font_weight = "700"
            border_style = "1px solid #1E8449"
        else:
            badge_bg = "#F4F6F8"
            badge_color = "#666666"
            text_color = "#888888"
            font_weight = "600"
            border_style = "1px solid #D0D5DA"
            
        badge_icon = "✓" if is_completed else f"{step_num}"
        
        html += f"""
        <div style="display: flex; align-items: center; gap: 12px; flex: 1;">
            <div style="width: 36px; height: 36px; border-radius: 50%; background: {badge_bg}; color: {badge_color}; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 15px; border: {border_style}; flex-shrink: 0;">
                {badge_icon}
            </div>
            <div>
                <div style="font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; color: #666666; font-weight: 700;">STEP {step_num}</div>
                <div style="font-size: 14px; font-weight: {font_weight}; color: {text_color}; white-space: nowrap;">{title}</div>
            </div>
        </div>
        """
        
        if idx < len(steps) - 1:
            line_color = "#1E8449" if (current_step > step_num) else "#D0D5DA"
            html += f'<div style="height: 3px; flex: 1; background-color: {line_color}; margin: 0 16px; border-radius: 2px;"></div>'
            
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


# VIEW 2 — MY BUSINESS PLAN (Dedicated 3-Screen Wizard Page)
def render_step_business_plan():
    """Renders full-screen 3-step wizard flow for My Business Plan: STEP 1 (Personal details), STEP 2 (Capital & Location), STEP 3 (Confirmation)."""
    render_common_header()
    t = get_trans()
    
    bp_step = st.session_state.get("step", 1)
    if bp_step in ["business_plan", "dashboard"]:
        bp_step = 1
        st.session_state["step"] = 1
        
    try:
        bp_step = int(bp_step)
    except (ValueError, TypeError):
        bp_step = 1

    # Progress Stepper Header
    render_wizard_stepper(bp_step)

    if bp_step == 1:
        # STEP 1 — Personal Details
        st.markdown(
            """
            <div class="step-card">
                <h2 class="step-heading">👤 STEP 1 — Personal Details</h2>
                <p class="step-description">Enter your personal information below to begin setting up your business plan.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown('<div style="background: #FFFFFF; border: 1px solid #D0D5DA; border-radius: 12px; padding: 24px; margin-bottom: 20px;">', unsafe_allow_html=True)
        
        name_val = st.text_input(
            t["name_label"],
            value=st.session_state.get("name", ""),
            placeholder=t["name_placeholder"],
            key="input_name_step1"
        )
        st.markdown('<div style="margin-bottom: 18px;"></div>', unsafe_allow_html=True)
        
        col_a, col_b = st.columns([1, 1])
        with col_a:
            age_val = st.number_input(
                t["age_label"],
                min_value=18,
                max_value=100,
                value=int(st.session_state.get("age", 25)),
                step=1,
                key="input_age_step1"
            )
        with col_b:
            cat_options = ["-- Select Category --", "General", "OBC", "SC", "ST", "Other"]
            curr_cat = st.session_state.get("category", "")
            default_idx = cat_options.index(curr_cat) if curr_cat in cat_options else 0
            category_val = st.selectbox(
                t["category_label"],
                options=cat_options,
                index=default_idx,
                key="input_category_step1"
            )
            st.markdown('<div class="category-note" style="color: #4A4A4A; font-weight: 600; font-size: 13px; margin-top: 4px;">Used only to check government scheme eligibility</div>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        if st.button(t["btn_continue"], use_container_width=True, type="primary", key="btn_continue_step1"):
            if not name_val.strip() or not category_val or category_val.startswith("--"):
                st.warning("⚠️ Please fill in all required fields (Name, Age, Category) before continuing.")
            else:
                st.session_state["name"] = name_val.strip()
                st.session_state["age"] = age_val
                st.session_state["category"] = category_val
                greeting_str = f"Welcome, {name_val.strip()}! 🙏"
                st.session_state["greeting"] = greeting_str
                st.session_state["step"] = 2
                st.rerun()

    elif bp_step == 2:
        # STEP 2 — Capital and Location
        greeting = st.session_state.get("greeting", "")
        if greeting:
            st.markdown(f'<div class="greeting-banner">{greeting}</div>', unsafe_allow_html=True)
            
        st.markdown(
            """
            <div class="step-card">
                <h2 class="step-heading">📍 STEP 2 — Capital and Location</h2>
                <p class="step-description">Provide your proposed business capital amount and select your location details.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown('<div style="background: #FFFFFF; border: 1px solid #D0D5DA; border-radius: 12px; padding: 24px; margin-bottom: 20px;">', unsafe_allow_html=True)
        
        col_c, col_d = st.columns([1, 1])
        with col_c:
            capital_val = st.number_input(
                t["capital_label"],
                min_value=0,
                max_value=10000000,
                value=int(st.session_state.get("capital", 50000)),
                step=5000,
                key="input_capital_step2"
            )
        with col_d:
            st.text_input(
                t["district_label"],
                value="Kalaburagi",
                disabled=True,
                key="input_district_step2"
            )
            
        st.markdown('<div style="margin-bottom: 18px;"></div>', unsafe_allow_html=True)
        
        col_l1, col_l2, col_l3 = st.columns([1, 1, 1])
        with col_l1:
            taluk_opts = ["Aland", "Afzalpur", "Jevargi", "Kalaburagi"]
            t_idx = taluk_opts.index(st.session_state.get("taluk", "Aland")) if st.session_state.get("taluk") in taluk_opts else 0
            selected_taluk = st.selectbox(
                t["taluk_label"],
                options=taluk_opts,
                index=t_idx,
                key="taluk_select",
                on_change=on_taluk_change
            )
        with col_l2:
            h_opts = st.session_state.get("hobli_options", TALUK_HOBLI_MAP["Aland"])
            h_idx = h_opts.index(st.session_state.get("hobli")) if st.session_state.get("hobli") in h_opts else 0
            selected_hobli = st.selectbox(
                t["hobli_label"],
                options=h_opts,
                index=h_idx,
                key="hobli_select",
                on_change=on_hobli_change
            )
        with col_l3:
            v_opts = st.session_state.get("village_options", HOBLI_VILLAGE_MAP["Aland Hobli"])
            v_idx = v_opts.index(st.session_state.get("village")) if st.session_state.get("village") in v_opts else 0
            selected_village = st.selectbox(
                t["village_label"],
                options=v_opts,
                index=v_idx,
                key="village_select"
            )
            
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)
        col_back, col_next = st.columns([1, 1])
        with col_back:
            if st.button(t["btn_back"], use_container_width=True, type="secondary", key="btn_back_step2"):
                st.session_state["capital"] = capital_val
                st.session_state["step"] = 1
                st.rerun()
        with col_next:
            if st.button(t["btn_continue"], use_container_width=True, type="primary", key="btn_continue_step2"):
                if capital_val <= 0 or not selected_taluk or not selected_hobli or not selected_village:
                    st.warning("⚠️ Please complete Capital, Taluk, Hobli, and Village selection before continuing.")
                else:
                    st.session_state["capital"] = capital_val
                    st.session_state["taluk"] = selected_taluk
                    st.session_state["hobli"] = selected_hobli
                    st.session_state["village"] = selected_village
                    st.session_state["step"] = 3
                    st.rerun()

    elif bp_step == 3:
        # STEP 3 — Confirmation
        st.markdown(
            """
            <div class="step-card">
                <h2 class="step-heading">✅ STEP 3 — Confirmation</h2>
                <p class="step-description">Review your location & capital summary below.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        village = st.session_state.get("village", "Nimbarga")
        taluk = st.session_state.get("taluk", "Aland")
        capital = st.session_state.get("capital", 50000)
        
        summary_str = f"{village}, {taluk} taluk, Kalaburagi — capital ₹{capital:,}"
        
        st.markdown(
            f"""
            <div class="summary-card">
                <div class="summary-title">📍 Location & Capital Summary</div>
                <div class="summary-content">{summary_str}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown(
            """
            <div class="feasibility-badge">
                <span style="font-size: 24px;">📊</span>
                <div>Generating your feasibility report next</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
        if st.button(t["btn_back"], use_container_width=True, type="secondary", key="btn_back_step3"):
            st.session_state["step"] = 2
            st.rerun()


# STEP 0 (UNNUMBERED PRE-STEP) — Language Selection
def render_step_lang():
    render_common_header()
    
    st.markdown(
        """
        <div class="step-card">
            <h2 class="step-heading">Choose Your Language / ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ</h2>
            <p class="step-description">Select your preferred language to proceed with the UDYAMPRAGYA portal. / UDYAMPRAGYA ಪೋರ್ಟಲ್ ಮುಂದುವರಿಸಲು ನಿಮ್ಮ ಆದ್ಯತೆಯ ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.</p>
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
    
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    
    for i, (name, code, flag) in enumerate(languages):
        with cols[i]:
            is_selected = (st.session_state.get("lang") == code)
            label = f"{flag}  {name}\n{'✓ (Selected)' if is_selected else ''}"
            btn_type = "primary" if is_selected else "secondary"
            if st.button(label, key=f"lang_btn_{code}", use_container_width=True, type=btn_type):
                st.session_state["lang"] = code
                st.session_state["step"] = "login"
                st.rerun()
                
    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    if st.session_state.get("lang"):
        t = get_trans()
        if st.button(t["btn_continue"], use_container_width=True, type="primary", key="btn_continue_lang"):
            st.session_state["step"] = "login"
            st.rerun()


# STEP 1 PRE-STEP (UNNUMBERED) — Login Page
def render_step_login():
    render_common_header()
    t = get_trans()
    
    col_hdr, col_change_lang = st.columns([4, 1])
    with col_change_lang:
        if st.button(t["change_lang_link"], key="btn_change_lang_login", type="secondary", use_container_width=True):
            st.session_state["step"] = "lang"
            st.rerun()
            
    st.markdown(
        f"""
        <div class="step-card">
            <h2 class="step-heading">🔐 {t['login_title']}</h2>
            <p class="step-description">{t['login_subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_left, col_center, col_right = st.columns([1, 2, 1])
    with col_center:
        user_id_val = st.text_input(
            t["user_id_label"],
            value=st.session_state.get("login_user_id", ""),
            placeholder=t["user_id_placeholder"],
            key="input_login_user_id"
        )
        
        password_val = st.text_input(
            t["password_label"],
            type="password",
            value=st.session_state.get("login_password", ""),
            placeholder=t["password_placeholder"],
            key="input_login_password"
        )
        
        st.markdown("<div style='margin-top: 15px;'></div>", unsafe_allow_html=True)
        
        if st.button(t["btn_login"], use_container_width=True, type="primary", key="btn_submit_login"):
            if not user_id_val.strip() or not password_val.strip():
                st.error(t["err_login_empty"])
            else:
                st.session_state["login_user_id"] = user_id_val.strip()
                st.session_state["login_password"] = password_val
                st.session_state["step"] = "dashboard"
                st.rerun()
                
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 18px;">
                <a href="#" onclick="return false;" style="color: #0B3D91; font-weight: 600; font-size: 14px; text-decoration: underline;">
                    {t['register_link']}
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )


# VIEW 1 — DASHBOARD (Default view after login)
def render_step_dashboard():
    """Contains ONLY: Welcome Banner, 4 Analytics Cards, and Growth Bar Chart."""
    render_common_header()
    t = get_trans()
    
    # Welcome banner
    st.markdown(
        f"""
        <div class="step-card">
            <h2 class="step-heading">{t['welcome_title']}</h2>
            <p class="step-description">{t['welcome_subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Analytics 4-card banner & growth chart
    render_analytics_banner()





# VIEW 3 — PROFILE & SETTINGS (Dedicated Page)
def render_step_profile():
    """Contains ONLY: Profile Info, Language Selector, and Logout Button."""
    render_common_header()
    t = get_trans()
    
    st.markdown(
        f"""
        <div class="step-card" style="margin-bottom: 15px;">
            <h2 class="step-heading">⚙️ {t['profile_title']}</h2>
            <p class="step-description">{t['profile_subtitle']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        user_name = st.session_state.get("name") or st.session_state.get("login_user_id") or "Ramesh Patil"
        user_id = st.session_state.get("login_user_id") or "USER123"
        user_cat = st.session_state.get("category") or "OBC"
        village = st.session_state.get("village") or "Nimbarga"
        taluk = st.session_state.get("taluk") or "Aland"
        capital_fmt = f"{st.session_state.get('capital', 50000):,}"
        
        st.markdown(
            f"""
            <div class="summary-card">
                <div style="display: flex; align-items: center; gap: 14px; margin-bottom: 16px;">
                    <div style="width: 56px; height: 56px; border-radius: 50%; background: #0B3D91; color: #FFFFFF; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: 800;">
                        👤
                    </div>
                    <div>
                        <div style="font-size: 20px; font-weight: 800; color: #0B2E59;">{user_name}</div>
                        <div style="font-size: 13px; color: #4A4A4A;">User ID: <b>{user_id}</b></div>
                    </div>
                </div>
                <hr style="border: none; border-top: 1px solid #D0D5DA; margin: 12px 0;" />
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; font-size: 13px;">
                    <div><b>Category:</b> {user_cat}</div>
                    <div><b>Capital:</b> ₹{capital_fmt}</div>
                    <div><b>Location:</b> {village}, {taluk}</div>
                    <div><b>District:</b> Kalaburagi</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col_right:
        st.markdown(
            f"""
            <div class="summary-card" style="border: 1px solid #D0D5DA;">
                <div class="summary-title">🔐 Session & Security</div>
                <div style="font-size: 14px; color: #4A4A4A; margin-bottom: 16px;">
                    You are currently logged in as <b>{user_id}</b>. You can log out anytime to end your session.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        if st.button(t["btn_logout"], use_container_width=True, type="primary", key="btn_profile_logout"):
            st.session_state["login_user_id"] = ""
            st.session_state["login_password"] = ""
            st.session_state["step"] = "lang"
            st.rerun()
            
    # Language Selector Component
    st.markdown('<h3 style="color: #0B2E59; font-size: 18px; font-weight: 700; margin-top: 10px; margin-bottom: 12px;">Choose Your Language / ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ</h3>', unsafe_allow_html=True)
    
    languages = [
        ("English", "en", "🇬🇧"),
        ("हिंदी (Hindi)", "hi", "🇮🇳"),
        ("ಕನ್ನಡ (Kannada)", "kn", "🇮🇳"),
        ("తెలుగు (Telugu)", "te", "🇮🇳"),
        ("اردو (Urdu)", "ur", "🇮🇳")
    ]
    
    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]
    
    for i, (name, code, flag) in enumerate(languages):
        with cols[i]:
            is_selected = (st.session_state.get("lang") == code)
            label = f"{flag}  {name}\n{'✓ (Selected)' if is_selected else ''}"
            btn_type = "primary" if is_selected else "secondary"
            if st.button(label, key=f"profile_lang_btn_{code}", use_container_width=True, type=btn_type):
                st.session_state["lang"] = code
                st.rerun()


# VIEW 4 — DATA SOURCES (Interactive Directory Page)
def render_step_data_sources():
    """Renders interactive Data Sources directory page with real-time search, category expanders, and official source badges."""
    render_common_header()
    t = get_trans()
    
    st.markdown(
        f"""
        <div class="step-card" style="margin-bottom: 20px;">
            <h2 class="step-heading">🗂️ {t.get('nav_data_sources', 'Data Sources')} & Portals</h2>
            <p class="step-description">Explore verified government databases, research portals, and financial models powering UDYAMPRAGYA advisory insights.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Real-time search filter box
    search_query = st.text_input(
        "🔍 Search Data Sources & Portals",
        placeholder="Type portal name, keyword, or domain (e.g., APMC, Census, PMEGP, NABARD)...",
        key="input_search_sources"
    ).strip().lower()
    
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)
    
    total_matched = 0
    
    for category, items in DATA_SOURCES.items():
        if search_query:
            matched_items = [
                item for item in items
                if search_query in item["name"].lower()
                or search_query in item["desc"].lower()
                or search_query in item["url"].lower()
                or search_query in category.lower()
            ]
        else:
            matched_items = items
            
        if matched_items:
            total_matched += len(matched_items)
            count_badge = f"{category} ({len(matched_items)})"
            is_expanded = bool(search_query)
            
            with st.expander(count_badge, expanded=is_expanded):
                for item in matched_items:
                    url = item["url"]
                    is_gov = any(dom in url for dom in [".gov.in", ".nic.in", ".kar.nic.in"])
                    gov_badge = '<span style="background: #E8F5E9; color: #1E8449; font-size: 11px; font-weight: 700; padding: 3px 10px; border-radius: 12px; border: 1px solid #C8E6C9; margin-left: 8px; display: inline-flex; align-items: center; gap: 4px;">Official Government Source ✓</span>' if is_gov else ''
                    
                    st.markdown(
                        f"""
                        <div style="background: #FFFFFF; border: 1px solid #D0D5DA; border-radius: 12px; padding: 16px 20px; margin-bottom: 14px; box-shadow: 0 2px 6px rgba(0,0,0,0.02);">
                            <div style="font-size: 16px; font-weight: 800; color: #0B2E59; margin-bottom: 6px;">
                                {item['name']} {gov_badge}
                            </div>
                            <div style="font-size: 13px; color: #4A4A4A; font-weight: 500; margin-bottom: 10px; line-height: 1.4;">
                                {item['desc']}
                            </div>
                            <div>
                                <a href="{url}" target="_blank" rel="noopener noreferrer" style="display: inline-flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 700; color: #0B3D91; text-decoration: underline;">
                                    🔗 {url} ↗
                                </a>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
    if search_query and total_matched == 0:
        st.info("No matching data sources found. Try searching with different keywords like 'Crop', 'Scheme', 'Mandi', or 'Census'.")
        
    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="background: #FFFFFF; border: 1px solid #D0D5DA; padding: 14px 18px; border-radius: 10px; text-align: center; color: #4A4A4A; font-size: 12px; font-style: italic; font-weight: 500;">
            All figures sourced from official government portals and NABARD model project reports unless otherwise marked.
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# Control Flow — Single-Page App Dispatcher
# ---------------------------------------------------------
current_step = st.session_state.get("step", "lang")

if current_step in [1, 2, 3, "dashboard", "data_sources", "business_plan", "profile"]:
    render_sidebar()

if current_step == "lang":
    render_step_lang()
elif current_step == "login":
    render_step_login()
elif current_step in ["dashboard"]:
    render_step_dashboard()
elif current_step == "data_sources":
    render_step_data_sources()
elif current_step in [1, 2, 3, "business_plan"]:
    render_step_business_plan()
elif current_step == "profile":
    render_step_profile()
else:
    st.session_state["step"] = "lang"
    st.rerun()
