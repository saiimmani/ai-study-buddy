"""
Study Spark - AI-Powered Study Buddy
A comprehensive study assistant for students
"""

import streamlit as st
import google.generativeai as genai
import os
import json
from typing import List, Dict
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Study Spark - AI Study Buddy",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize API
def initialize_ai():
    """Initialize the Google Generative AI API"""
    try:
        # Try to get API key from Streamlit secrets (for deployment)
        api_key = st.secrets.get("GOOGLE_API_KEY")
    except:
        # Fall back to environment variable (for local development)
        api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        st.error("⚠️ No API key found! Please set GOOGLE_API_KEY in your environment or Streamlit secrets.")
        st.stop()
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-2.0-flash')

# AI Helper Functions
def generate_ai_response(model, prompt: str) -> str:
    """Generate a response from the AI model"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"

def explain_concept(model, concept: str) -> str:
    """Generate an explanation for a concept"""
    prompt = f"""You are a helpful study assistant for high school and college students. 
    Explain the following concept in a clear, easy-to-understand way. 
    Use simple language, analogies, and examples where appropriate.
    
    Concept: {concept}
    
    Provide a comprehensive but concise explanation that a student can understand."""
    
    return generate_ai_response(model, prompt)

def summarize_text(model, text: str, length: str = "Medium") -> str:
    """Summarize the provided text"""
    length_instructions = {
        "Short": "in 3-5 bullet points",
        "Medium": "in 7-10 bullet points",
        "Detailed": "in detailed paragraphs with key points highlighted"
    }
    
    prompt = f"""You are a study assistant helping students understand their notes and materials.
    Summarize the following text {length_instructions[length]}.
    Focus on the main ideas and key concepts that students need to know.
    
    Text to summarize:
    {text}
    
    Summary:"""
    
    return generate_ai_response(model, prompt)

def generate_quiz(model, text: str, num_questions: int = 5) -> List[Dict]:
    """Generate quiz questions from the text"""
    prompt = f"""You are a study assistant creating quiz questions for students.
    Based on the following text, generate exactly {num_questions} multiple-choice questions.
    
    Text:
    {text}
    
    Format your response as a JSON array with this exact structure:
    [
        {{
            "question": "Question text here?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correct_answer": 0,
            "explanation": "Brief explanation of why this is correct"
        }}
    ]
    
    Make sure:
    - Questions test understanding, not just memorization
    - All options are plausible
    - correct_answer is the index (0-3) of the correct option
    - Include a brief explanation for each answer
    
    Return ONLY the JSON array, no additional text."""
    
    try:
        response = generate_ai_response(model, prompt)
        # Try to extract JSON if there's extra text
        start_idx = response.find('[')
        end_idx = response.rfind(']') + 1
        if start_idx != -1 and end_idx != 0:
            json_str = response[start_idx:end_idx]
            return json.loads(json_str)
        else:
            return json.loads(response)
    except Exception as e:
        st.error(f"Error parsing quiz questions: {str(e)}")
        return []

def generate_flashcards(model, text: str, num_cards: int = 10) -> List[Dict]:
    """Generate flashcards from the text"""
    prompt = f"""You are a study assistant creating flashcards for students.
    Based on the following text, identify the {num_cards} most important terms, concepts, or ideas
    and create flashcards for them.
    
    Text:
    {text}
    
    Format your response as a JSON array with this exact structure:
    [
        {{
            "front": "Term or Question",
            "back": "Definition or Answer"
        }}
    ]
    
    Make sure:
    - The front is concise (a term, concept, or question)
    - The back provides a clear, complete explanation or answer
    - Focus on the most important concepts for studying
    
    Return ONLY the JSON array, no additional text."""
    
    try:
        response = generate_ai_response(model, prompt)
        # Try to extract JSON if there's extra text
        start_idx = response.find('[')
        end_idx = response.rfind(']') + 1
        if start_idx != -1 and end_idx != 0:
            json_str = response[start_idx:end_idx]
            return json.loads(json_str)
        else:
            return json.loads(response)
    except Exception as e:
        st.error(f"Error parsing flashcards: {str(e)}")
        return []

# Feature 1: Concept Explainer
def concept_explainer_page(model):
    """Page for explaining concepts"""
    st.header("🧠 Concept Explainer")
    st.write("Ask me to explain any concept, term, or topic you're learning about!")
    
    concept = st.text_input(
        "Enter a concept or question:",
        placeholder="e.g., What is photosynthesis? or Explain the Pythagorean theorem"
    )
    
    if st.button("Explain", type="primary", use_container_width=True):
        if concept:
            with st.spinner("🤔 Thinking..."):
                explanation = explain_concept(model, concept)
                st.success("Here's your explanation:")
                st.markdown(explanation)
        else:
            st.warning("Please enter a concept or question to explain.")

# Feature 2: Note Summarizer
def note_summarizer_page(model):
    """Page for summarizing notes"""
    st.header("📝 Note Summarizer")
    st.write("Paste your notes, articles, or textbook chapters to get a concise summary!")
    
    # Input method selection
    input_method = st.radio("Choose input method:", ["Paste Text", "Upload File"])
    
    text_to_summarize = ""
    
    if input_method == "Paste Text":
        text_to_summarize = st.text_area(
            "Paste your text here:",
            height=200,
            placeholder="Paste your lecture notes, article, or chapter text here..."
        )
    else:
        uploaded_file = st.file_uploader("Upload a text file", type=["txt", "md"])
        if uploaded_file is not None:
            text_to_summarize = uploaded_file.read().decode("utf-8")
            st.text_area("File content:", text_to_summarize, height=150, disabled=True)
    
    summary_length = st.selectbox(
        "Summary length:",
        ["Short", "Medium", "Detailed"],
        index=1
    )
    
    if st.button("Summarize", type="primary", use_container_width=True):
        if text_to_summarize:
            with st.spinner("📚 Analyzing and summarizing..."):
                summary = summarize_text(model, text_to_summarize, summary_length)
                st.success("Here's your summary:")
                st.markdown(summary)
        else:
            st.warning("Please provide text to summarize.")

# Feature 3: Quiz Generator
def quiz_generator_page(model):
    """Page for generating and taking quizzes"""
    st.header("❓ Quiz Generator")
    st.write("Test your knowledge! Provide text or a topic to generate a quiz.")
    
    # Initialize session state for quiz
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = []
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'answered' not in st.session_state:
        st.session_state.answered = False
    if 'selected_answer' not in st.session_state:
        st.session_state.selected_answer = None
    if 'quiz_complete' not in st.session_state:
        st.session_state.quiz_complete = False
    
    # Quiz generation section
    if not st.session_state.quiz_questions or st.session_state.quiz_complete:
        text_for_quiz = st.text_area(
            "Paste text or describe a topic:",
            height=150,
            placeholder="Paste study material or describe a topic you want to be quizzed on..."
        )
        
        num_questions = st.slider("Number of questions:", 3, 10, 5)
        
        if st.button("Generate Quiz", type="primary", use_container_width=True):
            if text_for_quiz:
                with st.spinner("🎯 Creating quiz questions..."):
                    questions = generate_quiz(model, text_for_quiz, num_questions)
                    if questions:
                        st.session_state.quiz_questions = questions
                        st.session_state.current_question = 0
                        st.session_state.score = 0
                        st.session_state.answered = False
                        st.session_state.selected_answer = None
                        st.session_state.quiz_complete = False
                        st.rerun()
            else:
                st.warning("Please provide text or a topic for the quiz.")
    
    # Quiz taking section
    if st.session_state.quiz_questions and not st.session_state.quiz_complete:
        current_q = st.session_state.current_question
        total_q = len(st.session_state.quiz_questions)
        
        st.progress((current_q) / total_q)
        st.write(f"**Question {current_q + 1} of {total_q}**")
        st.write(f"**Score: {st.session_state.score}/{current_q}**")
        
        question_data = st.session_state.quiz_questions[current_q]
        
        st.subheader(question_data['question'])
        
        # Display options
        if not st.session_state.answered:
            selected = st.radio(
                "Select your answer:",
                question_data['options'],
                key=f"q_{current_q}"
            )
            
            if st.button("Submit Answer", type="primary"):
                st.session_state.selected_answer = question_data['options'].index(selected)
                st.session_state.answered = True
                if st.session_state.selected_answer == question_data['correct_answer']:
                    st.session_state.score += 1
                st.rerun()
        
        else:
            # Show result
            correct_idx = question_data['correct_answer']
            user_answer_idx = st.session_state.selected_answer
            
            for idx, option in enumerate(question_data['options']):
                if idx == correct_idx:
                    st.success(f"✅ {option} (Correct Answer)")
                elif idx == user_answer_idx and idx != correct_idx:
                    st.error(f"❌ {option} (Your Answer)")
                else:
                    st.write(f"○ {option}")
            
            st.info(f"**Explanation:** {question_data['explanation']}")
            
            # Navigation
            col1, col2 = st.columns(2)
            with col2:
                if current_q < total_q - 1:
                    if st.button("Next Question →", type="primary", use_container_width=True):
                        st.session_state.current_question += 1
                        st.session_state.answered = False
                        st.session_state.selected_answer = None
                        st.rerun()
                else:
                    if st.button("Finish Quiz", type="primary", use_container_width=True):
                        st.session_state.quiz_complete = True
                        st.rerun()
    
    # Quiz completion
    if st.session_state.quiz_complete and st.session_state.quiz_questions:
        total_q = len(st.session_state.quiz_questions)
        percentage = (st.session_state.score / total_q) * 100
        
        st.balloons()
        st.success("🎉 Quiz Complete!")
        st.metric("Final Score", f"{st.session_state.score}/{total_q}")
        st.metric("Percentage", f"{percentage:.1f}%")
        
        if percentage >= 80:
            st.success("🌟 Excellent work! You've mastered this material!")
        elif percentage >= 60:
            st.info("👍 Good job! Review the material to improve further.")
        else:
            st.warning("📖 Keep studying! Review the material and try again.")
        
        if st.button("Take Another Quiz", type="primary", use_container_width=True):
            st.session_state.quiz_questions = []
            st.session_state.quiz_complete = False
            st.rerun()

# Feature 4: Flashcard Creator
def flashcard_creator_page(model):
    """Page for creating and studying flashcards"""
    st.header("🃏 Flashcard Creator")
    st.write("Create flashcards from your study material!")
    
    # Initialize session state
    if 'flashcards' not in st.session_state:
        st.session_state.flashcards = []
    if 'current_card' not in st.session_state:
        st.session_state.current_card = 0
    if 'show_back' not in st.session_state:
        st.session_state.show_back = False
    
    # Flashcard generation section
    if not st.session_state.flashcards:
        text_for_cards = st.text_area(
            "Paste text or describe a topic:",
            height=150,
            placeholder="Paste your study material or describe a topic..."
        )
        
        num_cards = st.slider("Number of flashcards:", 5, 15, 10)
        
        if st.button("Generate Flashcards", type="primary", use_container_width=True):
            if text_for_cards:
                with st.spinner("🎴 Creating flashcards..."):
                    cards = generate_flashcards(model, text_for_cards, num_cards)
                    if cards:
                        st.session_state.flashcards = cards
                        st.session_state.current_card = 0
                        st.session_state.show_back = False
                        st.rerun()
            else:
                st.warning("Please provide text or a topic for the flashcards.")
    
    # Flashcard study section
    if st.session_state.flashcards:
        current_idx = st.session_state.current_card
        total_cards = len(st.session_state.flashcards)
        
        st.progress((current_idx + 1) / total_cards)
        st.write(f"**Card {current_idx + 1} of {total_cards}**")
        
        card = st.session_state.flashcards[current_idx]
        
        # Display flashcard
        card_container = st.container()
        with card_container:
            if not st.session_state.show_back:
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid #4CAF50;
                        border-radius: 10px;
                        padding: 40px;
                        text-align: center;
                        background-color: #f0f8f0;
                        min-height: 200px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    ">
                        <h2 style="margin: 0;">{card['front']}</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div style="
                        border: 2px solid #2196F3;
                        border-radius: 10px;
                        padding: 40px;
                        text-align: center;
                        background-color: #e3f2fd;
                        min-height: 200px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                    ">
                        <p style="margin: 0; font-size: 1.1em;">{card['back']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        st.write("")  # Spacing
        
        # Controls
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if current_idx > 0:
                if st.button("← Previous", use_container_width=True):
                    st.session_state.current_card -= 1
                    st.session_state.show_back = False
                    st.rerun()
        
        with col2:
            if st.button(
                "Show Answer" if not st.session_state.show_back else "Show Question",
                type="primary",
                use_container_width=True
            ):
                st.session_state.show_back = not st.session_state.show_back
                st.rerun()
        
        with col3:
            if current_idx < total_cards - 1:
                if st.button("Next →", use_container_width=True):
                    st.session_state.current_card += 1
                    st.session_state.show_back = False
                    st.rerun()
        
        # Reset button
        st.write("")
        if st.button("Create New Flashcards", use_container_width=True):
            st.session_state.flashcards = []
            st.session_state.current_card = 0
            st.session_state.show_back = False
            st.rerun()

# Main App
def main():
    """Main application"""
    
    # Initialize AI model
    model = initialize_ai()
    
    # Sidebar
    with st.sidebar:
        st.title("🎓 Study Spark")
        st.write("Your AI-Powered Study Buddy")
        st.write("---")
        
        page = st.radio(
            "Choose a feature:",
            [
                "🧠 Concept Explainer",
                "📝 Note Summarizer",
                "❓ Quiz Generator",
                "🃏 Flashcard Creator"
            ]
        )
        
        st.write("---")
        st.write("### About")
        st.write("Study Spark helps you learn better with AI-powered tools for explaining concepts, summarizing notes, and testing your knowledge.")
        st.write("---")
        st.caption("Built with Streamlit & Google Gemini")
    
    # Main content
    if page == "🧠 Concept Explainer":
        concept_explainer_page(model)
    elif page == "📝 Note Summarizer":
        note_summarizer_page(model)
    elif page == "❓ Quiz Generator":
        quiz_generator_page(model)
    elif page == "🃏 Flashcard Creator":
        flashcard_creator_page(model)

if __name__ == "__main__":
    main()
