# -- coding: utf-8 --

from cx_Freeze import setup, Executable

options = {
    'build.exe': {
        'includes': [
            'my_bot',
            'text_bot_gui'
        ]
    }
}

setup(
    name='Set bot PyQt',
    version='1.0',
    description='Text_bot PyQt',
    options=options,
    executables=[Executable('hello_qt.py')]
)

#build
#bdist_msi

