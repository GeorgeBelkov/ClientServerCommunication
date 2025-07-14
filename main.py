#  import os
import sys
import logging
import asyncio as aio

from serial_socket.serial_socket import socket
from handlers.heartbit import heartbit_loop


async def event_loop():
    while True:
        print("I am here! Please use me...")
        await aio.sleep(10)


async def main():
    """ Entry point for the application. """

    try:
        async with aio.TaskGroup() as taskgroup:
            taskgroup.create_task(event_loop())
            taskgroup.create_task(heartbit_loop())

    except aio.CancelledError as error:
        logging.error("Cancelled error was occured")
    finally:
        logging.info("Application finished...")

        


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="logfile.log")
    aio.run(main())
