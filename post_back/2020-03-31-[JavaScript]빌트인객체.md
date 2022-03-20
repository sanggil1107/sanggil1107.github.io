
## Object 객체
---
```javascript
// Object.keys()
// Object.prototype.toString() -> 모든 객체가 사용할 수 있는 메소드

var arr = ["a", "b", "c"];
document.write('Object.keys(arr) : ', Object.keys(arr), '<br/>');

var o = new Object();
document.write('o.toString() : ', o.toString(), '<br/>');


var a = new Array(1,2,3);
document.write('a.toString() : ', a.toString(), '<br/>');
            
```
```
Object.keys(arr) : 0,1,2
o.toString() : [object Object]
a.toString() : 1,2,3
```            


