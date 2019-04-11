import numpy as np

def ex1_calculPai(lbd, p01,p02,mu1,mu2,mu3):
    p = np.array([p01, p02, 0])
    mu = np.array([1/mu1, 1/mu2, 1/mu3])
    P = np.array([[0.0, 0.0, 1.0],
                   [0.0, 0.0, 1.0],
                   [0.0, 0.0, 0.0]])
    I = np.eye(3)
    Q = I-P
    e = p*Q.I
    LBD = lbd*e
    ro = np.multiply(LBD, mu)
    pai = 1
    for i in range(0,3):
        r = ro.item(i)
        pai = pai*(1-r)*r

    return pai, ro

def hospital_calculRho(nbFiles, lbd, mu, p0, P):
    I = np.eye(nbFiles, nbFiles)
    Q = np.linalg.inv(I - P)
    e = np.dot(p0, Q)
    rho = (lbd * e) / mu
    return np.around(rho, decimals=5)