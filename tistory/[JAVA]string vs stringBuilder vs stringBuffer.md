**string** - 계속 값을 더해가는 경우 새로운 String 클래스가 만들어진다.

**stringBuilder, stringBuffer** \- 새로운 객체를 생성시키지 않고 기존 객체의 크기를 증가시킴.

stringBuilder vs stringBuffer - 동기화 지원 여부

**stringBuffer** - 스레드에 안전하게 설계, 여러 개의 스레드에서 하나의 stringBuffer 객체를 처리해도 문제되지 않는다.

**stringBuilder** - 단일 스레드에서의 안전성만을 보장, 여러 개의 스레드에서 하나의 stringBuilder 객체를 처리하면 문제가 발생.