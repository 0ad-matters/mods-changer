# mods-changer
changing your mod profiles fast. AutoKey script tested in (k)ubuntu

# how to change config

open folowing files:
- `0ad_mods_changer.py`
check user.cfg path is correct :
```python
    userCfg = "~/snap/0ad/current/.config/0ad/config/user.cfg"
```

- (optional) `user.cfg`  file, that sometimes localted here: `~/snap/0ad/current/.config/0ad/config/user.cfg`
and get the entries behind `enabledmods` in your `user.cfg`

add your wanted mods behind 

plus += "..."

like

`plus += "myMod1  myMod2 myMod3 myMod4"`

save it start it

# tested with

[autokey](https://github.com/autokey/autokey) script tested in 

```
Operating System: Kubuntu 20.04
KDE Plasma Version: 5.18.8
```
