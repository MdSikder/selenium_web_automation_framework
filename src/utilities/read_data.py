import pandas as pd

def get_test_data(sheet_name, file_path="TestData/data.xlsx"):
    try:
        data = pd.read_excel(file_path, sheet_name=sheet_name)
        return data
    except Exception as e:
        print(f"Error reading test data: {e}")
        return None
