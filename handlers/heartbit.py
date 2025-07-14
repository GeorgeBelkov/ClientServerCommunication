import asyncio as aio

from serial_socket.serial_socket import socket

from config import USEFUL_PACKAGE_SIZE


async def send_heartbit() -> bool:
    """
        Sends a heartbeat signal and waits for a response.
        If no response is received within 5 seconds, it raises an exception.
    """
    await socket.send(bytes([0xF0]))
    await aio.sleep(5)
    data, bytelen = await socket.recv()
    if bytelen == 0 or data != [0x0F]:
        return False
    else:
        print("Heartbeat from raspberry successfully received")
        return True


async def heartbit_loop():
    """
        Handler for the heartbeat signal.
    """

    while True:
        is_online = await send_heartbit()

        if not is_online:
            print("call handler!")
