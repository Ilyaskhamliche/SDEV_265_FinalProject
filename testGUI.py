import tkinter as tk
from tkinter import ttk

class StrategoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stratego")
        self.geometry("800x600")

        # Create the main container
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Create the game board
        board_frame = ttk.Frame(main_frame)
        board_frame.pack(side="left", padx=10, pady=10)

        self.board_canvas = tk.Canvas(board_frame, width=500, height=500, bg="green")
        self.board_canvas.pack()

        # Draw the game board
        self.draw_board()

        # Create the sidebar
        sidebar_frame = ttk.Frame(main_frame)
        sidebar_frame.pack(side="right", padx=10, pady=10, fill="y")

        # Add player information
        player_info_frame = ttk.LabelFrame(sidebar_frame, text="Player Information")
        player_info_frame.pack(fill="x", padx=10, pady=10)

        # Add game controls
        control_frame = ttk.LabelFrame(sidebar_frame, text="Game Controls")
        control_frame.pack(fill="x", padx=10, pady=10)

        # Add buttons for game controls
        start_button = ttk.Button(control_frame, text="Start Game")
        start_button.pack(pady=5)

        move_button = ttk.Button(control_frame, text="Move Piece")
        move_button.pack(pady=5)

    def draw_board(self):
        # Clear the canvas
        self.board_canvas.delete("all")

        # Draw the grid lines
        for i in range(10):
            self.board_canvas.create_line(0, i * 50, 500, i * 50, fill="black")
            self.board_canvas.create_line(i * 50, 0, i * 50, 500, fill="black")

if __name__ == "__main__":
    app = StrategoGUI()
    app.mainloop()
