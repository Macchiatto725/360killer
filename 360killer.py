import cv2
import pyautogui
from time import sleep
import base64
import os


b64_360logo =  b'iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABIFBMVEUAAAA5mxM3mBA3mBI7nRM9nxU9nxVYpgxKmQA/kwBiogBrpQBysQBpqQyswgB1qgBorQDAywDMzAB9sQD/3gD/3AD/2gD/2gD/1gD/1AD/1AD/0gD/0ABFiwBfngCwswBLmAhGlwlVkQAtiws9lA9SjgAqfggsgggfjRcejRcdiRUfjRcehxUYhRQbhxROmAAtjQ03mRI7nhXKywD/4wD/4ADd1ACqvgA1jwf/3QBgowH/5gUaiBXu1gC0vwDm0wD/2gAWhw//2ABXmQAOgwsQgwkNhAhhnQD/1gAHgAFfmgD/0wAAegDmyQCxtgDwzAAdgRArggnJvQD/0ABPjwBTkQD/zgAjjhensAAafxFekwDUvgDFuQAZehE/hQL///+3RzNDAAAAL3RSTlMASKzf99CIH9v39f2sBy7y8R7Q5E6s5uf51NeNJP7Pnwzi2hWf9vXOJYzZ9visR+Pu5DsAAAABYktHRF9z0VEtAAAAB3RJTUUH5QIPCg4VVjcvFAAAANlJREFUGNNjYAACRiZmFhZWNnYGCGDn4OTi1jcwNDLi4QXx+fiNTUxMTM24DYyMBASBAkKmpkA+EJhbGBoJMzCIWAL5JiZWVpaWxhYG+iIMokABa2sTGxtLS0tbO3tRBjEHkBJTR0cHMBBncHJycnB2cXV1c3F1B7KdGCQ8PDycPcHAC8iUYJD0BgMfHwgtxSDt6+ePJCDNICMbEBgUHBwSGgwCYTIMDHLh4YERYVAgD3SpgmJ4eGRUNIgbo6QM8gyvSni4TWxclKqaujLUvxqaWto6Wrp6IDYAbc4x1mL6u6YAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjEtMDItMTVUMTA6MTQ6MjErMDA6MDAjx4CTAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIxLTAyLTE1VDEwOjE0OjIxKzAwOjAwUpo4LwAAAABJRU5ErkJggg=='
b64_360_logout1 = b'iVBORw0KGgoAAAANSUhEUgAAAF0AAAAkCAIAAABkPqGdAAAEWElEQVRoBe2YSUsjQRTHjbu4r6jYOgSjKCJ6FWEaL34GDx48BD+DOcxRP0OYwxwcGD+CAZEIQw7qyYO4YBSi4oIo7rjOr9N2p5OuxFTrLA7dF6tfVb2u+uVf773Sc3FxkeM+NgK5Notr0Ai4XMQ6cLm4XMQExFZXLy4XMQGx1dWLy0VMQGx9q15ubm5mZmZisZjY/Ye1vpXL/f39xsbGP1E0R6ZU1f/jnX6gfGe/6N3d3eXl5fPzc0FBge4BNLe3txUVFUVFRbI+Yz/8oztj4YkBfaL2GtwUOPGNT38dUV46wBCIWg22CXE/3knTr21ABoM0F1g8PDwcHx9vb2/jt7e3V/fOUdrd3e3o6GhoaCguLs7NlVHi4NBwMKDmWLYwbGnHP6Btcj7DRt65S2b18U+jlOXl5bm5OdCAwFwOSgHZ7OxsJBI5PT017dk0FGVkIjw5HApMRbIZ/ifGyOnl7OxsdXUVaXR3dzc3N1dVVT0+PurLrK+v7+/vVxSFASsrKz6fr6WlRWYHAxPhcGJ8KKCGEm8vLd+QzfS7DBJcUMrh4eHW1lZnZyfbrqys9Hg85+fn+tIIK8inurr66elpfX19b2+vtra2pKTE4cL/9jmS4IJYODsEWsRSVlYm3LDee3BwwOCjo6O2tjbhMKtRi5+6NGwsrMOE7c3gqBpM6rEZvEndWb9IcGG3BI6+vj7CqukfycAoPz/hh4jb3t6OrKLRaDZctPMzkaPRMZ3SeP0c6fMsc2wJKp6PLANkmon9vDrr6urq+vq6sbHRmmtKS0v9fr+VFH7q6uqAgmRe9Zl2gLx27K6Uka/hEbs5K4tEPqI8oYpDHWjE9A2j8vJys4rR7XpYYbw5zFGD31u1ZigEoRoGrc9op3euzbB6SD8ytUdCL0wlE5OA8vLyUt0kvzOGh8HJZum3wS+TO6Oq6hsf9waDxCBEFFa0K4dR20l7zHqChF4KCwuJI4QYMk5m/5TCjHGejF68K0psIQSMsR2gUOvGC1cqgcwff59eCS7kYKLJ/v5+Zi7IhLTF6qhoHK0x9nN+U4u7PN8+aTC0CDs9NI9ynJ0JJ6uQ4NLU1ESFsrS0pMsh3deIQZR2sKPGSTcm1R6Z0lJ1aCFe7iqDQ774kQmHE7chLYZOj0cDfwqNJ/urMNcixLK4uEig5VoEo5RAAwv+7QA4zprX6+3q6uLopSKwvxv5te07hUzS1dA+1rTEc7DobmmOMBrOMpsEFz5EquYSwD8WSMzcA8jZMGLzaISuk5MTeoHS2toKl5qaGmNtmf6CZeGzcefVGKGcjI/ERjV3Oak30IzOjU45LsziNkCZT3mCWNg5wRVGcEEpFCy6UjhBXJ2s6dz43If5K81F3xn7p6JdW1ujCOZ86YzQSE9PD7BSzteHgWFZqEMuhBJw8FCn4I0cBAuyOAUeMvnQStHhOORiIft/NiXy9P8JIM2uXC5iMC4Xl4uYgNjq6sXlIiYgtv4CTj34+noobgAAAAAASUVORK5CYII='
b64_360_logout2 = b'iVBORw0KGgoAAAANSUhEUgAAAGoAAAAaCAIAAADQYV4BAAAEaUlEQVRoBe2YuVLjQBCGZW6W+1gIKFwmcPECigkINiJySuAqko1IyMj8BE4ckVBFQEpERLBbRawXoAi85Yz7Pnyyn6SRLI9leYSxFxacaI6/e2Z+d093T+Tl5UX7+r2Wga7XCn7JmQz01NOAPT4/P19eXt7c3Dw8POTzeTD9/f1DQ0NjY2OTk5MDAwORSKRe8BOORCTnfXp6Oj8/v7i4gKzBwcHe3t6uLtNCK5VKsVhk9v7+fmpqamZmBhI/IV/SkWucF2rgDtMbHR2dmJjA0Kanp79bPxp0GcQAAZydnd3d3Um62tzN7azq+upOrs3LWOpV16o6L5Z1dXWFt8IR9tXTU51CY3d39zfrNz4+jm2CxGyxzeY2eJjStxb2dpNR+9hsLJE58qVgJW2klpwZCxf3jjgzni+6N47XXeVmd98zHdSsWSwIGDgnOIIL2+5gZ3Z2NkAEWgGAx/pOT0/n5+eD78FcbHld20joWQ8Ti9UTOyuZJ3far/4upQwjVZWWyHUnrH/G7bXUEM6LP2JTmBhOqqIPGGBsEMFgfDS6lNzdW1/c3+qM2wXvxp1dXIi57RYawvqIs7jmyMiI5LONNAMDXC6XEZybm2sEc8ajyV0j6XQ07SiT0DPVrtNacRpt/v7Jcnn8eJNFBH3kKIQLoq26UsDkNNfX1wr0SVrb5bzSMh3oCvoeHx8JF319fepLAiZ0IKgu8g6RAZFM0/ydxPvnC/q4wsjvFD3XZgEwIoVCIYCU6ua8a6o77/6GLkfSuiMtBqzfeCq+YGcC0rXiCNjRpT7COfPOV9DndEN8K1qlrJWlrFuStzdn7uXAO1PDpXfC064/l8+RrNjqEVJq5rLHmhZXgjYFichL+kZdQShoKuACKmUINIs5dyRcg6OnDr0i0KNLQ95pv7aZqbgZpR/AZ+xwm7RzZdlNMH0g6kOCPsIuNZld3ioKF/KFUrEUKtp4Nedia2ltQ/BlMZfIkCWvxXIWCnJVKgxFyk1tzo/EeiVdTc+9ewrfFs5LKUa9gSnBo6IS8BQqCCriJViUH7azbB6MKfzZsAsTUZ1I8Na6Uj7dmjKvtLA+6lnooJBQ9F9ggBFB0KsuTNuynF/LhpEm4Ts6+G2bXRgN/x4r6OPuI3GBFEo3lU0BAwx3zWteSZ2Zs5pps64nsj+psbiDTNtIxxnr0HuAtKNWuoI+6lYeVuCCOuzk5CTABpkCAAwwz1bBBa+5s9zOJnf1UWb70Orhp5anGjZ1zt6hcG9dy2y+q8rO2Vzjb817Hw9WdhlLPUsRwj3IbUibEEucJVaQJN/e3pZKJZ4CeVygbmus2ZrBQa2IkNLMxxCVhEUo5LIP+XhiLeX/lNNok2I/4ddyFdbQxyjRAMfkNzw8jH1BH/ZFfhd5iRQLoZ9L2RiXmwhziucL9ZLk/j1vk4e4tKg2ZPqQIxOmCOEtgHqW4EBCwwg8YnH2Gyq0NvdZ1Q18bJwPfR/7QJ3dvQgdnV30/1nti76W/ssv+lqi7y9iMS154NyoIwAAAABJRU5ErkJggg=='
b64_360_logout3 = b'iVBORw0KGgoAAAANSUhEUgAAAC4AAAAZCAIAAADBpIt1AAACbElEQVRIDe1Vv2rbQBj/VDpcN3U715PBHlQ6SKVZ1BdI0oC3PoApUT0pSzeDKXTrYk9GGQx9hEIT5wXSJdBoKAhagafYt9WjNvfuFFV3urMtKRRSqBH4vr/3u++vAd/ewv34PbgfMBiKfxCK2xiuHe/4b8awXFRQ9xPGMflyWgHK3rkzHKEKBg8lXdNbt2yJs5oa88Wotd+mXDxY41w4m/cPVzlZPFEQCfatIUTvT5KiUEsbug6iD+pBdtNxaxKYZCx45JzQuw6yIDVH1sAvH4Dk4mX0+asCR45KKkZPOhB+5C+mJVLAAabHOX9w3LqMyYfO8kbxX2RQh5dmkZnSGijuY7udhN+ZfG+AYUyIb0182TzjSNGSVSpTaoKk7DB/rIDgNh3iGXV/WvaZkLjKl8sGSlTM5wdUozVZMz3+aNlAQ6nFrlGSWNqSL0Bpjhqsg7gqDc9h5sAOnEmQEcKZMN4qMK4zmfgvhlDkbzhLc8VtvNnQCLRf+gb95iFAdo4uYtnpHcegCKX52sSz+XQmX1CeeoYwJITXe3mjXFNM0M1J1Kddc55LK52aT9lYW8gDQ8osd7ex6UQoWy6WPBZrJbVDL14hiFcL2Ys4CWWJQokJUoSc4T7CQMf/rlph0wigjY9qr0w9lAPazE6PdTWwAoqTwltV0FyNTMeJHVhdV5WX4OgTlPc9nWOInP3aNdHNIx+F3vLqdLkAa3Dp7DMPJa4XVdRpK0qBbT4kbK90VETkncV3NdvbV6zSnV5H3EFsEHMFyVlOaBfWdihsyv3YNdoZXEgx5ZfVOG2HUsNhfRN92db3dwfL/1B0wfsNBEX+Onqxq7IAAAAASUVORK5CYII='
if os.path.exists("c:\\temp"):
    pass
else:
    os.mkdir("c:\\temp")
base_temp_path = 'c:\\temp\\'
logoImage = base_temp_path + r'logo.png'
logout1Image = base_temp_path + r'lougout1.png'
logout2Image = base_temp_path + r'logout2.png'
logout3Image = base_temp_path + r'logout3.png'
screen_before = base_temp_path + r'before.png'
screen_logout1 = base_temp_path + r'screen_logout1.png'
screen_logout2 = base_temp_path + r'screen_logout2.png'
screen_logout3 = base_temp_path + r'screen_logout3.png'

logo_img = base64.b64decode(b64_360logo)
with open(logoImage, 'wb') as f:
    f.write(logo_img)

logout1_Image = base64.b64decode(b64_360_logout1)
with open(logout1Image, 'wb') as f:
    f.write(logout1_Image)

logout2_Image = base64.b64decode(b64_360_logout2)
with open(logout2Image, 'wb') as f:
    f.write(logout2_Image)

logout3_Image = base64.b64decode(b64_360_logout3)
with open(logout3Image, 'wb') as f:
    f.write(logout3_Image)


def press_keys(*args):
    pyautogui.hotkey(args[0], args[1])
    sleep(0.2)
    pyautogui.press(args[2])

def get_screen(screenName):
    pyautogui.screenshot(screenName)

def get_position(imgSource, imgTarget):
    source = cv2.imread(imgSource, 0)
    target = cv2.imread(imgTarget, 0)
    wight, height = target.shape[::-1]
    res = cv2.matchTemplate(source, target, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    pos_x = int(max_loc[0] + wight / 2)
    pos_y = int(max_loc[1] + height / 2)
    print(pos_x, pos_y)
    return pos_x, pos_y

def killav():
    press_keys('win', 'b', 'enter')
    get_screen(screen_before)
    sleep(1)
    pyautogui.rightClick(get_position(screen_before, logoImage))

    get_screen(screen_logout1)
    sleep(1)
    pyautogui.click(get_position(screen_logout1, logout1Image))
    sleep(0.5)

    get_screen(screen_logout2)
    sleep(1)
    pyautogui.click(get_position(screen_logout2, logout2Image))

    get_screen(screen_logout3)
    sleep(1)
    pyautogui.click(get_position(screen_logout3, logout3Image))


def clean():
    os.popen(r'del /q {} {} {} {} {} {} {} {}&rmdir c:\\temp '.format(logoImage, logout1Image, logout2Image,
                                            logout3Image, screen_before, screen_logout1, screen_logout2, screen_logout3))

if __name__ == '__main__':
    killav()
    clean()