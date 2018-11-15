import orm
from models import User, Blog, Comment
import asyncio
import random


async def test(loop):
    await orm.create_pool(loop, user='root', password='', db='awesome')

    u = User(name='Test', email='test@example.com',
             passwd='1234567890', image='about:blank')

    await u.save()

# 要运行协程，需要使用事件循环
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('Test finished.')
    loop.close()

# for x in test():
#     pass
