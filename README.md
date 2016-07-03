# boxwilddog 

#### boxwilddog api 第三方工具

boxwilddog官方网站：www.wilddog.com



##### 工具介绍：

- 生成 json ORM
- 增强功能：counter ，datum ， expires



##### 补充说明：

> 即使不使用wilddog的数据，joon ORM功能可以独立使用。



##### 使用安装：

安装：

```
pip install boxwilddog
```



##### 文档说明：

- datum ，counter ， expires 使用：

  ​

  datum 使用，datum使用2个函数，

  **datum_set(name,value)**设置值

  **datum_get(name)**获取值

  ​

  ```python
  from boxwilddog import boxwilddog

  url = 'You Wilddog URL'
  auth = 'You Wilddog AUTH'

  box = boxwilddog.Box(url,auth)
  box_datum_set = box.datum_set('wild','dog')
  #>>>u'dog'
  #参数必须是字符串，两个参数。第一个是name,第二个是value，返回值：是unicode字符串

  box_datum_get = box.datum_get('wild')
  #>>>u'dog'
  #参数必须是字符串，一个参数，第一个是name。返回值：是unicode字符串
  ```

  ​

  counter 使用：counter使用3个函数，

  **counter_get(name)** 获取值

  **counter_add(name)**值得数值加1,

  **counter_reduce(name)**值得数值减1

  ​  
  ```python
  from boxwilddog import boxwilddog

  url = 'You Wilddog URL'
  auth = 'You Wilddog AUTH'

  box = boxwilddog.Box(url,auth)
  box_counter_get = box.counter_get('wild')
  #>>>'0'
  #参数必须是字符串，一个参数。第一个是name,返回值：是字符串

  box_counter_add = box.counter_add('wild')
  #>>>u'1'
  #参数必须是字符串，一个参数，第一个是name。返回值：是unicode字符串

  box_counter_reduce = box.counter_reduce('wild')
  #>>>u'0'
  #参数必须是字符串，一个参数，第一个是name。返回值：是unicode字符串

  ```

  ​

  expires 使用，expires使用2个函数，常用于token的使用

  **expires_set(name,value,expires)**设置值，和过期时间

  **expires_get(name)**获取值

  ​

  ```python
  from boxwilddog import boxwilddog

  url = 'You Wilddog URL'
  auth = 'You Wilddog AUTH'

  box = boxwilddog.Box(url,auth)
  box_expires_set = box.expires_set('wild','dog','1000')
  #>>>'["wild","dog","1000"]'
  #参数必须是字符串，三个参数。第一个是name,第二个是value，第二个是expires，返回值：是列表形式的字符串

  box_expires_get = box.expires_get('wild')
  #>>>u'["wild","dog","902"]'
  #参数必须是字符串，一个参数，第一个是name。返回值：是列表形式的字符串
  ```

  ​



- Model 是，方便生成json数据使用，一个小工具：

  AuthProperty TimeProperty StringProperty 三种类型值，使用default参数

  AuthProperty 随机生成key

  TimeProperty 现在时间戳

  StringProperty 默认没有值得时候，生成字符串'none'

  **参数与返回值都为字符串**

  ​

  ```python
  from boxwilddog import boxwilddog 

  class WilddogJson(boxwilddog.Model):
      a_auth = boxwilddog.AuthProperty()
      a_time = boxwilddog.TimeProperty()
      a1 = boxwilddog.StringProperty()
      
  s = WilddogJson()
  s_json = s.value
  #>>>{'a_auth': '1467536273uIHwar63qmG3XetwDAR6', 'a_time': '1467536273', 'a1': 'none'}
  #AuthProperty 与 TimeProperty StringProperty 在不赋值的时候，会自动生成随机值，现在时间戳 以及 None ，所有值都是字符串

  class WilddogJsonDefault(boxwilddog.Model):
      a_auth = boxwilddog.AuthProperty(default='1111')
      a_time = boxwilddog.TimeProperty(default='33333')
      a1 = boxwilddog.StringProperty(default='wlid')
   
  s = WilddogJsonDefault()
  s_json = s.value
  #>>>{'a_auth': '1111', 'a_time': '33333', 'a1': 'wlid'}

  class WilddogJsonValue(boxwilddog.Model):
      a_auth = boxwilddog.AuthProperty()
      a_time = boxwilddog.TimeProperty()
      a1 = boxwilddog.StringProperty()
   
  s = WilddogJsonValue(a_auth='wild',a_time='19283445',a1='dog')
  s_json = s.value
  #>>>{'a_auth': 'wild', 'a_time': '19283445', 'a1': 'dog'}
  ```




------





##### 作者说明：

ccdjh.marx@gmail.com

*接受兼职:300元一小时*



