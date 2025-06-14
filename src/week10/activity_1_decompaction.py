'''
Activity Week10-1: Do decompaction for the following function
Decompose the following function and share your results via a GitHub link. See the function below:
 
import datetime
 
def log_event(event_type, user_id, message):

    """Logs an event to a file with timestamp, event type, user ID, and message."""

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"

    with open("rental_log.txt", "a") as log_file:

        log_file.write(log_message)
 
'''
import datetime
 
def log_event(event_type, user_id, message):
    """Logs an event to a file with timestamp, event type, user ID, and message."""
    timestamp = get_current_timestamp()
    log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"
    print(log_message)
    write_file("rental_log.txt", "a", log_message)

def get_current_timestamp():
    """Return the current timestamp"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def write_file(file_name, mode, content):
    """Write content into a file based on the given mode"""
    with open(file_name, mode) as file:
        file.write(content)

log_event("event_type_test", "user_id_test", "message_test")