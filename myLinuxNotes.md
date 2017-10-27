# ARDUINO
  
## Enable PORT permmissions to user
> `sudo usermod -a -G dialout terrik`

and Log Out / Log In 

# DD_IBS_TEST.SH():
program za testiranje dd komnade...
kako hitro comp lahko kopira datoteke v odvisnosti ob bs= ? podatka...
Program je na [GitHubu](https://github.com/tdg5/blog/blob/master/_includes/scripts/dd_ibs_test.sh)

# ECLIPSE

## installation:
  ... nisem zapisal...
  ... presnameš, odpakiraš kopiraš v:
  /opt/eclipse/
  narediš link za vse uporabnike:
`sudo ln -sf /opt/eclipse/cpp-neon/eclipse/eclipse /usr/bin/eclipse`

## eclipse.desktop:
Naredimo datoteko.desktop: 
 `sudo nano /usr/share/applications/eclipse.desktop`

    [Desktop Entry]
    Version = Neon 2.0
    Type = Application
    Terminal = false
    Name = eclipse
    Exec = /usr/bin/eclipse
    Icon = /opt/eclipse/cpp-neon/eclipse/icon.xpm
    Categories = Development;

# EFI MODE:
 boot -> CSM enable  
 security -> security boot control -> dissable

## installBUNSEN
 instaliral ...
 grub dal na sda1 (kjer sem našel efi... [sudo parted -l])
 kar nekaj sem probal... ni delalo - sedaj pišem kaj ne dela
 ---
 BIOS:
 new boot oprions:
 path:\efi\boot\bootx64.efi
 ne dela
 ---
 Test x-n
 probaj ta navodila:
 http://sarah.thesharps.us/2014/12/31/installing-debian-on-asus-ux301la/
 ---
 install
 grub -> /dev/sda1
 takoj ne dela... zažene se win10...
 path :\EFI\debian\grubx64.efi [ne dela]
 path :\efi\boot\bootx64.efi [ne dela]

# FILEMANAGER:
 Všeč mi je filemanager THUNAR:
 > `sudo apt-get install thunar`

# FILES STRUCTURE
Tu bi napisal kako bom uredil file
- Files
  + To-Do(links)
  + Work
    * PeF
      - Vaje
        + Modelarstvo
        + Promet
      - Habilitacija
      - Diplome
      - Članki
      - Predstavitve 
    * DRTI
      - Poletne Šole
      - Finance
      - 
    * 
  + Hobi
    * Linux
      - BunsenLab
      - RPi
    * Dom
    * Kolesarjenje
  + Musics
  + GitHub

# FORMAT
First, you have to find out which device (/dev/sd??) your USB stick is. Therefore look at the output of
>sudo fdisk -l

Jaz raje uporabim:
>lsblk

    NAME   MAJ:MIN RM    SIZE RO TYPE MOUNTPOINT
    sda      8:0    0  931.5G  0 disk 
    ├─sda1   8:1    0    100M  0 part 
    ├─sda2   8:2    0  639.9G  0 part /media/david/964EABCA4EABA18B
    ├─sda3   8:3    0      1K  0 part 
    ├─sda5   8:5    0  284.7G  0 part /
    └─sda6   8:6    0    6.9G  0 part [SWAP]
    sdb      8:16   1 1010.3M  0 disk 
    sr0     11:0    1   1024M  0 rom  

Lepo se vidijo diski in kje so mountirani. Po potrebi ga lahko od-mountiraš..
After that unmount the device/partition (if necessary) by running
> sudo umount /dev/sdb

Make sure you replaced ?? with the correct device/partition name from the previous output.
To format The partition as FAT32 use
> sudo mkdosfs -F 32 -I /dev/sdb

# FRITZING
  asdf

# FREECAD
  asdf
# GIMP
  asdf 
# GITHUB
## LITERATURA:
  1. [Link](https://www.youtube.com/watch?v=1h9_cB9mPT8)
  
## install:
Debian le:  
>sudo apt-get install git
  
## config:
>git config --global user.name "davidrihtarsic"

>git config --global user.email "david.rihtarsic@gmail.com"

>git config --global core.editor="subl"
  
## general_use:
make new repository ... BlaBla_project (need to be on URL gitHub)
make dir on your computer for that project 
navigate to that dir
> git init

### editing:
na tem mestu spreminjaš FAJL...
> git add .
> git commit -m "comment"`
> git commit -a -m "comment"
> git status
> git diff

### uploading:
kako da stvar na GitHub...
v spremenljivko "origin" spravimo URL projekta
> git remote add origin https://github.com/davidrihtarsic/myZapiski.git
> git push ~~origin master~~

### updating:
naprimer, da nekdo popravi kodo (recimo ti sam na GitHubu...
in nekdo tudi na compu ter naredi commit)
> git commit -a -m "comment"`

hočeš naložit... novo verzijo in dobiš konflikt s tisto na GitHub-u
> git push origin master

    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.

potem naredis :
> git pull

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
  
in je to - to :)
skratka popraviš in uploadaš še enkrat :) jeah!

# GRAPHIC CARD
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
>sudo service lightdm stop
 


# INKSCAPE
  asdf

# ISO BURN TO USB
> sudo dd bs=4M if=*.iso of=/dev/sdb status=progress && sync

## More advanced copy with progress
Inštaliran mora biti `pv`
> sudo apt-get install pv 

Ker pv (pipe Viever) dela več različnih stvari in ne le dd,
med drugim tudi progress bar... je ukaz potrebno izvesti v sudo načinu:
> sudo -s
> pv <NekIsoFile.iso> /dev/sdb

    857MiB 0:01:05 [13.1MiB/s] [======================================================================>] 100%
> exit
>

# JAVA in FIREFOX BROWSER
1. naložiš javo JRE...
2. mkdir ~/.mozilla/plugins
3. cd ~/.mozilla/plugins
4. ln -s /usr/lib/jvm/jre1.8.0_121/lib/amd64/libnpjp2.so
          [tu pride java direktorij kjer je `libnpjp2.so`]
5. restart FireFox
6. v FF vpišeš `about:plugins` in preveriš če je java podprta... 

# KEYBOARD SETTINFS:
  Settings -> Reigon&Language -> Input Source
  for KeyBindings:

## ShortCuts():
  v settings>Keyboaard sem si nastavil nekaj bližnjic:
   > super+w > Firefox
   > super+e > Text Editor
   > super+f > File Manager
   > super+t > terminator

  v ~/.bashrc (file se zazene na zacetku)
   > bliznica ll namesto ...
   > alias ll='ls -alF'
   > tipki [đ] dodelimo znak [/]
   > xmodmap -e "keycode 35 = slash"
  
# LAZARUS
Programing program in pascal... As Delphi

## instalation
instaliral tako kot je opisano na [internetu](https://forum.lazarus.freepascal.org/index.php?topic=36093.0):
1. Install fpc_3.0.2-170225_amd64.deb via package manager
2. Install fpc_3.0.2.x86_64-linux.tar via shell (unzip and run sh install.sh). Install into /usr directory, so it overwrites 3. the existing installation
4. Install the deb sources via package manager (__tega nisem naredu... neznam__)
5. Install lazarus-project_1.6.4-0_amd64.deb via package manager
6. Instaliral gdb

# LIBREOFFICE:
 Instal preko terminala:
 > `apt-get install libreoffice`

# MERGE PDF DOCUMENTS
Če moramo združiti več pdf dokumentov v enega v terminal napišemo:
> pdfunite pdf0.pdf pdf1.pdf merged.pdf

# POPCORN-TIME
# PASSWORD
To change a password on behalf of a user, first sign on or "su" to the "root" account. Then type:
(where user is the username for the password you are changing).
> passwd user

The system will prompt you to enter a password. Passwords do not echo to the screen when you enter them.
You can also change your own password, by typing:
(without specifying a username).
> passwd

You will be prompted to enter your old password for verification, and then a new password.

# PPRINTER SUPPORT on BunsenLab
sledil sem tocno tem [navodilom](http://hplipopensource.com/hplip-web/install/manual/distros/debian.html)
- prej moraš vedeti tudi root geslo

Program za gledanje filmov:
  1. Download [Popcorn-Time](https://www.popcorntime.ws/about)
  2. razpakiraš in daš dokumente v /opt/popcorn-time/
  3. polinkaš, da bo dosegljivo vsem:
  `sudo ln -sf /opt/popcorn-time/Popcorn-Time /usr/bin/popcorn-time`
  4. Narediš še .desktop datoteko
  `sudo nano /usr/share/applications/popcorntime.desktop`
  5. in vot vpišeš:

    [Desktop Entry]
    Version = 1.0
    Type = Application
    Terminal = false
    Name = Popcorn Time
    Exec = /usr/bin/popcorn-time
    Icon = /opt/popcorn-time/src/app/images/icon.png
    Categories = Application;

# PRINT SCREEN = DARK


# QCAD
  1. presnameš inštalacijo iz njihove [strani][https://qcad.org/en/qcad-downloads-trial]
  2. nato spremeniš rivilegije datoteke:
  > `sudo chmod 777 qcad*.run`
  3. in poženeš script:
  > `./qcad*.run`


# Qt5
Za nekateri program sem si moral nainštalirat Qt5 knjižnice:
1. Manjkala mi je `Qt5LinguistToolsConfig`
Ostale mislim, da sem imel...

## Instalacija Qt5LinguistToolsConfig
Mislim, da mi jo je uspelo naložit z:
> sudo apt-get install qttools5-dev

nato sem datoteko našel:
> sudo find /usr/lib/* -name Qt5Lin*

nato je manjkal še Qt5Quck
instaliral sem ga z
> sudo apt-get install qtdeclarative5-dev

nato je manjkal Qt5SvgConfig, instaliral z:
> sudo apt-get install libqt5svg5-dev
> sudo apt-get install libraw-dev
--sudo apt-get install exiv2 (najverjetneje ni bil taprav paket!!!)--
> sudo apt-get install libexiv2-dev
> sudo apt-get install graphicsmagick

še vedno ni delalo
nato sem inštaliral qt5 creator... (neumnost, ker je to cel program za programiranje)
> sudo apt-get install qtcreator

še ni pomagalo:
sudo apt-get install qml-module-qtgraphicaleffects
sudo apt-get install qml-module-qtquick-dialogs
sudo apt-get install pyqt5-dev
sudo apt-get install qtdeclarative5-models-plugin


# SOUNDON:
 Na začetku mi ni delal zvok... Rešitev je bila:
 1. `lspci`: 
  tako preveriš, če je Linux prepoznal zvočno...
  na terminalu sem dobil:

      '00:1b.0 Audio device: Intel Corporation 7 Series/C210 Series Chipset Family High #inition Audio Controller (rev 04)'

 2. `apt-get install libasound2 alsa-utils alsa-oss`
 3. `alsamixer`:
  in od "mutiraš" kanale, ki so zamutani
 Druga rešitev (ali celo dopolnitev):
  - je, da v terminal napišeš:
    pulseaudio -D
  - secer napiše, da ni mišljeno, da bi bil zagnan kot root
    ampak Ok... po tem dela tudi:
    Settings>Soun

# SUBLIME TEXT 3

## Install:
  Greš na njihovo stran in snameš dol pravo verzijo (Ubuntu 64)
  nato pa v terminalu zaženeš:
  > `cd Downloads`
  > `dpkg -i Sublime...64.deb`

## Package Controll:
  Paket za koristne funkcionalnosti:

### install:
  1. goto [link][https://packagecontrol.io/installation]
  2. _copy_ code for Sublime 3:
    `import urllib.request,os,hashlib; h = 'df21e130d211cfc94d9b0905775a7c0f' + '1e3d39e33b79698005270310898eea76'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)`
  3. View -> Show Console
  4. _paste_ 

### install GitHub:
  1. C+S+p -> Install Packages
  2. [Git()][https://github.com/kemayo/sublime-text-git/wiki]

####  nastavitve:
  The detail step:
   1. go to your local git project directory, [open][.git/config] file and
   2. edit: `https://{username}:{password}@github.com/{username}/{project}.git`
   3. input git push to check if it works.
    > jaz sem moral prej še spedenat v terminalu:
    > git commit -a -m "sublime pedenanje"
    > git push (če je kak error prej še git pull... in popraviš razlike)

#### uporaba:
  1. popraviš file... & C+s (save)
  2. C+S+p -> quick commit (repo) -> `msg`
  3. C+S+p -> push

### MarkDown:
Paket Package Controll mora biti nameščen...
  1. Install Package: _Markdown extended_ (mogoče ni treba)
  2. Install Package: _Monokai extended_
  3. Preferences -> Color Scheme -> Monokail Extended -> Monokail Extended
  4. Install Package: _Markdown Editing_
  5. Set doc. syntax = Monokai Extended
  6. Preferences -> Package settings -> Markdown Editing -> Markdown Settings (standard) - User:

     {
       "color_scheme": "Packages/Monokai Extended/Monokai Extended.tmTheme",
       "tab_size": 2,
       "line_numbers": true,
       // Layout
       "draw_centered": false,
       "wrap_width": 0,
       "rulers": []
     }
#### MarkDown uporaba:
>linux ukazi

    z dvema TAB-oma
    njegov izpis na ekranu
    ali nek drug text v filu...
1. nastevanje
2. nastevanje..
  - nast
  - nast
  * nato pa se
  * nato tudi to
    + lahko pa tudi
    + ali a +
__podčtrano__

~~prečrtano~~ bom uporabljal tam kjer sem nekaj probal pa ni delovalo

[link](http://google.com)

### LaTeX:
namestis paket preko:
 C+S+p -> __Install Packages__
 ~~LaTeXTools~~
  * OK, prej moras namestiti dodatne pakete..:
  * `sudo apt-get install texlive-full`
  * `sudo apt-get install latexmk`
  * `sudo apt-get install biber`

### Spell Checker:
 download:
  v direktorij: /home/david/.config/sublime-text-3/Packages/
  
  > `wget https://github.com/titoBouzout/Dictionaries/archive/master.zip`  
  > `unzip..`
   
 ali ...
  1. [Download](http://extensions.openoffice.org/en/project/venian-dictionary-package-slovenski-paket-slovarjev) the language file from the appropiate OpenOffice extension
  2. Rename the "some.oxt" file to "some.zip"
  3. Unzip the file
  4. Look for two files: "lang.aff" and "lang.dic". For example es_ES.aff and   ES.dic
  5. Open the "lang.aff" to check the encoding used. Such the line: SET   -8859-1
  6. Convert that file to UTF-8 from the used encoding
  7. Convert "lang.dic" to UTF-8 from the used encoding.
  8. Change SET ISO-8859-1 to SET UTF-8
  9. In ST3, click on Preferences -> Browse Packages
  10. Create a new folder, for example Language - Spanish
  11. Move lang.dic and lang.aff to that folder
  12. Activate the dictionary in ST3 (View -> Dictionary -> Language - Spanish   es_ES)
  13. Press F6 to enable spell check
  14. View->Dictionaries
 
 Google spell check:
  + `apt-get update`
  + `dpkg -i teamviewer_****_i386.deb`
  + `sudo apt-get -f install` namestitev:
    C+S+p -> Install Packages
    Google Spell Check


# TERMINAL:
 Terminal je najboljši terminator
 > `sudo apt-get install terminator`

## Preferences:
 [ ] Show title bar
 Profiles -> Colors = Green on Black
 Profiles -> Background -> Transparency = 50%

# TAB_CLICK:

 Da vklnjučiš Tab-CLICK greš v:
 1. settings
 2. mouse
 3. in nato : Tab-CLICK = ON
 Videl sem tudi, da problem reši tudi:
 > `synclient tapbutton1 = 1`

## Touchpad
 v [datoteki][/usr/share/X11/xorg.conf.d/50-synaptics.conf]
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
  presnames teamviewer i386 (cetudi imas 64-bitni comp.)
  v terminalu>
  + `sudo dpkg --add-architecture i386`
  + `sudo apt-get update`
  + `sudo dpkg -i teamviewer_****_i386.deb`
  + `sudo apt-get -f install`

# TEXMAKER
  1. Spell Checker:
  [download][http://extensions.services.openoffice.org/en/project/slovenian-dictionary-package-slovenski-paket-slovarjev]
  2. `unzip pac-sl.oxt`
  3. in prekopiraš datoteko sl-SI.dic v Sublime paketi direktorij (Preferences->Browse packages)
  4. nato nastaviš jezik : View->Dictionary->si-SL.dic


# THUNDERBIRD()
  inštalacija je čisto reprosta:
  > apt-get install thunderbird

  ali če ni apt paketa:
  1. greš na njihovo stran in presnameš datoteko thunderbird.tar.db2
  2. extrahiraš v /opt/thunderbird
  3. preveriš če dela: ./thunderbird
  4. nastaviš privilegije (če je potrebno):  

> sudo chown -R root:root /opt/hunderbird
  
  5. in linkaš exe skript:

> sudo ln -fs /opt/thunderbird/thunderbird /usr/bin/hunderbird

## Nastavitev Thunderbirda za PeF
  - Your name: David Rihtarsic
  - Email add: david.rihtarsic@pef.uni-lj.si
  - Password: Work-mei-kabinet
  - Incoming: IMAP
    + server: imap.uni-lj.si
    + port: 993
    + SSL: SSL/TLS
    + Authentication: NMLT
  - Outgoing: SMTP
    + server: mail.uni-lj.si
    + port: 587
    + SSL: None
    + Authentication: NMLT

## Google Koledar v Thunderbirdu
1. inštaliraš koledar:
Menu->AddOns->Lightnings->Install
2. inštaliraš Google Provider:
Menu->AddOns->Provider for Google Calender->Install... Restart Now
3. Vključevanje koledarja:
  - v "Callenders" klikneš z desno in "New Calenders"
  - On the network -> Next
  - Google Calender -> Next
  - david.rihtarsic@gmail.com + gesla + itd.
  - izbereš koledarje za sync -> Next
  - Finish

# W3M:
## instalation:
> `apt-get install w3m`

## frendlyUse:
  v ~/bashrc vpišeš:
> `alias w3mm='w3m www.google.com'`

# WIRELESS SETUP
 Wavemon...
 > `sudo apt-get install wavemon`


# XANMOD KERNEL:
  XanMod is a mainline Linux kernel distribution with custom settings.
  Optimized to take full advantage of high-performance Desktops, PC Gamers,
  Workstations, Media Centers and others. Supports all recent 64-bit
  versions of Debian and Ubuntu-based systems.

  - ne priporočam, ker potemnisem mogel inštalirati GeForce driverjev... 

## Tested
 based on [article](http://www.hecticgeek.com/2016/09/supercharge-ubuntu-16-04-lts-xanmod-kernel/)
 tested on Ubuntu MATE (DELA SUPER!):
  * Firefox prej 10.5 s ... po tem 4.6 s
  * kopiranje dd (komanda) prej 9MB/s le pri bs=128K
  * po tem... 9MB/s pri 1K, 4K, 8K, 32K, 

## Installation 
 1. https://xanmod.org/
 2. First install the XanMod Repository Setup
 3. manual...
 > `echo 'deb http://deb.xanmod.org releases main' | sudo tee /etc/apt/  urces.list.d/xanmod-kernel.list && wget -qO - http://deb.xanmod.org/gpg.key   sudo apt-key add -`  
 > `sudo apt update && sudo apt install linux-xanmod-4.9`  
 > `sudo reboot`  
 > `cat /proc/version` (preveri kernel verzijo:)
 4. chane [cfg] disk scheduler:
  1. preveri:
  > `sudo cat /sys/block/sda/queue/scheduler` (kateri so na razpolago)  
  > `sudo subl /etc/#ault/grub` (edit grub settings)  
  2. spremeni vrstico:
  > GRUB_CMDLINE_LINUX_#AULT="quiet splash"  
  > GRUB_CMDLINE_LINUX_#AULT="quiet splash elevator=bfq"
  3. shrani
  4. sudo update-grub2
  5. reboot
  6. preveri disk scheduler:
  > `sudo cat /sys/block/sda/queue/scheduler`
 5. install Intel CPU support:
  1. ker sem prej dobil error:
  `W: Possible missing firmware /lib/firmware/rtl_nic/rtl8107e-2.fw for dule   r8169`
  sem namestil še firmware, a mislim, da ni šlo skoz...
  > `sudo apt install intel-microcode iucode-tool`
  > `sudo reboot`
    

# XRANDR:
te nastavitve so odvisne od monitorja... !
najprej:
> cvt 1280 1024 60
    # 1280x1024 59.89 Hz (CVT 1.31M4) hsync: 63.67 kHz; pclk: 109.00 MHz
    Modeline "1280x1024_60.00"  109.00  1280 1368 1496 1712  1024 1027 1034 1063 -hsync +vsync

...kopiras kar ti terminal vrže...:
> sudo xrandr --newmode "1280x1024"  109.00  1280 1368 1496 1712  1024 1027   1034   1063 -hsync +vsync`

dodas v moznosti:
> sudo xrandr --addmode VGA1 1280x1024`

potem nastavis resolucijo v 
__MENU -> Settings -> Arandr__ ali v terminalu:
> xrandr --output VGA1 --mode 1280x1024 --pos 1366x0


