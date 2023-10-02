import tkinter as tk
import random
import tkinter.messagebox

SIZE = 4
CELL_SIZE = 100
BG_COLOR = "#bbada0"
COLORS = {
    0: "#cdc1b4",
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e"
}

class Game:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("2048")
        self.window.geometry(f"{SIZE * CELL_SIZE}x{SIZE * CELL_SIZE}+300+300")
        self.window.configure(bg=BG_COLOR)
        self.window.resizable(False, False)
        self.window.bind("<Up>", self.up)
        self.window.bind("<Down>", self.down)
        self.window.bind("<Left>", self.left)
        self.window.bind("<Right>", self.right)
        self.data = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
        self.score = 0  
        self.generate()
        self.generate()
        self.labels = [[tk.Label(self.window, text="", font=("Arial", 32), bg=BG_COLOR, width=4, height=2) for _ in range(SIZE)] for _ in range(SIZE)]
        self.update()
        self.window.mainloop()

    def update(self):
        for i in range(SIZE):
            for j in range(SIZE):
                value = self.data[i][j]
                label = self.labels[i][j]
                if value == 0:
                    label["text"] = ""
                else:
                    label["text"] = str(value)
                label["bg"] = COLORS[value]
                label.grid(row=i, column=j)
        self.window.title(f"2048 - Score: {self.score}")

    def generate(self):
        empty_cells = []
        for i in range(SIZE):
            for j in range(SIZE):
                if self.data[i][j] == 0:
                    empty_cells.append((i, j))
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.data[i][j] = 2 if random.random() < 0.9 else 4

    def is_over(self):
        for i in range(SIZE):
            for j in range(SIZE):
                if self.data[i][j] == 0:
                    return False
                if j < SIZE - 1 and self.data[i][j] == self.data[i][j + 1]:
                    return False
                if i < SIZE - 1 and self.data[i][j] == self.data[i + 1][j]:
                    return False
        return True

    def up(self, event):
        moved = False
        for j in range(SIZE):
            non_zeros = []
            for i in range(SIZE):
                if self.data[i][j] != 0:
                    non_zeros.append(self.data[i][j])
            merged = []
            index = 0
            while index < len(non_zeros):
                if index == len(non_zeros) - 1 or non_zeros[index] != non_zeros[index + 1]:
                    merged.append(non_zeros[index])
                    index += 1
                else:
                    merged.append(non_zeros[index] * 2)  
                    self.score += non_zeros[index] * 2  
                    index += 2
            merged.extend([0] * (SIZE - len(merged)))
            for i in range(SIZE):
                if self.data[i][j] != merged[i]:
                    moved = True
                self.data[i][j] = merged[i]
        if moved:
            self.generate()
            self.update()
        if self.is_over():
            tk.messagebox.showinfo("Game Over", f"You lose! Your score: {self.score}")
            self.window.destroy()

    def down(self, event):
        moved = False
        for j in range(SIZE):
            non_zeros = []
            for i in range(SIZE - 1, -1, -1):
                if self.data[i][j] != 0:
                    non_zeros.append(self.data[i][j])
            merged = []
            index = 0
            while index < len(non_zeros):
                if index == len(non_zeros) - 1 or non_zeros[index] != non_zeros[index + 1]:
                    merged.insert(0, non_zeros[index])
                    index += 1
                else:
                    merged.insert(0, non_zeros[index] * 2)  
                    self.score += non_zeros[index] * 2  
                    index += 2
            merged = [0] * (SIZE - len(merged)) + merged
            for i in range(SIZE):
                if self.data[i][j] != merged[i]:
                    moved = True
                self.data[i][j] = merged[i]
        if moved:
            self.generate()
            self.update()
        if self.is_over():
            tk.messagebox.showinfo("Game Over", f"You lose! Your score: {self.score}")
            self.window.destroy()

    def left(self, event):
        moved = False
        for i in range(SIZE):
            non_zeros = []
            for j in range(SIZE):
                if self.data[i][j] != 0:
                    non_zeros.append(self.data[i][j])
            merged = []
            index = 0
            while index < len(non_zeros):
                if index == len(non_zeros) - 1 or non_zeros[index] != non_zeros[index + 1]:
                    merged.append(non_zeros[index])
                    index += 1
                else:
                    merged.append(non_zeros[index] * 2)  
                    self.score += non_zeros[index] * 2  
                    index += 2
            merged.extend([0] * (SIZE - len(merged)))
            for j in range(SIZE):
                if self.data[i][j] != merged[j]:
                    moved = True
                self.data[i][j] = merged[j]
        if moved:
            self.generate()
            self.update()
        if self.is_over():
            tk.messagebox.showinfo("Game Over", f"You lose! Your score: {self.score}")
            self.window.destroy()

    def right(self, event):
        moved = False
        for i in range(SIZE):
            non_zeros = []
            for j in range(SIZE - 1, -1, -1):
                if self.data[i][j] != 0:
                    non_zeros.append(self.data[i][j])
            merged = []
            index = 0
            while index < len(non_zeros):
                if index == len(non_zeros) - 1 or non_zeros[index] != non_zeros[index + 1]:
                    merged.insert(0, non_zeros[index])
                    index += 1
                else:
                    merged.insert(0, non_zeros[index] * 2)  
                    self.score += non_zeros[index] * 2  
                    index += 2
            merged = [0] * (SIZE - len(merged)) + merged
            for j in range(SIZE):
                if self.data[i][j] != merged[j]:
                    moved = True
                self.data[i][j] = merged[j]
        if moved:
            self.generate()
            self.update()
        if self.is_over():
            tk.messagebox.showinfo("Game Over", f"You lose! Your score: {self.score}")
            self.window.destroy()

if __name__ == "__main__":
    game = Game()
