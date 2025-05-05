import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

def show():
    """Display User Dashboard with progress and achievements"""
    
    st.title("User Dashboard")
    
    if not st.session_state.username:
        st.warning("Please log in to view your dashboard.")
        return
    
    # Display user info
    st.header(f"Welcome, {st.session_state.username}!")
    
    # Overview metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Level", st.session_state.level_name, 
                 f"{st.session_state.level}/{st.session_state.total_levels}",
                 help="Your current learning level based on points earned")
    
    with col2:
        points_to_next = ""
        if st.session_state.level < st.session_state.total_levels:
            points_to_next = f"{st.session_state.points_to_next_level} to next level"
        st.metric("Total Points", st.session_state.points, 
                 points_to_next, 
                 help="Points earned through learning and quizzes")
    
    with col3:
        st.metric("Streak", st.session_state.streak, help="Consecutive successful quizzes (70%+ score)")
    
    with col4:
        badge_count = len(st.session_state.badges)
        st.metric("Badges", badge_count, help="Achievement badges earned")
    
    # Level progress
    if st.session_state.level < st.session_state.total_levels:
        st.subheader(f"Progress to {st.session_state.next_level_name} Level")
        st.write(f"{st.session_state.points}/{st.session_state.next_level_threshold} points")
        st.progress(st.session_state.level_progress)
        st.write(f"Earn {st.session_state.points_to_next_level} more points to reach the {st.session_state.next_level_name} level")
    else:
        st.subheader("Maximum Level Achieved!")
        st.progress(1.0)
        st.write("Congratulations! You've reached the highest level: Legend!")
        
    # Levels overview
    with st.expander("View All Levels", expanded=False):
        levels = [
            {"level": 1, "name": "Beginner", "threshold": 0, "next_threshold": 50},
            {"level": 2, "name": "Rising Star", "threshold": 50, "next_threshold": 150},
            {"level": 3, "name": "Star", "threshold": 150, "next_threshold": 300},
            {"level": 4, "name": "Expert", "threshold": 300, "next_threshold": 500},
            {"level": 5, "name": "Master", "threshold": 500, "next_threshold": 750},
            {"level": 6, "name": "Legend", "threshold": 750, "next_threshold": "∞"}
        ]
        
        levels_df = pd.DataFrame(levels)
        st.table(levels_df)
    
    # Learning progress
    st.header("Learning Progress")
    
    # Progress by module
    modules = ["Insurance", "Equity", "PMS & AIF", "Stocks", "Bonds"]
    module_keys = ["insurance", "equity", "pms_aif", "stocks", "bonds"]
    
    # Calculate combined metrics for a more accurate progress calculation
    module_metrics = []
    for module, key in zip(modules, module_keys):
        # Base module progress (from reading sections)
        base_progress = st.session_state.get(f"{key}_progress", 0)
        
        # Get quiz performance if available
        quiz_scores = []
        quiz_module = module.replace(" & ", "_").replace(" ", "_")
        if quiz_module in st.session_state.completed_quizzes:
            for quiz in st.session_state.completed_quizzes[quiz_module]:
                quiz_scores.append(quiz["percentage"])
        
        # Calculate metrics
        avg_quiz_score = sum(quiz_scores) / len(quiz_scores) if quiz_scores else 0
        
        # Combined metric: 60% weight on content progress, 40% on best quiz score
        # This prevents showing high progress when quiz scores are low
        best_quiz_score = max(quiz_scores) if quiz_scores else 0
        combined_progress = (base_progress * 0.6)
        if quiz_scores:
            combined_progress += (best_quiz_score * 0.4)
            # If quiz score is low, cap the combined progress
            if best_quiz_score < 50:
                combined_progress = min(combined_progress, 60)  # Cap at 60% if quiz score is below 50%
        
        # Cap at 100%
        combined_progress = min(combined_progress, 100)
        
        module_metrics.append({
            "Module": module,
            "Content Progress": base_progress,
            "Best Quiz Score": best_quiz_score if quiz_scores else None,
            "Combined Progress": combined_progress,
            "Quizzes Taken": len(quiz_scores)
        })
    
    # Create dataframe for visualization 
    progress_df = pd.DataFrame([{
        "Module": metric["Module"],
        "Progress": metric["Combined Progress"]
    } for metric in module_metrics])
    
    # Display progress chart
    st.subheader("Overall Module Progress")
    st.bar_chart(progress_df.set_index("Module"))
    
    # More detailed view with tabs
    progress_tab1, progress_tab2 = st.tabs(["Progress Bars", "Detailed Metrics"])
    
    with progress_tab1:
        # Show progress bars with explanation
        for metric in module_metrics:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{metric['Module']}**: {metric['Combined Progress']:.1f}% completed")
                st.progress(metric['Combined Progress'] / 100)
            with col2:
                if metric['Quizzes Taken'] > 0:
                    st.write(f"Best quiz: {metric['Best Quiz Score']:.1f}%")
                else:
                    st.write("No quizzes taken")
    
    with progress_tab2:
        # Prepare data for the table
        table_data = []
        for metric in module_metrics:
            table_data.append({
                "Module": metric["Module"],
                "Content Progress": f"{metric['Content Progress']:.1f}%",
                "Best Quiz Score": f"{metric['Best Quiz Score']:.1f}%" if metric['Best Quiz Score'] is not None else "N/A",
                "Quizzes Taken": metric["Quizzes Taken"],
                "Overall Progress": f"{metric['Combined Progress']:.1f}%"
            })
        
        # Show detailed metrics in a table
        st.dataframe(pd.DataFrame(table_data), hide_index=True, use_container_width=True)
    
    # Quiz performance
    st.header("Quiz Performance")
    
    if not st.session_state.completed_quizzes:
        st.write("You haven't taken any quizzes yet. Start learning and test your knowledge!")
    else:
        # Create data for quiz performance visualization
        quiz_data = []
        
        for module, results in st.session_state.completed_quizzes.items():
            for result in results:
                quiz_data.append({
                    "Module": module.replace("_", " ").title(),
                    "Score (%)": result["percentage"],
                    "Date": datetime.strptime(result["timestamp"], "%Y-%m-%d %H:%M").strftime("%Y-%m-%d")
                })
        
        quiz_df = pd.DataFrame(quiz_data)
        
        # Show recent quiz results
        st.subheader("Recent Quiz Results")
        st.dataframe(
            quiz_df.sort_values("Date", ascending=False).head(5),
            hide_index=True,
            use_container_width=True
        )
        
        # Chart of quiz scores by module
        st.subheader("Average Quiz Scores by Module")
        
        avg_scores = quiz_df.groupby("Module")["Score (%)"].mean().reset_index()
        st.bar_chart(avg_scores.set_index("Module"))
    
    # Badges and achievements
    st.header("Badges & Achievements")
    
    if not st.session_state.badges:
        st.write("No badges earned yet. Complete modules and quizzes to earn badges!")
    else:
        # Display badges in a grid
        badges_per_row = 3
        rows = (len(st.session_state.badges) + badges_per_row - 1) // badges_per_row
        
        for i in range(rows):
            cols = st.columns(badges_per_row)
            for j in range(badges_per_row):
                idx = i * badges_per_row + j
                if idx < len(st.session_state.badges):
                    with cols[j]:
                        st.markdown(f"### 🏆 {st.session_state.badges[idx]}")
    
    # Recent activity
    st.header("Recent Activity")
    
    if not st.session_state.activity:
        st.write("No activity recorded yet. Start exploring the learning modules!")
    else:
        for activity in st.session_state.activity[:10]:
            st.write(f"- {activity}")
    
    # Recommendations based on progress
    st.header("Personalized Recommendations")
    
    # Use the combined progress metrics for better recommendations
    progress_by_module = [(metric["Module"], metric["Combined Progress"]) for metric in module_metrics]
    progress_by_module.sort(key=lambda x: x[1])  # Sort by combined progress
    
    recommended_modules = progress_by_module[:2]
    
    st.subheader("Continue Learning")
    for module_name, progress in recommended_modules:
        if progress < 100:
            st.write(f"📚 **{module_name}** - {progress:.1f}% completed")
            if st.button(f"Go to {module_name}", key=f"goto_{module_name.lower().replace(' & ', '_').replace(' ', '_')}"):
                st.session_state.page = module_name
                st.rerun()
    
    # Recommend quizzes section
    st.subheader("Test Your Knowledge")
    
    # Find modules with no quizzes taken or low quiz scores
    quiz_recommendations = []
    for metric in module_metrics:
        module = metric["Module"]
        quiz_module = module.replace(" & ", "_").replace(" ", "_")
        
        # Priority 1: Modules with content progress > 50% but no quizzes
        if metric["Content Progress"] > 50 and metric["Quizzes Taken"] == 0:
            quiz_recommendations.append((module, "No quiz taken yet", 1))
        
        # Priority 2: Modules with low quiz scores
        elif metric["Quizzes Taken"] > 0 and metric["Best Quiz Score"] < 70:
            quiz_recommendations.append((module, f"Current best score: {metric['Best Quiz Score']:.1f}%", 2))
    
    # Sort by priority
    quiz_recommendations.sort(key=lambda x: x[2])
    
    if quiz_recommendations:
        # Show top 2 recommendations
        for module, reason, _ in quiz_recommendations[:2]:
            module_key = module.lower().replace(" & ", "_").replace(" ", "_")
            st.write(f"📝 Take the **{module} Quiz** ({reason})")
            if st.button(f"Take {module} Quiz", key=f"quiz_{module_key}"):
                st.session_state.selected_quiz = module
                st.session_state.page = "Quiz Zone"
                st.rerun()
    else:
        # Find modules with best performance to suggest retaking for mastery
        best_modules = sorted([(m["Module"], m["Combined Progress"]) for m in module_metrics], 
                             key=lambda x: x[1], reverse=True)
        
        st.write("Great job! You've made good progress in all modules.")
        
        if best_modules:
            top_module = best_modules[0][0]
            module_key = top_module.lower().replace(" & ", "_").replace(" ", "_")
            st.write(f"💯 Consider retaking the **{top_module} Quiz** to achieve mastery!")
            if st.button(f"Master {top_module}", key=f"master_{module_key}"):
                st.session_state.selected_quiz = top_module
                st.session_state.quiz_difficulty = "Difficult"  # Suggest the difficult quiz
                st.session_state.page = "Quiz Zone"
                st.rerun()
