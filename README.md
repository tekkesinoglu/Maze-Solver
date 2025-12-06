# 🕹️ Cyberpunk Neon Maze Solver (A* Algorithm)

An algorithmic pathfinding project that generates random "Cyberpunk-style" mazes and solves them using the **A* (A-Star)** algorithm. The solution is rendered with a high-contrast neon aesthetic.

![Solution Demo](neon_solution.png)

## 🧠 The Logic: A* vs BFS

Why use A* instead of standard BFS?
* **Smart Search:** Unlike BFS which searches blindly in all directions (like spilling water), A* uses a **Heuristic Function** (Manhattan Distance) to estimate the cost to the goal.
* **Efficiency:** It prioritizes paths that move *towards* the target, acting like a guided missile.
* **Optimality:** It is mathematically guaranteed to find the shortest possible path.

## 🛠️ Tech Stack
* **Python**
* **NumPy:** For matrix-based maze generation.
* **OpenCV:** For image processing and rendering.

## 🚀 How to Run

1.  Install dependencies:
    ```bash
    pip install numpy opencv-python
    ```

2.  Run the solver:
    ```bash
    python main.py
    ```

3.  The script will generate a unique maze, solve it, and save the result as `neon_solution.png`.

## 🎨 Visualization Colors
* 🟦 **Cyan:** Walls
* 🟪 **Pink:** Optimal Path (Calculated by AI)
* 🟩 **Green:** Start
* 🟥 **Red:** End

## 🤝 License
MIT License.
