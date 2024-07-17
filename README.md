# Auto Lock Screen

## Usage

1. **Install Dependencies**:
   Ensure you have the required libraries installed. You can install them using pip:
   ```bash
   pip install pillow
   ```

2. **Run the Program**:
   Execute the Python script to start the idle monitor:
   ```bash
   python main.py
   ```

3. **Idle Monitoring**:
   - The program will start monitoring your idle time (mouse and keyboard activity).
   - If no activity is detected for 10 seconds, a full-screen password window will appear.

4. **Unlocking the Screen**:
   - Enter the password `123321` in the password entry field to unlock the screen.
   - The screen will remain locked until the correct password is entered.

## Customization

- **Idle Time**:
  - You can change the idle time threshold by modifying the `if self.idle_time >= 10:` line in the `monitor_idle_time` method.

- **Password**:
  - Change the password by modifying the `if password_entry.get() == "112233":` line in the `check_password` function.

## Notes

- The main Tkinter window is hidden by default (`root.withdraw()`), and only the password window will be shown when the idle time is exceeded.
- The program uses a screenshot of the current screen as the background for the password window to provide a seamless lock screen experience.
