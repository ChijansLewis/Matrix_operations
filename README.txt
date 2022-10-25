python AnyMatrix.py det
python AnyMatrix.py multi
python AnyMatrix.py transposition
python AnyMatrix.py inv
python AnyMatrix.py adjoint

Run the program to reach python 3.10 or above, if you have python4 or above in the future, please install this version
The numpy library needs to be installed or updated to the latest
Ask non-programmer users not to change the running code
The first row finds the determinant of the matrix a, and can only produce floating-point @ If you need a fraction, run 4,5 respectively, using det=adjoint/inverse calculation
The second row finds the matrix a right multiplied by the matrix b
The third line seeks the transpose of a
The fourth line is to find the inverse of the matrix a, make sure that the matrix is invertible
The 5th row is the adjoint matrix of the matrix a, and does not yet support determinants of 0
Go to AnyMatrix.py modify the format of a and b

运行程序要达到python3.10以上版本，若以后有python4以上，请安装此版本
需要安装或更新numpy库至最新
请非程序员用户不要更改运行代码
第1行为求矩阵a的行列式,只能出浮点型@若是需要分式型，请分别运行4，5，利用det=adjoint/inverse计算
第2行为求矩阵a右乘矩阵b
第3行为求a的转置
第4行为求矩阵a的逆矩阵，请确保矩阵可逆
第5行为求矩阵a的伴随矩阵,暂不支持行列式为0的
进入AnyMatrix.py修改a,b的格式即可