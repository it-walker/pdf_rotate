import os
import sys
import PyPDF2

from settings_manager import SettingsManager


def main():
    config_file_path = os.path.join(os.path.dirname(sys.argv[0]), "config.yaml")
    conf = SettingsManager()
    conf.load(config_file_path)

    target = open(conf.target_file_path, "rb")
    reader = PyPDF2.PdfFileReader(target)
    writer = PyPDF2.PdfFileWriter()

    print("対象PDF:{0}".format(conf.target_file_path))
    print("出力ファイルパス:{0}".format(conf.out_file_path))
    print("回転角度:{0}度".format(conf.rotate))
    for page in range(reader.numPages):
        obj = reader.getPage(page)
        obj.rotateClockwise(conf.rotate)  # 回転させる
        writer.addPage(obj)

    outfile = open(conf.out_file_path, "wb")
    writer.write(outfile)
    outfile.close()
    target.close()


if __name__ == "__main__":
    main()
