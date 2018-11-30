# -*- mode: python -*-

block_cipher = None


a = Analysis(['src\\gui_PyQt5.py'],
             pathex=['F:\\\\Work\\\\domeSelenium1', 'F:\\\\Work\\\\domeSelenium1\\\\src', 'F:\\\\Work\\\\domeSelenium1\\\\src\\\\images', 'F:\\\\Work\\\\domeSelenium1\\\\src\\\\images\\\\robot-nothing.png', 'F:\\\\Work\\\\domeSelenium1\\\\src\\\\images\\\\robot-text.png', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36\\\\python36.zip', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36\\\\DLLs', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36\\\\lib', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Roaming\\\\Python\\\\Python36\\\\site-packages', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36\\\\lib\\\\site-packages', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\win32', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\win32\\\\lib', 'C:\\\\Users\\\\Dev\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\Pythonwin', 'F:\\Work\\domeSelenium1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='gui_PyQt5',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='src\\images\\logo.ico')
