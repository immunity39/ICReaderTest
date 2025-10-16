import nfc

def on_connect(tag):
    print("カードが検出されました。")
    print(f"カードタイプ: {tag.type}")
    # 個人情報（IDmなど）を出さずに長さだけ確認
    idm_length = len(getattr(tag, 'identifier', b'')) if hasattr(tag, 'identifier') else 0
    print(f"IDm長さ: {idm_length} bytes")
    return True  # 1枚目で終了

clf = nfc.ContactlessFrontend('usb')
print("カードをかざしてください...")
clf.connect(rdwr={'on-connect': on_connect})
clf.close()
