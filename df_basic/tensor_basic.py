import tensorflow as tf

var=tf.Variable([5.0],dtype=tf.float32)#5.0~5.999:객체 값을 바꿀수 있다
con=tf.constant([10.0],dtype=tf.float32)#상수
session=tf.Session()
init=tf.global_variables_initializer()
session.run(init)
print(session.run(var*con))
print('---------------')
session.run(var.assign([10.0]))
print(session.run(var))

p1=tf.placeholder(dtype=tf.float32)#파라미터
p2=tf.placeholder(dtype=tf.float32)

t1=p1*3
t2=p1*p2
#t1을 이용하여12.0를 출력해주세요
print(session.run(t1,{p1:[4.0]}))#list형태를 만들기 위하여 [4.0]으로 한다.
print(session.run(t2,feed_dict={p1:4.0,p2:[2.0,5.0]}))
