from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

sys.path.append(str(Path(__file__).resolve().parent / "src"))
from study_entry_submission.app import _initialize_session_state, render_form

if __name__ == "__main__":
    _initialize_session_state()
    render_form()
