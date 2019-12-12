#! /usr/bin/env python
import os
import json

print("Generating update files for Socializer...")# Determine if we are going to write stable or alpha update file.
# Stable file is when we build tags and alpha otherwise.
version = os.environ.get("CI_COMMIT_TAG") or os.environ.get("CI_COMMIT_SHORT_SHA")
if os.environ.get("CI_COMMIT_TAG") == None:
	version_type = "alpha"
else:
	version_type = "stable"
print("Version detected: %s" % (version_type,))

# Read update description and URL'S
if version_type == "alpha":
	description = os.environ.get("CI_COMMIT_MESSAGE")
	urls = dict(windows32="http://socializer.su/static/files/alpha/socializer_x86_alpha.zip", windows64="http://socializer.su/static/files/alpha/socializer_x64_alpha.zip")
else:
	with open("update-description",'r') as f:
		description = f.read()
	urls=dict(windows32="http://socializer.su/static/files/{v}/socializer_{v}_x86.zip".format(v=version[1:]), windows64="http://socializer.su/static/files/{v}/socializer_{v}_x64.zip".format(v=version[1:]))

# build the main dict object
data = dict(current_version=version, description=description, downloads=urls)
print("Generating file with the following arguments: %r" % (data,))
if version_type == "alpha":
	updatefile = "alpha.json"
else:
	updatefile = "stable.json"
f = open(updatefile, "w")
json.dump(data, f, ensure_ascii=False)
f.close()
