import streamlit as st

st.set_page_config(
    page_title="Job Application Tracker Agent",
    layout="centered"
)

#create a list that persists during the streamlit session
if "applications" not in st.session_state:
    st.session_state["applications"] = []

# Store selected app in st.session_state
if "selected_app_id" not in st.session_state:
    st.session_state["selected_app_id"] = None

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

#chunk 1: add an add application form
st.divider()
st.header("➕ Add an application")

with st.form("add_application_form", clear_on_submit=True):
    company = st.text_input("Company *", placeholder="e.g., Nutrien")
    role = st.text_input("Role title *", placeholder="e.g, Intern, Enterprise Applications")
    date_applied = st.date_input("Date applied")
    status = st.selectbox("Status", ["Applied", "Interviewing", "Offer", "Rejected"])
    notes = st.text_area("Notes(optional)", placeholder="Anything important: referral, recuiter name, job link, etc.")

    submitted = st.form_submit_button("Save(for now, just preview)")

# Save form submission into session_state (storing data inside the app temporary)
if submitted:
    if not company.strip() or not role.strip():
        st.error("Please fill in the required fileds: Company and Role title.")
    else:
        
        new_app = {
                "id": len(st.session_state["applications"]) + 1,
                "company": company.strip(),
                "role": role.strip(),
                "date_applied" : str(date_applied),
                "status": status,
                "notes": notes.strip(),
                
        }

        st.session_state["applications"].append(new_app)
        st.success("Application saved (in memory.)")
        

# Render the application in a table
st.divider()
st.header("📋 Applications")

apps = st.session_state["applications"]

if len(apps) == 0:
    st.info("No application yet. Add one above.")
else:
    st.dataframe(apps, use_container_width=True)

# Select an application
if len(apps) > 0:

    st.subheader("🔎 Select an application")

    options = [f'#{a["id"]} — {a["company"]} — {a["role"]}' for a in apps]
    selected = st.selectbox("Choose one", options)

    selected_id = int(selected.split("—")[0].strip().replace("#", ""))
    selected_app = next(a for a in apps if a["id"] == selected_id)

    st.write("### Selected application")
    st.json(selected_app)
