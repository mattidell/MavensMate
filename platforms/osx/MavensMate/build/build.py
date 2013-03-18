import os
import sys
import shutil
mavensmate_app_path = os.path.dirname(os.path.dirname(__file__))
if os.path.exists(mavensmate_app_path+"/dist/MavensMate.app"):
    os.system("rm -rf {0}".format(mavensmate_app_path+"/dist/MavensMate.app"))
if os.path.exists(mavensmate_app_path+"/dist/MavensMate.zip"):
    os.system("rm -rf {0}".format(mavensmate_app_path+"/dist/MavensMate.zip"))
if os.path.exists(mavensmate_app_path+"/release/MavensMate.zip"):
    os.system("rm -rf {0}".format(mavensmate_app_path+"/release/MavensMate.zip"))

os.chdir(mavensmate_app_path)
build_command = '/usr/bin/xcodebuild -target MavensMate -scheme MavensMate archive'
os.system(build_command)
os.chdir(mavensmate_app_path+"/dist")
shutil.make_archive(mavensmate_app_path+'/release/MavensMate', 'zip', root_dir = mavensmate_app_path+'/dist')