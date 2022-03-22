import sys
import time
import asyncio
import aiofiles
import aiohttp

log_file = open("../artifacts/easy/easy_log.txt", 'w')


async def file_downloader(site, download_directory, img_num):
    async with aiohttp.ClientSession() as session:
        async with session.get(site) as response:
            # writing to file
            file_path = f"{download_directory}/image{img_num}.png"
            async with aiofiles.open(file_path, 'bw') as file:
                # with downloading time for every image
                start_time = time.time()
                await file.write(await response.read())
                # logging
                log_file.write(f"Image №{img_num} was downloading for {time.time() - start_time}s\n")


async def download_process(site, download_directory, image_cnt):
    task_array = []
    for img_num in range(image_cnt):
        task_array.append(asyncio.create_task(file_downloader(site, download_directory, img_num)))
    await asyncio.gather(*task_array)


def main():
    download_directory = "../artifacts/easy"  # sys.argv[0]
    image_cnt = 10                            # sys.argv[1]

    # site = "https://thiscatdoesnotexist.com/" --> too long interval between picture updating
    site = "https://picsum.photos/800/800?blur=1"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_process(site, download_directory, image_cnt))
    loop.close()


if __name__ == '__main__':
    main()
