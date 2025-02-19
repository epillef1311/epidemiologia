import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SIRSimulation:
    def __init__(self, grid_size=50, tau=0.2, gamma=0.3, steps=100, initial_infected=10):
        self.grid_size = grid_size
        self.tau = tau
        self.gamma = gamma
        self.steps = steps
        
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        
        idx = np.random.choice(grid_size * grid_size, initial_infected, replace=False)
        self.grid[np.unravel_index(idx, (grid_size, grid_size))] = 1
    
    def get_neighbors(self, i, j):
        neighbors = []
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < self.grid_size and 0 <= nj < self.grid_size:
                neighbors.append((ni, nj))
        return neighbors
    
    def update(self, frame):
        new_grid = self.grid.copy()
        
        infected = np.argwhere(self.grid == 1)
        susceptible = np.argwhere(self.grid == 0)
        
        for i, j in susceptible:
            if any(self.grid[x, y] == 1 for x, y in self.get_neighbors(i, j)):
                if np.random.rand() < self.tau:
                    new_grid[i, j] = 1
        
        for i, j in infected:
            if np.random.rand() < self.gamma:
                new_grid[i, j] = 2
        
        self.grid = new_grid
        self.mat.set_array(self.grid)
        return [self.mat]
    
    def run(self):
        fig, ax = plt.subplots()
        self.mat = ax.matshow(self.grid, cmap='plasma', vmin=0, vmax=2)
        plt.colorbar(self.mat, ticks=[0, 1, 2], label='State')
        ax.set_title('SIR Simulation on Grid')
        
        ani = animation.FuncAnimation(fig, self.update, frames=self.steps, interval=100, blit=True)
        plt.show()

sim = SIRSimulation(grid_size=50, tau=0.3, gamma=0.1, steps=100, initial_infected=10)
sim.run()

