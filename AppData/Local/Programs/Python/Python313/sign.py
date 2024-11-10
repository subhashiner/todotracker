import tkinter as tk
import cv2
from tkinter import messagebox

# Tkinter GUI to display webcam
class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Open video source (0 for default webcam)
        self.vid = cv2.VideoCapture(0)

        if not self.vid.isOpened():
            messagebox.showerror("Error", "Unable to access webcam.")
            self.window.quit()
            return

        # Create a canvas to hold the video feed
        self.canvas = tk.Canvas(window, width=640, height=480)
        self.canvas.pack()

        # Button to close the app
        self.btn_snapshot = tk.Button(window, text="Quit", width=10, command=window.quit)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)

        # Update the video feed
        self.update()

        # Run the GUI loop
        self.window.mainloop()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()

        if ret:
            # Convert frame from BGR to RGB (for displaying in Tkinter)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert the frame to a Tkinter-compatible image object
            photo = tk.PhotoImage(width=frame.shape[1], height=frame.shape[0])

            # Create an image from the frame
            for y in range(frame.shape[0]):
                for x in range(frame.shape[1]):
                    r, g, b = frame[y, x]
                    photo.put(f'#{r:02x}{g:02x}{b:02x}', (x, y))

            # Display the image in the canvas
            self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)

        # Call update every 15ms
        self.window.after(15, self.update)

    def __del__(self):
        # Release the video source when the object is destroyed
        if self.vid.isOpened():
            self.vid.release()


# Run the application
WebcamApp(tk.Tk(), "Webcam Viewer")
