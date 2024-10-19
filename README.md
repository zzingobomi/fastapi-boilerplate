### FastAPI Boilerplate

## Migration

- autogenerate 할때 model 들을 인식하기 위해 필요한 모델을을 import 한다
- migration이 시간순서대로 쌓기기 위해 alembic.ini 파일의 file_template 을 변경한다
- migration 파일을 만든다
  ```
  poetry run alembic revision --autogenerate -m "message"
  ```
- migration 을 적용한다
  ```
  poetry run alembic upgrade head
  ```
