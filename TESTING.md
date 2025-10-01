# 🧪 Testing Guide - Study Spark

This guide will help you test all features of the Study Spark application.

## Prerequisites for Testing

- ✅ Application running locally (`streamlit run app.py`)
- ✅ Google Gemini API key configured
- ✅ App opens at http://localhost:8501

## Test Plan

### 1. 🧠 Concept Explainer Testing

**Test Case 1: Simple Concept**
- Input: `What is photosynthesis?`
- Expected: Clear explanation with simple language
- Verify: Explanation includes key concepts and is student-friendly

**Test Case 2: Complex Topic**
- Input: `Explain quantum entanglement in simple terms`
- Expected: Simplified explanation with analogies
- Verify: Uses analogies and avoids overly technical jargon

**Test Case 3: Math Concept**
- Input: `Explain the Pythagorean theorem`
- Expected: Explanation with formula and practical examples
- Verify: Includes formula and real-world application

**Test Case 4: Empty Input**
- Input: (leave empty)
- Click: "Explain" button
- Expected: Warning message asking for input
- Verify: No error, just a friendly warning

---

### 2. 📝 Note Summarizer Testing

**Test Case 1: Paste Text - Short Summary**
- Input: Use `sample_notes.txt` content (paste entire file)
- Summary Length: Short
- Expected: 3-5 concise bullet points
- Verify: Key concepts are captured

**Test Case 2: Paste Text - Medium Summary**
- Input: Same content from `sample_notes.txt`
- Summary Length: Medium
- Expected: 7-10 bullet points
- Verify: More detail than short summary

**Test Case 3: Paste Text - Detailed Summary**
- Input: Same content
- Summary Length: Detailed
- Expected: Paragraph format with comprehensive details
- Verify: Maintains key information with more context

**Test Case 4: File Upload**
- Action: Click "Upload File" radio button
- Upload: `sample_notes.txt`
- Summary Length: Medium
- Expected: File content displayed and summarized
- Verify: File successfully read and processed

**Test Case 5: Small Text Input**
- Input: Just 1-2 sentences
- Expected: Summary generated (might be same as input)
- Verify: No errors, handles short text gracefully

**Test Case 6: Empty Input**
- Input: (leave empty)
- Click: "Summarize" button
- Expected: Warning message
- Verify: User-friendly error handling

---

### 3. ❓ Quiz Generator Testing

**Test Case 1: Generate Quiz from Sample Notes**
- Input: Paste content from `sample_notes.txt`
- Number of Questions: 5
- Expected: 5 multiple-choice questions generated
- Verify: Questions are relevant to the input text

**Test Case 2: Answer Questions**
- Action: Select an answer for each question
- Click: "Submit Answer"
- Expected: Immediate feedback (correct/incorrect)
- Verify: Correct answer highlighted in green, wrong answer in red

**Test Case 3: View Explanations**
- After answering: Check explanation text
- Expected: Brief explanation for each answer
- Verify: Explanations are helpful and accurate

**Test Case 4: Complete Quiz**
- Action: Answer all questions
- Click: "Finish Quiz" on last question
- Expected: Final score displayed with percentage
- Verify: Score calculated correctly, balloons animation plays

**Test Case 5: Retake Quiz**
- After completion: Click "Take Another Quiz"
- Expected: Return to quiz generation page
- Verify: Session state reset, can create new quiz

**Test Case 6: Different Question Counts**
- Test: Generate quiz with 3, 7, and 10 questions
- Expected: Correct number of questions generated each time
- Verify: Slider works properly

**Test Case 7: Progress Tracking**
- During quiz: Check progress bar
- Expected: Progress updates after each question
- Verify: Score updates in real-time

---

### 4. 🃏 Flashcard Creator Testing

**Test Case 1: Generate Flashcards**
- Input: Paste content from `sample_notes.txt`
- Number of Cards: 10
- Expected: 10 flashcards generated
- Verify: Cards contain relevant terms and definitions

**Test Case 2: Flip Cards**
- Action: Click "Show Answer"
- Expected: Card flips to show definition/answer
- Verify: Front (term) and back (definition) are both visible

**Test Case 3: Navigate Forward**
- Action: Click "Next →" button
- Expected: Move to next card (front side)
- Verify: Card number updates, new content displayed

**Test Case 4: Navigate Backward**
- Action: Click "← Previous" button
- Expected: Move to previous card
- Verify: Can navigate back through cards

**Test Case 5: Progress Indicator**
- Check: Progress bar at top
- Expected: Shows current card position (e.g., "Card 3 of 10")
- Verify: Updates correctly with navigation

**Test Case 6: Different Card Counts**
- Test: Generate 5, 10, and 15 cards
- Expected: Correct number of cards created
- Verify: Slider functions properly

**Test Case 7: Create New Set**
- After viewing cards: Click "Create New Flashcards"
- Expected: Return to generation page
- Verify: Previous cards cleared, ready for new input

---

### 5. 🎨 UI/UX Testing

**Test Case 1: Sidebar Navigation**
- Action: Click each menu item in sidebar
- Expected: Page changes to selected feature
- Verify: All four features accessible

**Test Case 2: Responsive Design**
- Action: Resize browser window
- Expected: Layout adjusts appropriately
- Verify: Elements remain readable and functional

**Test Case 3: Button States**
- Check: All primary buttons have appropriate styling
- Expected: Buttons clearly indicate they're clickable
- Verify: Hover effects work (if applicable)

**Test Case 4: Loading States**
- Action: Trigger any AI generation
- Expected: Spinner with message appears
- Verify: User knows processing is happening

**Test Case 5: Card Styling**
- Check: Flashcards in 🃏 feature
- Expected: Green border (front), blue border (back)
- Verify: Visual distinction between front/back

---

### 6. ⚠️ Error Handling Testing

**Test Case 1: No API Key**
- Setup: Remove API key from `.env` or `secrets.toml`
- Action: Start app
- Expected: Clear error message about missing API key
- Verify: App stops gracefully with helpful message

**Test Case 2: Invalid API Key**
- Setup: Use incorrect API key
- Action: Try any AI feature
- Expected: Error message about API issue
- Verify: Error is caught and displayed

**Test Case 3: Network Issues**
- Setup: Disconnect from internet (if possible)
- Action: Try generating content
- Expected: Error message about connection
- Verify: App doesn't crash

**Test Case 4: Malformed JSON Response**
- Action: Try quiz/flashcard generation with very short text
- Expected: If JSON parsing fails, error is caught
- Verify: User-friendly error message displayed

---

### 7. 🔄 Session State Testing

**Test Case 1: Quiz State Persistence**
- Action: Start quiz, answer questions, don't finish
- Switch: Go to different feature page
- Return: Come back to Quiz Generator
- Expected: Quiz state is lost (by design)
- Verify: Clean state when switching pages

**Test Case 2: Flashcard State**
- Action: Create flashcards, flip some cards
- Navigate: Through several cards
- Switch: Go to different page and return
- Expected: Flashcard state is lost
- Verify: Expected behavior for new session

---

## 🎯 Quick Test Checklist

Use this checklist for rapid testing:

- [ ] App starts without errors
- [ ] API key is recognized
- [ ] Sidebar navigation works
- [ ] Concept Explainer generates responses
- [ ] Note Summarizer with all three lengths
- [ ] File upload works
- [ ] Quiz generates questions
- [ ] Quiz scoring works correctly
- [ ] Flashcards generate and flip
- [ ] Navigation between cards works
- [ ] All buttons function correctly
- [ ] No console errors (check browser console with F12)
- [ ] Loading indicators appear
- [ ] Error messages are user-friendly

---

## 📊 Test Sample Data

### For Concept Explainer:
```
What is mitochondria?
Explain Newton's first law of motion
What is the difference between DNA and RNA?
```

### For Note Summarizer & Quiz/Flashcards:
Use the provided `sample_notes.txt` or paste this:

```
The water cycle, also known as the hydrological cycle, describes the continuous movement of water on, above, and below the surface of the Earth. Water can change states among liquid, vapor, and ice at various stages of the cycle. The main processes include evaporation, condensation, precipitation, and collection. Solar energy drives the cycle by evaporating water from the surface of the ocean. This water vapor rises and cools, condensing into clouds. Eventually, the water falls back to Earth as precipitation (rain, snow, sleet, or hail). Some of this precipitation flows into rivers and streams, eventually returning to the ocean, while some soaks into the ground, replenishing aquifers.
```

---

## 🐛 Known Issues to Test

1. **Long response times**: AI generation can take 5-15 seconds
2. **JSON parsing**: Sometimes AI returns text outside JSON format
3. **Short text input**: May not generate enough content for quizzes/flashcards

---

## ✅ Testing Complete

Once all test cases pass:
- [ ] Document any bugs found
- [ ] Note any performance issues
- [ ] Suggest improvements
- [ ] Ready for deployment!

---

**Happy Testing! 🧪✨**
