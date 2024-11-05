# TODO implements later
# from database.models import *
# from sqlalchemy import select
#
#
# async def set_user(tg_id: int) -> None:
#     async with async_session() as session:
#         user = await session.scalar(select(Name).where(Name.tg_id == tg_id))
#
#         if not user:
#             session.add(Name(tg_id=tg_id))
#             await session.commit()
#
#
# async def get_categories():
#     async with async_session() as session:
#         return await session.scalars(select(Category))
#
#
# async def get_category_item(category_id):
#     async with async_session() as session:
#         return await session.scalars(select(Important).where(Important.category == category_id))
#
#
# async def get_item(item_id):
#     async with async_session() as session:
#         return await session.scalar(select(Important).where(Important.id == item_id))