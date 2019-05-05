import numpy as np

def ex1_calculPai(lbd, p01,p02,mu1,mu2,mu3):
    p = np.array([[p01, p02, 0]])
    mu = np.array([[mu1, mu2, mu3]])
    P = np.array([[0.0, 0.0, 1.0],
                  [0.0, 0.0, 1.0],
                  [0.0, 0.0, 0.0]
                  ])
    I = np.eye(3)
    Q = np.linalg.inv(I-P)
    e = np.dot(p, Q)
    ro = (lbd * e)/mu
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
    return np.around(rho, decimals=4), e

def calcul_MeanNumInNode(rho):
    N = []
    for r in rho:
        n = (r * 10) / ((1 - r) * 10)
        N.append(n)
    return np.around(N, decimals=4)

def calcul_MeanSojornTimeInNode(N, lbd, e):
    return np.around(N/(lbd * e), decimals=4)

def calcul_MeanWaitTimeInNode(T, mu):
    W = []
    for i in range(len(T)):
        w = T[i] - 1/mu[i]
        W.append(w)
    return np.around(W, decimals=4)

def best_mu(lbd, e, C):
    mu_best = []
    lbdi_sqrt_sum = 0
    lbdi_sum = 0
    for ele in e:
        lbdi = lbd * ele
        lbdi_sqrt_sum += np.sqrt(lbdi)
        lbdi_sum += lbdi
    for ele in e:
        lbdi = lbd * ele
        mui = lbdi + np.sqrt(lbdi)/lbdi_sqrt_sum * (C - lbdi_sum)
        mu_best.append(mui)
    return np.around(mu_best, decimals=4)
