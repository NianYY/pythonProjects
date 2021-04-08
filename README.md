# pythonProjects

# 主要思路： #
1.记录每个人的位置坐标，病毒传播时需计算两个人之间的距离。小于安全距离时，病毒以一定几率传播。  
3.每一轮迭代，选定一部分人在一个以自身为圆心的圆形范围内随机移动。  
4.每轮迭代的时候每个感染者遍历其他人的位置，尝试向其传播病毒。  
5.每一轮迭代，每个人的状态可能发生改变，状态有：健康，感染病毒（未确诊），确诊，死亡和被治愈。  
6.状态改变通过设定一定的几率实现，比如设置感染后被确诊的几率会随着感染的时间逐渐变大（感染有潜伏期，时间越长越可能表现出症状）  
7.每个人初始位置的设定，服从正态分布。并设定初始感染人数为固定值。  
# 运行结果 #
## 1.限制活动范围-戴口罩-确诊即隔离 ##
![image](https://user-images.githubusercontent.com/24203428/114024256-66b40900-98a6-11eb-87af-0a03ddbc3686.png)
![image](https://user-images.githubusercontent.com/24203428/114024414-98c56b00-98a6-11eb-915d-f98f9b918192.png)
![image](https://user-images.githubusercontent.com/24203428/114024425-9d8a1f00-98a6-11eb-95cf-1d0e245e1f53.png)
![image](https://user-images.githubusercontent.com/24203428/114024421-9bc05b80-98a6-11eb-83a7-490eb152197f.png)
![image](https://user-images.githubusercontent.com/24203428/114024430-9fec7900-98a6-11eb-8928-fddfdc3547c1.png)
![image](https://user-images.githubusercontent.com/24203428/114024441-a4b12d00-98a6-11eb-8ded-c3dc39890b81.png)
## 2.正常活动范围-不戴口罩-确诊即隔离 ##
![image](https://user-images.githubusercontent.com/24203428/114024580-cca09080-98a6-11eb-8534-b91566181dfa.png)
![image](https://user-images.githubusercontent.com/24203428/114024587-ce6a5400-98a6-11eb-9bf6-4d6748a8db1f.png)
![image](https://user-images.githubusercontent.com/24203428/114024607-d6c28f00-98a6-11eb-88e8-cccb2717418f.png)
![image](https://user-images.githubusercontent.com/24203428/114024613-d9bd7f80-98a6-11eb-8b5e-1bd40cc86de2.png)
![image](https://user-images.githubusercontent.com/24203428/114024620-dc1fd980-98a6-11eb-9176-cb26ebc32596.png)
![image](https://user-images.githubusercontent.com/24203428/114024632-df1aca00-98a6-11eb-9fa9-a2c1f831bb03.png)
## 3.正常活动范围-戴口罩-确诊即隔离 ##
![image](https://user-images.githubusercontent.com/24203428/114024761-02de1000-98a7-11eb-95b3-2b9af6e1ae66.png)
![image](https://user-images.githubusercontent.com/24203428/114024771-06719700-98a7-11eb-98b4-45ba74b24d70.png)
![image](https://user-images.githubusercontent.com/24203428/114024790-0bcee180-98a7-11eb-8661-8733b1c22e81.png)
![image](https://user-images.githubusercontent.com/24203428/114024804-10939580-98a7-11eb-98c0-6dd077ec49b0.png)
![image](https://user-images.githubusercontent.com/24203428/114024816-14271c80-98a7-11eb-96b6-4c7367393a77.png)
![image](https://user-images.githubusercontent.com/24203428/114024832-18533a00-98a7-11eb-8cc1-a79952b9714f.png)
## 4.限制活动范围-戴口罩-确诊即隔离 ##
![image](https://user-images.githubusercontent.com/24203428/114024965-33be4500-98a7-11eb-82f1-efbfa51adce2.png)
![image](https://user-images.githubusercontent.com/24203428/114024982-36b93580-98a7-11eb-99cd-ae92090ebece.png)
![image](https://user-images.githubusercontent.com/24203428/114024993-3a4cbc80-98a7-11eb-80a4-ca2e8e7961e1.png)
![image](https://user-images.githubusercontent.com/24203428/114025006-3de04380-98a7-11eb-91e3-587184480cf3.png)
![image](https://user-images.githubusercontent.com/24203428/114025018-40db3400-98a7-11eb-9420-2c6e86588653.png)
![image](https://user-images.githubusercontent.com/24203428/114025030-43d62480-98a7-11eb-95de-3078f5c7bf0a.png)
![image](https://user-images.githubusercontent.com/24203428/114025041-4769ab80-98a7-11eb-8d0d-bdd9838c563d.png)
## 限制活动范围-不带口罩-确诊即隔离 ##
![image](https://user-images.githubusercontent.com/24203428/114025107-5c463f00-98a7-11eb-84e5-27f8475a1438.png)
![image](https://user-images.githubusercontent.com/24203428/114025121-60725c80-98a7-11eb-9f0e-34c54655d184.png)
![image](https://user-images.githubusercontent.com/24203428/114025128-636d4d00-98a7-11eb-897c-25fa7c6fe24c.png)
![image](https://user-images.githubusercontent.com/24203428/114025140-66683d80-98a7-11eb-9b3d-cb96411a0b27.png)
![image](https://user-images.githubusercontent.com/24203428/114025150-68ca9780-98a7-11eb-87e7-2e981948f46a.png)
![image](https://user-images.githubusercontent.com/24203428/114025156-6bc58800-98a7-11eb-9b87-c7da83a06701.png)
