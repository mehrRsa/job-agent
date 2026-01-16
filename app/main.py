import streamlit as st

st.set_page_config(
    page_title="Job Application Tracker Agent",
    layout="centered"
)

st.title("🤖 Job Application Tracker Agent")
st.subheader("An agentic AI app to track applications and draft follow-ups")

st.write(
    """
This is the starting point of the appliation.

- store applications 
- use an AI agent to suggest the follow up dates
- draft professional follow-up messages
- require human approval bfore saving actions
"""
)

st.info(" agent logic, database and tools will be added")

"chunk 1: add an add application form"
st.divider()
st.header("➕ Add an application")

with st.form("add_application_form", clear_on_submit=True):
    company = st.text_input("Company *", placeholder="e.g., Nutrien")
    role = st.text_input("Role title *", placeholder="e.g, Intern, Enterprise Applications")
    date_applied = st.date_input("Date applied")
    status = st.selectbox("Status", ["Applied", "Interviewing", "Offer", "Rejected"])
    notes = st.text_area("Notes(optional)", placeholder="Anything important: referral, recuiter name, job link, etc.")

    submitted = st.form_submit_button("Save(for now, just preview)")