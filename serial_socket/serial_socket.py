import logging
import asyncio

import aioserial

from config import (
    BPS, PORTNAME, USEFUL_PACKAGE_SIZE
)


class AsyncSerialSocket(aioserial.AioSerial):
    """
        Async serial socket for communication with modem
    """

    def __init__(self):
        super().__init__(
            port=PORTNAME,                # Имя порта
            baudrate=BPS,                 # Скорость передачи (bits per second)
            timeout=0,
            write_timeout=0,
        )
        self.fullpack_size = USEFUL_PACKAGE_SIZE
        
        logging.info(
            (f"Bind completed at address: {self.port} with baud rate: \
            {self.baudrate} timeout: {self.timeout}")
        )
    
    async def send(self, bytes: bytearray):
        """ Send bytes to modem """
        await self.write_async(data=bytes)

    async def recv(self) -> tuple[bytearray, int]:
        """ Recv bytes from modem """
        await self.read_async()


socket = AsyncSerialSocket()
