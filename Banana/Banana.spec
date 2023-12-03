# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

__version__ = '0.1.2'

info_plist = {
    'LSUIElement': True,
    #'LSBackgroundOnly': True,
}

a = Analysis(
    ['Banana.py'],
    pathex=['/Users/ryanshenefield/Downloads/Banana.py'],
    binaries=[],
    datas=[('banana_desk.icns', '.'), ( 'alipay20.png', '.'), ( 'embeding.icns', '.'), ( 'wechat10.png', '.'), ( 'webarchiver.command', '.'), ( 'tarfolder.txt', '.'), ( 'choose.txt', '.'), ( 'alipay5.png', '.'), ( 'wechat5.png', '.'), ( 'alipay50.png', '.'), ( 'with_embeddings3.csv', '.'), ( 'with_embeddings2.csv', '.'), ( 'banana.icns', '.'), ( 'api.txt', '.'), ( 'wechat50.png', '.'), ( 'alipay10.png', '.'), ( 'banana.png', '.'), ( 'wechat20.png', '.'), ( 'with_embeddings.csv', '.'), ( 'output.txt', '.'), ( 'which.txt', '.'), ( 'chatwith.txt', '.'), ( 'temperature.txt', '.'), ( 'maxtokens.txt', '.'), ( 'todeletemidindex.txt', '.'), ('/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/jieba', 'jieba')],
    hiddenimports=['subprocess'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Banana',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Banana',
)
app = BUNDLE(
    coll,
    name='Banana.app',
    icon='banana_desk.icns',
    info_plist=info_plist,
    bundle_identifier=None,
    version=__version__,
)
