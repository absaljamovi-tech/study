# Deployment Guide

## Target platform

This application is prepared for deployment to Streamlit Community Cloud. The frontend is implemented as a Streamlit app and the backend logic is contained in a pure function module using the Strategy pattern.

## Deployment files

- `requirements.txt` — specifies `streamlit>=1.25,<2.0`
- `streamlit_app.py` — root Streamlit entry point for deployment
- `src/study_entry_submission/app.py` — actual UI implementation
- `docs/DESIGN.md` — UI contract and design system

## How to deploy

1. Push the repository files to a GitHub repository.
2. Open Streamlit Community Cloud at https://share.streamlit.io
3. Connect your GitHub repository.
4. Set the app entry point to:
   - `streamlit_app.py`
5. Use the default branch (`main`) and deploy.

## Notes

- The app uses Streamlit session state to preserve duplicate title checks during a browser session.
- The deployment only requires `requirements.txt` because Streamlit handles Python dependencies automatically.
- If additional Python dependencies are added in the future, update `requirements.txt` accordingly.
