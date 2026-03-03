"""
Response Generation Module
Note: This prototype uses rule-based responses to demonstrate the concept reliably.
The architecture is designed to be model-agnostic - swap this function with any LLM API.
"""

async def get_bot_response(user_input: str):
    """
    Analyze user input and return structured response.
    
    This function currently uses keyword matching to demonstrate the concept.
    In production, I would replace this with calls to OpenAI, OpenRouter, or Gemini.
    The interface remains identical - that's the beauty of clean architecture!
    
    Args:
        user_input: Raw text from the user
        
    Returns:
        Dictionary with reply, category, and priority
    """
    
    # Normalize input for matching
    # Learned: always lowercase for case-insensitive matching
    text = user_input.lower().strip()
    
    # Define keyword categories
    # This felt right after my experience at Outlier and Ministry
    account_keywords = ["password", "login", "forgot", "account", "access", "signin", "locked", "verify"]
    billing_keywords = ["charge", "billing", "payment", "refund", "money", "paid", "invoice", "subscription", "cost"]
    technical_keywords = ["error", "bug", "crash", "broken", "glitch", "not working", "issue", "fail", "freeze"]
    
    # Check for matches
    # I could make this more sophisticated with NLP, but keeping it simple for now
    if any(word in text for word in account_keywords):
        category = "account"
        priority = "high"
        # Notice: we don't ask for passwords - security first!
        reply = "I can help with account access. For security reasons, please use the 'Forgot Password' link on the login page. If you need immediate assistance, a human agent can help verify your identity."
        
    elif any(word in text for word in billing_keywords):
        category = "billing"
        priority = "high"
        # This is the critical human boundary - flagged for review
        reply = "I understand you have a billing question. Since this involves financial data, I've flagged this for a human agent to review your account details. A team member will reach out within 2 hours."
        
    elif any(word in text for word in technical_keywords):
        category = "technical"
        priority = "medium"
        # Gathering context helps the human agent later
        reply = "I've identified a potential technical issue. Can you describe what you were doing when this occurred? Including your device and browser helps us troubleshoot faster."
        
    elif "help" in text or "question" in text or "how" in text or "what" in text:
        category = "general"
        priority = "low"
        # Routine questions can be self-served
        reply = "Thanks for your question. While a human agent reviews your ticket, you might find answers faster in our help center. Would you like me to point you there?"
        
    else:
        # Catch-all for anything we missed
        category = "general"
        priority = "low"
        reply = "Thanks for reaching out. I've logged your message and will route it to the right team. You'll hear back within 24 hours."
    
    # Structure the response
    # This format matches what the frontend expects
    return {
        "reply": reply,
        "category": category,
        "priority": priority
    }

# Future improvements I'd make:
# 1. Add sentiment analysis using transformers
# 2. Connect to actual LLM API
# 3. Add learning from agent corrections
# 4. Implement feedback loop for continuous improvement