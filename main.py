import cv2
import numpy as np
import heapq
import random

SIZE = 40        # Labirent Boyutu
FILENAME = "solution.png"

COLOR_BG = (0, 0, 0)           # Siyah
COLOR_WALL = (255, 255, 0)     # Neon Cyan
COLOR_PATH = (20, 20, 20)      # Koyu Gri
COLOR_SOL = (255, 0, 255)      # Neon Pembe
COLOR_START = (0, 255, 0)      # Yeşil
COLOR_END = (0, 0, 255)        # Kırmızı

class MazeSolver:
    def __init__(self, size):
        self.size = size
        self.maze = None
        self.start = (1, 1)
        self.end = (size-2, size-2)

    def generate(self):
        while True:
            self.maze = np.zeros((self.size, self.size), dtype=int)
           
            self.maze = (np.random.rand(self.size, self.size) > 0.7).astype(int)
            
           
            self.maze[self.start], self.maze[self.end] = 0, 0
            self.maze[0, :], self.maze[-1, :], self.maze[:, 0], self.maze[:, -1] = 1, 1, 1, 1
            
            if self.is_solvable():
                break
        print(f"✅ {self.size}x{self.size} Labirent oluşturuldu.")

    def is_solvable(self):
        queue = [self.start]
        visited = {self.start}
        while queue:
            curr = queue.pop(0)
            if curr == self.end: return True
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = curr[0]+dr, curr[1]+dc
                if 0<=nr<self.size and 0<=nc<self.size and self.maze[nr,nc]==0 and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc))
        return False

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def solve_astar(self):
        rows, cols = self.maze.shape
        img = np.zeros((rows, cols, 3), dtype=np.uint8)
        img[:] = COLOR_BG
        for r in range(rows):
            for c in range(cols):
                if self.maze[r, c] == 1: img[r, c] = COLOR_WALL
      
        open_set = []
        heapq.heappush(open_set, (0, 0, self.start))
        came_from = {}
        g_score = {node: float('inf') for node in np.ndindex(self.maze.shape)}
        g_score[self.start] = 0
        
        found = False
        print("🧠 A* Algoritması çalışıyor...")

        while open_set:
            _, current_g, current = heapq.heappop(open_set)
            
            if current == self.end:
                found = True
                break
            
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                neighbor = (current[0]+dr, current[1]+dc)
                if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and 
                    self.maze[neighbor] == 0):
                    
                    tentative_g = current_g + 1
                    if tentative_g < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + self.heuristic(neighbor, self.end)
                        heapq.heappush(open_set, (f_score, tentative_g, neighbor))
        
        if found:
            print(f"🎯 Hedef bulundu! {g_score[self.end]} adım.")
            # Yolu Çiz
            curr = self.end
            while curr in came_from:
                img[curr] = COLOR_SOL
                curr = came_from[curr]
            
            img[self.start] = COLOR_START
            img[self.end] = COLOR_END
            scale = 20
            img_resized = cv2.resize(img, (cols*scale, rows*scale), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite(FILENAME, img_resized)
            print(f"💾 Çözüm görseli '{FILENAME}' olarak kaydedildi.")
        else:
            print("❌ Yol bulunamadı.")

if __name__ == "__main__":
    solver = MazeSolver(SIZE)
    solver.generate()
    solver.solve_astar()
