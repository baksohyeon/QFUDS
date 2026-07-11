# Worlds

허구 세계에서 현재 참으로 채택한 사실을 보관한다. 세계 전체 규칙, 연속성,
용어, 인물·장소·기관은 프로젝트 원고와 분리해 찾을 수 있어야 한다.

- [QFUDS Verse](qfuds-verse/README.md): QFUDS에서 파생된 픽션 세계
- [Vector Sandbox](vector-sandbox/README.md): 별도의 비상속 샌드박스 세계

## 설정 상태 규칙

세계의 사실 상태와 세계 폴더의 운영 상태를 구분한다.

```yaml
canon_state: provisional | accepted | retired
lifecycle_state: active | dormant | retired
```

- `provisional`: 후보. 프로젝트가 의존하면 안 되는 임시 설정
- `accepted`: 이 세계에서 현재 참으로 채택한 사실
- `retired`: 폐기됐지만 이력 이해를 위해 남긴 설정

`lifecycle_state`는 지금 작업 중인지 여부일 뿐 canon을 바꾸지 않는다.

가능성 공간(아이디어·씨앗)은 여기 두지 않는다 — `knowledge/`나 프로젝트로
보낸다. 복잡한 canon 승인 체계는 만들지 않는다. 기존 이관 문서의 canon
상태 표기는 그대로 두되, 개정할 때 이 세 단계로 정리한다.
