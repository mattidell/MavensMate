# -*- mode: python -*-
a = Analysis(['/Users/josephferraro/Development/Python/mavensmate/mmserver/mmserver.py', '/Users/josephferraro/Development/Python/mavensmate/mmserver/mmserver.spec'],
             pathex=['/Users/josephferraro/Development/Python/mavensmate/tools/pyinstaller-dev'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.darwin/mmserver', 'mmserver'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name=os.path.join('dist', 'mmserver'))
