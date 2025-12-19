"""
Dashboard GUI Module for MedshipmentTrackingTool

Provides a user-friendly graphical interface for executing tracking operations
and scheduling automated runs.
"""

import os
import sys
import subprocess
import datetime
import tkinter as tk
from tkinter import messagebox, ttk

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.scheduler import set_time


class TrackingDashboard:
    """GUI Dashboard for the MedshipmentTrackingTool."""
    
    def __init__(self, root):
        """
        Initialize the dashboard.
        
        Args:
            root: Tkinter root window
        """
        self.root = root
        self.root.title("Medshipment Tracking Tool")
        self.root.geometry('600x400')
        self.root.resizable(False, False)
        
        # Company name - can be customized
        self.company_name = "DRITEE IMPEX"
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Create and layout all GUI widgets."""
        # Header
        now = datetime.datetime.now()
        header_label = tk.Label(
            self.root,
            text=f"Welcome, {self.company_name}",
            font=("Arial Bold", 14)
        )
        header_label.grid(column=0, row=0, columnspan=3, pady=10)
        
        date_label = tk.Label(
            self.root,
            text=f"Date: {now.strftime('%d-%m-%Y')}",
            font=("Arial", 9)
        )
        date_label.grid(column=0, row=1, columnspan=3)
        
        # Action selection
        action_label = tk.Label(
            self.root,
            text="Choose an Action:",
            font=("Arial Bold", 10)
        )
        action_label.grid(column=0, row=2, columnspan=3, pady=10)
        
        # Radio buttons for action selection
        self.selected_action = tk.IntVar(value=1)
        
        rad1 = tk.Radiobutton(
            self.root,
            text='Execute Now',
            value=1,
            variable=self.selected_action,
            font=("Arial", 9)
        )
        rad1.grid(column=0, row=3, sticky='w', padx=20)
        
        rad2 = tk.Radiobutton(
            self.root,
            text='Set Time to Execute the script',
            value=2,
            variable=self.selected_action,
            font=("Arial", 9)
        )
        rad2.grid(column=0, row=4, sticky='w', padx=20)
        
        # Time selection comboboxes (initially disabled)
        time_frame = tk.Frame(self.root)
        time_frame.grid(column=0, row=5, columnspan=3, pady=20)
        
        tk.Label(time_frame, text="Hours:", font=("Arial", 9)).grid(column=0, row=0, padx=5)
        self.combo_hours = ttk.Combobox(time_frame, width=5, state='readonly')
        self.combo_hours['values'] = tuple(range(24))
        self.combo_hours.current(0)
        self.combo_hours.grid(column=1, row=0, padx=5)
        
        tk.Label(time_frame, text="Minutes:", font=("Arial", 9)).grid(column=2, row=0, padx=5)
        self.combo_minutes = ttk.Combobox(time_frame, width=5, state='readonly')
        self.combo_minutes['values'] = tuple(range(60))
        self.combo_minutes.current(0)
        self.combo_minutes.grid(column=3, row=0, padx=5)
        
        tk.Label(time_frame, text="Seconds:", font=("Arial", 9)).grid(column=4, row=0, padx=5)
        self.combo_seconds = ttk.Combobox(time_frame, width=5, state='readonly')
        self.combo_seconds['values'] = tuple(range(60))
        self.combo_seconds.current(0)
        self.combo_seconds.grid(column=5, row=0, padx=5)
        
        # Status label
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 9),
            fg="blue"
        )
        self.status_label.grid(column=0, row=6, columnspan=3, pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(column=0, row=7, columnspan=3, pady=20)
        
        execute_btn = tk.Button(
            button_frame,
            text="Execute",
            bg="#3f51b5",
            fg="white",
            height=2,
            width=12,
            command=self._execute_script,
            font=("Arial", 10, "bold")
        )
        execute_btn.grid(column=0, row=0, padx=10)
        
        schedule_btn = tk.Button(
            button_frame,
            text="Schedule",
            bg="#3f51b5",
            fg="white",
            height=2,
            width=12,
            command=self._schedule_script,
            font=("Arial", 10, "bold")
        )
        schedule_btn.grid(column=1, row=0, padx=10)
        
        exit_btn = tk.Button(
            button_frame,
            text="Exit",
            bg="#d32f2f",
            fg="white",
            height=2,
            width=12,
            command=self._close_window,
            font=("Arial", 10, "bold")
        )
        exit_btn.grid(column=2, row=0, padx=10)
    
    def _execute_script(self):
        """Execute the tracking script immediately."""
        try:
            self.status_label.config(text="Executing tracking script...", fg="blue")
            self.root.update()
            
            # Get the path to tracker.py
            script_dir = os.path.dirname(os.path.abspath(__file__))
            tracker_script = os.path.join(script_dir, "tracker.py")
            
            # Run the tracker script
            result = subprocess.run(
                [sys.executable, tracker_script],
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour timeout
            )
            
            if result.returncode == 0:
                messagebox.showinfo(
                    'Success',
                    'Tracking script executed successfully!\n\n'
                    'Check the output directory for generated files.'
                )
                self.status_label.config(text="Execution completed successfully!", fg="green")
            else:
                error_msg = result.stderr[:500] if result.stderr else "Unknown error"
                messagebox.showerror(
                    'Error',
                    f'Script execution failed:\n{error_msg}'
                )
                self.status_label.config(text="Execution failed!", fg="red")
                
        except subprocess.TimeoutExpired:
            messagebox.showerror('Error', 'Script execution timed out (exceeded 1 hour)')
            self.status_label.config(text="Execution timed out!", fg="red")
        except Exception as e:
            messagebox.showerror('Error', f'Failed to execute script: {str(e)}')
            self.status_label.config(text="Execution failed!", fg="red")
    
    def _schedule_script(self):
        """Schedule the script to run at a specific time."""
        try:
            hours = int(self.combo_hours.get())
            minutes = int(self.combo_minutes.get())
            seconds = int(self.combo_seconds.get())
            
            # Calculate next occurrence
            now = datetime.datetime.now()
            scheduled_time = now.replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
            
            # If time has passed today, schedule for tomorrow
            if scheduled_time <= now:
                scheduled_time += datetime.timedelta(days=1)
            
            # Set the schedule
            set_time(hours, minutes, seconds)
            
            day_name = scheduled_time.strftime("%A")
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            
            self.status_label.config(
                text=f"Scheduled for {time_str} on {day_name}",
                fg="green"
            )
            
            messagebox.showinfo(
                'Scheduled',
                f'Script scheduled to run at {time_str} on {day_name}'
            )
            
        except ValueError:
            messagebox.showerror('Error', 'Please select valid time values')
            self.status_label.config(text="Invalid time selection!", fg="red")
        except Exception as e:
            messagebox.showerror('Error', f'Failed to schedule script: {str(e)}')
            self.status_label.config(text="Scheduling failed!", fg="red")
    
    def _close_window(self):
        """Close the dashboard window."""
        self.root.destroy()


def main():
    """Main entry point for the dashboard."""
    root = tk.Tk()
    app = TrackingDashboard(root)
    root.mainloop()


if __name__ == "__main__":
    main()
