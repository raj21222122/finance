import streamlit as st
import random
import time
from data.quizzes import quiz_data
from data.additional_quizzes import insurance_quizzes, equity_quizzes
from utils import add_points, award_badge, record_quiz_completion

def show():
    """Display the Quiz Zone"""
    
    st.title("Quiz Zone")
    
    if not st.session_state.username:
        st.warning("Please log in to take quizzes and track your progress.")
        return
    
    # Check if a selected quiz exists in session state
    if "selected_quiz" not in st.session_state:
        # Display quiz selection
        st.header("Select a Quiz")
        st.write("Test your knowledge on different financial topics.")
        
        # Create columns for quiz selection
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Insurance Quiz"):
                st.session_state.selected_quiz = "Insurance"
                st.rerun()
        
            if st.button("Stocks Quiz"):
                st.session_state.selected_quiz = "Stocks"
                st.rerun()
                
        with col2:
            if st.button("Equity Quiz"):
                st.session_state.selected_quiz = "Equity"
                st.rerun()
                
            if st.button("Bonds Quiz"):
                st.session_state.selected_quiz = "Bonds"
                st.rerun()
                
        with col3:
            if st.button("PMS & AIF Quiz"):
                st.session_state.selected_quiz = "PMS & AIF"
                st.rerun()
        
        # Display user's quiz history
        st.header("Quiz History")
        
        if not st.session_state.completed_quizzes:
            st.write("You haven't taken any quizzes yet. Start learning and test your knowledge!")
        else:
            history_tab, achievements_tab = st.tabs(["Quiz History", "Achievements"])
            
            with history_tab:
                for module, results in st.session_state.completed_quizzes.items():
                    st.subheader(f"{module} Quiz")
                    for i, result in enumerate(results, 1):
                        st.write(f"Attempt {i}: Score {result['score']}/{result['total']} ({result['percentage']:.1f}%) - {result['timestamp']}")
            
            with achievements_tab:
                if not st.session_state.badges:
                    st.write("No badges earned yet. Complete quizzes to earn badges!")
                else:
                    st.write("Your earned badges:")
                    badges_cols = st.columns(3)
                    for i, badge in enumerate(st.session_state.badges):
                        with badges_cols[i % 3]:
                            st.success(f"🏆 {badge}")
                
                st.subheader("Current Streak")
                st.write(f"You have a streak of {st.session_state.streak} consecutive successful quizzes!")
        
    else:
        # Display the selected quiz
        module = st.session_state.selected_quiz
        
        # Check if a valid module is selected
        if not module:
            st.warning("No quiz selected. Please go back to the main page and select a quiz.")
            if st.button("Back to Home"):
                st.session_state.page = "Home"
                st.rerun()
            return
            
        st.header(f"{module} Quiz")
        
        # Select quiz difficulty if not already done
        if "quiz_difficulty" not in st.session_state:
            st.subheader("Select Quiz Difficulty")
            difficulty_cols = st.columns(3)
            
            with difficulty_cols[0]:
                if st.button("Easy", key="easy_button"):
                    st.session_state.quiz_difficulty = "Easy"
                    st.rerun()
            
            with difficulty_cols[1]:
                if st.button("Moderate", key="moderate_button"):
                    st.session_state.quiz_difficulty = "Moderate"
                    st.rerun()
            
            with difficulty_cols[2]:
                if st.button("Difficult", key="difficult_button"):
                    st.session_state.quiz_difficulty = "Difficult"
                    st.rerun()
            
            return
        
        difficulty = st.session_state.quiz_difficulty
        st.subheader(f"{module} Quiz - {difficulty} Level")
        
        # Initialize quiz state if not already done
        if "current_question" not in st.session_state:
            # Initialize quiz state
            st.session_state.current_question = 0
            st.session_state.correct_answers = 0
            st.session_state.user_answers = []
            st.session_state.quiz_completed = False
            
            # Select questions based on module and difficulty
            if module == "Insurance" and difficulty in insurance_quizzes:
                quiz_questions = insurance_quizzes[difficulty].copy()
            elif module == "Equity" and difficulty in equity_quizzes:
                quiz_questions = equity_quizzes[difficulty].copy()
            else:
                # Fall back to standard quiz if difficulty not available
                quiz_questions = quiz_data[module].copy()
            
            # Shuffle and limit questions
            random.shuffle(quiz_questions)
            num_questions = 10 if difficulty in ["Easy", "Moderate", "Difficult"] else 5
            
            # Assign to session state
            st.session_state.quiz_questions = quiz_questions[:num_questions]
            
        # Make sure quiz_questions exists before proceeding
        if "quiz_questions" not in st.session_state:
            st.warning("Quiz questions not loaded properly. Please go back and try again.")
            if st.button("Back to Quiz Selection"):
                # Reset quiz state
                for key in ["selected_quiz", "quiz_difficulty", "current_question", "correct_answers", 
                           "quiz_questions", "user_answers", "quiz_completed"]:
                    if key in st.session_state:
                        del st.session_state[key]
                time.sleep(0.1)
                st.rerun()
            return
        
        # Display progress
        total_questions = len(st.session_state.quiz_questions)
        progress_text = f"Question {st.session_state.current_question + 1} of {total_questions}"
        progress_value = (st.session_state.current_question + 1) / total_questions
        
        if not st.session_state.quiz_completed:
            st.progress(progress_value, text=progress_text)
        
        # If quiz is not completed, show questions
        if not st.session_state.quiz_completed:
            current_q = st.session_state.quiz_questions[st.session_state.current_question]
            
            st.subheader(f"Q{st.session_state.current_question + 1}: {current_q['question']}")
            
            # Record answer with radio buttons
            answer = st.radio(
                "Select your answer:",
                options=current_q["options"],
                key=f"quiz_answer_{st.session_state.current_question}"
            )
            
            selected_index = current_q["options"].index(answer)
            
            # Submit answer
            if st.button("Submit Answer"):
                # Check if answer is correct
                if selected_index == current_q["correct_answer"]:
                    st.session_state.correct_answers += 1
                    st.success("✅ Correct!")
                    # Add points for correct answer
                    add_points(10, "correct quiz answer")
                else:
                    st.error("❌ Incorrect!")
                
                # Show explanation
                st.info(f"Explanation: {current_q['explanation']}")
                
                # Store user's answer
                st.session_state.user_answers.append({
                    "question": current_q["question"],
                    "selected": selected_index,
                    "correct": current_q["correct_answer"],
                    "is_correct": selected_index == current_q["correct_answer"]
                })
                
                # Move to next question or end quiz
                if st.session_state.current_question < total_questions - 1:
                    st.session_state.current_question += 1
                    time.sleep(1)
                    st.rerun()
                else:
                    st.session_state.quiz_completed = True
                    # Record quiz completion
                    record_quiz_completion(
                        module.lower().replace(" & ", "_").replace(" ", "_"),
                        st.session_state.correct_answers,
                        total_questions
                    )
                    time.sleep(1)
                    st.rerun()
        
        # If quiz is completed, show results
        if st.session_state.quiz_completed:
            score = st.session_state.correct_answers
            percentage = (score / total_questions) * 100
            
            st.header("Quiz Results")
            
            # Display score with a gauge chart
            if percentage >= 80:
                st.success(f"🎉 Excellent! Your score: {score}/{total_questions} ({percentage:.1f}%)")
            elif percentage >= 60:
                st.info(f"👍 Good job! Your score: {score}/{total_questions} ({percentage:.1f}%)")
            else:
                st.warning(f"📚 Keep learning! Your score: {score}/{total_questions} ({percentage:.1f}%)")
            
            # Award badges based on performance
            if percentage == 100:
                award_badge(f"{module} Master")
            elif percentage >= 80:
                award_badge(f"{module} Expert")
            elif percentage >= 60:
                award_badge(f"{module} Scholar")
            
            # Display a review of all questions and answers
            st.subheader("Review Your Answers")
            
            for i, user_answer in enumerate(st.session_state.user_answers):
                q_data = st.session_state.quiz_questions[i]
                
                with st.expander(f"Question {i+1}: {user_answer['question']}"):
                    # Display all options, highlighting the user's choice and the correct answer
                    for j, option in enumerate(q_data["options"]):
                        if j == user_answer["correct"]:
                            st.markdown(f"✅ **{option}** (Correct Answer)")
                        elif j == user_answer["selected"] and j != user_answer["correct"]:
                            st.markdown(f"❌ **{option}** (Your Answer)")
                        else:
                            st.markdown(f"○ {option}")
                    
                    # Show explanation
                    st.info(f"Explanation: {q_data['explanation']}")
            
            # Options to retake the quiz or go back to quiz selection
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("Retake Quiz"):
                    # Reset quiz state but keep difficulty
                    for key in ["current_question", "correct_answers", "quiz_questions", "user_answers", "quiz_completed"]:
                        if key in st.session_state:
                            del st.session_state[key]
                    
                    # Add points for retaking quiz
                    add_points(5, "retaking a quiz to improve knowledge")
                    time.sleep(0.1)
                    st.rerun()
            
            with col2:
                if st.button("Back to Quiz Selection"):
                    # Go back to quiz selection
                    for key in ["selected_quiz", "quiz_difficulty", "current_question", "correct_answers", 
                               "quiz_questions", "user_answers", "quiz_completed"]:
                        if key in st.session_state:
                            del st.session_state[key]
                    
                    # Make sure page state is reset
                    st.session_state.page = "Quiz Zone"
                    time.sleep(0.1)
                    st.rerun()
