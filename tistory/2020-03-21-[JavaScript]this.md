
# this
--
함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 `this`에 바인딩할 객체가 동적으로 결정된다.  
자바스크립트에서 함수를 호출하는 방식은 다음과 같다.
- 함수호출
- 메소드 호출
- 생성자 함수 호출
- apply / call / bind 호출

## 함수호출
---
일반 함수 호출 시 기본적으로 `this`는 전역객체에 바인딩된다. 뿐만 아니라 내부함수의 경우에도 내부함수를 호출하는 외부함수가 아닌 전역객체에 바인딩된다.

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">function</span>&nbsp;func()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#ffd500">'func&nbsp;this&nbsp;:&nbsp;'</span>,&nbsp;<span style="color:#4be6fa">this</span>);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;window</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">function</span>&nbsp;inner()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#ffd500">'inner&nbsp;this&nbsp;:&nbsp;'</span>,&nbsp;<span style="color:#4be6fa">this</span>);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;window</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner();</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;func();</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

또한, 메소드의 내부함수일 경우에도 `this`는 전역객체에 바인딩된다.

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;<span style="color:#4be6fa">name</span>&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ffd500">'Y'</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;obj&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">name</span>&nbsp;:&nbsp;<span style="color:#ffd500">'Yang'</span>,</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;func&nbsp;:&nbsp;<span style="color:#ff3399">function</span>()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#ffd500">'func&nbsp;this&nbsp;:&nbsp;'</span>,&nbsp;<span style="color:#4be6fa">this</span>);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;obj</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#ffd500">'func&nbsp;this.name&nbsp;:&nbsp;'</span>,&nbsp;<span style="color:#4be6fa">this</span>.<span style="color:#4be6fa">name</span>);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Yang'</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">function</span>&nbsp;inner()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#ffd500">'inner&nbsp;this&nbsp;:&nbsp;'</span>,&nbsp;<span style="color:#4be6fa">this</span>);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;window</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#ffd500">'inner&nbsp;this.name&nbsp;:&nbsp;'</span>,&nbsp;<span style="color:#4be6fa">this</span>.<span style="color:#4be6fa">name</span>);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Y'</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner();</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;obj.func();</div></div><div style="text-align:right;margin-top:-13px;margin-right:5px;font-size:9px;font-style:italic"><a href="http://colorscripter.com/info#e" target="_blank" style="color:#4f4f4ftext-decoration:none">Colored by Color Scripter</a></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

## 메소드 호출
---
함수가 객체의 프로퍼티 값이면 메소드로서 호출된다. 이 때, 메소드 내부의 `this`는 해당 메소드를 호출한 객체에 바인딩된다.

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;obj&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">name</span>&nbsp;:&nbsp;<span style="color:#ffd500">'Yang'</span>,</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;getThis&nbsp;:&nbsp;<span style="color:#ff3399">function</span>()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#4be6fa">this</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;obj.say&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">function</span>()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#4be6fa">this</span>.<span style="color:#4be6fa">name</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;obj1&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">name</span>&nbsp;:&nbsp;<span style="color:#ffd500">'Sang'</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;obj1.say&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;obj.say;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;obj.say();&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Yang'</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;obj.getThis();&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;obj</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;obj1.say();&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Sang'</span></div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

### 생성자 함수 호출
---
생성자 함수 호출의 경우 `this`는 새로 생성하는 객체에 바인딩되며, new 연산자와 함께 생성자 함수를 호출하면 아래와 같이 동작한다.
1. 빈 객체 생성 및 this 바인딩
   - 코드 실행 전 빈 객체가 우선 생성되며, 이 빈 객체는 생성자 함수가 새로 생성하는 객체가 된다. 이후, `this`는 이 객체에 바인딩된다.
2. this를 이용한 프로퍼티/메소드 추가
   - 생성자 함수 내에 `this`를 사용하여 프로퍼티나 메소드를 생성할 시, `this`는 새로 생성된 객체를 의미하므로 `this`로 추가된 프로퍼티나 메소드는 새로 생성된 객체에 추가된다.
3. 객체 반환
   - 반환문이 없는 경우, `this`에 바인딩된 새로운 객체가 반환된다.


<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">function</span>&nbsp;Person(<span style="color:#4be6fa">name</span>)&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">this</span>.<span style="color:#4be6fa">name</span>&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#4be6fa">name</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;Person.<span style="color:#4be6fa">prototype</span>.getName&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">function</span>()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#4be6fa">this</span>.<span style="color:#4be6fa">name</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;my&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">new</span>&nbsp;Person(<span style="color:#ffd500">'Yang'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;my.getName();&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Yang'</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;Person.<span style="color:#4be6fa">prototype</span>.<span style="color:#4be6fa">name</span>&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ffd500">'Sang'</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#4be6fa">console</span>.log(Person.<span style="color:#4be6fa">prototype</span>.getName());&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Sang'</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;m&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">new</span>&nbsp;Person(<span style="color:#ffd500">'Gil'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;m.getName();&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Gil'</span></div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

생성자 함수를 new 연산자 없이 그냥 호출할 경우(일반 함수 호출), `this`에는 전역객체가 바인딩된다.

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">function</span>&nbsp;Person(<span style="color:#4be6fa">name</span>)&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">this</span>.<span style="color:#4be6fa">name</span>&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#4be6fa">name</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">this</span>.say&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">function</span>()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#4be6fa">this</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;me&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;Person(<span style="color:#ffd500">'Yang'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#4be6fa">console</span>.log(me);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;undefined</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#4be6fa">console</span>.log(<span style="color:#4be6fa">name</span>);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;'Yang'</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;say();&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;window</span></div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;funcThis&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#4be6fa">null</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">function</span>&nbsp;Obj(<span style="color:#4be6fa">name</span>)&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">this</span>.<span style="color:#4be6fa">name</span>&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#4be6fa">name</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;funcThis&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#4be6fa">this</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;o1&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;Obj(<span style="color:#ffd500">'Yang'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#4be6fa">console</span>.log(funcThis);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;window</span></div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;o2&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;<span style="color:#ff3399">new</span>&nbsp;Obj(<span style="color:#ffd500">'Sang'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#4be6fa">console</span>.log(funcThis);&nbsp;&nbsp;&nbsp;<span style="color:#999999">//&nbsp;Obj</span></div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;o&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;{};</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">var</span>&nbsp;p&nbsp;<span style="color:#aaffaa"></span><span style="color:#ff3399">=</span>&nbsp;{};</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;<span style="color:#ff3399">function</span>&nbsp;func()&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">switch</span>(<span style="color:#4be6fa">this</span>)&nbsp;{</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">case</span>&nbsp;o:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">document</span>.write(<span style="color:#ffd500">'o&nbsp;&lt;br/&gt;'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">break</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">case</span>&nbsp;p:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">document</span>.write(<span style="color:#ffd500">'p&nbsp;&lt;br/&gt;'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">break</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">case</span>&nbsp;<span style="color:#4be6fa">window</span>:</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#4be6fa">document</span>.write(<span style="color:#ffd500">'window&nbsp;&lt;br/&gt;'</span>);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#ff3399">break</span>;</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;}</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;func();</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;func.apply(o);</div><div style="padding:0 6px; white-space:pre; line-height:130%">&nbsp;func.apply(p);</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>

<div class="colorscripter-code" style="color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important; position:relative !important;overflow:auto"><table class="colorscripter-code-table" style="margin:0;padding:0;border:none;background-color:#272727;border-radius:4px;" cellspacing="0" cellpadding="0"><tr><td style="padding:6px 0;text-align:left"><div style="margin:0;padding:0;color:#f0f0f0;font-family:Consolas, 'Liberation Mono', Menlo, Courier, monospace !important;line-height:130%"><div style="padding:0 6px; white-space:pre; line-height:130%">window</div><div style="padding:0 6px; white-space:pre; line-height:130%">o</div><div style="padding:0 6px; white-space:pre; line-height:130%">p</div></div></td><td style="vertical-align:bottom;padding:0 2px 4px 0"><a href="http://colorscripter.com/info#e" target="_blank" style="text-decoration:none;color:white"><span style="font-size:9px;word-break:normal;background-color:#4f4f4f;color:white;border-radius:10px;padding:1px">cs</span></a></td></tr></table></div>