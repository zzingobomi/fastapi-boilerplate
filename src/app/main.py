from .api import router
from .core.config import settings
from .core.setup import create_application

# from fastapi.exceptions import RequestValidationError
# from fastapi import Request, status
# from fastapi.responses import JSONResponse
# from fastapi.encoders import jsonable_encoder

app = create_application(router=router, settings=settings)

# -------------- custom exception handlers --------------
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
#     )
