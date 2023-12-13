import numpy as np #numpy 불러오기

array1 = np.array([1, 2, 3]) #numpy의 array함수 사용, 파라미터로 [1, 2, 3] 넘김
print(array1)

array2 = np.array([[1, 2], [4, 5], [3,6]])
print(array2)

#ndarray : n차원 배열
print(type(array1)) 
print(type(array2))

#행렬 shape
print(array1.shape)
print(array2.shape)

#요소 개수
print(array1.size)
print(array2.size)

#7을 6개의 균일한 값으로 나열
array3 = np.full(6, 7)
print(array3)

#모든 값을 0으로 만듬, zeros 대신 ones 사용시 모든 값이 1이 됨
array4 = np.zeros(6, dtype=int)
print(array4)

#랜덤 값 생성(numpy모듈 안에 random모듈, random모듈 안에 random함수 사용)
array5 = np.random.random(6)
print(array5)

#arange(m) : 0 ~ (m-1)까지의 값
array6 = np.arange(6)
print(array6)

#arange(n, m) : n부터 (m-1)까지의 값
array7 = np.arange(2, 7)
print(array7)

#arange(n, m, s) : n부터 (m-1)까지 간격이 s만큼의 값
array8 = np.arange(3, 17, 3)
print(array8)

#numpy array : 문법이 간단하여 뛰어난 성능, 한 배열에 같은 type만 가능
array9 = np.array([1, 2, 3])
array10 = np.array([1, 2, 3])
print(array9 + array10)

#list : 한 배열에 다른 type 가능
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 + list2)

print(array9 + 5)
#print(list1 + 5)
print(array9 * 3)
print(list1 * 3)

#numpy 기본 통계 기능
print(array1.max()) #최댓값
print(array1.min()) #최솟값
print(array1.mean()) #평균값
print(np.median(array1)) #중간값( numpy araay의 메소드가 아닌 numpy의 메소드)
print(array1.std()) #표준편차
print(array1.var()) #분산