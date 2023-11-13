## length / length() / size()

Java에서 길이를 구할 때 사용하는 length / length() / size() 에 대해 알아보자

<br>

### length
---

`length` 는 배열의 길이를 알고자 할 때 사용된다.


```java
int[] lengthTest1 = new int[7];
System.out.println(lengthTest1.length);  // 7
```

<br>

### length()
---

`length()` 는 문자열의 길이를 알고자 할 때 사용된다.


```java
String lengthTest2 = "lengthSizeTest";
System.out.println(lengthTest2.length());  // 14
```

<br>

### size()
---
 
`size()` 는 Collections Framework 타입의 길이를 알고자 할 때 사용된다.

```java
//ArrayList
ArrayList<Object> list = new ArrayList<Object>();
list.add(0, "123");
list.add(1, "234");
System.out.println(list.size());  // 2


//HashMap
HashMap<String, String> map = new HashMap<String, String>();
map.put("가", "초콜릿");
map.put("나", "비빔면");
map.put("다", "제로콜라");
System.out.println(map.size());  // 3
```

