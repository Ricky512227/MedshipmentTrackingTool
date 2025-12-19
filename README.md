# MedshipmentTrackingTool

A Python-based shipment tracking tool that automates the process of tracking medical shipments through the Indian Postal Service (IPS) system. This tool reads tracking numbers from Excel files, scrapes tracking information from the IPS website, categorizes shipments by status, and generates detailed Excel reports.

## Features

- **Automated Tracking**: Reads tracking numbers from Excel input files
- **Web Scraping**: Fetches real-time tracking data from IPS website
- **Status Categorization**: Automatically categorizes shipments into:
  - Booked
  - In Transit
  - Inbound
  - Outbound
  - Delivered
  - Notice Left
  - Stuck/Customs
  - Returned
- **Excel Reports**: Generates organized Excel files with categorized data
- **GUI Dashboard**: User-friendly interface for executing tracking operations
- **Scheduled Execution**: Ability to schedule tracking runs at specific times
- **Location Enhancement**: Automatically enriches location data with zip code information

## Project Structure

```
MedshipmentTrackingTool/
├── src/
│   ├── tracker.py          # Main tracking logic
│   ├── excel_handler.py    # Excel file operations
│   ├── web_scraper.py      # Web scraping functionality
│   ├── dashboard.py        # GUI dashboard
│   └── scheduler.py        # Scheduled execution
├── data/
│   └── Input-Data.xlsx     # Input file with tracking numbers
├── output/                 # Generated output files
├── config/
│   └── config.json         # Configuration file
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.7+
- See `requirements.txt` for package dependencies

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Ricky512227/MedshipmentTrackingTool.git
cd MedshipmentTrackingTool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the paths in `config/config.json`:
```json
{
  "input_file": "data/Input-Data.xlsx",
  "output_dir": "output",
  "final_data_file": "output/Final-Data.xlsx"
}
```

## Usage

### GUI Dashboard
Run the dashboard:
```bash
python src/dashboard.py
```

### Command Line
Run tracking directly:
```bash
python src/tracker.py
```

## Input Format

The input Excel file should have the following columns:
- Column A: Order ID
- Column B: First Name
- Column C: Last Name
- Column D: Tracking Number

## Output

The tool generates:
1. `Final-Data.xlsx`: Complete tracking data with all shipments
2. `Data[timestamp].xlsx`: Categorized Excel file with separate sheets for each status
3. Summary sheet with counts for each category

## Notes

- This tool was developed for tracking medical shipments through the Indian Postal Service
- The tool scrapes data from `ipsweb.ptcmysore.gov.in`
- Some tracking numbers may not return data if they're not yet in the system

## License

Private project - All rights reserved

## Author

Developed for DRITEE IMPEX
