"""
Main Tracking Module for MedshipmentTrackingTool

This is the core module that orchestrates the tracking process:
1. Reads tracking numbers from Excel
2. Fetches tracking data from IPS website
3. Enhances location data with zip codes
4. Generates Excel reports
"""

import os
import sys
import json
import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.web_scraper import fetch_tracking_data, get_zip_codes
from src.excel_handler import ExcelHandler


class ShipmentTracker:
    """Main class for tracking shipments."""
    
    def __init__(self, config_path="config/config.json"):
        """
        Initialize the tracker.
        
        Args:
            config_path (str): Path to configuration file
        """
        self.excel_handler = ExcelHandler(config_path)
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.miscellaneous = []  # Track numbers that couldn't be processed
    
    def process_tracking_numbers(self):
        """
        Main method to process all tracking numbers.
        
        Returns:
            list: List of tracking records
        """
        # Read input data
        order_ids, first_names, last_names, tracking_numbers = self.excel_handler.read_input_data()
        
        # Process each tracking number
        tracking_data = []
        
        for i, tracking_number in enumerate(tracking_numbers):
            if tracking_number is None:
                continue
            
            print(f"\n[{i+1}/{len(tracking_numbers)}] Processing: {tracking_number}")
            
            # Fetch tracking data
            event_data = fetch_tracking_data(tracking_number, self.config['ips_tracking_url'])
            
            if event_data == 0:
                self.miscellaneous.append(tracking_number)
                continue
            
            # Enhance location data with zip code if needed
            try:
                if len(event_data) > 2:
                    location_field = event_data[2]
                    # Try to get zip code information if it's a numeric zip code
                    if isinstance(location_field, (int, str)):
                        try:
                            zip_code = int(location_field)
                            zip_info = get_zip_codes(str(zip_code))
                            if zip_info != 0:
                                event_data[2] = zip_info
                        except ValueError:
                            # Not a zip code, keep original location
                            pass
            except (IndexError, ValueError) as e:
                print(f"Warning: Could not enhance location data: {e}")
            
            # Add order information to the tracking data
            record = list(event_data)
            record.insert(3, order_ids[i] if i < len(order_ids) else "")
            record.insert(4, first_names[i] if i < len(first_names) else "")
            record.insert(5, last_names[i] if i < len(last_names) else "")
            record.insert(6, tracking_number)
            
            # Handle empty extra information field
            if len(record) > 10 and (not record[-1] or len(str(record[-1]).strip()) == 0):
                record[-1] = "No information available"
            
            tracking_data.append(record)
        
        return tracking_data
    
    def run(self):
        """
        Execute the complete tracking process.
        """
        print("=" * 60)
        print("MedshipmentTrackingTool - Starting Tracking Process")
        print("=" * 60)
        print(f"Start Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # Process tracking numbers
        tracking_data = self.process_tracking_numbers()
        
        if not tracking_data:
            print("\nNo tracking data was successfully retrieved.")
            return
        
        # Write final data
        print(f"\nWriting {len(tracking_data)} records to Final-Data.xlsx...")
        self.excel_handler.write_final_data(tracking_data)
        
        # Categorize shipments
        print("\nCategorizing shipments...")
        categories = self.excel_handler.categorize_shipments()
        
        # Generate categorized report
        print("Generating categorized report...")
        report_file = self.excel_handler.generate_categorized_report(categories)
        
        # Print summary
        print("\n" + "=" * 60)
        print("TRACKING SUMMARY")
        print("=" * 60)
        print(f"Total Processed: {len(tracking_data)}")
        print(f"Delivered: {len(categories.get('Delivered', []))}")
        print(f"Booked: {len(categories.get('Booked', []))}")
        print(f"In Transit: {len(categories.get('InTransit', []))}")
        print(f"Inbound: {len(categories.get('InBound', []))}")
        print(f"Outbound: {len(categories.get('OutBound', []))}")
        print(f"Notice Left: {len(categories.get('NoticeLeft', []))}")
        print(f"Stuck: {len(categories.get('Stuck', []))}")
        print(f"Returned: {len(categories.get('Returned', []))}")
        print(f"Failed/No Info: {len(self.miscellaneous)}")
        print("=" * 60)
        print(f"\nReport generated: {report_file}")
        print(f"End Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main():
    """Main entry point."""
    try:
        tracker = ShipmentTracker()
        tracker.run()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
