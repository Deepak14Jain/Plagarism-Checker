import streamlit as st
import requests

st.set_page_config(page_title="Plagiarism Checker", page_icon="📄", layout="centered")

st.title("Plagiarism Checker")
st.markdown(
    """
    <style>
    .result-box {
        background-color: #f6f6f6;
        border-radius: 8px;
        padding: 1.5em;
        margin-bottom: 1em;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("#### Upload the original and submission text files below:")

col1, col2 = st.columns(2)
with col1:
    original_file = st.file_uploader("Original File", type=["txt"], key="original")
with col2:
    submission_file = st.file_uploader("Submission File", type=["txt"], key="submission")

st.markdown("---")

if st.button("🔍 Check Plagiarism", use_container_width=True) and original_file and submission_file:
    with st.spinner("Analyzing files for plagiarism..."):
        files = {
            "original": original_file,
            "submission": submission_file
        }
        try:
            response = requests.post("http://localhost:5050/check", files=files)
            if response.status_code == 200:
                data = response.json()
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                st.subheader("Results")
                similarity_score_col, plagarism_prob_col = st.columns(2)
                with similarity_score_col:
                    st.metric("Similarity Score", f"{data['similarity_score'] * 100:.2f}%")
                with plagarism_prob_col:
                    st.metric("Plagiarism Probability", f"{data['probability'] * 100:.2f}%")
                if data["plagiarized"]:
                    st.error("⚠️ Plagiarism Detected")
                else:
                    st.success("✅ No Plagiarism Detected")
                st.markdown('</div>', unsafe_allow_html=True)

                with st.expander("🔍 Highlighted Matches", expanded=True):
                    original_col, submission_col = st.columns(2)
                    with original_col:
                        with st.container(border=True):
                            st.markdown("**Original Text:**")
                            st.markdown(f'Original: {data["highlighted_original"]}', unsafe_allow_html=True)
                    with submission_col:
                        with st.container(border=True):
                            st.markdown("**Submission Text:**")
                            st.markdown(f'Submission: {data["highlighted_submission"]}', unsafe_allow_html=True)
                    
            else:
                st.error("❌ Error from Flask API. Please check the backend server.")
        except Exception as e:
            st.error(f"🚫 Connection failed: {e}")

else:
    st.info("Please upload both files and click 'Check Plagiarism' to begin.")