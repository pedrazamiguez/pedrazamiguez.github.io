---
name: job-tracker
description: >-
  Tracks, logs, and queries Andrés Pedraza Míguez's job applications, interview debriefs, notes, contacts, and compensation details. Use whenever Andrés mentions applying for a role, debriefing an interview, recording thoughts/feelings/difficult questions, or asking about salary ranges, contacts, or application status.
---

# Job Application & Interview Tracker Skill

Use this skill whenever Andrés:
1. Mentions applying for a new role or company.
2. Shares interview experiences, "brain-dumps" feedback, feelings, or notes from a call.
3. Mentions tricky questions or topics he stumbled on during an interview.
4. Asks for information about his applications (e.g., *"What was the salary range for Company X?"*, *"Who interviewed me in round 2?"*, *"What were my action items for next round?"*).
5. Updates an application's stage (e.g., moved to tech interview, offer received, rejected).

---

## 📁 Storage Architecture (Private & Git-Ignored)

All tracking data lives under `applications/`, which is **strictly excluded from Git** via `.gitignore` to protect private recruiter names, salary numbers, and personal sentiments:

- **`applications/TRACKER.md`**: The master pipeline dashboard table (Company, Role, Stage, Rate/Salary, Vibe, Next Step, Link).
- **`applications/companies/<company_slug>.md`**: Dedicated dossier for each opportunity (e.g., `applications/companies/revolut.md`), initialized from `applications/companies/_template.md`.

---

## 🛠️ Step-by-Step Procedures

### 1. Adding a New Application
When Andrés applies or prepares an application:
1. Create a slugified markdown file: `applications/companies/<company_slug>.md` using `applications/companies/_template.md` as the baseline.
2. Fill in known details: Company Name, Role Title, Stated Salary / Day Rate, Contract Type (Outside IR35 / Perm), Link to the tailored CV (e.g. `tailored/CV_Andres_Pedraza_<Company>_<Role>.md`), and any known recruiters/contacts.
3. Add a new row to the **Active Pipeline Overview** table in `applications/TRACKER.md`.

---

### 2. Processing an Interview Debrief ("Brain-Dump" to Structured Notes)
When Andrés shares casual thoughts like:
> *"I had this feeling with X... during the interview they asked me Y that I didn't know the answer to, so I need to come up with something else to make up for it... Interviewer was Dave, vibe was 4/5."*

**Agent Action:**
1. Open and update `applications/companies/<company_slug>.md`.
2. Add a new round entry under `## 📋 Interview Rounds & Debriefs` with:
   - **Date & Interviewer(s)**.
   - **Vibe & Culture Impressions**: Capture the honest gut feeling and tone.
   - **Questions & Responses**: Cleanly format what was asked.
   - **Tough Questions / Stumbled Areas**: Document the exact question and what happened without sugarcoating.
   - **Make-up / Prep Strategy**: Provide actionable points or study topics to address this gap in the next round or follow-up email.
3. Update `applications/TRACKER.md`:
   - Update **Stage**, **Vibe**, and **Next Action / Date**.

---

### 3. Querying & Retrieving Application Data
When Andrés asks questions like:
- *"What was the salary / rate for Revolut?"*
- *"Who was my contact at Company X?"*
- *"What were the questions I struggled with in my last interview?"*
- *"Show me all my active applications."*

**Agent Action:**
1. Inspect `applications/TRACKER.md` or use `grep_search` / `view_file` on `applications/companies/<company_slug>.md`.
2. Provide a clear, concise, direct answer summarizing the exact requested details (e.g., rates, recruiter contacts, tricky questions, next dates).

---

### 4. Updating Outcomes (Offers, Rejections, Withdrawals)
When an application concludes:
1. Update status in `applications/companies/<company_slug>.md`.
2. Move the entry in `applications/TRACKER.md` from **Active Pipeline Overview** to **Inactive / Closed Applications**, noting the final outcome and key takeaways.
