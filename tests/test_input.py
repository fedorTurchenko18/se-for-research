"""Tests for input data formatters."""

from src.io_formatters.input import CSVReader, JSONReader, ExcelReader

def test_readers():
    """Test reading data from various formats."""
    csv_reader = CSVReader()
    json_reader = JSONReader()
    excel_reader = ExcelReader()

    # Test CSV reading
    csv_data = csv_reader.load_data('tests/data/sample_EEG-Eye-State.csv')
    assert not csv_data.empty, "CSV data should not be empty"

    # Test JSON reading
    json_data = json_reader.load_data('tests/data/sample_EEG-Eye-State.json')
    assert not json_data.empty, "JSON data should not be empty"

    # Test Excel reading
    excel_data = excel_reader.load_data('tests/data/sample_EEG-Eye-State.xlsx')
    assert not excel_data.empty, "Excel data should not be empty"


if __name__ == "__main__":
    test_readers()
