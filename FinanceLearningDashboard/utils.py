import streamlit as st
import time
from datetime import datetime

def initialize_session_state():
    """Initialize all required session state variables if they don't exist"""
    if 'username' not in st.session_state:
        st.session_state.username = ""
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'points' not in st.session_state:
        st.session_state.points = 0
    
    if 'badges' not in st.session_state:
        st.session_state.badges = []
    
    if 'completed_quizzes' not in st.session_state:
        st.session_state.completed_quizzes = {}
    
    if 'streak' not in st.session_state:
        st.session_state.streak = 0
    
    if 'activity' not in st.session_state:
        st.session_state.activity = []
    
    if 'page' not in st.session_state:
        st.session_state.page = "Home"
    
    # Quiz related variables
    if 'selected_quiz' not in st.session_state:
        st.session_state.selected_quiz = None
    
    if 'quiz_difficulty' not in st.session_state:
        st.session_state.quiz_difficulty = None
    
    # Initialize progress for each module
    for module in ["insurance", "equity", "pms_aif", "stocks", "bonds"]:
        if f"{module}_progress" not in st.session_state:
            st.session_state[f"{module}_progress"] = 0
    
    # Set level based on points
    update_level()

def update_level():
    """Update user level based on points"""
    points = st.session_state.points
    
    # Define level thresholds and names
    levels = [
        {"threshold": 0, "name": "Beginner", "next_threshold": 50},
        {"threshold": 50, "name": "Rising Star", "next_threshold": 150},
        {"threshold": 150, "name": "Star", "next_threshold": 300},
        {"threshold": 300, "name": "Expert", "next_threshold": 500},
        {"threshold": 500, "name": "Master", "next_threshold": 750},
        {"threshold": 750, "name": "Legend", "next_threshold": float('inf')}
    ]
    
    # Find current level
    current_level = 0  # Default to first level
    for i, level in enumerate(levels):
        if points >= level["threshold"] and (i == len(levels) - 1 or points < levels[i+1]["threshold"]):
            current_level = i
            break
    
    # Set level information
    level_info = levels[current_level]
    next_level_index = min(current_level + 1, len(levels) - 1)
    next_level_info = levels[next_level_index]
    
    st.session_state.level = current_level + 1
    st.session_state.level_name = level_info["name"]
    
    # Calculate progress toward next level
    if level_info["next_threshold"] == float('inf'):
        st.session_state.level_progress = 1.0
    else:
        progress = (points - level_info["threshold"]) / (level_info["next_threshold"] - level_info["threshold"])
        st.session_state.level_progress = min(progress, 1.0)
    
    # Store additional level information
    st.session_state.current_level_threshold = level_info["threshold"]
    st.session_state.next_level_threshold = level_info["next_threshold"]
    st.session_state.next_level_name = next_level_info["name"]
    st.session_state.points_to_next_level = max(0, level_info["next_threshold"] - points)
    st.session_state.total_levels = len(levels)

def add_points(points, reason=""):
    """Add points to user account and record activity"""
    if st.session_state.username:
        st.session_state.points += points
        update_level()
        
        # Add to activity log
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        activity = f"{timestamp}: Earned {points} points"
        if reason:
            activity += f" for {reason}"
        
        st.session_state.activity.insert(0, activity)
        
        # Keep only the most recent 100 activities
        if len(st.session_state.activity) > 100:
            st.session_state.activity = st.session_state.activity[:100]
        
        return True
    return False

def award_badge(badge_name, module=""):
    """Award a badge to the user and record activity"""
    if st.session_state.username:
        if badge_name not in st.session_state.badges:
            st.session_state.badges.append(badge_name)
            
            # Add to activity log
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            activity = f"{timestamp}: Earned badge: {badge_name}"
            st.session_state.activity.insert(0, activity)
            
            # Show a congratulatory message
            st.balloons()
            st.success(f"🏆 Congratulations! You've earned the {badge_name} badge!")
            time.sleep(2)
            
            return True
    return False

def update_module_progress(module, progress_value):
    """Update progress for a specific module"""
    if st.session_state.username:
        progress_key = f"{module}_progress"
        current_progress = st.session_state.get(progress_key, 0)
        
        # Only update if the new progress is higher
        if progress_value > current_progress:
            st.session_state[progress_key] = progress_value
            
            # Check if module is complete and award a badge
            if progress_value >= 100:
                module_name = module.replace("_", " ").title()
                award_badge(f"{module_name} Expert")
            
            # Add to activity log
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            activity = f"{timestamp}: Made progress in {module.replace('_', ' ').title()} module"
            st.session_state.activity.insert(0, activity)
            
            return True
    return False

def record_quiz_completion(module, score, total):
    """Record quiz completion and update streaks"""
    if st.session_state.username:
        # Calculate percentage
        percentage = (score / total) * 100
        
        # Store quiz result
        if module not in st.session_state.completed_quizzes:
            st.session_state.completed_quizzes[module] = []
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        st.session_state.completed_quizzes[module].append({
            "timestamp": timestamp,
            "score": score,
            "total": total,
            "percentage": percentage
        })
        
        # Update streak if score is good (at least 70%)
        if percentage >= 70:
            st.session_state.streak += 1
            # Award streak badges
            if st.session_state.streak == 3:
                award_badge("Streak Starter")
            elif st.session_state.streak == 5:
                award_badge("Consistent Learner")
            elif st.session_state.streak == 10:
                award_badge("Learning Machine")
        else:
            st.session_state.streak = 0
        
        # Create module progress key with proper formatting
        module_key = module.lower().replace(" & ", "_").replace(" ", "_")
        
        # Update module progress based on quiz performance
        # Base progress on quiz percentage - don't auto-set to 100%
        current_progress = st.session_state.get(f"{module_key}_progress", 0)
        
        # If the score is better, update the progress
        if percentage > current_progress:
            st.session_state[f"{module_key}_progress"] = percentage
        
        # Add to activity log
        activity = f"{timestamp}: Completed {module.replace('_', ' ').title()} quiz with score {score}/{total}"
        st.session_state.activity.insert(0, activity)
        
        return True
    return False

def highlight_text(text, search_term):
    """Highlight search term in text with yellow background"""
    if not search_term or not text:
        return text
    
    # Create a case-insensitive replacement
    import re
    pattern = re.compile(f'({re.escape(search_term)})', re.IGNORECASE)
    highlighted = pattern.sub(r'<span style="background-color: #FFFF00">\1</span>', text)
    return highlighted
