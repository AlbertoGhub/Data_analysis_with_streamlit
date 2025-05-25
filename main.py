# IMPORTING LIBRARIES
import pandas as pd 
import matplotlib.pyplot as plt 
import streamlit as st

# STREAMLIT APP
st.title("ML Dashboard")

# Uploading the dataframe to the app
file = st.file_uploader("Please, upload your CSV file", type = "csv")

# Handling the file
if file is not None:

	# Rendering the uploaded file to a Pandas dataframe
	df = pd.read_csv(file)
	st.write("File uploaded sucessfully...")

	# Subheader
	st.subheader("Data preview")
	st.write(df.iloc[:5])

	# Stats
	st.subheader("Data Summary")
	st.write(df.describe().T)

	# Data filter (to show only the information we need)
	st.subheader("Data Filter")
	# Getting the list of options from the df
	col = list(df.columns) 
	# Droplist button
	select_col = st.selectbox("Select the column name from the dropdown", col)
	unique_values = df[select_col].unique()
	selected_values = st.selectbox("Select Values", unique_values)

	# Showing the filtered data
	filtered_data = df[df[select_col] == selected_values]
	st.write(filtered_data)

	# Update column options to match the filtered data (safeguard)
	filtered_col = list(filtered_data.columns)

	# Dropdowns for plot axes based on filtered data
	X_col = st.selectbox("Select the values for the X-Axis", filtered_col)
	Y_col = st.selectbox("Select the values for the Y-Axis", filtered_col)

	# Generating the plot with a button
	if st.button("Generate line chart"):
		st.line_chart(filtered_data.set_index(X_col)[Y_col])

else:
	st.write("No file has been uploaded yet")