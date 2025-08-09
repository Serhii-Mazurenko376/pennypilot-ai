import streamlit as st
from tools.file_extract import extract_text_from_file

st.set_page_config(page_title="PennyPilot • File Upload", page_icon="📎", layout="centered")

st.title("📎 PennyPilot — File Upload & Text Extraction")

tab_manual, tab_upload = st.tabs(["Manual Input", "Upload Files"])

# Keep state so switching tabs won't lose text
if "job_description" not in st.session_state:
    st.session_state.job_description = ""
if "cv_text" not in st.session_state:
    st.session_state.cv_text = ""

with tab_manual:
    st.session_state.job_description = st.text_area("Paste Job Description", value=st.session_state.job_description, height=200)
    st.session_state.cv_text = st.text_area("Paste Your CV", value=st.session_state.cv_text, height=200)

with tab_upload:
    file = st.file_uploader("Upload a file (.pdf, .docx, .txt)", type=["pdf", "docx", "txt"])
    kind = st.radio("This file is:", ["Job Description", "CV"], horizontal=True)

    if file is not None:
        extracted = extract_text_from_file(file)
        if extracted.startswith("Error") or extracted.startswith("Unsupported"):
            st.error(extracted)
        else:
            st.success("Text extracted successfully.")
            st.text_area("Preview", extracted, height=300)
            apply = st.button(f"Use as {kind}")
            if apply:
                if kind == "Job Description":
                    st.session_state.job_description = extracted
                else:
                    st.session_state.cv_text = extracted
                st.toast(f"Inserted into {kind.lower()} field.", icon="✅")

st.divider()
st.subheader("Status")
col1, col2 = st.columns(2)
with col1:
    st.write("**Job Description characters:**", len(st.session_state.job_description))
with col2:
    st.write("**CV characters:**", len(st.session_state.cv_text))

st.caption("Next: hook this into proposal generation.")
