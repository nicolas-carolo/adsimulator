import os
import platform
from adsimulator.utils.file import check_file_existence


init_path = os.path.expanduser("~")


def install_updates():
    """
    Run the script for making the pull of adsimulator
    """
    installer_path = os.path.abspath(init_path + "/.adsimulator/adsimulator/")
    if platform.system() == "Darwin":
        installer_path = os.path.abspath(installer_path + "/installer_darwin.sh")
        os.system(installer_path)
    elif platform.system() == "Linux":
        installer_path = os.path.abspath(installer_path + "/installer_linux.sh")
        os.system(installer_path)
    else:
        printf("ERROR: System not supported")
        exit(1)
    if check_file_existence(init_path + "/.adsimulator/adsimulator_sw.lock"):
        exit(0)
