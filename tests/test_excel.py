from utils.excel_utils import get_data_from_excel


class TestExcel:
    def test_excel(self):
        get_data_from_excel(r"C:\Users\ASUS\Downloads\Success Map 8.0.xlsx", "Important")
