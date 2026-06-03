import tkinter as tk
import numpy as np

def capture_drawing():
    raw_x = []
    raw_y = []
    last_x = 0
    last_y = 0
    complex_points = None

    root = tk.Tk()
    root.title("The Scribe's Canvas")
    root.geometry("800x800")
    root.resizable(False, False)

    canvas = tk.Canvas(root, bg="white", width=800, height=800)
    canvas.pack(fill=tk.BOTH, expand=True)

    def on_press(event):
        nonlocal last_x, last_y
        raw_x.clear()
        raw_y.clear()
        canvas.delete("all")
        last_x = event.x
        last_y = event.y
        raw_x.append(event.x)
        raw_y.append(event.y)

    def on_drag(event):
        nonlocal last_x, last_y
        canvas.create_line(last_x, last_y, event.x, event.y, fill="black", width=2, capstyle=tk.ROUND, smooth=True)
        last_x = event.x
        last_y = event.y
        raw_x.append(event.x)
        raw_y.append(event.y)

    def on_release(event):
        nonlocal complex_points
        
        if len(raw_x) < 2:
            return

        x_arr = np.array(raw_x)
        y_arr = 800 - np.array(raw_y)
        
        dx = np.diff(x_arr)
        dy = np.diff(y_arr)
        distances = np.sqrt(dx**2 + dy**2)
        S = np.concatenate(([0], np.cumsum(distances)))
        
        M = 20000
        S_ideal = np.linspace(0, S[-1], M)
        
        even_x = np.interp(S_ideal, S, x_arr)
        even_y = np.interp(S_ideal, S, y_arr)
        
        complex_points = even_x + 1j * even_y
        
        root.quit()
        root.destroy()

    canvas.bind("<Button-1>", on_press)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_release)

    root.mainloop()

    return complex_points

if __name__ == "__main__":
    points = capture_drawing()
    if points is not None:
        print(f"Forged {len(points)} uniform complex points.")