---
title: "Zapiski o LINUX sistemu in se kaj drugega"
author: [David Rihtaršič]
date: 2017 02 20
tags: [Markdown, Example]
bibliography: bibtex.bib
listings: true
template: eisvogel
---

\newpage
\tableofcontents
\newpage

# ANDROID:
## ADB

$$a=\frac {2}{3}$$

na tem mestu bomo zapisali nekaj programov za android program na telefonu. glavno program je
__adb__ ( __a__ ndroid __d__ e __b__ ugger)... to omogoča, da priključimo telefon ns računalnik in se nanj
povežemo tako, da delamo na terminalu...

= android deBugger... da se lahko z računalnikom povežeš na tel...
in od tam urejaš linux (android)

## BUSYBOX (nujno 4 me:)

splača se inštalirat ta program, ker omogoča razširjen nabor Linux ukaov
kot so npr: cp, crond, vi (Editor) ...

## CROND

1. busybox
2. su
2. mount  o remount,rw /
3. mkdir bin
4. ln  s /system/bin/sh /bin/sh
5. crond  c /data/crontab

# ARDUINO:
## Enable PORT permmissions to user

    sudo usermod  a  G dialout terrik

and Log Out / Log In

# ARCH:

## Maintainence (vzdrževanje)
[youtube vidoe](https://www.youtube.com/watch?v=3OoMvyHYWDY)

## Backup

		sudo rsync -aAXv --dry-run --exclude='*_noSync*' --exclude='*Work*' ~/Files/ /run/media/david/BackupDisk/FilesBACKUP/

### disk
		ncdu (disk pregled velikosti datotek)

## Programi
skripta...

# AUTOSTART
to do...

# BACKLIGHT
Včasih je težko krmiliti osvetlitev najlažje je, če dela
xbacklight  set 10

če ne:
osvetljenost je krmiljena v datoteki:

		/sys/class/backlight/.../brightness

in v to datoteko zapišeš številko...

		tee brightness <<<100

Moral sem spremeniti tudi dovoljenja, saj je po defaultu omogočeno le root u. Zato v:

    sudo vim /etc/udev/rules.d/basklight.rules

dodaš:

    ACTION=="add", SUBSYSTEM=="backlight", KERNEL=="intel_backlight", RUN+="/bin/chgrp video /sys/class/backlight/%k/brightness"
    ACTION=="add", SUBSYSTEM=="backlight", KERNEL=="intel_backlight", RUN+="/bin/chmod   g+w /sys/class/backlight/%k/brightness"

## keyboard backlight (podobno kot za lcd backlight)

### Dolphine
search ne dela...
zato sem naložil še FSearch...
naloži še Konsol )terminal

# BLUETOOTH

> Zaenkrat dela najbolje tako, da na samem začetku zaženeš

	Bluetooth Manager

>bluetoothctl
>scan
>trust
>pair

## povezava
v terminau zaženeš:

>bluetoothctl
    bluetooth]# show
    Controller 74:E5:F9:19:10:2B (public)
      Name: archlabs
      Alias: archlabs
      Class: 0x001e010c
      Powered: yes
      Discoverable: no
      Pairable: yes
      UUID: Headset AG                (00001112 0000 1000 8000 00805f9b34fb)
      UUID: Generic Attribute Profile (00001801 0000 1000 8000 00805f9b34fb)
      UUID: A/V Remote Control        (0000110e 0000 1000 8000 00805f9b34fb)
      UUID: OBEX File Transfer        (00001106 0000 1000 8000 00805f9b34fb)
      UUID: Generic Access Profile    (00001800 0000 1000 8000 00805f9b34fb)
      UUID: OBEX Object Push          (00001105 0000 1000 8000 00805f9b34fb)
      UUID: PnP Information           (00001200 0000 1000 8000 00805f9b34fb)
      UUID: A/V Remote Control Target (0000110c 0000 1000 8000 00805f9b34fb)
      UUID: IrMC Sync                 (00001104 0000 1000 8000 00805f9b34fb)
      UUID: Audio Source              (0000110a 0000 1000 8000 00805f9b34fb)
      UUID: Audio Sink                (0000110b 0000 1000 8000 00805f9b34fb)
      UUID: Vendor specific           (00005005 0000 1000 8000 0002ee000001)
      UUID: NAP                       (00001116 0000 1000 8000 00805f9b34fb)
      UUID: Message Notification Se.. (00001133 0000 1000 8000 00805f9b34fb)
      UUID: Phonebook Access Server   (0000112f 0000 1000 8000 00805f9b34fb)
      UUID: Message Access Server     (00001132 0000 1000 8000 00805f9b34fb)
      UUID: Headset                   (00001108 0000 1000 8000 00805f9b34fb)
      Modalias: usb:v1D6Bp0246d0532
      Discovering: no

... kot kaže ne išče BT naprav
>[bluetooth]# scan on
    Discovery started
    [CHG] Controller 74:E5:F9:19:10:2B Discovering: yes

    [NEW] Device 13:31:19:07:15:8C Bluetooth Mouse

ga označiš kot "trusted" in "pair" aš
>bluetooth]# trust 13:31:19:07:15:8C
    [CHG] Device 13:31:19:07:15:8C Trusted: yes
    Changing 13:31:19:07:15:8C trust succeeded
>[bluetooth]# pair 13:31:19:07:15:8C
    Attempting to pair with 13:31:19:07:15:8C
    [CHG] Device 13:31:19:07:15:8C Connected: yes
    [CHG] Device 13:31:19:07:15:8C Modalias: usb:v05ACp3232d0001
    [CHG] Device 13:31:19:07:15:8C UUIDs: 00001124 0000 1000 8000 00805f9b34fb
    [CHG] Device 13:31:19:07:15:8C UUIDs: 00001200 0000 1000 8000 00805f9b34fb
    [CHG] Device 13:31:19:07:15:8C ServicesResolved: yes
    [CHG] Device 13:31:19:07:15:8C Paired: yes
    Pairing successful



# DD_IBS_TEST.SH():
## test
program za testiranje dd komnade...
kako hitro comp lahko kopira datoteke v odvisnosti ob bs= ? podatka...
Program je na [GitHubu](https://github.com/tdg5/blog/blob/master/_includes/scripts/dd_ibs_test.sh)

# C++:
## PassBy VALUE REFERENCE POINTER

Pomembno pri funkcijah, naprimer:
void passByVal(int val);
void passByRef(int &ref);
void passByPtr(int *ptr);

### Value
  int x = 5;

naredi kopijo spremenljivke v stacku

[ ] več spomina

[+] vrednost prvotne spremenljivke se ne spremeni

### Reference
int &ref = x
to je alias spremenljivke x
[+] ne zasede novega spomina
[+] če potrebuješ, da funkcija vrne več parametrov in NI potrebno imeti globalne spremenljivke. Vrednost spremenljivke  se lahko spremeni med samo funkcijo

### Pionter
int *xptr = &x;
xptr je naslov spremenljivke x, če želimo vrednost na tem naslovu = *xptr
  nekoliko bolj zakomplicirana sintaksa, ker je prej potrebno v *xptr dati naslov spremenljivke
+ le s pointerji lahko dostopamo do __HEAP__ spomina (spomin večjih razsežnosti)

# CATFISH:
## namestitev
Odličen iskalnik filov...
po defaultu naložen.. hm ne vem od kdaj...
v Thunar sem imel po defaultu Commnad:

    catfish   fileman=bl file manager   hidden   path=%f

:) aha ... sem spremenil v :

    catfish   path=%f

in dela :)
glej gmone search tool

# CHARACTER MAP:
## pregled znakov
Super programček za brskanje znakov

    gucharmap
Če uporabimo font "common" je tam veliko primernih znakov kot naprimer:

# CONFIG FILES (my)
## My all . dotfiles

		find .  type f
./.zshrc
./.config/polybar/modules.conf
./.config/polybar/config
./.config/polybar/lounch_polybar.sh
./.config/polybar/master.conf
./.config/terminator/config
./.config/tint2/tint2rc
./.config/openbox/rc.xml
./.config/i3/LcdBrightnesUP.sh
./.config/i3/KbdBrightnesUP.sh
./.config/i3/myMonitorSetup.sh
./.config/i3/config
./.config/i3/LcdBrightnesDOWN.sh
./.config/i3/KbdBrightnesDOWN.sh
./.config/i3/lcd_backlight.rules
./.config/i3/kbd_backlight.rules
./.config/conky/dave_s_conky.conkyrc
./.config/termite/config
./.config/termite/config (copy_original)
./.local/share/nemo/actions/PDF_extract.nemo_action
./.local/share/nemo/actions/PDF_unite.nemo_action
./.local/share/nemo/actions/Office  >PDF.nemo_action
./.local/share/nemo/actions/MD  >PDF.nemo_action
./.local/share/nemo/actions/MD  >PDF_bib.nemo_action
./.vimrc
./.pandoc/templates/eisvogel.latex



# DOLPHINE FILE MANAGER
## KDE SERVICES
(ni blo dobr!!)
For Arch Linux, edit /etc/pacman.conf and add the following (note that the order of repositories in pacman.conf is important, since pacman always downloads the first found package):

    [home_metakcahura_Arch_Extra]
    SigLevel = Never
    Server = https://download.opensuse.org/repositories/home:/metakcahura/Arch_Extra/$arch

Then run the following as root

    pacman  Syu
    pacman  S home_metakcahura_Arch_Extra/kde services

### instalation
libkonq frameworks git
iz [link](http://download.opensuse.org/pub/opensuse/repositories/home:/mazdlc:/kde frameworks 5/Arch_Extra/x86_64/)
Dela !!!
nato še run

    kbuildsycoca5

datoteke pa so shranjene v:
/usr/share/kservices5/ServiceMenus

# ECLIPSE:
## installation
  ... nisem zapisal...
  ... presnameš, odpakiraš kopiraš v:
  /opt/eclipse/
  narediš link za vse uporabnike:
sudo ln  sf /opt/eclipse/cpp neon/eclipse/eclipse /usr/bin/eclipse

## eclipse.desktop:
Naredimo datoteko.desktop:
 sudo nano /usr/share/applications/eclipse.desktop

    [Desktop Entry]
    Version = Neon 2.0
    Type = Application
    Terminal = false
    Name = eclipse
    Exec = /usr/bin/eclipse
    Icon = /opt/eclipse/cpp neon/eclipse/icon.xpm
    Categories = Development;

## Arduino ECLIPSE Plugin
[link](http://eclipse.baeyens.it/)
__Instalation__

1. run eclipse c++ with "sudo"
2. Help  >eclipse marketplace
4.  [x] Solber Arduino IDE
5. next   >  "i agree"   > Finish...


# EFI MODE:
## test
boot  > CSM enable
security  > security boot control  > dissable

## installBUNSEN
 instaliral ...
 grub dal na sda1 (kjer sem našel efi... [sudo parted  l])
 kar nekaj sem probal... ni delalo   sedaj pišem kaj ne dela

 BIOS:
 new boot oprions:
 /efi/boot/bootx64.efi
 ne dela

 Test x n
 probaj ta navodila:
 http://sarah.thesharps.us/2014/12/31/installing debian on asus ux301la/

 install
 grub  > /dev/sda1
 takoj ne dela... zažene se win10...
 path :/EFI/debian/grubx64.efi [ne dela]
 path :/efi/boot/bootx64.efi [ne dela]

# EMOJI
da kaže vse emoji-je moraš inštalirat:
> yaourt yaourt ttf-emojione

in mogoče tudi:
> yaourt ttf-symbola

in nato lahko vsatvljaš znake:

✅

# FEH
program s katerim lahko nastaviš background sliko.. naprimer takol:

    feh   bg scale Leopard Wallpapers HD Free Download.jpg

# FZF:
[link](https://github.com/junegunn/fzf)
## uporaba
Fust FuzZy File Search ...
Res dober način zaiskanje filov... dve bljižnjici:
  Ctrl+r => iskanje po zadnjih cmd jih
  Ctrl+t => iskanje po filih naprej po foldru
  Tab => označi več filov..

# FILEMANAGERs:
## Thuar
Všeč mi je filemanager THUNAR:

    sudo apt get install thunar

## Nemo
### Samba support
samba mi ni delala naložil sem še:

		pacman  S gvfs smb

nato je delalo...

to je to !!! v Nemotu v zgornjo vrstico vpišeš:

		smb://192.168.1.3/

in si not...

narejene so tudi skripte za ...

### shortcuts:
*   expand all subfolders :)

# FILES STRUCTURE
## moja struktura
Mogoče da si narediš template za folders
Tu bi napisal kako bom uredil file
  Files
  + To Do(links)
  + Work
    * PeF
        Vaje
        + Modelarstvo
        + Promet
        Habilitacija
        Diplome
        Članki
        Predstavitve
    * DRTI
        Poletne Šole
        Finance

    *
  + Hobi
    * Linux
        BunsenLab
        RPi
    * Dom
    * Kolesarjenje
  + Musics
  + GitHub
## Folder structure <template>
  recimo za project
## Programs category
  1. System
  2. Development
  3. Multimedia
  4. Office
  5. Graphics
  6. Internet
  7. Accesories
  8. Other

# FORMAT SD
## ukazi
First, you have to find out which device (/dev/sd??) your USB stick is. Therefore look at the output of
>sudo fdisk  l

Jaz raje uporabim:
>lsblk

    NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda      8:0    0 465.8G  0 disk
    + sda1   8:1    0   300M  0 part /boot/efi
    + sda2   8:2    0   600M  0 part
    + sda3   8:3    0   128M  0 part
    + sda4   8:4    0 185.5G  0 part
    + sda5   8:5    0 271.3G  0 part /
    + sda6   8:6    0   7.9G  0 part [SWAP]

Lepo se vidijo diski in kje so mountirani. Po potrebi ga lahko od mountiraš..
After that unmount the device/partition (if necessary) by running

    sudo umount /dev/sdb

Make sure you replaced ?? with the correct device/partition name from the previous output.
To format The partition as FAT32 use
> sudo mkdosfs  F 32  I /dev/sdb

# FRITZING


# FREECAD

zadjo verzijo dobiš na https://www.freecadweb.org/wiki/Download

Macroti mi niso delali, zato sem inštaliral:

- qt5-default
- qt5creator


# GIMP
  asdf
# GITHUB
## LITERATURA:
  1. [Link](https://www.youtube.com/watch?v=1h9_cB9mPT8)

## install:
Debian le

    sudo apt get install git

## config:
    git config   global user.name "davidrihtarsic"
    git config   global user.email "david.rihtarsic@gmail.com"
    git config   global core.editor="subl"

## general_use:
make new repository ... BlaBla_project (need to be on URL gitHub)
make dir on your computer for that project
navigate to that dir

    git init

### editing:
na tem mestu spreminjaš FAJL...

    git add .
    git commit  m "comment"
    git commit  a  m "comment"
    git status
    git diff

### uploading:
kako da stvar na GitHub...
v spremenljivko "origin" spravimo URL projekta

    git remote add origin https://github.com/davidrihtarsic/myZapiski.git
    git push ~~origin master~~

### updating:
naprimer, da nekdo popravi kodo (recimo ti sam na GitHubu...
in nekdo tudi na compu ter naredi commit)

    git commit  a  m "comment"

hočeš naložit... novo verzijo in dobiš konflikt s tisto na GitHub u

    git push origin master

    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast forwards' in 'git push   help' for details.

potem naredis :

    git pull

in če je bil dokument spremenjen na ISTEM mestu (recimo v isti crstici)
potem je to v dokumentu označeno z:

      <<<<<<< HEAD
          #to je novo na compu
      =======
          #to je novo na GitHubu
          #heh nisem si zapisoval
      >>>>>>> 14d185fbd48d55e9a37d7de3e4d9bde157aa8915

če pa je na različnih mestih pa dokument združi preko:

   "recursive strategy"...

in je to   to :)
skratka popraviš in uploadaš še enkrat :) jeah!

# GRAPHIC CARD:
## driverji
Kako preveriti in namestiti driverje za grafično kartico
## GeForce 9600 GT
Jaz imam na PCju to kartico to lahko preveriš s:
  > 'lspci'

V terminalu se ti izpiše nekaj takega:

    05:00.0 VGA compatible controller: NVIDIA Corporation G94 [GeForce 9600 GT] (rev a1)

Nato greš na tole stran:
  [GeForce Drivers](http://www.geforce.com/drivers)
1. vtipkaš podatke
2. Download
3. CTRL+ALT+F1
4. user:
5. password:

    sudo service lightdm stop

# HIBERNATION (arch)
Kako nastaviš da imaš hibernacijo računaljika...
  potrebuješ dovolj swap particije
  nasraviš resume
  dodaš v grub pod HOOK tudi resume
  zbildaš grub
__ni delalo!!!!!!__ nato je začelo delati... samo ne vem kdaj in kaj sem še naredil... večinoma sem se ukvarjal s pandocom... ampak to nima veze...
[link](https://www.youtube.com/watch?v=GF13ZpYsrI0)
(to do)

# i3 WORKSPACE MANAGER
## nastavitve
[arch i3 navodila](https://wiki.archlinux.org/index.php/I3#Launching_programs_on_specific_workspaces)

## moje bližnjice

1. _Mod_  > za okna/programe
  1. +Left/Right  > focus left/right
  2. +Shift+1/2/3  > premakni program na workspace 1/2/3
2. _Mod+Control_  > za workspace
  1. +Left/Right  > premakni WS na drug zaslon
  2. +r  > RESTART WORKSPACE
  3. +l  > reLoad i3 config
  4. +v/h  > naslednji program naj se doda Vertikalno/Horizontalno
3. _Alt_  > za funkcije v programu
  1. +Left/Right  > resize left/right
  2. +1/2/3/4  > tab focus
  3. +F/E/H  > menu File/Edit/Help

## uporaba

list vseh oken:

		wmctrl -l

narediš fokus na okno z imenom:

		wmctrl -a VIM1


# ISO BURN TO USB
## terminal cmd
		sudo dd bs=4M if=*.iso of=/dev/sdb status=progress && sync

## More advanced copy with progress

Inštaliran mora biti pv

    sudo apt get install pv

Ker pv (pipe Viever) dela več različnih stvari in ne le dd,
med drugim tudi progress bar... je ukaz potrebno izvesti v sudo načinu:

    sudo  s
    pv <NekIsoFile.iso> /dev/sdb
    857MiB 0:01:05 [13.1MiB/s] [==============================>] 100%
    exit

# JAVA in FIREFOX BROWSER

1. naložiš javo JRE...
2. mkdir ~/.mozilla/plugins
3. cd ~/.mozilla/plugins
4. ln  s /usr/lib/jvm/jre1.8.0_121/lib/amd64/libnpjp2.so
          [tu pride java direktorij kjer je libnpjp2.so]
5. restart FireFox
6. v FF vpišeš about:plugins in preveriš če je java podprta...

# KEYBOARD SETTINFS:
  Settings  > Reigon&Language  > Input Source
  for KeyBindings:

  # Settings for ARCH

    sudo nano /etc/X11/xorg.conf.d/01.keyboard layout.conf

    Section "InputClass"
        Identifier "system keyboard"
        MatchIsKeyboard "on"
        Option "XkbLayout" "si"
    EndSection

## ShortCuts():
v settings>Keyboaard sem si nastavil nekaj bližnjic:
   > super+w > Firefox
   > super+e > Text Editor
   > super+f > File Manager
   > super+t > terminator

  v ~/.bashrc (file se zazene na zacetku)
   > bliznica ll namesto ...
   > alias ll='ls  alF'
   > tipki [đ] dodelimo znak [/]
   > xmodmap  e "keycode 35 = slash"

# LAZARUS
Programing program in pascal... As Delphi

## instalation
instaliral tako kot je opisano na [internetu](https://forum.lazarus.freepascal.org/index.php?topic=36093.0):
1. Install fpc_3.0.2 170225_amd64.deb via package manager
2. Install fpc_3.0.2.x86_64 linux.tar via shell (unzip and run sh install.sh). Install into /usr directory, so it overwrites 3. the existing installation
4. Install the deb sources via package manager (__tega nisem naredu... neznam__)
5. Install lazarus project_1.6.4 0_amd64.deb via package manager
6. Instaliral gdb

# LIBREOFFICE:
Instal preko terminala:

    apt get install libreoffice

## WRITER
### How to Change ICONS
1. run libreoffice
2. Tools -> Options
3. View
4. Icon style ...

__Short Cuts__

| Short cut      | Action              |
|                |                     |
| [Ctrl] + [Ent] | Insert Break Page   |
| []+[]          | Insert greek letter |

## CALC
### How To   Insert DATE:

1. Tools  > Customize  > Keyboard  >
2. Short Keys :Ctrl+.
3. Category: Insert
4. Function: Insert Current Ddate
5. [Modify]

### How To   Insert TIME:

1. Tools  > Customize  > Keyboard  >
2. Short Keys :Ctrl+Shift.
3. Category: Insert
4. Function: Insert Current Time
5. [Modify]

### __Short Cuts__

| Short cut     | Action              |
|               |                     |
| [Ct]+[.]      | Insert Date         |
| [Ct]+[Sh]+[.] | Insert Time         |

### How to   Filter duplicated

Ko imamo tabelo:

|  ime  | vpisna |  smer |
|       |        |       |
| DAvid | 123456 | Fi Te |
| DAvid | 123456 | Fi Te |
| Mija  | 345678 | Ma Te |
| Jure  | 098765 | Fi Ma |

1. vklnjučiš filter
2. nato greš v meni [ime v]
      Standard Filter
      ime = NotEmpty
      > Options : No Duplicates
[ok]

# Simon Sinek

## Presentation
[Presentation as Simon Sink would do...](https://www.youtube.com/watch?v=e80BbX05D7Y)

What do we want to do to have good presentation...

1. Start with the story - kot neka metafora, kar jim hočeš povedati...
2. spirit of giving - publiki moraš nekaj dat (idejo, nekaj open source,) za kar ne rabiš nič v zameno)
3. ne govori o sebi
4. ne začni s podatki... zakaj je to pomembno - To pride na koncu in mora biti del sestavljanke...


# Linus Torvalds
1. get the work done
2. do not let go
3. have passion
4. start small
5. learn trough trail & error
6. embrase your uniqnes
7. find your motivation
8. be brutally honest
9. create for yourself
10. optimize your working environment

# MARKDOWN
## Uporaba:
> Takole s ">" je označen tekst, ki je nokako označen kot _citat_.
> Lahko pa ga tudi citiramo[^1]

[^1]: In tu je tudi sprotna opomba.
Potem nekaj navadnega texta...

    z dvema TAB oma je ločena
    vsaka vrstica kode. V Sublimu je pobarvana
    vijolično v pdf ju pa je v okvirčku
    z ostevilčinimi vrsticami..

<!   Menda naj bi bil tole komentar   >

Če poznamo kodo jo lahko poumenujemo:
Naprimer: c++ in Python

```c
#!/usr/bin/env python
from Arduino import Arduino
import time

# setup an Arduino board object
ArduinoNano = Arduino()

# set pin 13 as OUTPUT
ArduinoNano.pinMode(13,'OUTPUT')

for x in range(1,5):
  ArduinoNano.digitalWrite(13,'HIGH')
  time.sleep(1)
  ArduinoNano.digitalWrite(13,'LOW')
  time.sleep(1)
```

```c
int test = 0;
void loop(){
  digitalWrite(led_pin, HIGH);
}
```
in Python

```python
s = "Python syntax highlighting"
print s
```

1. nastevanje
2. nastevanje..
    nast
    nast
  * nato pa se
  * nato tudi to
    + lahko pa tudi
    + ali a

_podčtrano_

~~prečrtano~~ bom uporabljal tam kjer sem nekaj probal pa ni delovalo

[link](http://google.com)

## Live preview
Instalation

    pacman  S npm
    sudo npm install  g markmon

SublimeText3  > Package Controll  > Install Package : Markmon

### run
Ctrl+Shift+p   > Markmon launch

## Metadata

```yaml
title: "Using Arduino based low cost DAQ in science teacher training"
subtitle: "Sub Title"
author: "David Rihtaršič\\\nUniversity of Ljubljana"
date: "2018 07 12"
# more fonts in: /usr/share/texmf dist/fonts/opentype
# more fonts in: /usr/share/texmf dist/fonts/truetype
mainfont: FiraSans Regular.otf
mainfontoptions: BoldFont=Font Bold.otf
mainfontoptions: ItalicFont=Font Italic.otf
mainfontoptions: BoldItalicFont=Font BoldItalic.otf
fontsize: 10pt
geometry: "top=0.9cm, bottom=1.5cm, left=2.0cm, right=2.0cm"
header includes:
      \usepackage{setspace}
      \singlespacing          #doublespacing
      \usepackage{lineno}
      \linenumbers
numbersections: false
classoption: onecolumn
documentclass: article    # [article, book, report]
csl: ieee.csl #/home/david/.pandoc/templates/ieee.csl
bibliography: [
  /home/david/Files/Work/PeF/Articles/bibtex_global.bib,
  bibtex.bib
]
lang: en US         # [sl, en US, us GB]
```

## LaTex Commnads

Deluje tudi če napišemo naslednje LaTex ukaze:

    \tableofcontent
    \newpage

## Enačbe
Enačbe lahko pišemo zelo enostavno, tako da celotno enačbo zaviješ v dva dolarja.
$$ y = mx +b $$
$$ \int_a^b x^2dx $$
$$ y(x)=2x_a^2+1 $$
$$ \frac{\frac{1}{x}+\frac{1}{y}}{y z} $$

Več o tem kako se pišejo enačbe lahko preberemo na tej strani:
[https://en.wikibooks.org/wiki/LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics).

## References (citiranje)
V metadata poleg title, author vpšemo tudi **bibliography:** in dodamo še ime datoteke z BibTex datoteko referenc...
in nato tu citiramo v besedilu naprimer @Rihti2015.

Da tako oblikovano md datoteko spravimo v pdf pa vpšemo naslednji ukaz:

    pandoc  o test.pdf   from markdown   template eisvogel   listings   pdf engine=xelatex myLinuxNotes.md   filter pandoc citeproc

in to je to.

### Možnosti citiranja
Poskusimo še tri načine citiranja. Če želimo citirati tako kot to počnemo običajno na koncu neke smiselne povedi to naredimo tako da v oglate oklepaje napišemo ime reference. Naprimer citat se izpiše takole**[@Rihti2015]** v besedilo pa ga vnesemo takole:

    [@Rihti2015]

Če pa želimo citirati tako, da se v besedilu navezujemo na avtorje, naprimer da nekateri avtorji kot **@Rihti2015** svetujejo to in ono... pa naredimo le takole:

    @Rihti2015

Poleg teh dveh citiranj lahko citiramo tudi brez priimkov avtorjev naprimer tam, kjer jih moramo sklanjati ali kako drugače opredeliti, da so prav ti omenjeni avtorji sodelovali dlje časa z Rihtaršičem ** @Rihti2015**. To pa naredimo takole:

     @Rihti2015

### DOI to BibTex
Ko iščemo vire imamo pogosto možnost oznake DOI (angl.: **D**igital **O**bject **I**dentyfier). Če želimo iz te oznake še ostale podatke o viru jih lahko dobimo preko te strani: [https://www.doi2bib.org/ ](https://www.doi2bib.org/). Tako podatke lahko shranimo v orimerno oblikovano besedilo, da ga lahko uporabimo v zgornji funkcionalnosti.

    @article{Rihti2015,
      doi = {10.1007/s10798 015 9310 7},
      url = {https://doi.org/10.1007/s10798 015 9310 7},
      year  = {2015},
      month = {may},
      publisher = {Springer Nature},
      volume = {26},
      number = {2},
      pages = {205  224},
      author = {David Rihtar{\v{s}}i{\v{c}} and Stanislav Avsec and Slavko Kocijancic},
      title = {Experiential learning of electronics subject matter in middle school robotics courses},
      journal = {International Journal of Technology and Design Education}
    }


# MERGE PDF DOCUMENTS

Če moramo združiti več pdf dokumentov v enega v terminal napišemo:
> pdfunite pdf0.pdf pdf1.pdf merged.pdf

# MERMAID (izgradnja diagramov iz kode v markdownu)

inštaliral sem:

		yaourt -S nodejs-mermaid-git
		npm install mermaid.cli

mermaid.cli sem moral inštalirat lokalno (dir je v ~ direktoriju), ker sem z globalno inštalacijo imel težave...
Narediti sem moral tudi config file:

		puppeteer-config.json

z vsebino:

		{
  		"args": ["--no-sandbox"]
		}

in nato izvesti ukaz:
> ~/node_modules/.bin/mmdc -p ~/node_modules/.bin/puppeteer-config.json -i b70fcd12274a43de8c625dfa9fbed6c8e73a21bf.mmd -o test.svg

datoteko b70fcd12274a43de8c625dfa9fbed6c8e73a21bf.mmd sem dobil z ukazom:
> pandoc mermaid.md -o test.pdf --filter pandoc-mermaid

... zgleda, da sem inštaliral tudi:
> pip install pandoc-mermaid-filter

...nato sem v filu:

		/home/david/node_modules/mermaid.cli/index.bundle.js

spremenil tako, da mi avtomatsko vzame file puppeteer-config.json


	let puppeteerConfig = {};
	puppeteerConfigFile = '/home/david/node_modules/mermaid.cli/puppeteer-config.json';
	if (puppeteerConfigFile) {
  	checkConfigFile(puppeteerConfigFile);
  	puppeteerConfig = JSON.parse(fs.readFileSync(puppeteerConfigFile, 'utf-8'));
	}

nato sem še nastavil env variable:

> export PUPPETEER_CFG=/home/david/node_modules/mermaid.cli/puppeteer-config.json
> export MERMAID_BIN=~/node_modules/.bin/mmdc

(ampak puppetirja nikakor nisem usposobil)

## popravek....

verjetno bi šlo, če inštaliraš:
- mermaid.cli iz githuba
- pandoc-mermaid-filter
- in narediš link iz /bin/mermade --> /home/david/node_modules/mermaid.cli/index.bundle.js
		
		sudo ln -s /home/david/node_modules/mermaid.cli/index.bundle.js /bin/mermade

# MUSIC TAGGING (audi tags)

V terminalu lahko uporabljalmo: _beets_:

    beet import ~/Music/BigFoodMama/

in nato beet poišče v bazah iz spleta kateri album, izvajalec naslov pesmi...

# NEMO
File browser

## Script
You can add yours scripts... Script must be added to:

    ~/.local/share/nemo/actions

**Script example:**



## Shortcuts
| Key combo | Action          |
|           |                 |
| A+Home    | go to HOME dir  |


# PACMAN
Program za pakete = PACkage MANager. Ena varianta je, da uporabiš:
PACLI programček v terminalu...

### pacman  S paket
> namesti paket

## ERRORS
failed to...
> odstraniš paket, ki ti ga javi in probaš še enkrat...


# PASSWORD (LINUX)

To change a password on behalf of a user, first sign on or "su" to the "root" account. Then type:
(where user is the username for the password you are changing).
> passwd user

The system will prompt you to enter a password. Passwords do not echo to the screen when you enter them.
You can also change your own password, by typing:
(without specifying a username).
> passwd

You will be prompted to enter your old password for verification, and then a new password.
# PDF MERGE/SPLIT
pdfunite source1.pdf source2.pdf out.pdf

pdftk source.pbf burst
pdftk source.pbf 4 just 4th page.pdf

# PATCH

Za naredit patch uporabiš:

> diff  u standard.file my new.file > patch.diff

Za izvršit patch na stari datoteki pa narediš:

> patch < patch.diff

# PIDGIN
## HANGOUTS
https://bitbucket.org/EionRobb/purple hangouts/
> sudo apt get install  y libpurple dev libjson glib dev libglib2.0 dev libprotobuf c dev protobuf c compiler mercurial make;
> hg clone https://bitbucket.org/EionRobb/purple hangouts/ && cd purple hangouts;
> make && sudo make install

Po tem greš na tole spletno stran:
https://accounts.google.com/ServiceLogin?passive=1&continue=https://accounts.google.com/o/oauth2/programmatic_auth?hl%3Den%26scope%3Dhttps://www.google.com/accounts/OAuthLogin%2Bhttps://www.googleapis.com/auth/userinfo.email%26client_id%3D936475272427.apps.googleusercontent.com%26access_type%3Doffline%26delegated_client_id%3D183697946088 m3jnlsqshjhh5lbvg05k46q1k4qqtrgn.apps.googleusercontent.com%26top_level_cookie%3D1%26from_login%3D1%26as%3D158e30052a6d899&ltmpl=nosignup&hl=en&oauth=1&sarp=1&scc=1&authuser=0

ko sem naredil tole, je delal tudi skype plugin...

## Skype
https://github.com/EionRobb/skype4pidgin
> cd skype...
> make
> sudo make install

## GoogleTalks
My account  > Prijava in varnost  > Gesla za aplikacije  > ime aplikacije : PIDGIN [ustvari]
 > qwer tzui opšd asdf

basic

Protocol:XMPP
user:david.rihtarsic
domain:gmail.com
Resource:Home
pass: qwer tzui opšd asdf
[x] remember pass
[x] new mail...

advanced

Connect server: talk.google.com
## WhatsApp
debhelper (>= 7.0.50), libglib2.0 dev, libpurple dev, libfreeimage dev (>= 3.0.0), libprotobuf dev, protobuf compiler
make ARCH=x86_64

sudo apt get install protobuf compiler
get :https://github.com/davidgfnet/whatsapp purple/
cd  > whatsapp purple
make

# POPCORN TIME


# POWERTOP
Program za zmanjševanje porabe el. energije laptopa...

## Running

    sudo powertop   auto tune

# PRELOAD (deamon service)
preload is a program written by Behdad Esfahbod which runs as a daemon and records statistics about usage of programs using Markov chains; files of more frequently used programs are, during a computer's spare time, loaded into memory. This results in faster startup times as less data needs to be fetched from disk.

## Running

    __systemctl start preload.service__
    systemctl enable preload.service


## Config

    /etc/preload.conf

# PPRINTER SUPPORT on BunsenLab

sledil sem tocno tem [navodilom](http://hplipopensource.com/hplip web/install/manual/distros/debian.html)
  prej moraš vedeti tudi root geslo

Program za gledanje filmov:
1. Download [Popcorn Time](https://www.popcorntime.ws/about)
2. razpakiraš in daš dokumente v /opt/popcorn time/
3. polinkaš, da bo dosegljivo vsem:
sudo ln  sf /opt/popcorn time/Popcorn Time /usr/bin/popcorn time
4. Narediš še .desktop datoteko
sudo nano /usr/share/applications/popcorntime.desktop
5. in vot vpišeš:

    [Desktop Entry]
    Version = 1.0
    Type = Application
    Terminal = false
    Name = Popcorn Time
    Exec = /usr/bin/popcorn time
    Icon = /opt/popcorn time/src/app/images/icon.png
    Categories = Application;

# PRINTSCREEN = DARK

## printscreen

Uporabiš program:

		scrot -s

- in klikneš na program ki ga želiš dat v sliko
- in slika se shrani v directory, v katerm si.


# QCAD

  1. presnameš inštalacijo iz njihove [strani][https://qcad.org/en/qcad downloads trial]
  2. nato spremeniš rivilegije datoteke:
  > sudo chmod 777 qcad*.run
  3. in poženeš script:
  > ./qcad*.run

# Qt5
Ostale mislim, da sem imel...
Za nekateri program sem si moral nainštalirat Qt5 knjižnice:
1. Manjkala mi je Qt5LinguistToolsConfig

## Instalacija Qt5LinguistToolsConfig
Mislim, da mi jo je uspelo naložit z:
> sudo apt get install qttools5 dev

nato sem datoteko našel:
> sudo find /usr/lib/*  name Qt5Lin*

nato je manjkal še Qt5Quck
instaliral sem ga z
> sudo apt get install qtdeclarative5 dev

nato je manjkal Qt5SvgConfig, instaliral z:
> sudo apt get install libqt5svg5 dev
> sudo apt get install libraw dev
  sudo apt get install exiv2 (najverjetneje ni bil taprav paket!!!)
> sudo apt get install libexiv2 dev
> sudo apt get install graphicsmagick

še vedno ni delalo
nato sem inštaliral qt5 creator... (neumnost, ker je to cel program za programiranje)
> sudo apt get install qtcreator

še ni pomagalo:
sudo apt get install qml module qtgraphicaleffects
sudo apt get install qml module qtquick dialogs
sudo apt get install pyqt5 dev
sudo apt get install qtdeclarative5 models plugin

# RANGER
pomembni datoteki sta :

- .config/i3/config
- .config/i3/rifle

## rifle
nastavitve za odpiranje programov...

## fzf

Glej navodila:

https://github.com/gotbletu/shownotes/blob/master/ranger_file_locate_fzf.md

## Issues...
z Ranger-jem, ki je v AUR sem imel težave, da se je sesul, ko sem pregledoval cvs... neki error "null character"

Issue je odpravljen... instaliraš ranger iz githuba...


# SCAN
simple scan

v terminalu pa lahko :
inštaliraš SANE


# SOUNDON:
 Na začetku mi ni delal zvok... Rešitev je bila:
 1. lspci:
  tako preveriš, če je Linux prepoznal zvočno...
  na terminalu sem dobil:

      '00:1b.0 Audio device: Intel Corporation 7 Series/C210 Series Chipset Family High #inition Audio Controller (rev 04)'

 2. apt get install libasound2 alsa utils alsa oss
 3. alsamixer:
  in od "mutiraš" kanale, ki so zamutani
 Druga rešitev (ali celo dopolnitev):
    je, da v terminal napišeš:
    pulseaudio  D
    secer napiše, da ni mišljeno, da bi bil zagnan kot root
    ampak Ok... po tem dela tudi:
    Settings>Soun

# SUBLIME TEXT 3
## Install:
  Greš na njihovo stran in snameš dol pravo verzijo (Ubuntu 64)
  nato pa v terminalu zaženeš:

    cd Downloads
    dpkg  i Sublime...64.deb

## Nastavitve   Key Bindings

Da imam kompatibilnost z ostalimi programi si nastavim še KeyBindings
veliko command najdemo tule:[link](http://www.sublimetext.com/docs/commands)

1.  > Preferences  > KeyBindings
2. v "User" pastneš tole:

```json
[

  { "keys": ["ctrl+e"],     "command": "toggle_side_bar" },
  { "keys": ["ctrl+t"],     "command": "new_file" },
  { "keys": ["ctrl+shift+c"], "command": "git_quick_commit" },
  { "keys": ["ctrl+shift+u"], "command": "git_push_current_branch" },
  { "keys": ["ctrl+shift+d"], "command": "git_pull_current_branch" },
  { "keys": ["ctrl+alt+s"],   "command": "pandown_build",
                  "args":{
                    "pandoc_from": "markdown",
                    "pandoc_to": ["latex", ".pdf"],
                    "prevent_viewing": true
                  }
  },
  { "keys": ["ctrl+alt+i"], "command": "insert",
                  "args": {
                    "characters": "![caption\\label{slika}](link)"
                  }
  },
  { "keys": ["ctrl+alt+e"],   "command": "insert",
                  "args": {
                    "characters": "$$Y=kX+n$$ {#eq:linearna f}"
                  }
  },
  { "keys": ["f10"],  "command": "citer_show_keys"},
  { "keys": ["ctrl+alt+t"],   "command": "shell_command",
                    "args": {
                      "command": "~/Files/GitHub_noSync/ArchLabs/MyDotFiles/timesheetNotes.sh",
                      "target": "point"
                    }
  },
  { "keys": ["ctrl+alt+d"], "command": "shell_command",
                    "args": {
                      "command": "date +'%F'",
                      "target": "point"
                    }
    },
    { "keys": ["ctrl+alt+h"], "command": "shell_command",
                    "args": {
                      "command": "date +'%R'",
                      "target": "point"
                    }
    },
  { "keys": ["ctrl+alt+m"],     "command": "insert",
                  "args": {
                    "characters": "   \ntitle: 'Naslov'\nauthor: [dr. David Rihtaršič]\ndate: \ntags: [tag1,tag2]\nbibliography: bibtex.bib\n   "
                  }
  },
  { "keys": ["ctrl+enter"], "command": "shell_command",
                  "args": {
                      //"prompt": "Enter a command",
                      "title": "My Command",
                      "target": "point"
                  }
  }
]
```

## Package Controll:
  Paket za koristne funkcionalnosti:

__install Package Controll:__
  1. goto [link][https://packagecontrol.io/installation]
  2. _copy_ code for Sublime 3:
    import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
  3. View  > Show Console
  4. _paste_

### Emmet
Emmet                    //completeing the code

### AllAutoComplete
complete any word from opened files

dodas v Preferences  > Settings:

> "auto_complete_selector": "source, text",
> "auto_complete_commit_on_tab": true,

### DoxyDoxygen
komentiranje funkcij [Alt]+[Q]

### SideBarEnhacement
more functionality in side bar

### GitGutter
kaže kaj si na novo naredil v primerjavi s fajlom na GitHubu

### Git
1. C+S+p  > Install Packages
2. [Git()][https://github.com/kemayo/sublime text git/wiki]

#### automatic uploading in Sublime
v .git/config zamenjaš namesto:

    [remote "origin"]
    url = https://github.com/davidrihtarsic/BunsenLab.git
    fetch = +refs/heads/*:refs/remotes/origin/*
v

    [remote "origin"]
    url = https://davidrihtarsic:rihtarsicda888@github.com/davidrihtarsic/BunsenLab.git
    fetch = +refs/heads/*:refs/remotes/origin/*

####  nastavitve
The detail step

1. go to your local git project directory, [open][.git/config] file and
2. edit: https://{username}:{password}@github.com/{username}/{project}.git
3. input git push to check if it works.

jaz sem moral prej še spedenat v terminalu

    git commit  a  m "sublime pedenanje"
    git push (če je kak error prej še git pull... in popraviš razlike)

#### uporaba:
1. popraviš file... & C+s (save)
2. C+S+p  > quick commit (repo)  > msg
3. C+S+p  > push

### MarkDown
Paket Package Controll mora biti nameščen...
  2. Install Package: _Monokai extended_
  3. Preferences  > Color Scheme  > Monokail Extended  > Monokail Extended
  4. Install Package: _Markdown Editing_
  5. Set doc. syntax = Monokai Extended
  6. Preferences  > Package settings  > Markdown Editing  > Markdown Settings (standard)   User:

     {
       "color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme",
       "tab_size": 2,
       "line_numbers": true,
       // Layout
       "draw_centered": false,
       "wrap_width": 0,
       "rulers": []
     }

### Citer
[link](https://github.com/mangecoeur/Citer)
Shraniti moraš projet in potem išče po vseh filit v projetku zapise z bibliography

Preferences  > Package Controll  > Citer  > Settings   default:

    ...
    "bibtex_file_path": "/home/david/Files/Work/PeF/Articles/bibtex_global.bib",
    ...

### ~~CiteBibtex~~

    {
        "bibtex_file": "bibtex.bib",
        "bibtex_file_encoding": "utf 8",
        "default_citation_style": "pandoc",
        "autodetect_citation_style": true,
        "additional_search_fields": [],
        "autodetect_syntaxes": {"LaTeX": "latex",
                                "LaTeX Beamer": "latex",
                                "LaTeX Memoir": "latex",
                                "Markdown": "pandoc",
                                "MultiMarkdown": "pandoc",
                                "Markdown GFM": "pandoc",
                                "AcademicMarkdown": "pandoc"},
        "styles": {"pandoc": "[@$CITATION]",
                   "latex": "\\citep{$CITATION}"},
        "citation_format_string": "{author} ({year}). {title}"
    }

### ~~LiveReload~~

### ~~MarkdownPreview~~

### Pandown (SublimeText3 Plugin)
V Preferences  > Package settings   > Pandown   > Settings  user:

    {
      "pandoc_arguments":
      {
        "command_arguments":
        {
          "template": "eisvogel",
          "variables":
          {
            "lang":"sl"
          },
          "filter":
                [
                    "pandoc eqnos",
                    "pandoc crossref"
                ],
          "listings": true,
          "incremental": false,
          "latex engine": "",
          "bibliography":
          [
            "bibtex.bib",
            "/home/david/Files/Work/PeF/Articles/bibtex_global.bib"
          ]
        }
      }
    }



### LaTeX:
namestis paket preko:
 C+S+p  > __Install Packages__
 ~~LaTeXTools~~
OK, prej moras namestiti dodatne pakete..:

    sudo apt ge" : "t install texlive full
    sudo apt get install latexmk
    sudo apt get install biber

#### LaTex:
Našel sem, da lahko iz MarkDown datoteke naredis pdf tako, da uporabim *pandoc*.
S tem programom lahko spremeniš tudi v druge formate WORD... Ampak moraš inštalirat
še LaTeX podporo...

    texlive full

program zasede full okoli 2GB
zato inštaliraš raje

    texlive

#### PanDoc
Install (ARCH=x86_64):

    yaourt pandoc 2.0.6.11

nato pa še packages:

    sudo apt get install texlive latex extra
    __sudo apt get install texlive fimts extra__

oba paketa sem inštaliral preko SynapticPackageManager, ker je preveč dependenciesov...
__CMD:__

    pandoc  o test.pdf   from markdown   template eisvogel   listings myLinuxNotes.md

__TEMPLATE GENERATOR___

da naredič template v terminal vpišeš:

    pandoc  D latex
(objavil je Luck Schmit)

### Spell Checker:
 download:
  v direktorij: /home/david/.config/sublime text 3/Packages/

    wget https://github.com/titoBouzout/Dictionaries/archive/master.zip
    //then unz
    unzip..

 ali ...
  1. [Download](http://extensions.openoffice.org/en/project/venian dictionary package slovenski paket slovarjev) the language file from the appropiate OpenOffice extension
  2. Rename the "some.oxt" file to "some.zip"
  3. Unzip the file
  4. Look for two files: "lang.aff" and "lang.dic". For example es_ES.aff and   ES.dic
  5. Open the "lang.aff" to check the encoding used. Such the line: SET    8859 1
  6. Convert that file to UTF 8 from the used encoding
  7. Convert "lang.dic" to UTF 8 from the used encoding.
  8. Change SET ISO 8859 1 to SET UTF 8
  9. In ST3, click on Preferences  > Browse Packages
  10. Create a new folder, for example Language   Spanish
  11. Move lang.dic and lang.aff to that folder
  12. Activate the dictionary in ST3 (View  > Dictionary  > Language   Spanish   es_ES)
  13. Press F6 to enable spell check
  14. View >Dictionaries

 Google spell check:
  + apt get update
  + dpkg  i teamviewer_****_i386.deb
  + sudo apt get  f install namestitev:
    C+S+p  > Install Packages
    Google Spell Check



# SYSTEMD
Program skrbi za zagon UNIT ov ali procesov oz. v linuxu se jim reče *deamon*. Bistvena razlika pri ARCH linuxu je,  da service ni enablan takoj, ko naložiš program in ga moraš inštalirat sam...  To je vidno tudi v kaki ARCH wiki ko piše le :

> you must enable UNIT.service...

## uporaba

    systemctl enable UNIT.service   > zagon servisa tudi ob restartu
    systemctl start UNIT.service   > zagon servisa za ta sesion
    systemctl stop UNIT.service   > izkljuci servis
    systemctl restart UNIT.service   > ponovni zagon servisa za ta sesion

    systemctl status UNIT.service   > nekaj več podatkov o UNITU

S status lahko vidiš, kje je LOG file... to lahko pomaga pri debagiranju kaj je šlo narobe...

Preverimo lahko ali je Unit enablan? to pomeni, če se bo service ZAGNAL že ob zagonu...

		systemctl is-enabled UNIT.service

in če je  rezultat

		enabled

potem ja OK



## log file
če je kak eror na začetku ga lahko pogledaš z:

    journalctl  b
    journalctl  f   za sprotno gledanje kaj gre narobe...

## system run

    systemctl
        hibernate
        suspend

## dodjanje svojih skriptov

Če želimo dodati svoje skripte tako, da bo delovalo kot CRONJOB moramo najprej:

1. ustvariti SCRIPT.SH
2. dodati pravice za execution
3. greš v /etc/systemd/system
4. dodaš datoteko: krneki.service (nujno .service)
5. v datoteki se mora nahajati besedilo:

		[Service]
		ExecStart=/home/david/SCRIPT.SH
		Restart=always
		WorkingDirectory=/home/david
		User=david
		Group=david
		...
(več na: https://www.youtube.com/watch?v=fYQBvjYQ63U)

6. nato le zaženemo service

		sudo systemctl start krneki (ne vem zakaj je izpustil .service)

7. le še preverimo če vse dela

		systemctl status krneki



# STATISTICS(PYTHON&PANDAS)
https://github.com/justmarkham/pandas videos

## Importing Data
    pd.read_csv(filename) | From a CSV file
    pd.read_table(filename) | From a delimited text file (like TSV)
    pd.read_excel(filename) | From an Excel file
    pd.read_sql(query, connection_object) | Read from a SQL table/database
    pd.read_json(json_string) | Read from a JSON formatted string, URL or file.
    pd.read_html(url) | Parses an html URL, string or file and extracts tables to a list of dataframes
    pd.read_clipboard() | Takes the contents of your clipboard and passes it to read_table()
    pd.DataFrame(dict) | From a dict, keys for columns names, values for data as lists

## Exporting Data
    df.to_csv(filename) | Write to a CSV file
    df.to_excel(filename) | Write to an Excel file
    df.to_sql(table_name, connection_object) | Write to a SQL table
    df.to_json(filename) | Write to a file in JSON format

## Create Test Objects
Useful for testing code segements

    pd.DataFrame(np.random.rand(20,5)) | 5 columns and 20 rows of random floats
    pd.Series(my_list) | Create a series from an iterable my_list
    df.index = pd.date_range('1900/1/30', periods=df.shape[0]) | Add a date index

## Viewing/Inspecting Data
    df.head(n) | First n rows of the DataFrame
    df.tail(n) | Last n rows of the DataFrame
    df.shape() | Number of rows and columns
    df.info() | Index, Datatype and Memory information
    df.describe() | Summary statistics for numerical columns
    s.value_counts(dropna=False) | View unique values and counts
    df.apply(pd.Series.value_counts) | Unique values and counts for all columns

## Selection
df[col] | Returns column with label col as Series
df[[col1, col2]] | Returns columns as a new DataFrame
    s.iloc[0] | Selection by position
    s.loc['index_one'] | Selection by index
    df.iloc[0,:] | First row
    df.iloc[0,0] | First element of first column

## Data Cleaning
    df.columns = ['a','b','c'] | Rename columns
    pd.isnull() | Checks for null Values, Returns Boolean Arrray
    pd.notnull() | Opposite of pd.isnull()
    df.dropna() | Drop all rows that contain null values
    df.dropna(axis=1) | Drop all columns that contain null values
    df.dropna(axis=1,thresh=n) | Drop all rows have have less than n non null values
    df.fillna(x) | Replace all null values with x
    s.fillna(s.mean()) | Replace all null values with the mean (mean can be replaced with almost any function from the statistics section)
    s.astype(float) | Convert the datatype of the series to float
    s.replace(1,'one') | Replace all values equal to 1 with 'one'
    s.replace([1,3],['one','three']) | Replace all 1 with 'one' and 3 with 'three'
    df.rename(columns=lambda x: x + 1) | Mass renaming of columns
    df.rename(columns={'old_name': 'new_ name'}) | Selective renaming
    df.set_index('column_one') | Change the index
    df.rename(index=lambda x: x + 1) | Mass renaming of index

## Filter, Sort, and Groupby
    df[df[col] > 0.5] | Rows where the column col is greater than 0.5
    df[(df[col] > 0.5) & (df[col] < 0.7)] | Rows where 0.7 > col > 0.5
    df.sort_values(col1) | Sort values by col1 in ascending order
    df.sort_values(col2,ascending=False) | Sort values by col2 in descending order
    df.sort_values([col1,col2],ascending=[True,False]) | Sort values by col1 in ascending order then col2 in descending order
    df.groupby(col) | Returns a groupby object for values from one column
    df.groupby([col1,col2]) | Returns groupby object for values from multiple columns
    df.groupby(col1)[col2] | Returns the mean of the values in col2, grouped by the values in col1 (mean can be replaced with almost any function from the statistics section)
    df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean) | Create a pivot table that groups by col1 and calculates the mean of col2 and col3
    df.groupby(col1).agg(np.mean) | Find the average across all columns for every unique col1 group
    df.apply(np.mean) | Apply the function np.mean() across each column
    nf.apply(np.max,axis=1) | Apply the function np.max() across each row

## Join/Combine
    df1.append(df2) | Add the rows in df1 to the end of df2 (columns should be identical)
    pd.concat([df1, df2],axis=1) | Add the columns in df1 to the end of df2 (rows should be identical)
    df1.join(df2,on=col1,how='inner') | SQL style join the columns in df1 with the columns on df2 where the rows for col have     identical values. how can be one of 'left', 'right', 'outer', 'inner'

## Statistics
    These can all be applied to a series as well.

    df.describe() | Summary statistics for numerical columns
    df.mean() | Returns the mean of all columns
    df.corr() | Returns the correlation between columns in a DataFrame
    df.count() | Returns the number of non null values in each DataFrame column
    df.max() | Returns the highest value in each column
    df.min() | Returns the lowest value in each column
    df.median() | Returns the median of each column
    df.std() | Returns the standard deviation of each column

# TERMINAL:
 Terminal je najboljši terminator
 > sudo apt get install terminator

## Preferences:
 [ ] Show title bar
 Profiles  > Colors = Green on Black
 Profiles  > Background  > Transparency = 50%

## Programi za terminal
### SC IM
excel za terminal... super omogoče veliko excelovih stvari ... tudi izvoz v .xlsx
__Uporabne komande:__
> 4<DOWN> // skočimo za 4 celice dol   uporabno pri kopiranju če se moraš premaknit
> yr      // copy (YUNK) celo ROW
> p       // paste cel YUNK
> +/      // increse/decrese number
> C d     // transform to DATE
> f<UP>   // 0.00  > 0.000
> f<DOWN> // 0.00  > 0.0
> f<LEFT> // spremeni širino stolpca


V /home/david/.scimrc napišemo:
> nmap "W" ":w<cr>:e! txt<cr>:e! xlsx<cr>"  //mapira "W" tako da shrani datoteko v .sc, .txt in .xlsx

# TAB_CLICK:

 Da vklnjučiš Tab CLICK greš v:
 1. settings
 2. mouse
 3. in nato : Tab CLICK = ON
 Videl sem tudi, da problem reši tudi:
 > synclient tapbutton1 = 1

## Touchpad
 v [datoteki][/usr/share/X11/xorg.conf.d/50 synaptics.conf]
 dodas:

    Section "InputClass"
      Identifier      "Touchpad"                      # required
      MatchIsTouchpad "yes"                           # required
      Driver          "synaptics"                     # required
      Option          "MinSpeed"              "0.5"
      Option          "MaxSpeed"              "1.0"
      Option          "AccelFactor"           "0.075"
      Option          "TapButton1"            "1"
      Option          "TapButton2"            "3"     # multitouch
      Option          "TapButton3"            "2"     # multitouch
      Option          "VertTwoFingerScroll"   "1"     # multitouch
      Option          "HorizTwoFingerScroll"  "1"     # multitouch
      Option          "VertEdgeScroll"        "1"
      Option          "CoastingSpeed"         "8"
      Option          "CornerCoasting"        "1"
      Option          "CircularScrolling"     "1"
      Option          "CircScrollTrigger"     "7"
      Option          "EdgeMotionUseAlways"   "1"
      Option          "LBCornerButton"        "8"     # browser "back" btn
      Option          "RBCornerButton"        "9"     # browser "forward" btn
    EndSection


# TEAMVIEWER
  presnames teamviewer i386 (cetudi imas 64 bitni comp.)
  v terminalu>
  + sudo dpkg   add architecture i386
  + sudo apt get update
  + sudo dpkg  i teamviewer_****_i386.deb
  + sudo apt get  f install

# TEXMAKER
  1. Spell Checker:
  [download][http://extensions.services.openoffice.org/en/project/slovenian dictionary package slovenski paket slovarjev]
  2. unzip pac sl.oxt
  3. in prekopiraš datoteko sl SI.dic v Sublime paketi direktorij (Preferences >Browse packages)
  4. nato nastaviš jezik : View >Dictionary >si SL.dic


# THUNDERBIRD()
  inštalacija je čisto reprosta:
  > apt get install thunderbird

  ali če ni apt paketa:
  1. greš na njihovo stran in presnameš datoteko thunderbird.tar.db2
  2. extrahiraš v /opt/thunderbird
  3. preveriš če dela: ./thunderbird
  4. nastaviš privilegije (če je potrebno):

> sudo chown  R root:root /opt/hunderbird

  5. in linkaš exe skript:

> sudo ln  fs /opt/thunderbird/thunderbird /usr/bin/hunderbird

## Nastavitev Thunderbirda za PeF
    Your name: David Rihtarsic
    Email add: david.rihtarsic@pef.uni lj.si
    Password: Work mei kabinet
    Incoming: IMAP
    + server: imap.uni lj.si
    + port: 993
    + SSL: SSL/TLS
    + Authentication: NMLT
    Outgoing: SMTP
    + server: mail.uni lj.si
    + port: 587
    + SSL: None
    + Authentication: NMLT

## Google Koledar v Thunderbirdu
1. inštaliraš koledar:
Menu >AddOns >Lightnings >Install
2. inštaliraš Google Provider:
Menu >AddOns >Provider for Google Calender >Install... Restart Now
3. Vključevanje koledarja:
    v "Callenders" klikneš z desno in "New Calenders"
    On the network  > Next
    Google Calender  > Next
    david.rihtarsic@gmail.com
     + gesla + itd.
    izbereš koledarje za sync  > Next
    Finish

## Paragraph space
Da ne pušča preveč prostora med posameznimi odstavki, je potrebno nastaviti:
  Menu [__=__]  > Preferences  > Composition :
+ [ ] Use Paragraph format instead of Body Text by default.


# TO DO
[ ] /i3/config
	+ naredi sh tako:
			da preveri, če je VIM_MAIN vključen
				potem naj naredi le focus na to okno
			drugače pa ga  odpre
[ ] Izključi CTRL+S da pavzira itvajanje terminala
  + vklljuči CTRL+S v Vim da shrani file...
[ ] v i3/config dodaj:
	+ Ctrl+PrintScreen -> scort -s (klikneš na okno in ti ga da v sliko)
[ ] NAUČI SE VIM
	+ uporaba multiple cursor
	+ kako shraniti (mogoče je kaj z rangerjem
			ukaz je :w ime.datotehe
			Ampak to se shrani v PWD

# VIM
## Instalation

    sudo apt get install vim nox

### install Vundle    Plugin Manger

Run v terminalu:

	git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

V ~/.vimrc na vrhu vpiš:

    set nocompatible
    filetype off
		set rtp+=~/.vim/bundle/Vundle.vim
		call vundle#begin()

   	Plugin 'VundleVim/Vundle.vim'
		Plugin 'majutsushi/tagbar'
		" za delovanje moraš inštalirati še:
		" exuberant stags

	 	call vundle#end()            " required
		filetype plugin indent on    " required

## Instalation Plugins from terminal

		yaourt  S vim tagbar
## Instalation of FZF
Super stvar : fuzzy file search!

1. Najprej pustiš, da vim nainštelira plugin:  junegunn/fzf
2. Nato poženeš:
    ~/.vim/bundle/fzf/install

3. in ponovno zaženeš terminal in vim.

Plugin uporabljaš tako, da :
  Ctrl+T => za iskanje filov
  Ctrl+R => za iskanje kommand v terminalu..

Če želimo, da lahko iščemo še po skritih dokumentih moramo v .zshrc vpisati:

    export FZF_DEFAULT_COMMAND="find .  type f  print  o  type l  print"
    export FZF_CTRL_T_COMMAND="find .  type f  print  o  type l  print"


## References

[How to fold](http://vimcasts.org/episodes/how to fold/)
  folding je izredno počasen... (to do)
  zato raje uporabljam kar TOC za markdown
## Spell checking
		:set spell spellang=sl
		:set nospell

SHORTCUTS:
		z= 		predlog za pravilno črkovano besedo
		]s 		naslednja napačno črkovana beseda

[več o spell](https://www.linux.com/learn/using spell checking vim)

## Shortcuts
| Shortcuts     | behaviour     |
|               |               |
| <leader> hjkl | resize window |
| <leader> u    | uprate .vimrc |

### Folding
 * zm   foldMore
 * zz   Fold tree toggle
 * zi   not/Foldable
 * zo   open
 * za

# VIRTUALBOX
## Instalation:
    pacman  S virtualbox
    pacman  S pacman  S virtualbox host dkms
    sudo modprobe vboxdrv

## Android
### Resolution Android 7.1
- terminal - go to : VirtualBox folder

    vboxmanage setextradata "Android3" "CustomVideoMode1" "360x640x16"

- run virtula Machine
- izberi resolucijo : 360x640


# W3M

## instalation:

    apt get install w3m

## frendlyUse:
  v ~/bashrc vpišeš:
> alias w3mm='w3m www.google.com'

# WIRELESS SETUP
 Wavemon...
 > sudo apt get install wavemon

## wifi drop
Če stvar dela imam takele nastavitve:
```
└─(09:47:05)──> ip addr                                                                              ──(Thu,30 Aug)─┘
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp4s0: <NO CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state DOWN group default qlen 1000
    link/ether 18:31:bf:73:8c:49 brd ff:ff:ff:ff:ff:ff
3: wlp3s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether 74:e5:f9:19:10:27 brd ff:ff:ff:ff:ff:ff
    inet 172.21.0.86/23 brd 172.21.1.255 scope global dynamic noprefixroute wlp3s0
       valid_lft 432sec preferred_lft 432sec
    inet6 fe80::e12b:7b71:5f59:d39a/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
┌─(~)────────────────────────────────────────────────────────────────────────────────────────(david@archlabs:pts/4)─┐
└─(09:48:55)──> ping www.google.com                                                                  ──(Thu,30 Aug)─┘
PING www.google.com (172.217.20.36) 56(84) bytes of data.
64 bytes from par10s09 in f36.1e100.net (172.217.20.36): icmp_seq=1 ttl=47 time=55.2 ms
64 bytes from par10s09 in f36.1e100.net (172.217.20.36): icmp_seq=2 ttl=47 time=1090 ms
64 bytes from par10s09 in f36.1e100.net (172.217.20.36): icmp_seq=4 ttl=47 time=55.1 ms
64 bytes from par10s09 in f36.1e100.net (172.217.20.36): icmp_seq=5 ttl=47 time=54.0 ms
64 bytes from par10s09 in f36.1e100.net (172.217.20.36): icmp_seq=6 ttl=47 time=55.5 ms
64 bytes from par10s09 in f36.1e100.net (172.217.20.36): icmp_seq=7 ttl=47 time=54.7 ms
^C
    www.google.com ping statistics
7 packets transmitted, 6 received, 14.2857% packet loss, time 87ms
rtt min/avg/max/mdev = 54.049/227.503/1090.393/385.896 ms, pipe 2
```
Slaba komunikacija ali slab wifi signal...
Zgodilo se je, da se je WIFI večkrat izgubil in je linija "padla dol"
mislim, da je pomagalo, da naložiš module z:

		modprobe iwlwifi 11n_disable=1 swcrypto=1

ali pa narediš to bolj za zmerej tako, da naredip file:

		#/etc/modprobe.d/iwlwifi.conf
		options iwlwifi 11n_disable=1 swcrypto=1

## Slow DNS

Če je

		ping 8.8.8.8

hiter in

		ping www.google.com

pocasen... potem je verjetno DNS problem... v  /etc/resolv.conf


				This config work for me:

				nameserver 213.186.33.99
				nameserver 127.0.0.1
				nameserver 208.67.222.222
				search ovh.net

This config work for me:

nameserver 213.186.33.99
nameserver 127.0.0.1
nameserver 208.67.222.222
search ovh.net

# YAOURT
To je program za ARCH za namestitev paketov... ni da ni!
  če vemo natančno ime lahko samo
yaourt  S <ime>   noconfirm

# XANMOD KERNEL:
  XanMod is a mainline Linux kernel distribution with custom settings.
  Optimized to take full advantage of high performance Desktops, PC Gamers,
  Workstations, Media Centers and others. Supports all recent 64 bit
  versions of Debian and Ubuntu based systems.
  ne priporočam, ker potemnisem mogel inštalirati GeForce driverjev...

## Tested
  based on [article](http://www.hecticgeek.com/2016/09/supercharge ubuntu 16 04 lts xanmod kernel/)
  tested on Ubuntu MATE (DELA SUPER!):
  Firefox prej 10.5 s ... po tem 4.6 s
  kopiranje dd (komanda) prej 9MB/s le pri bs=128K
  po tem... 9MB/s pri 1K, 4K, 8K, 32K,

## Installation
1. https://xanmod.org/
2. First install the XanMod Repository Setup
3. manual...
> echo 'deb http://deb.xanmod.org releases main' | sudo tee /etc/apt/  urces.list.d/xanmod kernel.list && wget  qO   http://deb.xanmod.org/gpg.key   sudo apt key add
> sudo apt update && sudo apt install linux xanmod 4.9
> sudo reboot
> cat /proc/version (preveri kernel verzijo:)
4. chane [cfg] disk scheduler:
 1. preveri:
 > sudo cat /sys/block/sda/queue/scheduler (kateri so na razpolago)
 > sudo subl /etc/#ault/grub (edit grub settings)
 2. spremeni vrstico:
 > GRUB_CMDLINE_LINUX_#AULT="quiet splash"
 > GRUB_CMDLINE_LINUX_#AULT="quiet splash elevator=bfq"
 3. shrani
 4. sudo update grub2
 5. reboot
 6. preveri disk scheduler:
 > sudo cat /!!sys/block/sda/queue/scheduler
5. install Intel CPU support:
 1. ker sem prej dobil error:
 W: Possible missing firmware /lib/firmware/rtl_nic/rtl8107e 2.fw for dule   r8169
 sem namestil še firmware, a mislim, da ni šlo skoz...
 > sudo apt install intel microcode iucode tool
 > sudo reboot
