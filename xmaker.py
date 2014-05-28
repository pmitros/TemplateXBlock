#!/usr/bin/env python
import yaml
import os

commands = '''
git mv ./template/template.py ./template/{shortname}.py
git mv ./template/static/html/template.html ./template/static/html/{shortname}.html
git mv ./template/static/css/template.css ./template/static/css/{shortname}.css
git mv ./template/static/js/src/template.js ./template/static/js/src/{shortname}.js
git mv template {shortname}

find . -type f | grep -v git | xargs sed -i 's/template/{shortname}/g'
find . -type f | grep -v git | xargs sed -i 's/Template/{Shortname}/g'

git remote rm origin
git remote add origin {github}
git rm --cached xmaker.py
git commit -a -m "Initializing repo"
git push --set-upstream origin master
'''

os.system("editor config.yaml")

settings = yaml.load(open("config.yaml", 'r'))
commands = commands.format(shortname = settings["short-name"],
                           Shortname = settings["short-name"].capitalize(),
                           github = settings["github"])

readme = open("README.md", "w")
readme.write("\n".join(["{Shortname}XBlock".format(Shortname = settings["short-name"].capitalize()),
                        "==============", 
                        "",
                        settings["description"],
                        "",
                        settings["overview"]]))
                   
readme.close()

for command in commands.split("\n"): 
    if len(command) > 0:
        print command
        os.system(command)

print "We've pushed to your git repo."
print "If you haven't yet done so, get and install this:"
print
print "  https://github.com/edx/xblock-sdk"
print 
print "As next steps, go to whereever you develop, and run: "
print
print "  git clone {github}".format(github = settings["github"])
print 
print "In your project, run" 
print
print "  python setup.py develop"
print
print "In github sdk, run:"
print
print "  python manage.py runserver"
print
print "And you should be good to go!"
