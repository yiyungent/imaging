import sys

import typer
import os

from .marker import add_mark
from .marker import gen_mark
from pathlib import Path

APP_NAME = "pyimaging"

app = typer.Typer()


class ArgsModel(object):
    # file：图片文件或图片文件夹路径
    # out：添加水印后的结果保存位置，默认生成到 output 文件夹
    # mark：要添加的水印内容
    # opacity：水印的透明度，默认 0.15
    # angle：水印旋转角度，默认 30 度
    # space：水印直接的间隔, 默认 75 个空格
    # size：水印字体的大小，默认 50
    # color：文字水印颜色设置 16进制
    def __init__(self):
        self.file = ""
        self.out = ""
        self.mark = ""
        self.opacity = 0.7
        self.angle = 30
        self.font_family = "./font/青鸟华光简琥珀.ttf"
        self.font_height_crop = "1.2"
        self.space = 75
        self.size = 35
        self.color = '#00ff00'
        self.quality = 80


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")


# file=""
# out = ""
# mark=""
# opacity = 0.7
# angle = 30
# font_family="./font/青鸟华光简琥珀.ttf"
# font_height_crop = "1.2"
# space = 75
# size = 35
# color = '#00ff00'
# quality=80

@app.command()
def watermark(imageDir: str = typer.Option(...), mark: str = typer.Option(...), opacity: float = typer.Option(0.5),
              angle: int = typer.Option(30), font_height_crop: str = typer.Option("1.2"), space: int = typer.Option(75),
              size: int = typer.Option(20), color: str = typer.Option('#00ff00'), quality: int = typer.Option(100)):
    """
    watermark
    """
    typer.echo("watermark...")

    # C:/Users/yiyun/AppData/Roaming/pyimaging
    app_dir = typer.get_app_dir(APP_NAME)
    app_dir_path = Path(app_dir)
    print("app_dir_path:" + str(app_dir_path))
    # 获取工作目录的路径, 也就是命令行执行的目录，比如在桌面打开cmd窗口，os.getcwd()得到的就是桌面路径
    cmdPath = os.getcwd()
    print("cmdPath:" + str(cmdPath))
    # 获取python文件的路径
    pyFilePath = os.path.dirname(os.path.realpath(__file__))
    print("pyFilePath:" + str(pyFilePath))
    # 获取当前被 python.exe 执行的文件的路径
    pyExeExecPyFilePath = sys.path[0]
    print("pyExeExecPyFilePath:" + str(pyExeExecPyFilePath))

    args = ArgsModel()
    args.font_family = os.path.join(pyFilePath, args.font_family)
    args.mark = mark
    args.opacity = opacity
    args.angle = angle
    args.font_height_crop = font_height_crop
    args.space = space
    args.size = size
    args.color = color
    args.quality = quality

    watermark_images_in_folder(imageDir=imageDir, args=args)


def watermark_images_in_folder(imageDir: str, args: ArgsModel):
    mark = gen_mark(args=args)
    for root, dirs, files in os.walk(imageDir):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file)
                print("watermark:" + image_path)
                args.file = image_path
                # 注意:这里要写父级文件夹路径, 因为后面会拼接源文件名
                # 直接在原图上修改
                args.out = os.path.dirname(args.file)
                add_mark(imagePath=image_path, mark=mark, args=args)


if __name__ == "__main__":
    app()
