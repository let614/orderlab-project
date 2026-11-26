# OrderLab — Python CI/CD Levels 1–5

교수님 `Python_CICD.pdf`의 Level 1–5 실습을 통합한 예제입니다.

## 구성
- Level 1: `subtotal()` 및 정상/0/음수 테스트
- Level 2: `final_total()` 할인/배송비/경계값/예외
- Level 3: CSV 집계, `tmp_path`, fixture, coverage.xml artifact
- Level 4: FastAPI `create_app()`, POST/GET, TestClient, Ubuntu/Windows matrix
- Level 5: `generate_report.py`, `site/index.html`, GitHub Pages 배포

## 로컬 실행
```bash
python -m pip install -r requirements-dev.txt
ruff check .
ruff format --check .
python -m pytest -q
python -m pytest --cov=orderlab --cov-report=xml
python generate_report.py
```

## GitHub 업로드
ZIP 압축을 풀어 **파일과 폴더를 저장소 최상위**에 업로드하세요.
기존 저장소의 `orderlab/tests/`에 남아 있는 오래된 파일은 별도로 정리해야 합니다.
`.github/workflows/ci.yml` 같은 숨김 폴더도 반드시 업로드해야 합니다.

## Pages 활성화
Settings → Pages → Build and deployment → Source: **GitHub Actions**.
`main` push의 lint와 test가 모두 통과하면 deploy가 실행됩니다.
Pull Request에서는 deploy가 건너뛰어집니다.

## 과제 실습 증빙 (ZIP에 포함되지 않는 실제 GitHub 기록)
1. Ruff 실패와 pytest 실패를 **별도 실습 커밋**으로 재현해 Actions 로그 캡처
2. 오류 수정 후 PASS 로그 캡처
3. 기능 브랜치에서 PR을 만들어 Ubuntu/Windows/lint PASS 캡처
4. `main` 병합 후 Pages 배포 성공 및 실제 URL 접속 캡처
5. 테스트를 의도적으로 깨뜨린 브랜치/PR에서 deploy가 실행되지 않음을 확인
실패를 재현한 뒤에는 반드시 복구하세요.

**주의:** 이 ZIP은 구현 코드이며 실제 GitHub 실행/배포를 대신하지 않습니다.
