# -2D-Schrodinger-Equation-Numerical-Solution-in-PYTHON
This Python script simulates the spatial distribution of a quantum particle bound inside a 2D infinite potential well. By evaluating the TDSWE across a coordinate grid, it determines allowed energy eigenvalues and their stationary wavefunctions. The resulting plot visualizes the standing wave patterns and nodal lines of a high-order quantum state.

## Physics Formulation

This simulator solves for the spatial distribution of a single non-relativistic particle bound within a 2D box ($V = 0$ inside, $V \to \infty$ at the boundaries). The governing physics is defined by the TISE:

$$-\frac{\hbar^2}{2m} \nabla^2 \psi(x,y) + V(x,y)\psi(x,y) = E\psi(x,y)$$

By mapping continuous space onto a discrete mesh, the spatial second derivatives are evaluated via the central finite difference method. The boundaries enforce the hard-wall Dirichlet condition ($\psi = 0$ at the box edges), yielding distinct standing wave configurations characterized by unique spatial frequencies and geometric nodal lines.

## Visualized Eigenstates

Below are the calculated standing wave patterns showing the probability amplitudes across the spatial dimensions of the system:

### 1. Ground State ($n_x=1, n_y=1$)
![Ground State Wavefunction](images/eigenstate_1.png)
*The foundational lowest-energy configuration, exhibiting a single broad wave amplitude maximum centered in the potential well.*

### 2. First Excited State ($n_x=1, n_y=2$)
![First Excited State](images/eigenstate_2.png)
*The first antisymmetric configuration split by a single horizontal zero-amplitude nodal boundary.*

### 3. Higher-Order Quantized Profile
![High Order State](images/eigenstate_3.png)
*A high-frequency standing wave layout containing multiple geometric nodes and complex localization peaks.*

## Computational Implementation

- **Laplacian Matrix Synthesis:** Uses a spatial grid size of $150 \times 150$ ($22,500$ dimensions). Instead of building a massive full coordinate matrix, the 2D spatial Laplacian ($\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$) is synthesized efficiently by combining 1D derivative operators through a sparse Kronecker sum (`scipy.sparse.kronsum`).
- **Targeted Lanczos Eigensolver:** Because the system Hamiltonian is vast but sparse, it avoids dense matrix operations by employing `scipy.sparse.linalg.eigsh` to target and extract only the lowest 10 energy eigenvalues and their corresponding eigenvectors.

## Prerequisites & Execution

You will need standard Python scientific computing libraries installed:

```bash
pip install numpy scipy matplotlib
