# ECM 원고 수정 전·후 비교 (본문·보충자료)

## 0. 비교 대상

| 구분 | 수정 전 | 수정 후 |
|---|---|---|
| 본문 | `Manuscript_ECM.pdf` (28쪽, 생성 2026-10-12 00:11) | `Manuscript_ECM____.pdf` (26쪽, 생성 2026-10-13 06:00, **변경 추적 표시 포함**) |
| 보충자료 | `Supplementary_Material_ECM.pdf` (22쪽, 2026-10-12 00:12) | `Supplementary_Material_ECM____.pdf` (22쪽, 2026-10-13 06:01, 변경 추적 표시 없음) |

비교 방법
- 텍스트: 줄번호·머리글을 제거한 뒤 문장 단위로 대조했다.
- 수치: 문서 전체의 숫자 토큰을 대조했다.
- 변경 추적: 수정 후 본문의 빨간 글자를 밑줄(삽입)과 취소선(삭제)으로 구분했다.
- 그림: 삽입 이미지를 같은 크기로 맞춰 화소를 비교하고, 바뀐 그림은 눈으로 확인했다.

---

## 1. 요약

1. **결과 수치는 바뀌지 않았다.**
   - 본문: 수정 전 수치가 하나도 빠지지 않았다. 새로 생긴 숫자는 변경 추적으로 다시 쓴 문장 안의 같은 값뿐이다.
   - 보충자료: 표 값(S8–S21)이 모두 같다. 빠진 숫자는 S4.1에서 삭제한 입력값·문헌 범위이고, 새 숫자는 S2.3의 SH2·SH3 특성선 계수다.
2. **본문 변경은 4곳의 문장 정리와 서론 표현 2곳, 데이터 공개 문장 삭제 1곳**이다(표 1).
   - 핵심은 결론 (2)·(3)의 표현을 명확히 한 것이다. "Combined rated-load cases" → "Rated-load cases with combined preheating and operational tuning".
   - 3.3절에서는 전열면 재배분(R)을 "운전튜닝의 하드웨어 대안"으로 정의하는 문장이 추가되었다.
3. **본문 그림 9개 중 Fig. 3–9의 7개가 다시 그려졌다(표 2).** 데이터는 같고 학술지 양식으로 바뀌었다. Fig. 1·2는 해상도만 낮아졌을 뿐 내용이 같다. 쪽수가 28 → 26쪽으로 준 것은 그림 크기가 줄었기 때문이다.
4. **보충자료는 S2.2–S2.3에 모델 설명을 보강하고, S4.1을 크게 압축했다(표 3).**
   - 보강: Fᵢ의 의미, SH2·SH3 저유량 특성선, 대향연소 버너 배치(40/40/20% 근거)
   - 삭제: 입자 입력값(입경 16/60 µm 등), 잔류 미연탄소 비율식과 계수, 문헌식 적용범위
5. **제출 전에 정리할 것**: 변경 추적 수락, "서식 지정함" 말풍선 제거, 결론 (3) 첫 단어 확인, S4.1에서 삭제한 입력값의 재현성 확보(6절).

---

## 2. 본문 텍스트 변경

**표 1. 본문 문장 변경 비교**

| # | 위치 | 수정 전 | 수정 후 | 유형 |
|---|---|---|---|---|
| 1 | 1장 서론 1단락 | Korea's 11th Basic Plan … also **envisages expanded** hydrogen and ammonia power generation [4]. | **South** Korea's 11th Basic Plan … **targets the expansion of** hydrogen- and ammonia-fueled power generation [4]. | 표현 |
| 2 | 1장 서론 2단락 | Efficiency recovery reduces both total fuel **use** and ammonia demand … | … total fuel **consumption** … | 표현 |
| 3 | 3.3절 재배분 제약 (p.11, 추적 표시) | Heating-surface redistribution at 50% and 100% ammonia is constrained to SH2 + SH3 ≤7,150 m², SH1 + RH1 + RH2 + ECO ≤80,750 m², and each surface ≤120% … | **Heating-surface redistribution (R; Table 3) is a hardware alternative to operational tuning: convective-surface areas are adjusted to meet the 7% spray target at baseline operating settings.** At 50% and 100% ammonia, the SH2 + SH3 and SH1 + RH1 + RH2 + ECO group areas are kept within their original totals of 7,150 and 80,750 m², and each surface is limited to 120% … (이하 동일) | 정의 추가·표현 |
| 4 | 4.5절 Fig. 9 설명 (p.20, 추적 표시) | Figure 9 compares … (R+T). **R adjusts areas to meet the 7% spray target at baseline air settings and ΔT = 0 K.** At both 50% … The **R+T–T comparison** gives the additional benefit … | R 정의 문장 **삭제**(3.3절로 이동). "**The comparison of R+T with T** gives the additional benefit …" | 중복 제거·표현 |
| 5 | Fig. 9 캡션 끝 (p.21, 추적 표시) | Baseline/R use 13.85% excess air and BZR 0.90; T/R+T use 9.42% excess air at 50% ammonia or 5.00% at 100% ammonia, with BZR 0.95. | Baseline **and** R use 13.85% excess air and BZR 0.90; T **and** R+T use BZR 0.95, with excess air of 9.42% at 50% ammonia and 5.00% at 100% ammonia. | 표현 |
| 6 | 5장 결론 (2) (p.22, 추적 표시) | … Under matched air and preheating conditions, **redistribution with retuning adds** 0.04–0.10 pp at 50% ammonia and 0.02–0.04 pp at 100% ammonia. **These additional gains are specific to the idealized surface-area constraints and include the associated operating adjustment.** | … **combining heating-surface redistribution with operating tuning provides an additional net-efficiency gain of** 0.04–0.10 pp … **over tuning alone. These gains were obtained under the idealized surface-area constraints.** | 표현 명확화(수치 동일) |
| 7 | 5장 결론 (3) 첫 문장 (p.22, 추적 표시) | **Combined rated-load cases** restore 0.18, 0.55, and 1.33 pp … | **Rated-load cases with combined preheating and operational tuning** restore 0.18, 0.55, and 1.33 pp … | 표현 명확화 |
| 8 | 5장 결론 마지막 단락 (p.22) | — | 여백에 "서식 지정함: 글꼴: (한글) 맑은 고딕" 말풍선(서식 변경 추적) | **정리 필요** |
| 9 | Data availability | … do not have permission to share them. **The authors plan to deposit an anonymized dataset of calculated results in a public repository.** | 마지막 문장 **삭제**(추적 표시 없이 삭제됨) | 내용 삭제 |
| — | 식 (3a)·(3b) | 𝜂_B,b^dir 표기 | 위첨자 앞 공백만 다름(추출상 차이) | 실질 변경 없음 |

변경 없음: 초록, 하이라이트, 2장, 3.1–3.2절, 3.4절, 4.1–4.4절, 4.6절, 표 1–6(값·제목), Fig. 1–9 캡션(Fig. 9 끝 문장 제외), 참고문헌.

---

## 3. 본문 그림 변경

**표 2. 본문 그림 비교** (데이터 값은 모두 같음)

| 그림 | 변경 여부 | 주요 변경 |
|---|---|---|
| Fig. 1 계통도 | 동일 | 해상도만 낮아짐(1338 → 989 px) |
| Fig. 2 보일러·제어 개요 | 동일 | 해상도만 낮아짐 |
| Fig. 3 효율·손실 구성 | 재작성 | 패널 제목 → 축 안 (a)–(d) 표기. 테두리 축·안쪽 눈금. x축 "Ammonia energy fraction (%)" → "Ammonia fraction (% of LHV input)". 범례 "LHV basis/HHV basis", "LHV, direct method". (c) 항목별 명암 구분 강화. (d) y축 "Loss increase from coal (pp)", 막대 위 합계값(2.79–12.90) 추가 |
| Fig. 4 열흡수·온도·분무 | 재작성 | (c) "100% NH₃" 표기, 막대 값(+55.2, +60.8, +43.5, −30.1, +58.3, +131.9) 추가. (d) 단위 kg s⁻¹, 상한선 라벨 위치 이동. 범례 순서 변경 |
| Fig. 5 예열 열원별 성능 | 재작성 | 열원별로 **표식 모양**(원·사각·삼각·역삼각·마름모·오각·육각)을 달리함(이전: 명암만). 최고점 표시(큰 원+마름모). 공통 범례를 그림 하단으로. x축 "Ammonia burner supply temperature" |
| Fig. 6 운전변수 응답 | 재작성 | (a) "Approx. −0.029 pp/1pp" 주석 삭제. (b) 혼소율별 표식 모양 구분, y축 "Difference from BZR 0.95". (c) "ΔT = −18 K: −15.07×10⁻³ pp, Main steam 601.67°C" 주석 상자 삭제. 범례 "Highest eligible point" → "Highest constraint-compliant", "Table 5 point" 유지 |
| Fig. 7 저하–회복 분해 | 재작성 | (a) 막대 위 석탄값(44.16) 라벨 삭제, 범례를 패널 안으로. (b)(c) "Degradation" → "Degr.", 패널 제목을 패널 안 문구("NH₃ 20% (recovery +0.18 pp)")로. 하단 범례를 6항목으로 단순화 |
| Fig. 8 부분부하 분해 | 재작성 | Fig. 7과 같은 양식. 범례 "Change from coal / Preheating (PH1+PH2) / Boiler / Tuning / Steam cycle" 등으로 통합 |
| Fig. 9 재배분·튜닝 | 재작성 | 패널 안 "Values: LHV net efficiency" 문구 삭제, 하단에 "Upper values: net efficiency (%); Lower values: spray ratio (%)" 추가. 추가 이득 표기 "Additional 0.104 pp" → "+0.104 pp" |

---

## 4. 보충자료 변경

**표 3. 보충자료 텍스트 변경 비교**

| # | 위치 | 수정 전 | 수정 후 | 유형 |
|---|---|---|---|---|
| 1 | S2.2 흡열 집계 | … with auxiliary convective walls reported separately. | … with **six** auxiliary convective walls … | 명확화 |
| 2 | S2.2 인접 구역 복사 | Q̇rad,adj,i sums radiation … It is transferred from the emitting-zone balance to the receiving-surface balance and counted once in total absorption. | … gas zones; **radiation from the gas within the same zone is represented by hrad,i. Total absorption is the sum of the water/steam enthalpy rises, so adjacent-zone radiation is counted once.** | 설명 보강 |
| 3 | S2.2 식 (S3) Fᵢ | Fi is the heat-transfer correction | **Fᵢ is the heat-transfer performance factor; its reference value is calibrated to the coal design outlet states and, in off-design calculations, varied with flow by Eq. (S5). It scales the overall conductance and is not an LMTD flow-arrangement correction.** | 정의 보강 |
| 4 | S2.2 VDI 판본 | Software documentation cites sections Gf … and Gb … of the seventh German VDI edition (1994) [1]. Related material appears in G7 … and G1 …; numerical identity across editions is not assumed [4]. | These tube-side and cross-flow correlations follow the EBSILON implementation, whose documentation refers to … Gb … and Gf … (1994) [1]. The same correlation families appear in … G1 … and G7 … [4]; **coefficients may differ between editions.** | 표현 |
| 5 | S2.2 인접 복사 온도·후부 유로 | Tr,adj = w Tad + (1 − w) Tout with w = 0 … / Adjacent radiation includes … / **The rear RH1 and SH1–ECO paths are parallel. Outlet gas-distribution dampers control reheat temperature; flow redistribution changes convection and absorption in each path.** | Adjacent-zone radiation uses the outlet temperature of the emitting zone [2] and includes … (w 식 삭제, **후부 병렬유로·댐퍼 두 문장 삭제**) | 압축·삭제 |
| 6 | S2.3 식 (S5) | … with coefficients of 0.7 and 0.3 set in this analysis [1]. | 계수 문장 삭제. 추가: **"gas-side resistance accounts for 88–98% of the clean-tube overall resistance of the convective surfaces." "Below ṁ/ṁN = 0.7, SH2 and SH3 use flatter characteristics (F/FN = 0.86 + 0.071ṁ/ṁN and 0.87 + 0.05ṁ/ṁN) to reproduce the design superheater spray at part load"** | **모델 설정 신규 공개** |
| 7 | S2.3 연료 배분 | Fuel is distributed 40/40/20% among the burner zones. | **The opposed-wall furnace has six burner rows, three on each of the front and rear walls, with six burners per row supplied by one mill. One upper row operates only at BMCR and is on standby at rated and lower loads;** the three burner zones therefore receive 40%, 40%, and 20% of the heat input of both coal and ammonia. | 근거 보강 |
| 8 | S2.3 수렴 | … all 252 **grid** combinations converged … | … all 252 **operating-variable** combinations … | 용어 통일 |
| 9 | S3 재배분 추가 이득 | The matched R+T−T gain is 0.017–0.104 pp … | **Under matched air and preheating conditions, the additional gain of R+T over T** is 0.017–0.104 pp … | 표현(본문과 통일) |
| 10 | S3 격자 정의 | The operating grid contains 3 … × 4 biases = 252 combinations. | The operating-variable search covers 252 combinations of … 4 separator temperature-bias settings. | 표현 |
| 11 | S4.1 복사 물성 (12문장 → 3문장) | VDI 판본 절 번호(Kc, Ke, Kb), 영문판 K3 식 (18)–(21)·K5 식 (14)·(16)의 쪽 번호, CO₂·H₂O 관계 설명 | "follow the same built-in VDI-based treatment as in S2 [1,4]" 한 문장으로 통합. 식 (S6a)·(S6b) 유지 | **압축** |
| 12 | S4.1 입자 입력 (약 25문장 → 6문장) | 대표 입경 **16/60 µm**, 분포지수 **1.5**, 흡수 단면적비 **0.25/0.85**, 밀도 **2,200/850 kg/m³**, 잔류비율식 **c(1 − x)/(1 − 0.5x), c = 0.020/0.035/0.050/0.020**, 버너1 광학길이 **8.932 m**, 그을음 영향 서술, 영문판 식 (24)–(26)의 적용범위(300–1,800 K 등) | 정성 서술로 대체: "representative particle properties are used", 미연탄소는 석탄 분율에 따라 줄고 전소에서 0, 그을음 0과 Table S15(c) 참조, "문헌식·내장식 모두 고온·고수분 상태를 포괄한다고 문서화되지 않았으므로 대표 상태 비교에만 사용" | **입력값 삭제** |
| 13 | S4.3 | — | S4.1에서 옮긴 문장: "Representative temperatures of 2,094–2,215 K were chosen to reproduce the model VDI gas emissivities …" | 이동 |

**표 4. 보충자료 표·그림**

| 항목 | 변경 여부 | 비고 |
|---|---|---|
| Table S1–S21 수치 | 동일 | 쪽 나눔으로 머리 행이 반복되는 위치만 바뀜(S8, S9, S11, S14, S16, S17, S19, S20(a), S21) |
| Fig. S1 (공기율–바이어스 격자) | 재작성 | (a)–(c) 패널 표기, 범례에 "Below air floor"(빈 원) 추가, 하한 미만 영역 음영, 색 막대 이름 "LHV net-efficiency difference (10⁻³ pp)" |
| Fig. S2 (HHV 회복안별) | 재작성 | 테두리 축 양식, 범례를 그림 안 우하단으로, "‡: spray above 111.1 kg s⁻¹" 주석을 그림 안에 추가 |
| 참고문헌 | 동일 | — |

---

## 5. 영향 평가

- **결과·결론**: 바뀌지 않았다. 모든 결과 표와 본문 수치가 같다.
- **가독성**
  - 결론 (2)·(3)의 문장이 명확해졌다. 특히 "Combined rated-load cases"라는 모호한 주어를 해소했다.
  - R의 정의가 3.3절 한 곳으로 모였다.
  - 그림은 표식 모양으로 계열을 구분해 흑백 인쇄에도 강해졌다.
- **모델 설명의 투명성**
  - 좋아진 점: Fᵢ의 의미, 가스측 저항 비중 88–98%, SH2·SH3 저유량 특성선, 버너 배치가 보충자료에 추가되었다.
  - 약해진 점: S4.1의 입자·잔류 미연탄소 입력값이 사라졌다.

---

## 6. 확인·정리할 사항

1. **[필수] 변경 추적 수락과 말풍선 제거.** 수정 후 본문은 삽입·삭제 표시와 "서식 지정함" 말풍선이 남은 상태다. 제출본은 모든 변경을 수락하고 말풍선을 지운 뒤 PDF로 만들 것.
2. **[필수] 결론 (3) 첫 단어.** 추적 표시상 "R"이 삽입되고 "Combined r"이 삭제되어, 수락하면 "(3) Rated-load cases with combined …"가 된다. 수락 후 대문자·띄어쓰기를 확인할 것.
3. **[권장] S4.1 입력값 복원 여부.** 입경·밀도·흡수 단면적비·잔류비율식은 복사 계산을 재현하는 데 필요한 값이다. 본문이 "particle inputs ±20% 민감도(Table S15(c))"를 근거로 쓰므로 기준값이 있어야 민감도의 의미가 선다. 분량이 문제라면 문장 대신 **작은 표 1개**(성분, 입경, 분포지수, Qabs, 밀도, 잔류비율 c)로 되살리는 것을 권한다.
4. **[권장] SH2·SH3 저유량 특성선의 근거.** 새로 공개한 F/FN = 0.86 + 0.071ṁ/ṁN, 0.87 + 0.05ṁ/ṁN은 "부분부하 설계 분무량을 재현"하려는 보정이다. 심사자는 이를 보정에 의한 일치(calibration)로 볼 수 있다. Table S20(b)의 부분부하 분무 편차(−6.71/+2.12%) 문장 근처에 "이 보정을 반영한 결과"임을 함께 밝히는 편이 안전하다.
5. **[확인 완료] 후부 병렬유로·댐퍼 설명 삭제(S2.2).** 본문 2.3절과 3.1절에 같은 내용(병렬 후부 유로, 댐퍼 우선 제어)이 있으므로 문제없다.
6. **[확인] Data availability 문장 삭제.** "익명화 결과 데이터를 공개 저장소에 올릴 계획"을 지웠다. ECM은 데이터 공개를 권장하므로, 계산 결과(그림 원자료 CSV 등)를 보충자료로 제출할 계획이 있다면 그 사실을 적는 편이 유리하다.
7. **[표현] Fig. 9 하단 문구 중복.** 새 그림 하단의 "Upper values … Lower values …"가 캡션 문장과 겹친다. 둘 중 하나만 남길 것.
8. **[표현] Fig. 6의 주석 삭제.** 이전 그림의 "ΔT = −18 K, 주증기 601.67°C" 주석이 빠졌다. 현재는 S3에 "주증기온도 요건 미충족"이라는 서술만 있고 온도값은 어디에도 없다. 값이 필요하면 S3 해당 문장에 괄호로 넣을 것(예: "(601.67°C)").
