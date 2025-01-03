# Import required modules
import time

def digital_clock():
    while True:
        # Get the current time
        current_time = time.strftime("%H:%M:%S")  # 24-hour format
        print("\r" + current_time, end="")  # Update the time on the same line
        time.sleep(1)  # Wait for 1 second before updating

# Run the digital clock
digital_clock()
