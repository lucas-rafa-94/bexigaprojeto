# -*- mode: python -*-

block_cipher = None


a = Analysis(['manage.py'],
             pathex=['/Users/lucasdossantos/Documents/mariana/bexigaprojeto'],
             binaries=[],
             datas=[("escolha/templates/escolha/*.html","escolha/templates/escolha/"), ("escolha/static/escolha/css/style.css","escolha/static/escolha/css/"), ("escolha/static/escolha/images/*.jpg","escolha/static/escolha/images/")],
             hiddenimports=['escolha.urls', 'escolha.views', 'escolha.models', 'escolha.apps', 'escolha.admin', 'escolha.__init__', 'bexigaprojeto.__init__', 'bexigaprojeto.settings', 'bexigaprojeto.urls', 'bexigaprojeto.wsgi' ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='bexiga',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='bexiga')
