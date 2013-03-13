# -*- mode: python -*-
a = Analysis(['/Users/josephferraro/Development/Python/mavensmate/mm/mm.py', '/Users/josephferraro/Development/Python/mavensmate/mm/mm.spec'],
             pathex=['/Users/josephferraro/Development/Python/mavensmate/tools/pyinstaller'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build/pyi.darwin/mm', 'mm'),
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
               name=os.path.join('dist', 'mm'))
