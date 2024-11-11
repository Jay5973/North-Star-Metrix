import streamlit as st
import pandas as pd
import json
import plotly.express as px

# Streamlit App Setup
st.title("Astrology Chat Data Processor")

import streamlit as st
import pandas as pd

# Sample existing data
data = {
    'name': ['Astro Anuj' ,
'Arya' ,
'Acharya Srikant' ,
'Deepti' ,
'Acharya Tarun' ,
'Acharya Shivank' ,
'Astro Satyadev' ,
'Riya' ,
'Aakriti' ,
'Astro Viswakarma' ,
'Astro Harsh' ,
'Astro Satya Prakash' ,
'Astro Punit' ,
'Astro Deepak' ,
'Aacharya Satya Prakash' ,
'Astro Ujjwal' ,
'Pradyumna ' ,
'Komal' ,
'Astro Aryan' ,
'Khushboo' ,
'Astro shiva' ,
'Astro Adarsh' ,
'Thulasi' ,
'Shreenika' ,
'Himadri' ,
'Moubani' ,
'Shivani' ,
'Anjali' ,
'Astro Ashish' ,
'Payal' ,
'Shri Bal Krishnan' ,
'Dinesh' ,
'Harjeet' ,
'Tarot Devansh' ,
'Harish' ,
'Roshni' ,
'Sanket' ,
'Astro Krishna ' ,
'Astro Radhe' ,
'Ragini' ,
'Astro Ram ' ,
'Sarjun' ,
'Aacharya Dharm' ,
'Astro Samarth ' ,
'Seema ' ,
'Astro Rakesh' ,
'Tarot Nancy' ,
'Tarot Ekkta' ,
'Pandit Joshi Ji' ,
'Acharya Ashok' ,
'Bhavna Shankar'
],
    'astro_id': ['6715fafeade957201d542e9c' ,
'6715215eade957201d488fcc' ,
'6713846fade957201d207823' ,
'6711fbc4d5547447324a5cde' ,
'66ffd23b650a226b39fd8693' ,
'66ffce5a650a226b39fc8eb9' ,
'66f63f95650a226b39f55472' ,
'66ea8b76278059b32e584bc7' ,
'66ea8846278059b32e5730c3' ,
'66c030ddbf902d2d207a7b70' ,
'66c02a71bf902d2d2077ccd6' ,
'66bf3fe4bf902d2d205c7852' ,
'66bf3d00bf902d2d205bb082' ,
'66bf23c0bf902d2d2052c857' ,
'66bf20a7bf902d2d2051b36a' ,
'66bef318bf902d2d203f2f1b' ,
'66beec2cbf902d2d203bc8a5' ,
'66bee517bf902d2d2038d777' ,
'66bee057bf902d2d2036cafa' ,
'66b79a62bd3a0555e6369873' ,
'66ae1f45955c3876d10246e7' ,
'66ae1d9e955c3876d1020d27' ,
'66acb1bc58785ce259281044' ,
'66ac76f858785ce2591bc2a2' ,
'66ac722758785ce2591aef0e' ,
'66ac633058785ce25918d9d8' ,
'66ab373f981ed550c2242106' ,
'66a9e88bfbfec7e69081f13f' ,
'66a7401a3b9dfebd3dda2cf1' ,
'66a373e69e88c38a47a9dfa5' ,
'6694c9278b500d8191ee57d8' ,
'66757941b6b9ae4714134999' ,
'665ee966f1897a3b24ed3cee' ,
'665d5b207f6f0449439e6139' ,
'664b19b98879311df0e77984' ,
'6646d404a8380c58c7ea0326' ,
'6642f646c9931a00df37fbb5' ,
'66339d64c9d092f4be50c248' ,
'66238c4c1a8cbb4d47647df9' ,
'662374ad1a8cbb4d4761c6c4' ,
'66236fec1a8cbb4d47612dc7' ,
'66150af9dc1928e3ede77904' ,
'65f583c9ce82594e16f234c7' ,
'65c5d82edf8742484626e471' ,
'659f89c4d8a3f3587d58487d' ,
'659e43f8d8a3f3587d4b0f4f' ,
'656f2e80ec223b83c181a75a' ,
'6544cc3f4fcff813eaa69d14' ,
'6544ca004fcff813eaa695df' ,
'6528d93f8e88ef67ce4c7579' ,
'6526970127a17d629618b610' ],
    'type': ['PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'PAYROLL' ,
'FREELANCE' ,
'PAYROLL' ,
'FREELANCE' ,
'PAYROLL' ,
'PAYROLL' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'FREELANCE' ,
'PAYROLL' ,
'PAYROLL' ]
}

# Initialize the DataFrame
astro_df = pd.DataFrame(data)

# Function to add an astrologer
def add_astrologer(df, astro_id, name, astro_type):
    new_row = {'astro_id': astro_id, 'name': name, 'type': astro_type}
    df = df.append(new_row, ignore_index=True)
    return df

# Function to delete an astrologer
def delete_astrologer(df, astro_id):
    df = df[df['astro_id'] != astro_id]
    return df

# Streamlit app
st.title("Astrologer Management")

# Option to add a new astrologer
st.subheader("Add a New Astrologer")
new_astro_id = st.number_input("Astrologer ID", value=0, step=1)
new_name = st.text_input("Name")
new_type = st.text_input("Type")
if st.button("Add Astrologer"):
    astro_df = add_astrologer(astro_df, new_astro_id, new_name, new_type)
    st.success(f"Astrologer {new_name} added successfully!")
    st.write(astro_df)

# Option to delete an existing astrologer
st.subheader("Delete an Astrologer")
delete_astro_id = st.number_input("Enter Astrologer ID to Delete", value=0, step=1)
if st.button("Delete Astrologer"):
    astro_df = delete_astrologer(astro_df, delete_astro_id)
    st.success(f"Astrologer with ID {delete_astro_id} deleted successfully!")
    st.write(astro_df)

# Display the current DataFrame
st.subheader("Current Astrologer Data")
st.write(astro_df)


# Step 1: Upload Files
raw_file = st.file_uploader("Upload raw_data.csv", type="csv")

if raw_file:
    
    # Step 2: Extract JSON Data from raw_data.csv and Save to a DataFrame
    def extract_json(raw_df, json_column):
        json_data = []
        for item in raw_df[json_column]:
            try:
                data = json.loads(item)
                json_data.append(data)
            except (json.JSONDecodeError, TypeError):
                continue
        json_df = pd.json_normalize(json_data)
        combined_df = pd.concat([raw_df, json_df], axis=1)
        return combined_df

    # Step 3: Process Events to Calculate Unique Users
    class UniqueUsersProcessor:
        def __init__(self, raw_df,astro_df):
            self.raw_df = raw_df
            self.astro_df = astro_df

        def process_chat_intake_requests(self):
            intake_events = self.raw_df[(self.raw_df['event_name'] == 'chat_intake_submit')]
            intake_events['event_time'] = pd.to_datetime(intake_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            intake_events['date'] = intake_events['event_time'].dt.date
            intake_events['hour'] = intake_events['event_time'].dt.hour
            user_counts = intake_events.groupby(['astrologerId', 'date', 'hour'])['user_id'].nunique().reset_index()
            user_counts.rename(columns={'user_id': 'chat_intake_requests', 'astrologerId': '_id'}, inplace=True)
            return user_counts

        def process_chat_cancels(self):
            cancel_events = self.raw_df[(self.raw_df['event_name'] == 'confirm_cancel_waiting_list')]
            cancel_events['event_time'] = pd.to_datetime(cancel_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            cancel_events['date'] = cancel_events['event_time'].dt.date
            cancel_events['hour'] = cancel_events['event_time'].dt.hour
            user_counts = cancel_events.groupby(['astrologerId', 'date', 'hour'])['user_id'].nunique().reset_index()
            user_counts.rename(columns={'user_id': 'cancelled_requests', 'astrologerId': '_id'}, inplace=True)
            return user_counts

        def cancellation_time(self):
            intake_events = self.raw_df[(self.raw_df['event_name'] == 'chat_intake_submit')].copy()
            intake_events['event_time'] = pd.to_datetime(intake_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            intake_events['date'] = intake_events['event_time'].dt.date
            intake_events['hour'] = intake_events['event_time'].dt.hour
            cancel_events = self.raw_df[(self.raw_df['event_name'] == 'confirm_cancel_waiting_list')].copy()
            cancel_events['event_time'] = pd.to_datetime(cancel_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            cancel_events['date'] = cancel_events['event_time'].dt.date
            cancel_events['hour'] = cancel_events['event_time'].dt.hour
            merged_events = pd.merge(intake_events, cancel_events, on=['user_id', 'astrologerId'], suffixes=('_intake', '_cancel'))
            merged_events['time_diff'] = (merged_events['event_time_cancel'] - merged_events['event_time_intake']).dt.total_seconds() / 60.0
            avg_time_diff = merged_events.groupby(['astrologerId', 'date_intake', 'hour_intake'])['time_diff'].mean().reset_index()
            avg_time_diff.rename(columns={'astrologerId': '_id', 'date_intake': 'date', 'hour_intake': 'hour', 'time_diff': 'avg_time_diff_minutes'}, inplace=True)
            return avg_time_diff

        def process_chat_accepted_events(self):
            intake_events = self.raw_df[self.raw_df['event_name'] == 'chat_intake_submit']
            valid_user_ids = intake_events['user_id'].unique()
            accept_events = self.raw_df[(self.raw_df['event_name'] == 'accept_chat') & (self.raw_df['paid'] == 0) & (self.raw_df['clientId'].isin(valid_user_ids))]
            accept_events['event_time'] = pd.to_datetime(accept_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            accept_events['date'] = accept_events['event_time'].dt.date
            accept_events['hour'] = accept_events['event_time'].dt.hour
            accept_counts = accept_events.groupby(['user_id', 'date', 'hour'])['clientId'].nunique().reset_index()
            accept_counts.rename(columns={'clientId': 'chat_accepted', 'user_id': '_id'}, inplace=True)
            return accept_counts
        
        def process_chat_completed_events(self):
            intake_events = self.raw_df[self.raw_df['event_name'] == 'chat_msg_send']
            valid_user_ids = intake_events['chatSessionId'].unique()
            accept_events = self.raw_df[(self.raw_df['event_name'] == 'accept_chat') & (self.raw_df['paid'] == 0) & (self.raw_df['chatSessionId'].isin(valid_user_ids))]
            accept_events['event_time'] = pd.to_datetime(accept_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            accept_events['date'] = accept_events['event_time'].dt.date
            accept_events['hour'] = accept_events['event_time'].dt.hour
            accept_counts = accept_events.groupby(['user_id', 'date', 'hour'])['clientId'].nunique().reset_index()
            accept_counts.rename(columns={'clientId': 'chat_completed', 'user_id': '_id'}, inplace=True)
            return accept_counts
        
        def process_paid_chat_completed_events(self):
            intake_events = self.raw_df[self.raw_df['event_name'] == 'chat_msg_send']
            valid_user_ids = intake_events['chatSessionId'].unique()
            accept_events = self.raw_df[(self.raw_df['event_name'] == 'accept_chat') & (self.raw_df['paid'] != 0) & (self.raw_df['chatSessionId'].isin(valid_user_ids))]
            accept_events['event_time'] = pd.to_datetime(accept_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            accept_events['date'] = accept_events['event_time'].dt.date
            accept_events['hour'] = accept_events['event_time'].dt.hour
            accept_counts = accept_events.groupby(['user_id', 'date', 'hour'])['clientId'].nunique().reset_index()
            accept_counts.rename(columns={'clientId': 'paid_chats_completed', 'user_id': '_id'}, inplace=True)
            return accept_counts

        # def process_chat_completed_events1(self):
        #     completed_events = self.completed_df[(self.completed_df['status'] == 'COMPLETED') & (self.completed_df['type'].isin(['FREE', 'PAID']))]
        #     completed_events['createdAt'] = pd.to_datetime(completed_events['createdAt'], utc=True)
        #     completed_events['date'] = completed_events['createdAt'].dt.date
        #     completed_events['hour'] = completed_events['createdAt'].dt.hour
        #     completed_counts = completed_events.groupby(['astrologerId', 'date', 'hour'])['userId'].nunique().reset_index()
        #     completed_counts.rename(columns={'userId': 'chat_completed', 'astrologerId': '_id'}, inplace=True)
        #     return completed_counts

        # def process_paid_chat_completed_events1(self):
        #     paid_events = self.completed_df[(self.completed_df['status'] == 'COMPLETED') & (self.completed_df['type'] == 'PAID')]
        #     paid_events['createdAt'] = pd.to_datetime(paid_events['createdAt'], utc=True)
        #     paid_events['date'] = paid_events['createdAt'].dt.date
        #     paid_events['hour'] = paid_events['createdAt'].dt.hour
        #     paid_counts = paid_events.groupby(['astrologerId', 'date', 'hour'])['userId'].nunique().reset_index()
        #     paid_counts.rename(columns={'userId': 'paid_chats_completed', 'astrologerId': '_id'}, inplace=True)
        #     return paid_counts

        def merge_with_astro_data(self, final_data):
            merged_data = pd.merge(final_data, self.astro_df, on='_id', how='left')
            columns = ['_id', 'name', 'type', 'date', 'hour', 'chat_intake_requests', 'chat_accepted', 'chat_completed','cancelled_requests','avg_time_diff_minutes', 'paid_chats_completed']
            return merged_data[columns]

        def merge_with_hour_only(self, final_data):
            columns = ['date', 'hour', 'chat_intake_overall', 'chat_accepted_overall', 'chat_completed_overall','astros_live']
            return merged_data[columns]
        
        # def process_overall_chat_completed_events1(self):
        #     completed_events = self.completed_df[(self.completed_df['status'] == 'COMPLETED') & (self.completed_df['type'].isin(['FREE', 'PAID']))]
        #     completed_events['createdAt'] = pd.to_datetime(completed_events['createdAt'], utc=True)
        #     completed_events['date'] = completed_events['createdAt'].dt.date
        #     completed_events['hour'] = completed_events['createdAt'].dt.hour
        #     completed_counts = completed_events.groupby(['date', 'hour'])['userId'].nunique().reset_index()
        #     completed_counts.rename(columns={'userId': 'chat_completed_overall'}, inplace=True)
        #     return completed_counts
        
        def process_overall_chat_completed_events(self):
            intake_events = self.raw_df[self.raw_df['event_name'] == 'chat_msg_send']
            valid_user_ids = intake_events['chatSessionId'].unique()
            accept_events = self.raw_df[(self.raw_df['event_name'] == 'accept_chat') & (self.raw_df['chatSessionId'].isin(valid_user_ids))]
            accept_events['event_time'] = pd.to_datetime(accept_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            accept_events['date'] = accept_events['event_time'].dt.date
            accept_events['hour'] = accept_events['event_time'].dt.hour
            accept_counts = accept_events.groupby(['date', 'hour'])['clientId'].nunique().reset_index()
            accept_counts.rename(columns={'clientId': 'chat_completed_overall'}, inplace=True)
            return accept_counts
        
        def process_overall_chat_accepted_events(self):
            intake_events = self.raw_df[self.raw_df['event_name'] == 'chat_intake_submit']
            valid_user_ids = intake_events['user_id'].unique()
            accept_events = self.raw_df[(self.raw_df['event_name'] == 'accept_chat') & (self.raw_df['paid'] == 0) & (self.raw_df['clientId'].isin(valid_user_ids))]
            accept_events['event_time'] = pd.to_datetime(accept_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            accept_events['date'] = accept_events['event_time'].dt.date
            accept_events['hour'] = accept_events['event_time'].dt.hour
            accept_counts = accept_events.groupby(['date', 'hour'])['clientId'].nunique().reset_index()
            accept_counts.rename(columns={'clientId': 'chat_accepted_overall'}, inplace=True)
            return accept_counts
        
        def process_overall_chat_intake_requests(self):
            intake_events = self.raw_df[(self.raw_df['event_name'] == 'chat_intake_submit')]
            intake_events['event_time'] = pd.to_datetime(intake_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            intake_events['date'] = intake_events['event_time'].dt.date
            intake_events['hour'] = intake_events['event_time'].dt.hour
            user_counts = intake_events.groupby(['date', 'hour'])['user_id'].nunique().reset_index()
            user_counts.rename(columns={'user_id': 'chat_intake_overall'}, inplace=True)
            return user_counts
        
        def astros_live(self):
            intake_events = self.raw_df[(self.raw_df['event_name'] == 'accept_chat')]
            intake_events['event_time'] = pd.to_datetime(intake_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            intake_events['date'] = intake_events['event_time'].dt.date
            intake_events['hour'] = intake_events['event_time'].dt.hour
            user_counts = intake_events.groupby(['date', 'hour'])['user_id'].nunique().reset_index()
            user_counts.rename(columns={'user_id': 'astros_live'}, inplace=True)
            return user_counts

        def users_live(self):
            intake_events = self.raw_df[(self.raw_df['event_name'] == 'page_open')]
            intake_events['event_time'] = pd.to_datetime(intake_events['event_time'], utc=True) + pd.DateOffset(hours=5, minutes=30)
            intake_events['date'] = intake_events['event_time'].dt.date
            intake_events['hour'] = intake_events['event_time'].dt.hour
            user_counts = intake_events.groupby(['date', 'hour'])['user_id'].nunique().reset_index()
            user_counts.rename(columns={'user_id': 'users_live'}, inplace=True)
            return user_counts

    # Read CSV files
    raw_df = pd.read_csv(raw_file)

    # Step 4: Process Data
    raw_df = extract_json(raw_df, 'other_data')
    processor = UniqueUsersProcessor(raw_df, astro_df)
    
    # Process each event type
    intake_data = processor.process_chat_intake_requests()
    accepted_data = processor.process_chat_accepted_events()
    completed_data = processor.process_chat_completed_events()
    paid_completed_data = processor.process_paid_chat_completed_events()
    cancelled = processor.process_chat_cancels()
    cancel_time = processor.cancellation_time()
    overall_chat_completed = processor.process_overall_chat_completed_events()
    overall_chat_intakes = processor.process_overall_chat_intake_requests()
    overall_chat_accepts = processor.process_overall_chat_accepted_events()
    astro_live = processor.astros_live()
    users_live = processor.users_live()

    # Combine results
    final_results = intake_data
    final_results = pd.merge(final_results, accepted_data, on=['_id', 'date', 'hour'], how='outer')
    final_results = pd.merge(final_results, completed_data, on=['_id', 'date', 'hour'], how='outer')
    final_results = pd.merge(final_results, paid_completed_data, on=['_id', 'date', 'hour'], how='outer')
    final_results = pd.merge(final_results, cancelled, on=['_id', 'date', 'hour'], how='outer')
    final_results = pd.merge(final_results, cancel_time, on=['_id', 'date', 'hour'], how='outer')

    final_overall = overall_chat_intakes
    final_overall = pd.merge(final_overall, overall_chat_accepts, on=['date', 'hour'], how='outer')
    final_overall = pd.merge(final_overall, overall_chat_completed, on=['date', 'hour'], how='outer')
    final_overall = pd.merge(final_overall, astro_live, on=['date', 'hour'], how='outer')
    final_overall = pd.merge(final_overall, users_live, on=['date', 'hour'], how='outer')

    # Merge with astro data and display final data
    merged_data = processor.merge_with_astro_data(final_results)
    merged_overall = final_overall
    
    # Display final output
    st.write("### Final Processed Data")
    st.dataframe(merged_data)

    import plotly.express as px
    
    # Plot the graph for Chat Intake Requests - Hour-wise and Astrologer-wise
    fig1 = px.line(merged_data, x='hour', y='chat_intake_requests', color='name', line_group='name', title="Chat Intake Requests Hour-wise Astrologer-wise")
    fig1.update_layout(xaxis_title="Hour", yaxis_title="Chat Intake Requests")
    fig1.update_traces(connectgaps=False)
    st.plotly_chart(fig1)
    
    # Plot the graph for Chat Accept - Hour-wise and Astrologer-wise
    fig2 = px.line(merged_data, x='hour', y='chat_accepted', color='name', line_group='name', title="Chat Accept Hour-wise Astrologer-wise")
    fig2.update_layout(xaxis_title="Hour", yaxis_title="Chat Accepted")
    fig2.update_traces(connectgaps=False)
    st.plotly_chart(fig2)
    
    # Plot the graph for Chat Completed - Hour-wise and Astrologer-wise
    fig3 = px.line(merged_data, x='hour', y='chat_completed', color='name', line_group='name', title="Chat Completed Hour-wise Astrologer-wise")
    fig3.update_layout(xaxis_title="Hour", yaxis_title="Chat Completed")
    fig3.update_traces(connectgaps=False)
    st.plotly_chart(fig3)
    
    print(merged_overall.columns)
    
    # Plot the graph for Overall Metrics
    fig4 = px.line(merged_overall, x='hour', y=['chat_intake_overall', 'chat_accepted_overall', 'chat_completed_overall', 'astros_live', 'users_live'], 
                   title="Overall Metrics",
                   labels={
                       'chat_intake_overall': 'Chat Intakes',
                       'chat_accepted_overall': 'Chat Accepts',
                       'chat_completed_overall': 'Chat Completes',
                       'astros_live': 'Astrologers Live',
                       'users_live': 'Users Live'
                   })
    fig4.update_layout(xaxis_title="Hour", yaxis_title="Count")
    fig4.update_traces(connectgaps=False)
    st.plotly_chart(fig4)


    # Option to download final data
    csv = merged_data.to_csv(index=False)
    st.download_button("Download Final Data as CSV", data=csv, file_name="combined_data_final_hour_wise.csv", mime="text/csv")
