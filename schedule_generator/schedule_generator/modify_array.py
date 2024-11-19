import sys
import re

def main():
    # Define the path to your settings.py
    settings_path = './settings.py'

    # Get the new app name from command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python modify_installed_apps.py <new_app_name>")
        sys.exit(1)

    new_app = sys.argv[1]

    # Read the contents of settings.py
    with open(settings_path, 'r') as f:
        settings = f.read()

    # Use regex to locate the INSTALLED_APPS array
    match = re.search(r'INSTALLED_APPS\s*=\s*\[(.*?)\]', settings, re.DOTALL)

    if not match:
        print("Could not find INSTALLED_APPS in settings.py.")
        sys.exit(1)

    installed_apps = match.group(1)

    # Check if the app is already installed
    if f"'{new_app}'" in installed_apps:
        print(f"'{new_app}' is already in INSTALLED_APPS.")
        return

    # Add the new app to the INSTALLED_APPS list
    updated_apps = installed_apps.strip() + f",\n    '{new_app}'"

    # Replace the original INSTALLED_APPS list with the updated one
    new_settings = settings.replace(installed_apps, updated_apps)

    # Write the changes back to settings.py
    with open(settings_path, 'w') as f:
        f.write(new_settings)

    print(f"Added '{new_app}' to INSTALLED_APPS.")

if __name__ == "__main__":
    main()