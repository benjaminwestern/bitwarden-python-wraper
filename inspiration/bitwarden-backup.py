# CREDIT FOR THIS REFERENCE SCRIPT GOES TO:
# https://pastebin.com/bGNL7Fhy
# https://www.reddit.com/r/Bitwarden/comments/frupl9/a_simple_backup_script_in_python/

# I am using this as inspiration for the CLI Wraper I am building for this project.

# Set up constants

from datetime import datetime

json_filename = 'vault.json'
now = datetime.now()
archive_filename = "vault-%s-%s-%s_%s-%s-%s.zip" % (now.year, now.month, now.day, now.hour, now.minute, now.second)

# Get the passwords
from getpass import getpass
bw_password = getpass(prompt="Bitwarden master password: ")
export_password = getpass(prompt="Archive password: ")

try:
    # Get the session id
    import re
    import subprocess

    unlock = subprocess.check_output(['bw', 'unlock', bw_password])
    session = re.search('BW_SESSION="(.*)"', str(unlock))[1]
    print("Your vault is unlocked")

    # Export the vault
    print(subprocess.check_output(['bw', 'export', '--output', json_filename, '--format', 'json', '--session', session, bw_password]))

    # Lock the vault
    try:
        print(subprocess.check_output(['bw', 'lock']))
    except:
        print("WARNING: Could not lock the vault, session token is still active. Execute '$bw lock' to lock your vault.")

    # Save json into encrypted archive.
    try:
        subprocess.check_output(['7z', 'a', archive_filename, json_filename, ('-p%s' % export_password)])
        print("Saved your vault inside of %s" % archive_filename)
    except:
        print("Could not create an encrypted archive. Reason could be a special characters in your password or '7z' missing.")

    # Delete the json
    import os
    try:
        os.remove(json_filename)
    except:
        print("Could not delete your uncrypted vault file. Please delete this file manually and safely.")

except:
    print(" Could not unlock your vault. Wrong password or missing Bitwarden CLI?")