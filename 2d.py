import numpy as np
from scipy.sparse.linalg import eigsh
from scipy.sparse.linalg import eigs
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import PillowWriter
from scipy import sparse
N=150
L=1.0
ds=L/(N-1)
x=np.linspace(0,L,N)
X,Y=np.meshgrid(np.linspace(0,1,N,dtype=float),np.linspace(0,1,N,dtype=float))

def getv(x,y):
    return np.zeros_like(x)

V_grid=getv(X,Y)
diag=np.ones([N])
diags=np.array([diag,-2*diag,diag])
D=sparse.spdiags(diags,np.array([-1,0,1]),N,N)
T=-1/2*sparse.kronsum(D,D)
U=sparse.diags(V_grid.reshape(N**2),(0))
H=T+U
eigenvalues,eigenvectors=eigsh(H,k=10,which="SM")

def gete(n):
    return eigenvectors.T[n].reshape((N,N))
plt.figure(figsize=(9,9))
plt.contourf(X,Y,gete(8),20)
plt.savefig('eigenstate_3.png', dpi=150)
plt.show()