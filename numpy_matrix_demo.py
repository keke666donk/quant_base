import numpy as np
# a=np.array([[1,2],[3,4]])
# b=np.array([10,20])
# print("juzhena:")
# print(a)
# print("juzhenb:")
# print(b)
# print("juzhena+b:")
# print(a+b)
# def mlt(A,B):
#     m=A.shape[0]
#     n=A.shape[1]
#     k=B.shape[1]
#     re=np.zeros((m,k))
#     for i in range(m):
#         for j in range(k):
#             h=0
#             for t in range(n):
#                 h=h+A[i,t]*B[t,j]
#             re[i,j]=h
#     return re
# M1=np.array([[1,2],[3,4]])
# M2=np.array([[5,6],[7,8]])
# m1=mlt(M1,M2)
# m2=M1@M2
# print(m1)
# print(m2)
# print("shifouxiangdeng:",np.allclose(m1,m2))
# def z(A):
#     m=A.shape[0]
#     n=A.shape[1]
#     ret=np.zeros((n,m))
#     for i in range(m):
#         for j in range(n):
#             ret[j,i]=A[i,j]
#     return ret
# M=np.array([[1,2],[3,4]])
# m=z(M)
# print(m)
# A=np.array([[1,2],[3,4]])
# r=A.T@A
# print(r)
# def dot(u,v):
#     t=u.shape[0]
#     s=0
#     for i in range(t):
#         s=s+u[i]*v[i]
#     return s
# u=np.array([1,2,3])
# v=np.array([4,5,6])
# re=dot(u,v)
# print(re)
def mat(A):
    n=A.shape[0]
    aug=np.hstack([A.copy(),np.eye(n)])
    for col in range(n):
        p=np.argmax(np.abs(aug[col:n,col]))+col
        aug[[col,p]]=aug[[p,col]]
        c=aug[col,col]
        if abs(c)<1e-10:
            raise ValueError("gaihuanyuancuowu")
        aug[col,:]=aug[col,:]/aug[col,col]
        for i in range(n):
            if i!=col:
            f=aug[i,col]
            aug[i,:]=aug[i,:]-f*aug[col,:]
    A1=aug[:,n:]
    return A1
def my(X,Y):
    XTX=X.T@X
    XTY=X.T@Y
    XTX_inv=mat(XTX)
    n=XTX_inv@XTY
    return n
X=np.array([[1,1],[1,2],[2,1],[2,2]],dtype=float)
Y=np.array([[5],[8],[7],[10]],dtype=float)
b=my(X,Y)
print("zuixiaoerchengfa",b)
