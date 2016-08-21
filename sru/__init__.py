import logging
import sys

log = logging.getLogger()
log.setLevel(logging.DEBUG)

pip_log = logging.getLogger("pip_shim")
pip_log.setLevel(logging.ERROR)

aiohttp_log = logging.getLogger("aiohttp")
aiohttp_log.setLevel(logging.ERROR)

asyncio_log = logging.getLogger("asyncio")
asyncio_log.setLevel(logging.ERROR)


handler = logging.StreamHandler(stream=sys.stdout)
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

log.addHandler(handler)
