**Telegram Container(TGC)** - is a simple program to store Telegram accounts. This is useful in case when need to hide Telegram accounts: just login into this program, then archive the files and hide it(for example send it to self on mail)

# Installation(in Termux)

To install requirements execute:
```
pkg update
pkg install python openssl
pip install telethon
```

Now download ```main.py``` and copy it in Termux storage. Then just run program by ```python main.py```.

Also you can archive it by command ```tar czf tgc.tar.gz main.py *.session```, and unpack by ```tar xf tgc.tar.gz```
