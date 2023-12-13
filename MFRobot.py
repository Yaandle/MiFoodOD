import tkinter as tk
import time

class RobotSimulator:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Simulator")
        self.master.geometry("300x400")

        self.canvas = tk.Canvas(master, bg="white", height=400, width=300)
        self.canvas.pack()

        self.robot = self.canvas.create_rectangle(140, 380, 160, 400, fill="blue")

        self.move_speed = 2
        self.turn_speed = 2
        self.direction = 1  # 1 for moving up, -1 for moving down

        self.master.bind("<Up>", self.move_up)

        self.update()

    def move_up(self, event):
        self.direction *= -1  # Change direction when the "Up" key is pressed

    def update(self):
        x1, y1, x2, y2 = self.canvas.coords(self.robot)

        if self.direction == -1 and y1 <= 0:
            self.direction = 1  # Reverse direction when hitting the top
        elif self.direction == 1 and y2 >= 400:
            self.direction = -1  # Reverse direction when hitting the bottom

        self.canvas.move(self.robot, 0, self.direction * self.move_speed)
        self.master.after(10, self.update)  # Update every 10 milliseconds

def main():
    root = tk.Tk()
    app = RobotSimulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
