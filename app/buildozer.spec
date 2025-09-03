[app]

# (str) Title of your application
title = Breakout Game

# (str) Package name
package.name = breakoutgame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example.breakout

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.1.0,pillow,pyjnius

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
#android.api = 27

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (str) Supported orientation (landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

[android]

# (str) Android entry point, default is ok for Kivy-based app
# android.entrypoint = org.renpy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Python Service
# android.service_main_class = org.kivy.android.PythonService

# (list) Pattern to whitelist for the whole project
# android.whitelist =

# (str) Path to a custom whitelist file
# android.whitelist_src =

# (str) Path to a custom blacklist file
# android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
# their classes. Don't add jars that you do not need, since extra jars can slow
# down the build process. Allows wildcards matching, for example:
# OUYA-ODK/libs/*.jar
# android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
# android.add_src =

# (str) OUYA Console category. Should be one of GAME or APP
# If you leave this blank, OUYA support will not be enabled
# android.ouya.category = GAME

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
# android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
# android.manifest.intent_filters =

# (str) launchMode to set for the main activity
# android.manifest.launch_mode = standard

# (list) Android additional libraries to copy into libs/armeabi
# android.add_libs_armeabi = libs/android/*.so
# android.add_libs_armeabi_v7a = libs/android-v7/*.so
# android.add_libs_arm64_v8a = libs/android-v8/*.so
# android.add_libs_x86 = libs/android-x86/*.so
# android.add_libs_mips = libs/android-mips/*.so

# (bool) Indicate whether the screen should stay on
# Don't forget to add the WAKE_LOCK permission if you set this to True
# android.wakelock = False

# (list) Android application meta-data to set (key=value format)
# android.meta_data =

# (list) Android library project to add (will be added in the
# project.properties automatically.)
# android.library_references = @null

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
# android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk or 'both').
android.release_artifact = apk