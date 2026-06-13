from __future__ import annotations

import datetime
import sys
from pathlib import Path

import streamlit as st

# Ensure the strategy module is importable when running this script directly
sys.path.append(str(Path(__file__).resolve().parent))
from strategy import evaluate_entry_submission


def _initialize_session_state() -> None:
    if "existing_titles" not in st.session_state:
        st.session_state.existing_titles = ["biology hw"]
    if "last_result" not in st.session_state:
        st.session_state.last_result = None


def render_header() -> None:
    st.set_page_config(page_title="Study Entry Submission", page_icon="📝", layout="centered")
    st.title("Study Entry Submission")
    st.caption("Accessible submission UI wired to the strategy-backed evaluation module.")


def render_form() -> None:
    render_header()
    with st.form("submission_form"):
        title = st.text_input(
            label="Entry title",
            placeholder="Enter a unique study entry title",
            help="The title is normalized and compared against past entries to prevent duplicates.",
        )
        content = st.text_area(
            label="Entry content",
            placeholder="Describe what you studied and what you learned.",
            help="Provide the study details for this submission.",
            height=140,
        )
        date_value = st.date_input(
            label="Date",
            value=datetime.date.today(),
            help="Select the date for this study entry.",
        )
        submit_button = st.form_submit_button("Submit entry")

        if submit_button:
            response = evaluate_entry_submission(
                {"title": title, "content": content},
                st.session_state.existing_titles,
                date_value.isoformat(),
            )
            st.session_state.last_result = response

    render_existing_titles()
    render_response_panel()


def render_existing_titles() -> None:
    with st.expander("Current existing titles", expanded=False):
        st.markdown(
            "- " + "\n- ".join(st.session_state.existing_titles)
            if st.session_state.existing_titles
            else "No existing entries yet."
        )


def render_response_panel() -> None:
    result = st.session_state.last_result
    if result is None:
        return

    status = result.get("status")
    if status == "accepted":
        normalized = result["normalized_entry"]
        st.success("Entry accepted.")
        st.write("### Normalized entry")
        st.json(normalized)

        title_key = normalized["title"]
        if title_key not in st.session_state.existing_titles:
            st.session_state.existing_titles.append(title_key)
    else:
        reason = result.get("reason")
        if reason == "validation_failed":
            st.error("Submission rejected: validation failed.")
            for field, message in result.get("errors", {}).items():
                st.warning(f"{field.title()}: {message}")
        elif reason == "duplicate_entry":
            st.warning(
                "Submission rejected: duplicate title detected. Please choose a different title."
            )
        else:
            st.error("Submission rejected: unknown reason.")

    st.write("---")
    st.write("### Backend response payload")
    st.json(result)


if __name__ == "__main__":
    _initialize_session_state()
    render_form()
