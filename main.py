import tkinter as tk
from tkinter import simpledialog
import threading
import time
from PIL import ImageGrab, ImageTk

class IdleMonitor:
    def __init__(self, root):
        self.root = root
        self.idle_time = 0
        self.monitoring = True
        self.password_window = None
        self.root.bind_all('<Motion>', self.reset_idle_time)
        self.root.bind_all('<Key>', self.reset_idle_time)
        self.monitor_thread = threading.Thread(target=self.monitor_idle_time)
        self.monitor_thread.start()

    def reset_idle_time(self, event=None):
        self.idle_time = 0

    def monitor_idle_time(self):
        last_mouse_position = self.root.winfo_pointerxy()
        while self.monitoring:
            time.sleep(1)
            current_mouse_position = self.root.winfo_pointerxy()
            if current_mouse_position != last_mouse_position:
                self.idle_time = 0
                last_mouse_position = current_mouse_position
            else:
                self.idle_time += 1
            print(f"现在的计时: {self.idle_time} 秒")
            # 如果超过10秒，显示密码窗口
            if self.idle_time >= 10:
                self.show_password_window()
                self.idle_time = 0

    def show_password_window(self):
        if self.password_window is not None and self.password_window.winfo_exists():
            return

        # 截屏
        screenshot = ImageGrab.grab()
        screenshot_image = ImageTk.PhotoImage(screenshot)

        self.password_window = tk.Toplevel(self.root)
        self.password_window.attributes('-topmost', True)
        self.password_window.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")
        # self.password_window.bind('<Escape>', lambda e: self.password_window.destroy())
        self.password_window.grab_set()
        self.password_window.protocol("WM_DELETE_WINDOW", lambda: None)  # 禁止关闭窗口
        self.password_window.resizable(False, False)  # 禁止调整窗口大小
        self.password_window.overrideredirect(True)  # 去掉窗口边框

        # 设置背景为截屏图片
        background_label = tk.Label(self.password_window, image=screenshot_image)
        background_label.image = screenshot_image  # 保持引用，防止被垃圾回收
        background_label.pack(fill=tk.BOTH, expand=True)

        def check_password():
            if password_entry.get() == "123321":
                self.password_window.destroy()
                self.password_window = None

        password_frame = tk.Frame(self.password_window, bg="white")
        password_frame.place(relx=0.5, rely=0.1, anchor=tk.CENTER)  # 将密码输入框放置在屏幕上方

        password_label = tk.Label(password_frame, text="请输入密码:", bg="white")
        password_label.pack(pady=20)
        password_entry = tk.Entry(password_frame, show="*")
        password_entry.pack(pady=20)
        password_button = tk.Button(password_frame, text="确定", command=check_password)
        password_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    monitor = IdleMonitor(root)
    root.mainloop()

