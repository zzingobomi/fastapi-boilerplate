import asyncio
import logging
import uuid
from datetime import UTC, datetime

from sqlalchemy import select

from ..app.core.db.database import local_session
from ..app.core.security import get_password_hash
from ..app.models.user import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_seed_user(name: str, email: str, username: str, password: str) -> None:
    async with local_session() as session:
        try:
            hashed_password = get_password_hash(password)

            query = select(User).filter_by(email=email)
            result = await session.execute(query)
            user = result.scalar_one_or_none()

            if user is None:
                new_user = User(
                    name=name,
                    username=username,
                    email=email,
                    hashed_password=hashed_password,
                    profile_image_url="https://profileimageurl.com",
                    uuid=uuid.uuid4(),
                    created_at=datetime.now(UTC),
                    is_deleted=False,
                    is_superuser=False,
                )
                session.add(new_user)
                await session.commit()
                logger.info(f"User {username} created successfully.")
            else:
                logger.info(f"User {username} already exists.")

        except Exception as e:
            logger.error(f"Error creating user: {e}")


async def create_multiple_users(num_users: int) -> None:
    tasks = []
    for i in range(1, num_users + 1):
        name = f"zzingo{i}"
        email = f"zzingo{i}@example.com"
        username = f"zzingo{i}"
        password = f"password{i}"
        logger.info(f"User {username} task...")
        tasks.append(create_seed_user(name, email, username, password))
    await asyncio.gather(*tasks)


async def main():
    await create_multiple_users(100)


if __name__ == "__main__":
    asyncio.run(main())
