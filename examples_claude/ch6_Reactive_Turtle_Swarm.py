import turtle
import random
 
# ---- 전역 상태 (여러 핸들러가 공유한다) -----------------------
STEP = 10          # 한 틱당 이동 거리
target = None      # 현재 목표점 (x, y). 아직 없으면 None
swarm = []         # 거북이 객체들의 리스트
 
 
# ---- 1. 무리 생성 -------------------------------------------
def make_swarm(n):
    """
    n 마리의 '서로 독립적인' Turtle 객체를 만들어 리스트로 반환한다.
    각 거북이는: shape('turtle'), 임의의 색, penup 상태,
    화면 안 임의의 위치(예: x,y in [-300, 300])에서 시작한다.
    n == 0 이면 빈 리스트를 반환한다.
    """
    if n == 0:
        return []
    res = []
    color = ['red','blue','yellow','black','white','violet','green','red','blue','yellow', 'black', 'white', 'violet', 'green']
    for k in range(n):
        t = turtle.Turtle()
        t.penup()
        t.shape('turtle')
        t.color(random.choice(color))
        t.goto(random.randrange(-300, 300), random.randrange(-300, 300))
        res.append(t)
    
    return res



# ---- 2. 고차함수: 무리 전체에 동작 적용 -----------------------
def broadcast(turtles, action):
    """
    turtles 안의 모든 거북이 t 에 대해 action(t) 를 호출한다.
    (제약 3: 이 함수 안에는 거북이 전용 메서드를 쓰지 말 것.
             오직 action 을 호출하는 코드만 둔다.)
    """
    for turtle in turtles:
        action(turtle) 
 
# ---- 3. 한 거북이를 목표점 쪽으로 한 걸음 ----------------------
def step_toward(t, tx, ty, dist):
    """
    거북이 t 가 (tx, ty) 를 바라보도록 방향(heading)을 맞춘 뒤,
    그 방향으로 dist 만큼 '상대 이동' 한다.
    힌트: t.towards(tx, ty) 는 (tx,ty) 를 향한 각도를 돌려준다.
    (제약 4: setposition/goto 금지 — setheading + forward 로만!)
    """
    t.setheading(t.towards(tx, ty))
    t.forward(dist)
 
 
# ---- 4. 핸들러들 --------------------------------------------
def tick():
    """
    타이머 핸들러.
    목표점(target)이 있으면, broadcast 를 이용해 무리 전체를
    목표점 쪽으로 한 걸음(STEP) 전진시킨다.
    그 뒤 화면을 갱신(window.update())하고,
    자기 자신을 100ms 뒤로 '다시 예약' 한다.
    """
    if target is not None:
        tx, ty = target

        def action(t):
            step_toward(t, tx, ty, STEP)

        broadcast(swarm, action)

    window.update()
    window.ontimer(tick, 100)

    pass
 
def on_click(x, y):
    """
    마우스 클릭 핸들러.
    클릭한 절대좌표 (x, y) 를 새 목표점으로 설정한다.
    """
    global target
    target = (x, y)
    pass
 
 
def toggle_pens():
    """'p' 키 핸들러. 무리 전체의 펜을 토글한다. (broadcast 를 사용)"""
    def toggle(t):
        if t.isdown():
            t.penup()
        else:
            t.pendown()
    broadcast(swarm, toggle)
    pass
 
 
def faster():
    """'Up' 키 핸들러. STEP 을 2 늘린다."""
    global STEP
    STEP += 2
    pass
 
 
def slower():
    """'Down' 키 핸들러. STEP 을 2 줄인다. 단, STEP 의 최솟값은 1."""
    global STEP
    STEP = min(1, STEP - 2)
    pass

 
# ---- 5. main: 화면 준비 + 이벤트 배선 -------------------------
window = turtle.Screen()
window.setup(700, 700)
window.title('Reactive Turtle Swarm')
window.tracer(0)               # 수동 갱신 모드 (직접 window.update() 호출)


swarm = make_swarm(8)
tick()
window.onclick(on_click)
window.onkey(faster, "Up")
window.onkey(slower, "Down")
window.onkey(toggle_pens, "p")

window.listen()
window.mainloop()
window.onkey(window.bye, "q")