import os
import pytest
from datetime import datetime

def pytest_configure(config):
    # Get the current working directory
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
   
    cwd = os.getcwd()
    # Or, if you want the directory where the tests are located
    # cwd = os.path.dirname(config.rootdir)  # config.rootdir gives the root directory of the test suite

    # Choose a filename (you can customize this logic)
    filename = f"ApiNew_test_report_{now.replace(' ', '_').replace(':', '-')}.html" # Example: test_report_2023-10-27_10-30-00.html

    # Ensure the reports directory exists
    reports_dir = os.path.join(cwd, "reports")  # Create a 'reports' subdirectory
    os.makedirs(reports_dir, exist_ok=True)       # Create it if it doesn't exist
    
    reportfilepath = os.path.join(reports_dir, filename)

    # Set the HTML path in the config
    config.option.htmlpath = reportfilepath
    