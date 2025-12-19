"""
Scheduler Module for MedshipmentTrackingTool

Handles scheduled execution of the tracking script at specified times.
"""

import os
import sys
import subprocess
from datetime import datetime, timedelta
from threading import Timer


def set_time(hours, minutes, seconds):
    """
    Schedule the tracking script to run at a specific time.
    
    Args:
        hours (int): Hour (0-23)
        minutes (int): Minute (0-59)
        seconds (int): Second (0-59)
    """
    # Get current time
    now = datetime.today()
    
    # Calculate target time for today
    target_time = now.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
    
    # If target time has passed today, schedule for tomorrow
    if target_time <= now:
        target_time += timedelta(days=1)
    
    # Calculate seconds until target time
    delta = target_time - now
    seconds_until_run = delta.total_seconds()
    
    print(f"Script scheduled to run at {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Time until execution: {delta}")
    
    def trigger_script():
        """Execute the tracking script."""
        print("=" * 60)
        print("Scheduled script execution triggered!")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        try:
            # Get the path to tracker.py
            script_dir = os.path.dirname(os.path.abspath(__file__))
            tracker_script = os.path.join(script_dir, "tracker.py")
            
            # Execute the script
            subprocess.run([sys.executable, tracker_script])
            
        except Exception as e:
            print(f"Error executing scheduled script: {e}")
            import traceback
            traceback.print_exc()
    
    # Create and start timer
    timer = Timer(seconds_until_run, trigger_script)
    timer.start()
    
    return timer
