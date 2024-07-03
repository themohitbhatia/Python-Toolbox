import pandas as pd
from ydata_profiling import ProfileReport

def generate_profile_report(input_file_name, output_file_name):
    df = pd.read_csv(input_file_name)
    profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
    profile.to_file(output_file_name)

input_file_name = 'enter_the_input_file_path'
output_file_name = 'enter_the_output_file_path'

generate_profile_report(input_file_name, output_file_name)