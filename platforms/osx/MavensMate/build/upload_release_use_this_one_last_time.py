import ftplib
import os
import urllib
from xml.dom import minidom
import xmltodict

mavensmate_app_path = os.path.dirname(os.path.dirname(__file__))

release_info_plist_path = mavensmate_app_path+"/dist/MavensMate.app/Contents/Info.plist"
xml_data = open(release_info_plist_path)
data = xmltodict.parse(xml_data)
xml_data.close()

##get release version number
plist_dict = data['plist']['dict']
bundle_index = None
for i,f in enumerate(plist_dict['key']):
    if f == 'CFBundleVersion':
        bundle_index = i

new_version_number = None
for i,f in enumerate(plist_dict['string']):
    if i == bundle_index:
        new_version_number = f

##write release to ftp
session = ftplib.FTP('ftp.joe-ferraro.com')
session.login('droppd', 'Rg3skins')
session.cwd("/public_html/mavensmate")

try:
    session.mkd("/public_html/mavensmate/builds")
except:
    pass

#archive legacy version
dom = minidom.parse(urllib.urlopen('http://joe-ferraro.com/mavensmate/appcast.xml'))
enclosure = dom.getElementsByTagName("enclosure")[0]
legacy_version = enclosure.getAttribute("sparkle:version")

session.mkd("/public_html/mavensmate/builds/"+legacy_version)
session.rename("/public_html/mavensmate/MavensMate.zip", "/public_html/mavensmate/builds/"+legacy_version+"/MavensMate.zip")
session.rename("/public_html/mavensmate/appcast.xml", "/public_html/mavensmate/builds/"+legacy_version+"/appcast.xml")
try:
    session.rename("/public_html/mavensmate/release_notes.html", "/public_html/mavensmate/builds/"+legacy_version+"/release_notes.html")
except:
    pass

# session.delete("MavensMate.zip")
# session.delete("appcast.xml")

file = open(mavensmate_app_path+"/release/appcast.xml", "rb")
session.storbinary('STOR appcast.xml', file)
file.close()

file = open(mavensmate_app_path+"/release/MavensMate.zip", "rb")
session.storbinary('STOR MavensMate.zip', file)
file.close()

#create new version
session.mkd("/public_html/mavensmate/builds/"+new_version_number)
session.cwd("/public_html/mavensmate/builds/"+new_version_number)
file = open(mavensmate_app_path+"/release/appcast.xml", "rb")
session.storbinary('STOR appcast.xml', file)
file.close()

file = open(mavensmate_app_path+"/release/MavensMate.zip", "rb")
session.storbinary('STOR MavensMate.zip', file)
file.close()


session.quit()