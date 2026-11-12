import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Bank Deposit Prediction",
    page_icon="🏦",
    layout="wide"
)


# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    with open("bank_term_deposit_model.pkl", "rb") as file:
        return pickle.load(file)


try:
    model = load_model()

except Exception as e:
    st.error(f"Unable to load the model: {e}")
    st.stop()


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* Page background */
.stApp {
    background-color: #F4F6FA;
}

/* Main title */
.main-title {
    text-align: left;
    color: #172B4D;
    font-size: 36px;
    font-weight: 700;
}

.bank-icon {
    font-size: 38px;
    margin-right: 12px;
    vertical-align: middle;
}

/* Subtitle */
.subtitle {
    color: #42546A !important;
    font-size: 17px !important;
}

/* Headings */
h1, h2, h3 {
    color: #17365D !important;
    font-weight: 700 !important;
}

/* Normal text */
.stMarkdown p,
.stCaption {
    color: #263445 !important;
}

/* Input labels */
.stTextInput label,
.stNumberInput label,
.stSelectbox label {
    color: #172B4D !important;
    font-weight: 600 !important;
}

/* Input fields */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #FFFFFF !important;
    border: 1px solid #AAB7C7 !important;
}

/* Input text */
div[data-baseweb="select"] span,
div[data-baseweb="input"] input {
    color: #172B4D !important;
}

/* Prediction messages */
div[data-testid="stAlert"] p,
div[data-testid="stAlert"] span {
    color: #172B4D !important;
    font-weight: 600 !important;
}

/* Metric labels */
div[data-testid="stMetricLabel"] p {
    color: #42546A !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #17365D !important;
    font-size: 30px !important;
    font-weight: 700 !important;
}

/* Predict button */
div[data-testid="stFormSubmitButton"] button {
    background-color: #17365D !important;
    color: #FFFFFF !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    min-height: 48px;
    border-radius: 8px;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #245887 !important;
    color: #FFFFFF !important;
}

/* Footer */
.stCaption,
small {
    color: #526174 !important;
}

/* Form */
div[data-testid="stForm"] {
    background-color: #FFFFFF;
    padding: 22px;
    border: 1px solid #DCE3ED;
    border-radius: 12px;
}

/* Help icon color */
[data-testid="stTooltipIcon"] svg,
[data-testid="stTooltipIcon"] svg path {
    color: #17365D !important;
    stroke: #17365D !important;
}

/* Positive prediction - Coral */
.positive-banner {
    margin-top: 20px;
    margin-bottom: 25px;
    background-color: #E1F2E7;
    color: #285C3B;
    padding: 18px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
}

/* Negative prediction - Green */
.negative-banner {
    margin-top: 20px;
    margin-bottom: 25px;
    background-color: #FCE4E1;
    color: #873D37;
    padding: 18px;
    border-radius: 10px;
    font-size: 17px;
    font-weight: 600;
}

/* Progress bar background */
.custom-progress {
    background-color: #E1E5EB;
    height: 10px;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 10px;
}


</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title"><span class="bank-icon">🏦</span>Bank Term Deposit Subscription Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict whether a customer is likely to subscribe to a term deposit before the marketing call.</div>',
    unsafe_allow_html=True
)

st.divider()


# ---------------- INPUT FORM ----------------

st.subheader("Customer Information")

with st.form("prediction_form"):

    st.markdown("### Personal Details")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=35
        )

        job = st.selectbox(
            "Job",
            [
                "Admin",
                "Blue-collar",
                "Entrepreneur",
                "Housemaid",
                "Management",
                "Retired",
                "Self-employed",
                "Services",
                "Student",
                "Technician",
                "Unemployed",
                "Unknown"
            ]
        )

        marital = st.selectbox(
            "Marital Status",
            ["Married", "Single", "Divorced"]
        )

        education = st.selectbox(
            "Education",
            ["Primary", "Secondary", "Tertiary", "Unknown"]
        )

    with col2:

        default = st.selectbox(
            "Has Credit in Default?",
            ["No", "Yes"]
        )

        balance = st.number_input(
            "Average Yearly Balance",
            value=1000
        )

        housing = st.selectbox(
            "Housing Loan",
            ["Yes", "No"]
        )

        loan = st.selectbox(
            "Personal Loan",
            ["Yes", "No"]
        )

    st.divider()

    st.markdown("### Previous Marketing Information")

    col3, col4 = st.columns(2)

    with col3:

        contact = st.selectbox(
            "Contact Communication Type",
            ["Cellular", "Telephone", "Unknown"]
        )

        pdays = st.number_input(
            "Days Since Previous Contact",
            min_value=-1,
            max_value=1000,
            value=-1,
            help="-1 indicates that the customer was not previously contacted."
        )

    with col4:

        previous = st.number_input(
            "Number of Previous Contacts",
            min_value=0,
            max_value=1000,
            value=0
        )

        poutcome = st.selectbox(
            "Previous Campaign Outcome",
            ["Success", "Failure", "Other", "Unknown"]
        )

    st.divider()

    submitted = st.form_submit_button(
        "🔍 Predict Subscription",
        use_container_width=True
    )


# ---------------- PREDICTION ----------------

if submitted:

    input_data = pd.DataFrame([{
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "balance": balance,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome
    }])

    # Check model features and arrange columns

    expected_features = [
        "age", "job", "marital", "education",
        "default", "balance", "housing", "loan",
        "contact", "pdays", "previous", "poutcome"
    ]

    if hasattr(model, "feature_names_in_"):

        model_features = list(model.feature_names_in_)

        if set(input_data.columns) != set(model_features):
            st.error(
                "The input features do not match the trained model. "
                "Please check your saved model."
            )
            st.stop()

        input_data = input_data[model_features]

    else:
        input_data = input_data[expected_features]

    try:

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]

        # Locate class probabilities correctly
        classes = list(model.classes_)

        subscription_index = classes.index(1)
        no_subscription_index = classes.index(0)

        subscription_probability = (
            probabilities[subscription_index] * 100
        )

        no_subscription_probability = (
            probabilities[no_subscription_index] * 100
        )

        st.divider()

        # Set colours based on prediction
        if prediction == 1:
            banner_class = "positive-banner"
            progress_color = "#62A77A"
            message = "The customer is likely to subscribe to the term deposit."

        else:
            banner_class = "negative-banner"
            progress_color = "#E77B70"
            message = "The customer is unlikely to subscribe to the term deposit."

        # Display prediction
        st.subheader("Prediction Result")

        st.markdown(f"""
        <div class="{banner_class}">
            {message}
        </div>
        """, unsafe_allow_html=True)


        st.markdown(
            f"""
            <div style="display:flex; align-items:center; gap:15px;">
                <div style="font-size:18px; color:#64748B; font-weight:600;">
                    Subscription Probability:
                </div>
                <div style="font-size:30px; color:#4338CA; font-weight:700;">
                    {subscription_probability:.2f}%
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(f"""
        <div class="custom-progress">
            <div style="
                width: {subscription_probability:.2f}%;
                background-color: {progress_color};
                height: 12px;
                border-radius: 10px;">
            </div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Prediction error: {e}")


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Machine Learning Project | Bank Term Deposit Subscription Prediction"
)

