"""
LangGraph Agent for Generating Expert Outreach Emails
Fully offline version - no API calls required!
"""

from langgraph.graph import StateGraph, END
from typing import TypedDict, List
import random

# State definition for the agent
class EmailState(TypedDict):
    recipient_name: str
    recipient_expertise: List[str]
    topics_researching: List[str]
    sender_name: str
    sender_background: str
    email_draft: str
    email_subject: str
    refinement_notes: str
    tone: str  # 'formal', 'casual', or 'balanced'

# Template-based content generation
class EmailGenerator:
    
    SUBJECT_TEMPLATES = [
        "Seeking Your Expertise on {topic}",
        "Question About {topic} - Would Love Your Insights",
        "Research Inquiry: {topic}",
        "Hoping to Learn From Your {expertise} Experience",
        "Quick Question on {topic}",
    ]
    
    OPENING_TEMPLATES = [
        "I hope this email finds you well.",
        "I hope you're doing well.",
        "I hope this message reaches you at a good time.",
        "I trust this email finds you well.",
    ]
    
    INTRODUCTION_TEMPLATES = [
        "My name is {sender}, and I'm {background}.",
        "I'm {sender}, currently {background}.",
        "Allow me to introduce myself—I'm {sender}, {background}.",
    ]
    
    RESEARCH_CONTEXT = [
        "I've been researching {topics} and came across your work in {expertise}.",
        "Recently, I've been diving deep into {topics}, and your expertise in {expertise} is highly relevant.",
        "I'm currently exploring {topics}, and I understand you have significant experience with {expertise}.",
        "While studying {topics}, I noticed your impressive background in {expertise}.",
    ]
    
    REQUEST_TEMPLATES = [
        "I would be incredibly grateful if you could share some insights or point me toward helpful resources.",
        "I'd love to hear your perspective on this, even if just briefly.",
        "Would you be open to a short conversation or email exchange about this?",
        "Any guidance you could provide would be tremendously valuable to my research.",
        "I would appreciate any thoughts or advice you might be willing to share.",
    ]
    
    RESPECT_TIME = [
        "I completely understand if you're too busy, and I appreciate you even reading this.",
        "I know your time is valuable, so even a brief response would be wonderful.",
        "No pressure at all—I know how busy you must be.",
        "I respect that you likely have a full schedule, so no worries if you can't respond.",
    ]
    
    CLOSING_TEMPLATES = [
        "Thank you so much for considering my request.",
        "Thank you for your time and consideration.",
        "I really appreciate you taking the time to read this.",
        "Thanks in advance for any help you can provide.",
    ]
    
    SIGNOFFS = [
        "Best regards",
        "Warm regards",
        "Sincerely",
        "Kind regards",
        "Best",
    ]

def generate_subject(state: EmailState) -> EmailState:
    """Generate email subject line"""
    templates = EmailGenerator.SUBJECT_TEMPLATES
    template = random.choice(templates)
    
    # Pick the most relevant topic/expertise
    topic = state['topics_researching'][0] if state['topics_researching'] else "your research"
    expertise = state['recipient_expertise'][0] if state['recipient_expertise'] else "expertise"
    
    subject = template.format(topic=topic, expertise=expertise)
    state['email_subject'] = subject
    return state

def draft_email(state: EmailState) -> EmailState:
    """Generate the email body"""
    
    # Select templates based on tone
    opening = random.choice(EmailGenerator.OPENING_TEMPLATES)
    intro = random.choice(EmailGenerator.INTRODUCTION_TEMPLATES)
    context = random.choice(EmailGenerator.RESEARCH_CONTEXT)
    request = random.choice(EmailGenerator.REQUEST_TEMPLATES)
    respect = random.choice(EmailGenerator.RESPECT_TIME)
    closing = random.choice(EmailGenerator.CLOSING_TEMPLATES)
    signoff = random.choice(EmailGenerator.SIGNOFFS)
    
    # Format topics and expertise
    topics_str = " and ".join(state['topics_researching'][:2])
    expertise_str = state['recipient_expertise'][0] if state['recipient_expertise'] else "your field"
    
    # Build email
    email_parts = [
        f"Dear {state['recipient_name']},",
        "",
        opening,
        "",
        intro.format(sender=state['sender_name'], background=state['sender_background']),
        "",
        context.format(topics=topics_str, expertise=expertise_str),
    ]
    
    # Add specific topics if multiple
    if len(state['topics_researching']) > 1:
        email_parts.append("")
        email_parts.append(f"Specifically, I'm trying to better understand:")
        for topic in state['topics_researching'][:3]:
            email_parts.append(f"• {topic}")
    
    email_parts.extend([
        "",
        request,
        "",
        respect,
        "",
        closing,
        "",
        signoff + ",",
        state['sender_name']
    ])
    
    state['email_draft'] = "\n".join(email_parts)
    return state

def personalize_email(state: EmailState) -> EmailState:
    """Add personalization touches"""
    email = state['email_draft']
    
    # Add connection if multiple expertise areas match topics
    matching_areas = set()
    for expertise in state['recipient_expertise']:
        for topic in state['topics_researching']:
            if any(word in topic.lower() for word in expertise.lower().split()):
                matching_areas.add(expertise)
    
    if matching_areas:
        # Add a line about the connection
        connection_line = f"\n\nYour work on {list(matching_areas)[0]} seems particularly relevant to what I'm exploring."
        # Insert before the request paragraph
        parts = email.split('\n\n')
        parts.insert(-3, connection_line.strip())
        email = '\n\n'.join(parts)
    
    state['email_draft'] = email
    return state

def validate_email(state: EmailState) -> EmailState:
    """Final validation and cleanup"""
    email = state['email_draft']
    
    # Ensure reasonable length (not too long)
    lines = email.split('\n')
    if len(lines) > 25:
        # Trim bullet points if too many
        email_parts = []
        bullet_count = 0
        for line in lines:
            if line.strip().startswith('•'):
                bullet_count += 1
                if bullet_count <= 3:
                    email_parts.append(line)
            else:
                email_parts.append(line)
        email = '\n'.join(email_parts)
    
    state['email_draft'] = email
    return state

# Build the graph
def create_email_agent():
    """Create the LangGraph workflow"""
    
    workflow = StateGraph(EmailState)
    
    # Add nodes
    workflow.add_node("subject", generate_subject)
    workflow.add_node("draft", draft_email)
    workflow.add_node("personalize", personalize_email)
    workflow.add_node("validate", validate_email)
    
    # Define edges
    workflow.set_entry_point("subject")
    workflow.add_edge("subject", "draft")
    workflow.add_edge("draft", "personalize")
    workflow.add_edge("personalize", "validate")
    workflow.add_edge("validate", END)
    
    return workflow.compile()

# Main execution function
def generate_outreach_email(
    recipient_name: str,
    recipient_expertise: List[str],
    topics_researching: List[str],
    sender_name: str,
    sender_background: str,
    tone: str = "balanced"
) -> dict:
    """
    Generate a personalized expert outreach email
    
    Args:
        recipient_name: Name of the expert you're reaching out to
        recipient_expertise: List of their areas of expertise
        topics_researching: List of topics you're researching
        sender_name: Your name
        sender_background: Brief description of your background
        tone: Email tone - 'formal', 'casual', or 'balanced' (default)
    
    Returns:
        Dictionary with subject and email_body
    """
    
    # Create initial state
    initial_state = EmailState(
        recipient_name=recipient_name,
        recipient_expertise=recipient_expertise,
        topics_researching=topics_researching,
        sender_name=sender_name,
        sender_background=sender_background,
        email_draft="",
        email_subject="",
        refinement_notes="",
        tone=tone
    )
    
    # Create and run the agent
    app = create_email_agent()
    result = app.invoke(initial_state)
    
    return {
        "subject": result['email_subject'],
        "body": result['email_draft'],
        "recipient": recipient_name
    }

# Example usage
if __name__ == "__main__":
    print("🤖 Expert Outreach Email Generator (Offline Mode)")
    print("=" * 70)
    
    # Example 1: Reaching out to a machine learning expert
    print("\n📧 Example 1: Machine Learning Expert\n")
    result = generate_outreach_email(
        recipient_name="Dr. Sarah Chen",
        recipient_expertise=[
            "neural network optimization",
            "computer vision",
            "model interpretability"
        ],
        topics_researching=[
            "attention mechanisms in vision transformers",
            "techniques for making deep learning models more interpretable",
            "efficient training strategies for large models"
        ],
        sender_name="Alex Rivera",
        sender_background="PhD student in Computer Science focusing on AI safety and transparency"
    )
    
    print(f"SUBJECT: {result['subject']}")
    print("\n" + "=" * 70)
    print(result['body'])
    print("=" * 70)
    
    # Example 2: Cybersecurity expert
    print("\n\n📧 Example 2: Cybersecurity Expert\n")
    result2 = generate_outreach_email(
        recipient_name="Prof. James Martinez",
        recipient_expertise=[
            "cybersecurity",
            "cryptography",
            "blockchain security"
        ],
        topics_researching=[
            "zero-knowledge proofs in authentication systems",
            "practical applications of homomorphic encryption"
        ],
        sender_name="Jordan Lee",
        sender_background="security researcher at a fintech startup"
    )
    
    print(f"SUBJECT: {result2['subject']}")
    print("\n" + "=" * 70)
    print(result2['body'])
    print("=" * 70)
    
    # Example 3: NLP expert
    print("\n\n📧 Example 3: Natural Language Processing Expert\n")
    result3 = generate_outreach_email(
        recipient_name="Dr. Emily Watson",
        recipient_expertise=[
            "natural language processing",
            "dialogue systems",
            "sentiment analysis"
        ],
        topics_researching=[
            "context-aware language models",
            "emotional intelligence in conversational AI"
        ],
        sender_name="Sam Patel",
        sender_background="graduate student researching human-AI interaction"
    )
    
    print(f"SUBJECT: {result3['subject']}")
    print("\n" + "=" * 70)
    print(result3['body'])
    print("=" * 70)
    
    # Batch generation example
    print("\n\n🔄 Batch Generation Example")
    print("=" * 70)
    
    recipients_list = [
        {
            "name": "Dr. Aisha Johnson",
            "expertise": ["quantum computing", "quantum algorithms"],
            "topics": ["NISQ algorithms", "quantum error correction"]
        },
        {
            "name": "Prof. Chen Wei",
            "expertise": ["robotics", "autonomous systems", "sensor fusion"],
            "topics": ["SLAM algorithms", "multi-robot coordination"]
        }
    ]
    
    for i, recipient in enumerate(recipients_list, 1):
        print(f"\n📨 Email {i} of {len(recipients_list)}")
        email = generate_outreach_email(
            recipient_name=recipient["name"],
            recipient_expertise=recipient["expertise"],
            topics_researching=recipient["topics"],
            sender_name="Taylor Morgan",
            sender_background="postdoctoral researcher"
        )
        print(f"TO: {recipient['name']}")
        print(f"SUBJECT: {email['subject']}\n")
        print(email['body'][:200] + "...\n")  # Preview only
        print("-" * 70)
    
    print("\n✅ All emails generated successfully!")
    print("\n💡 Tip: Each run generates slightly different variations!")
    print("   Run the script multiple times to see different phrasings.\n")