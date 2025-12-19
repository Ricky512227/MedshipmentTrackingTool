"""
Web Scraper Module for MedshipmentTrackingTool

This module handles web scraping operations for tracking numbers from the IPS website
and zip code lookup from external sources.
"""

import requests
from bs4 import BeautifulSoup
import json
import os


def get_zip_codes(zip_code):
    """
    Fetches location information for a given zip code.
    
    Args:
        zip_code (str/int): The zip code to look up
        
    Returns:
        str: Comma-separated location information, or 0 if lookup fails
    """
    try:
        url = f"https://www.zip-codes.com/zip-code/{zip_code}/zip-code-{zip_code}.asp"
        response = requests.get(url, timeout=10)
        data = BeautifulSoup(response.text, "lxml")
    except Exception as e:
        print(f"Error fetching zip code data: {e}")
        return 0
    
    try:
        out_set = data.find("h1")
        if not out_set:
            return 0
        
        # Extract and format location data
        location_parts = out_set.text.encode('ascii', 'ignore').decode('ascii').split(",")
        location_parts.insert(3, location_parts[0])
        location_parts.pop(0)
        return ",".join(location_parts)
    except Exception as e:
        print(f"Error parsing zip code data: {e}")
        return 0


def fetch_tracking_data(tracking_number, ips_url):
    """
    Fetches tracking information for a given tracking number from IPS website.
    
    Args:
        tracking_number (str): The tracking number to look up
        ips_url (str): Base URL for IPS tracking
        
    Returns:
        list: List of tracking event data, or 0 if fetch fails
    """
    try:
        # Construct the tracking URL
        tracking_url = f"{ips_url}?itemid={tracking_number}&Submit=Submit"
        response = requests.get(tracking_url, timeout=15)
        
        if response.status_code != 200:
            print(f"Tracking Number {tracking_number}: Unable to hit the link (Status: {response.status_code})")
            return 0
        
        data = BeautifulSoup(response.text, "lxml")
        
        # Try to find tracking data in the expected format
        try:
            out_set = data.find('td', class_="tabproperty")
            if not out_set or len(out_set.contents) < 3:
                raise ValueError("Tracking data not found in expected format")
            
            # Extract tracking events
            tracking_rows = out_set.findAll("tr")
            if not tracking_rows:
                raise ValueError("No tracking rows found")
            
            # Get the last (most recent) tracking event
            latest_event = tracking_rows[-1]
            event_text = latest_event.text
            event_data = event_text.encode('ascii', 'ignore').decode('ascii').split("\n")
            
            # Clean up the data
            event_data.pop(0)  # Remove header
            if event_data:
                event_data.pop()  # Remove empty trailing element
            if event_data:
                event_data.pop()  # Remove another trailing element
            
            print(f"Tracking Number {tracking_number}: Successfully fetched data")
            return event_data
            
        except (AttributeError, IndexError, ValueError) as e:
            # Try alternative parsing method
            paragraphs = data.findAll("p")
            if len(paragraphs) > 1:
                error_message = paragraphs[1].text
                print(f"Tracking Number {tracking_number}: Hit link, but NO INFORMATION Available. "
                      f"Please check the ITEM MANUALLY. Message: {error_message}")
            else:
                print(f"Tracking Number {tracking_number}: Hit link, but NO INFORMATION Available. "
                      f"Please check the ITEM MANUALLY")
            return 0
            
    except requests.RequestException as e:
        print(f"Tracking Number {tracking_number}: Network error - {e}")
        return 0
    except Exception as e:
        print(f"Tracking Number {tracking_number}: Unexpected error - {e}")
        return 0
