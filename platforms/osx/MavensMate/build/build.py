import os
import sys
mavensmate_app_path = os.path.dirname(os.path.dirname(__file__))
os.chdir(mavensmate_app_path)
build_command = '/usr/bin/xcodebuild -target MavensMate -scheme MavensMate archive'
os.system(build_command)