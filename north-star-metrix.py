import pandas as pd
import streamlit as st
from datetime import datetime, timedelta
import plotly.express as px

# Streamlit UI
st.title("North Star Metric Dashboard")

# File upload for chat data
chat_file = st.file_uploader("Upload Chat Data CSV", type=["csv"])
if chat_file is not None:
    chat_df = pd.read_csv(chat_file)
    # Convert createdAt to datetime
    chat_df['createdAt'] = pd.to_datetime(chat_df['createdAt']).dt.tz_localize(None)
    
    # Filter chat data based on hasFreeMins and end_reason
    filtered_chat_df = chat_df[(chat_df['hasFreeMins'] == 0) & (chat_df['endReason'] != 'NOT_STARTED')]

# File upload for user profile data
profile_file = st.file_uploader("Upload User Profile Data CSV", type=["csv"])
if profile_file is not None:
    profile_df = pd.read_csv(profile_file)
    profile_df['userId'] = profile_df['_id']
    # Convert createdAt to datetime
    profile_df['createdAt'] = pd.to_datetime(profile_df['createdAt']).dt.tz_localize(None)

# Function to count users who are completing their 4th chat on the target date
def get_users_completing_4th_chat_today(filtered_chat_df, profile_df, target_date):
    three_months_ago = target_date - timedelta(days=90)
    
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

# Function to iterate over date range
def iterate_date_range(filtered_chat_df, profile_df, start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%d-%m-%y')
    end_date = datetime.strptime(end_date_str, '%d-%m-%y')
    
    results = []
    
    current_date = start_date
    while current_date <= end_date:
        valid_users = get_users_completing_4th_chat_today(filtered_chat_df, profile_df, current_date)
        results.append({
            'date': current_date.strftime('%Y-%m-%d'),
            'unique_user_count': len(valid_users),
            'user_ids': ','.join(valid_users)  # Join user IDs into a single string
        })
        current_date += timedelta(days=1)
    
    return pd.DataFrame(results)

# Date input fields
start_date = st.text_input("Enter start date (DD-MM-YY):", "15-08-24")
end_date = st.text_input("Enter end date (DD-MM-YY):", "22-10-24")

if st.button("Calculate"):
    if chat_file is not None and profile_file is not None:
        result_df = iterate_date_range(filtered_chat_df, profile_df, start_date, end_date)
        
        # Display the results
        st.write(result_df)
        
        # Plot the graph
        fig = px.line(result_df, x='date', y='unique_user_count', title='North Star Metric Over Time', markers=True)
        st.plotly_chart(fig)
        
        # Save results to CSV
        result_df.to_csv('North_Star_Metrix_june_oct_with_userIDs.csv', index=False)
    else:
        st.warning("Please upload both chat and user profile data files.")
