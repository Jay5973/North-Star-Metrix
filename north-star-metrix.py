import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Load chat and user profile data
@st.cache_data
def load_data(chat_file_path, profile_file_path):
    chat_df = pd.read_csv(chat_file_path)
    profile_df = pd.read_csv(profile_file_path)
    profile_df['userId'] = profile_df['_id']
    
    # Convert `createdAt` columns to datetime format
    chat_df['createdAt'] = pd.to_datetime(chat_df['createdAt']).dt.tz_localize(None)
    profile_df['createdAt'] = pd.to_datetime(profile_df['createdAt']).dt.tz_localize(None)
    
    return chat_df, profile_df

# Filter chat data based on hasFreeMins and endReason
def filter_chat_data(chat_df):
    return chat_df[(chat_df['hasFreeMins'] == 0) & (chat_df['endReason'] != 'NOT_STARTED')]

# Function to count users completing their 4th chat on the target date
def get_users_completing_4th_chat_today(filtered_chat_df, profile_df, target_date):
    three_months_ago = target_date - timedelta(days=90)
    day_before_target = target_date - timedelta(days=1)
    
    recent_profiles_df = profile_df[(profile_df['createdAt'] >= three_months_ago) & (profile_df['createdAt'] <= target_date)]
    recent_user_ids = recent_profiles_df['userId'].unique()
    
    recent_chats_df_up_to_yesterday = filtered_chat_df[(filtered_chat_df['createdAt'] >= three_months_ago) & (filtered_chat_df['createdAt'] < target_date)]
    chats_on_target_date = filtered_chat_df[filtered_chat_df['createdAt'].dt.date == target_date.date()]
    
    user_chat_counts_up_to_yesterday = recent_chats_df_up_to_yesterday.groupby('userId').size()
    users_less_than_4_chats_yesterday = user_chat_counts_up_to_yesterday[user_chat_counts_up_to_yesterday < 4].index
    user_chat_counts_today = chats_on_target_date.groupby('userId').size()
    
    users_completing_4th_chat_today = [
        user_id for user_id in users_less_than_4_chats_yesterday
        if user_chat_counts_up_to_yesterday.get(user_id, 0) + user_chat_counts_today.get(user_id, 0) == 4
    ]
    
    valid_users = [user_id for user_id in users_completing_4th_chat_today if user_id in recent_user_ids]
    
    return valid_users

# Function to iterate over date range and generate results
def iterate_date_range(filtered_chat_df, profile_df, start_date, end_date):
    results = []
    current_date = start_date
    
    while current_date <= end_date:
        valid_users = get_users_completing_4th_chat_today(filtered_chat_df, profile_df, current_date)
        results.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'unique_user_count': len(valid_users),
            'user_ids': ','.join(valid_users)
        })
        current_date += timedelta(days=1)
    
    return pd.DataFrame(results)

# Streamlit interface
st.title("4th Chat Completion Analysis")

# File upload widgets
chat_file = st.file_uploader("Upload Raw Chat Data CSV", type="csv")
profile_file = st.file_uploader("Upload User Profile Data CSV", type="csv")

if chat_file and profile_file:
    chat_df, profile_df = load_data(chat_file, profile_file)
    filtered_chat_df = filter_chat_data(chat_df)
    
    # Date input widgets
    start_date = st.date_input("Select Start Date", datetime(2024, 8, 15))
    end_date = st.date_input("Select End Date", datetime(2024, 10, 22))
    
    if st.button("Run Analysis"):
        result_df = iterate_date_range(filtered_chat_df, profile_df, start_date, end_date)
        
        # Display the results
        st.write(result_df)
        
        # Download results as CSV
        csv = result_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='North_Star_Metrix_june_oct_with_userIDs.csv',
            mime='text/csv'
        )
