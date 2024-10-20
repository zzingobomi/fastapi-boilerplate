### FastAPI Boilerplate

## Migration

- autogenerate 할때 model 들을 인식하기 위해 필요한 모델을을 import 한다
- migration이 시간순서대로 쌓기기 위해 alembic.ini 파일의 file_template 을 변경한다
- migration 파일을 만든다
  ```
  cd src
  poetry run alembic revision --autogenerate -m "message"
  ```
- migration 을 적용한다
  ```
  poetry run alembic upgrade head
  ```

## Seed data 넣기

```
poetry run python -m src.scripts.create_seed_user
```

- asyncio.gather 을 이용해서 실행하는데 왜 실행시간이 오래 걸릴까? 100명의 요청을 한번에 보내니까 시간은 1명 걸리는 것처럼 나와야 할거 같은데..
- 요청은 한번에 다 보냈는데 db 에서 처리하는 시간이 걸리는 것일까?

## TODO

- postgres mysql 로 변경하기
