import sys
import os
import time
import asyncio
import aiofiles
import aiohttp


async def files_downloader(site, download_directory, image_cnt):
    log_file = open("../artifacts/easy/easy_log.txt", 'w')

    semaphore_cnt = 5
    async with aiohttp.ClientSession() as session, asyncio.BoundedSemaphore(semaphore_cnt) as semaphore:
        for img_num in range(image_cnt):
            # with downloading time for every image
            start_time = time.time()

            async with session.get(site) as response:
                # writing to file
                file_path = f"{download_directory}/image{img_num}.png"
                async with aiofiles.open(file_path, 'bw') as file:
                    await file.write(await response.content.read())
                    # logging
                    log_file.write(f"Image №{img_num} was downloading for {time.time() - start_time}s\n")
                time.sleep(2)


def main():
    download_directory = "../artifacts/easy"  # sys.argv[0]
    image_cnt = 10                            # sys.argv[1]

    site = "https://thiscatdoesnotexist.com/"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(files_downloader(site, download_directory, image_cnt))
    loop.close()


if __name__ == '__main__':
    main()
