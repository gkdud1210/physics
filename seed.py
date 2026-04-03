"""
등속/등가속도 운동 문제 10개를 DB에 삽입하는 시드 스크립트.
이미 DB에 같은 문제가 있으면 건너뜁니다.

실행: python seed.py
"""
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

PROBLEMS = [
    {
        "title_ko": "등가속도 - 나중 속도",
        "title_en": "Uniform Acceleration - Final Velocity",
        "concept_ko": "등가속도 운동",
        "concept_en": "Uniform Acceleration",
        "difficulty": "easy",
        "question_text_ko": "정지해 있던 물체가 $2\\ m/s^2$의 일정한 가속도로 운동한다. 4초 후의 속도는? (단위: m/s)",
        "question_text_en": "An object starting from rest accelerates at $2\\ m/s^2$. What is its velocity after 4 seconds? (m/s)",
        "correct_answer": "8",
        "explanation_ko": (
            "<b>📌 적용 공식</b><br>"
            "$$v = v_0 + at$$<br>"
            "<b>🔍 풀이</b><br>"
            "처음 속도 $v_0 = 0\\ m/s$ (정지 상태), 가속도 $a = 2\\ m/s^2$, 시간 $t = 4\\ s$<br><br>"
            "$$v = 0 + 2 \\times 4 = 8\\ m/s$$<br>"
            "<b>💡 핵심 개념</b><br>"
            "가속도가 일정할 때 속도는 시간에 <b>비례</b>하여 선형 증가합니다.<br>"
            "$v$-$t$ 그래프에서 기울기 = 가속도입니다."
        ),
        "explanation_en": (
            "<b>Formula:</b> $v = v_0 + at$<br><br>"
            "$v = 0 + 2 \\times 4 = 8\\ m/s$<br><br>"
            "<b>Key:</b> With constant acceleration, velocity increases linearly with time."
        ),
    },
    {
        "title_ko": "등가속도 - 가속도 계산",
        "title_en": "Uniform Acceleration - Finding Acceleration",
        "concept_ko": "등가속도 운동",
        "concept_en": "Uniform Acceleration",
        "difficulty": "easy",
        "question_text_ko": "$4\\ m/s$로 운동하던 물체의 속도가 3초 후 $10\\ m/s$가 되었다. 가속도의 크기는? (단위: m/s²)",
        "question_text_en": "An object moving at $4\\ m/s$ reaches $10\\ m/s$ after 3 seconds. What is its acceleration? (m/s²)",
        "correct_answer": "2",
        "explanation_ko": (
            "<b>📌 적용 공식</b><br>"
            "$$a = \\frac{v - v_0}{t}$$<br>"
            "<b>🔍 풀이</b><br>"
            "$v_0 = 4\\ m/s$, $v = 10\\ m/s$, $t = 3\\ s$<br><br>"
            "$$a = \\frac{10 - 4}{3} = \\frac{6}{3} = 2\\ m/s^2$$<br>"
            "<b>💡 핵심 개념</b><br>"
            "가속도는 단위 시간 동안의 <b>속도 변화량</b>입니다.<br>"
            "속도가 증가 → 가속도 방향 = 운동 방향"
        ),
        "explanation_en": (
            "<b>Formula:</b> $a = \\dfrac{v - v_0}{t}$<br><br>"
            "$$a = \\frac{10 - 4}{3} = 2\\ m/s^2$$"
        ),
    },
    {
        "title_ko": "등가속도 - 시간 계산",
        "title_en": "Uniform Acceleration - Time",
        "concept_ko": "등가속도 운동",
        "concept_en": "Uniform Acceleration",
        "difficulty": "medium",
        "question_text_ko": "정지 상태에서 $1\\ m/s^2$로 출발한 기차가 $50\\ m$를 이동하는 데 걸린 시간은? (단위: 초)",
        "question_text_en": "A train starts from rest with $a = 1\\ m/s^2$. How many seconds to travel $50\\ m$?",
        "correct_answer": "10",
        "explanation_ko": (
            "<b>📌 적용 공식</b><br>"
            "$$s = v_0 t + \\frac{1}{2}at^2$$<br>"
            "<b>🔍 풀이</b><br>"
            "$v_0 = 0$, $a = 1\\ m/s^2$, $s = 50\\ m$ 대입<br><br>"
            "$$50 = 0 + \\frac{1}{2} \\times 1 \\times t^2$$"
            "$$t^2 = 100 \\implies t = 10\\ s$$<br>"
            "<b>💡 핵심 개념</b><br>"
            "정지 출발 시 $s = \\dfrac{1}{2}at^2$ 이므로 변위는 시간의 <b>제곱에 비례</b>합니다.<br>"
            "$s \\propto t^2$"
        ),
        "explanation_en": (
            "<b>Formula:</b> $s = \\dfrac{1}{2}at^2$ (since $v_0=0$)<br><br>"
            "$$50 = \\frac{1}{2}(1)t^2 \\implies t^2 = 100 \\implies t = 10\\ s$$"
        ),
    },
    {
        "title_ko": "감속 - 이동 거리",
        "title_en": "Deceleration - Stopping Distance",
        "concept_ko": "등가속도 운동",
        "concept_en": "Uniform Acceleration",
        "difficulty": "easy",
        "question_text_ko": "$20\\ m/s$로 달리던 차가 브레이크를 밟아 5초 만에 정지했다. 이동 거리는? (단위: m)",
        "question_text_en": "A car at $20\\ m/s$ stops in 5 s. What is the stopping distance? (m)",
        "correct_answer": "50",
        "explanation_ko": (
            "<b>📌 방법 1 — 평균 속도 이용</b><br>"
            "등가속도 운동에서 평균 속도:"
            "$$\\bar{v} = \\frac{v_0 + v}{2} = \\frac{20 + 0}{2} = 10\\ m/s$$"
            "$$s = \\bar{v} \\times t = 10 \\times 5 = 50\\ m$$<br>"
            "<b>📌 방법 2 — 공식 직접 대입</b><br>"
            "$a = \\dfrac{0 - 20}{5} = -4\\ m/s^2$<br><br>"
            "$$s = v_0 t + \\frac{1}{2}at^2 = 20(5) + \\frac{1}{2}(-4)(25) = 100 - 50 = 50\\ m$$<br>"
            "<b>💡 핵심 개념</b><br>"
            "감속도 등가속도이므로 공식을 그대로 씁니다. 가속도 부호가 음수(−)입니다."
        ),
        "explanation_en": (
            "<b>Method (avg velocity):</b><br>"
            "$$s = \\frac{v_0+v}{2} \\times t = \\frac{20+0}{2} \\times 5 = 50\\ m$$"
        ),
    },
    {
        "title_ko": "v-t 그래프 해석",
        "title_en": "v-t Graph Interpretation",
        "concept_ko": "그래프 해석",
        "concept_en": "Graph Analysis",
        "difficulty": "easy",
        "question_text_ko": "$v$-$t$ 그래프에서 그래프와 시간축 사이의 면적이 의미하는 것은? (한 단어로)",
        "question_text_en": "In a $v$-$t$ graph, what does the area between the curve and the time axis represent? (one word)",
        "correct_answer": "변위",
        "explanation_ko": (
            "<b>📌 v-t 그래프의 세 가지 물리량</b><br>"
            "<table style='border-collapse:collapse;margin:8px 0;font-size:.85rem'>"
            "<tr><td style='padding:4px 12px 4px 0;font-weight:700'>y절편</td><td>처음 속도 $v_0$</td></tr>"
            "<tr><td style='padding:4px 12px 4px 0;font-weight:700'>기울기</td><td>가속도 $a = \\dfrac{\\Delta v}{\\Delta t}$</td></tr>"
            "<tr style='background:#fef9c3'><td style='padding:4px 12px 4px 0;font-weight:700'>넓이(면적)</td><td>변위 $s = \\int v\\, dt$</td></tr>"
            "</table><br>"
            "<b>💡 왜 면적 = 변위인가?</b><br>"
            "미소 시간 $\\Delta t$ 동안의 변위 = $v \\cdot \\Delta t$ (직사각형 넓이)<br>"
            "이를 모두 더하면 $\\displaystyle s = \\int_{t_1}^{t_2} v\\, dt$ = 그래프 아래 면적<br><br>"
            "<b>⚠️ 주의:</b> 그래프가 시간축 <b>아래</b>이면 <b>음(−) 변위</b> (반대 방향)"
        ),
        "explanation_en": (
            "<b>v-t graph summary:</b><br>"
            "• Slope = acceleration $a$<br>"
            "• Area under curve = displacement $s = \\int v\\,dt$<br>"
            "• y-intercept = initial velocity $v_0$"
        ),
    },
    {
        "title_ko": "등가속도 - v²-v₀² 공식",
        "title_en": "Uniform Acceleration - v² formula",
        "concept_ko": "등가속도 운동",
        "concept_en": "Uniform Acceleration",
        "difficulty": "hard",
        "question_text_ko": "$10\\ m/s$로 운동하던 물체가 $2\\ m/s^2$로 가속하여 $16\\ m/s$가 되었다. 이동 거리는? (단위: m)",
        "question_text_en": "An object at $10\\ m/s$ accelerates at $2\\ m/s^2$ to reach $16\\ m/s$. What is the distance? (m)",
        "correct_answer": "39",
        "explanation_ko": (
            "<b>📌 적용 공식 — 시간 없이 푸는 속도-변위 관계식</b><br>"
            "$$v^2 = v_0^2 + 2as$$<br>"
            "<b>🔍 풀이</b><br>"
            "$v_0 = 10\\ m/s$, $v = 16\\ m/s$, $a = 2\\ m/s^2$<br><br>"
            "$$16^2 = 10^2 + 2 \\times 2 \\times s$$"
            "$$256 = 100 + 4s$$"
            "$$4s = 156 \\implies s = 39\\ m$$<br>"
            "<b>💡 언제 이 공식을 쓰나?</b><br>"
            "문제에 <b>시간 $t$가 없고</b>, $v_0$·$v$·$a$·$s$ 중 셋이 주어질 때 사용합니다."
        ),
        "explanation_en": (
            "<b>Formula:</b> $v^2 = v_0^2 + 2as$<br><br>"
            "$$16^2 = 10^2 + 2(2)s \\implies 4s = 156 \\implies s = 39\\ m$$<br>"
            "<b>Use when:</b> time is not given."
        ),
    },
    {
        "title_ko": "빗면 - 질량과 가속도",
        "title_en": "Incline - Mass and Acceleration",
        "concept_ko": "뉴턴 법칙",
        "concept_en": "Newton's Laws",
        "difficulty": "medium",
        "question_text_ko": "마찰 없는 빗면에서 질량이 다른 두 물체를 같은 높이에서 놓으면 가속도의 관계는?",
        "question_text_en": "Two objects of different mass are released from the same height on a frictionless incline. How do their accelerations compare?",
        "correct_answer": "같다",
        "explanation_ko": (
            "<b>📌 뉴턴 제2법칙 적용</b><br>"
            "$$F = ma$$<br>"
            "<b>🔍 풀이</b><br>"
            "빗면 방향 중력 성분: $F = mg\\sin\\theta$<br><br>"
            "$$mg\\sin\\theta = ma$$"
            "$$\\boxed{a = g\\sin\\theta}$$<br>"
            "질량 $m$이 양변에서 <b>약분</b>됩니다!<br>"
            "→ 가속도는 질량과 <b>무관</b>하게 $a = g\\sin\\theta$로 동일합니다.<br><br>"
            "<b>💡 갈릴레오의 사고 실험</b><br>"
            "무거운 물체와 가벼운 물체를 동시에 놓으면, 마찰이 없을 때 완전히 같은 가속도로 운동합니다."
        ),
        "explanation_en": (
            "Net force along incline: $mg\\sin\\theta = ma$<br>"
            "$$a = g\\sin\\theta$$<br>"
            "Mass $m$ cancels → acceleration is <b>independent of mass</b>."
        ),
    },
    {
        "title_ko": "등가속도 - s∝t² 비례",
        "title_en": "Uniform Acceleration - s∝t²",
        "concept_ko": "등가속도 운동",
        "concept_en": "Uniform Acceleration",
        "difficulty": "medium",
        "question_text_ko": "정지 상태에서 출발한 물체가 1초 동안 $d$만큼 이동했다면, 2초 동안 총 이동 거리는? ($d$의 배수로)",
        "question_text_en": "An object from rest travels $d$ in 1 second. How far does it travel in 2 seconds? (in multiples of $d$)",
        "correct_answer": "4d",
        "explanation_ko": (
            "<b>📌 정지 출발 변위 공식</b><br>"
            "$$s = \\frac{1}{2}at^2 \\implies s \\propto t^2$$<br>"
            "<b>🔍 풀이</b><br>"
            "1초: $s_1 = \\dfrac{1}{2}a(1)^2 = d \\implies a = 2d$<br>"
            "2초: $s_2 = \\dfrac{1}{2}a(2)^2 = \\dfrac{1}{2}(2d)(4) = 4d$<br><br>"
            "비율로 바로 계산:<br>"
            "$$\\frac{s_2}{s_1} = \\frac{t_2^2}{t_1^2} = \\frac{4}{1} = 4 \\implies s_2 = 4d$$<br>"
            "<b>💡 홀수 법칙 (참고)</b><br>"
            "연속된 등시간 구간의 변위 비 = $1 : 3 : 5 : 7 : \\cdots$"
        ),
        "explanation_en": (
            "<b>Formula:</b> $s = \\frac{1}{2}at^2 \\implies s \\propto t^2$<br><br>"
            "$$\\frac{s_2}{s_1} = \\frac{2^2}{1^2} = 4 \\implies s_2 = 4d$$"
        ),
    },
    {
        "title_ko": "감속 - 가속도 방향",
        "title_en": "Deceleration - Direction of Acceleration",
        "concept_ko": "가속도 방향",
        "concept_en": "Direction of Acceleration",
        "difficulty": "easy",
        "question_text_ko": "속도가 일정하게 감소하여 정지하는 물체의 가속도 방향은 운동 방향과 어떤가?",
        "question_text_en": "For an object uniformly decelerating to rest, how does the acceleration direction relate to the velocity direction?",
        "correct_answer": "반대",
        "explanation_ko": (
            "<b>📌 가속도 정의</b><br>"
            "$$\\vec{a} = \\frac{\\Delta \\vec{v}}{\\Delta t} = \\frac{\\vec{v} - \\vec{v_0}}{\\Delta t}$$<br>"
            "<b>🔍 분석</b><br>"
            "감속: $v < v_0$ → $\\Delta v = v - v_0 < 0$ (처음 속도와 반대 방향)<br>"
            "$\\vec{a}$의 방향 = $\\Delta \\vec{v}$의 방향 = <b>운동 방향과 반대</b><br><br>"
            "<b>💡 정리표</b><br>"
            "<table style='border-collapse:collapse;font-size:.85rem;margin:6px 0'>"
            "<tr style='background:#dbeafe'><td style='padding:4px 10px'>$a$ 방향</td><td style='padding:4px 10px'>$v$ 방향과 <b>같음</b></td><td style='padding:4px 10px'>속도 <b>증가</b> (가속)</td></tr>"
            "<tr style='background:#fee2e2'><td style='padding:4px 10px'>$a$ 방향</td><td style='padding:4px 10px'>$v$ 방향과 <b>반대</b></td><td style='padding:4px 10px'>속도 <b>감소</b> (감속)</td></tr>"
            "</table>"
        ),
        "explanation_en": (
            "Deceleration: $\\Delta v < 0$ → $a$ is opposite to $v$<br><br>"
            "• $a$ same as $v$ → speeding up<br>"
            "• $a$ opposite to $v$ → slowing down"
        ),
    },
    {
        "title_ko": "등가속도 - 나중 속도 (평균속도 이용)",
        "title_en": "Uniform Acceleration - Final Velocity via avg",
        "concept_ko": "등가속도 운동",
        "concept_en": "Uniform Acceleration",
        "difficulty": "medium",
        "question_text_ko": "$5\\ m/s$로 운동하던 물체가 2초 동안 $20\\ m$를 이동했다. 나중 속도는? (단위: m/s)",
        "question_text_en": "An object at $5\\ m/s$ travels $20\\ m$ in 2 s. What is its final velocity? (m/s)",
        "correct_answer": "15",
        "explanation_ko": (
            "<b>📌 등가속도 운동의 평균 속도</b><br>"
            "$$\\bar{v} = \\frac{v_0 + v}{2} = \\frac{s}{t}$$<br>"
            "<b>🔍 풀이</b><br>"
            "평균 속도를 두 가지로 표현:<br>"
            "$$\\frac{s}{t} = \\frac{20}{2} = 10\\ m/s$$"
            "$$\\frac{v_0 + v}{2} = 10$$"
            "$$\\frac{5 + v}{2} = 10 \\implies v = 15\\ m/s$$<br>"
            "<b>⚠️ 중요:</b> $\\bar{v} = \\dfrac{v_0+v}{2}$ 는 등가속도 조건에서만 성립합니다!<br>"
            "가속도가 일정하지 않은 경우엔 사용 불가."
        ),
        "explanation_en": (
            "<b>Formula (uniform accel only):</b><br>"
            "$$\\bar{v} = \\frac{v_0+v}{2} = \\frac{s}{t}$$<br>"
            "$$\\frac{5+v}{2} = \\frac{20}{2} = 10 \\implies v = 15\\ m/s$$"
        ),
    },
]


def seed():
    db = SessionLocal()
    existing = {p.question_text_ko for p in db.query(models.Problem).all()}
    added = 0
    for prob in PROBLEMS:
        if prob["question_text_ko"] in existing:
            print(f"  [skip] {prob['title_ko']}")
            continue
        db.add(models.Problem(**prob))
        added += 1
        print(f"  [add]  {prob['title_ko']}")
    db.commit()
    db.close()
    print(f"\n완료: {added}개 추가 ({len(PROBLEMS) - added}개 이미 존재)")


if __name__ == "__main__":
    seed()
