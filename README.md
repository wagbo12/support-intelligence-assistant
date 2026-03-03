# Support Intelligence Assistant

**An AI-assisted ticket triage system that demonstrates effective human and AI collaboration in customer support.**

Built for the Wealthsimple AI Builder submission by **
About Me
I'm Williams Agbo, a recent Software Engineering graduate with experience in:

Data validation and ETL workflows (Outlier)

API integration and cloud deployment (Ministry)

Full-stack development (Drum Rock, Kid R Key)

User support and training (Walmart, Kid R Key)

Certifications: Azure AI900, IBM Data Analyst
Years with AI tools: 2+ years**.

---

## The Problem

Customer support teams receive large volumes of tickets every day. A significant portion of an agent’s time is spent on repetitive intake work such as reading tickets, identifying the issue type, assigning priority, and drafting basic responses.

This manual triage process slows down response times and prevents agents from focusing on complex cases that require human judgment, empathy, and decision making.

---

## The Solution

The **Support Intelligence Assistant** automates the early stage of the support workflow. The system analyzes incoming tickets, categorizes them, assigns priority, and generates suggested responses.

This allows human agents to spend their time where it matters most: resolving complex issues and interacting with customers.

### Key Capabilities

• Automatic ticket categorization  
(account, billing, technical, general)

• Priority assignment  
(high, medium, low)

• AI generated response suggestions

• Human decision boundary detection  
Sensitive tickets are automatically flagged for human review

---

## System Architecture

Frontend (HTML / CSS / JavaScript(soon)) ↔ FastAPI Backend ↔ Response Logic

The project is intentionally structured with clear separation of responsibilities.

**index.html**  
User interface for submitting and reviewing tickets.

**main.py**  
FastAPI server that handles routing, request processing, and CORS configuration.

**chatbot.py**  
Response generation logic. This component is intentionally modular so it can easily be replaced with any LLM integration.

---

## Design Philosophy

The central idea behind this project is **defining clear boundaries between AI capability and human responsibility**.

AI should accelerate workflows, not replace judgment when sensitive decisions are involved.

| Ticket Type | AI Role | Human Role |
|-------------|--------|------------|
| General questions | Provide immediate answers | Review if needed |
| Technical issues | Gather context and suggest steps | Troubleshoot |
| Account access | Provide recovery instructions | Verify identity |
| Billing or financial | Flag for human review | Handle securely |

### Critical Safety Boundary

Any ticket involving financial data or account security is automatically escalated.

AI may prepare context for the support agent but **cannot take action on sensitive requests**.

---

## Running the Project Locally

Clone the repository

```bash
git clone https://github.com/[your-username]/support-intelligence-assistant
cd support-intelligence-assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac or Linux**

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the server

```bash
uvicorn main:app --reload --port 8000
```

Open your browser and go to

```
http://127.0.0.1:8000
```

---

## About This Prototype

This prototype uses a rule based response system to demonstrate the concept.

I discovered the Wealthsimple AI Builder opportunity only hours before the submission deadline, so I focused on designing a reliable system that clearly demonstrates the **human AI collaboration model**.

The architecture is intentionally **model agnostic**. The `get_bot_response()` function can be replaced with any LLM provider such as OpenAI, Gemini, or OpenRouter without changing the rest of the system.

This design choice highlights the most important aspects of the solution:

• system architecture  
• workflow automation  
• clear human AI decision boundaries

---

## Future Improvements

With additional development time, the system could be extended with:

• Integration with a real LLM API for smarter responses  
• Sentiment analysis to better detect urgency and frustration  
• Feedback loops where agent corrections improve the model  
• Authentication and secure ticket storage with a database  
• Analytics dashboard to track support performance and ticket trends
