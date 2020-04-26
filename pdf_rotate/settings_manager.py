import yaml


class SettingsManager:

    _key_target_file_path = "target_file_path"
    _key_out_file_path = "out_file_path"
    _key_rotate = "rotate"

    @property
    def target_file_path(self):
        """対象のPDFファイルパス"""
        return self._target_file_path

    @property
    def out_file_path(self):
        """出力PDFファイルパス"""
        return self._out_file_path

    @property
    def rotate(self):
        """回転させる角度"""
        return self._rotate

    def __init__(self):
        self._target_file_path = ""
        self._out_file_path = ""
        self._rotate = 0

    def load(self, yaml_path):
        """設定ファイルを読み込みます

        Arguments:
            yaml_path {string} -- 設定ファイル（config.yaml）
        """
        try:
            with open(yaml_path, "r", encoding="utf-8") as f:
                y = yaml.load(stream=f, Loader=yaml.SafeLoader)
                self._target_file_path = y[self._key_target_file_path]
                self._out_file_path = y[self._key_out_file_path]
                self._rotate = y[self._key_rotate]
        except BaseException:
            print("error", yaml_path)
            raise
