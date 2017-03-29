def KeyBoardSettings():
	Settings -> Reigon&Language -> Input Source
def ShortCuts():
	v settings>Keyboaard sem si nastavil nekaj bližnjic:
		super+w > Firefox
		super+e > Text Editor
		super+f > File Manager
		super+t > terminator
def FileManager():
	Všeč mi je filemanager THUNAR:
		- apt-get install thunar
def Terminal():
	Terminal je najboljši terminator
		-apt-get install terminator
	Preferences:
		[ ] Show title bar
		Profiles -> Colors = Green on Black
		Profiles -> Background -> Transparency = 50%
def LibreOffice():
	apt-get install libreoffice
def Tab-CLICK():
	Da vklnjučiš Tab-CLICK greš v:
		-settings
		-mouse
		-in nato : Tab-CLICK = ON
	Videl sem tudi, da problem reši tudi:
		synclient tapbutton1=1
def SoundON():
	Na začetku mi ni delal zvok... Rešitev je bila:
		- lspci:
			tako preveriš, če je Linux prepoznal zvočno...
			na terminalu sem dobil:
			'00:1b.0 Audio device: Intel Corporation 7 Series/C210 Series Chipset Family High Definition Audio Controller (rev 04)'
		- apt-get install libasound2 alsa-utils alsa-oss 
		- alsamixer:
			in od "mutiraš" kanale, ki so zamutani
	Druga rešitev (ali celo dopolnitev):
		- je, da v terminal napišeš:
			pulseaudio -D
		- secer napiše, da ni mišljeno, da bi bil zagnan kot root
			ampak Ok... po tem dela tudi:
			Settings>Soun
def Thunderbird():
	inštalacija je čisto reprosta:
		- apt-get install thunderbird
	ali če ni povezave...
		- greš na njihovo stran in presnameš datoteko thunderbird.tar.db2
		- extrahiraš v /opt/thunderbird
		- preveriš če dela: ./thunderbird
		- nastaviš privilegije (če je potrebno): sudo chown -R root:root /opt/thunderbird
		- in linkaš exe skript: sudo ln -fs /opt/thunderbird/thunderbird /usr/bin/thunderbird
def Sublime text 3():
	greš na njihovo stran in snameš dol pravo verzijo (Ubuntu 64)
	nato pa v terminalu zaženeš:
	- cd Download1
	- dpkg -i Sublime...64.deb
def TeamViewer
	- presnames teamviewer i386 (cetudi imas 64-bitni comp.)
	- v terminalu> dpkg --add-architecture i386
	- apt-get update
	- dpkg -i teamviewer_****_i386.deb
	- sudo apt-get -f install

# RISANJE
def qCad():
	- presnameš inštalacijo iz njihove strani:
	https://qcad.org/en/qcad-downloads-trial
	- nato spremeniš rivilegije datoteke:
	sudo chmod 777 qcad*.run
	- in poženeš script:
	./qcad*.run
def FreeCAD():
	asdf
def Gimp():
	asdf
def Inkscape():
	asdf
def Fritzing():
	asdf
def Popcorn-Time
	Download1 Popcorn-Time : https://www.popcorntime.ws/about
	razpakiraš in daš dokumente v /opt/popcorn-time/
	polinkaš, da bo dosegljivo vsem:
		sudo ln -sf /opt/popcorn-time/Popcorn-Time /usr/bin/popcorn-time
	Narediš še .desktop datoteko
		sudo nano /usr/share/applications/popcorntime.desktop
	in vot vpišeš:
		[Desktop Entry]
		Version = 1.0
		Type = Application
		Terminal = false
		Name = Popcorn Time
		Exec = /usr/bin/popcorn-time
		Icon = /opt/popcorn-time/src/app/images/icon.png
		Categories = Application;

# PROGRAMIRANJE
def eclipse
	for installation:
		... nisem zapisal...
		... presnameš, odpakiraš kopiraš v:
		/opt/eclipse/
		narediš link za vse uporabnike:
			sudo ln -sf /opt/eclipse/cpp-neon/eclipse/eclipse /usr/bin/eclipse
	for eclipse.desktop:
		sudo nano /usr/share/applications/eclipse.desktop
		[Desktop Entry]
		Version = Neon 2.0
		Type = Application
		Terminal = false
		Name = eclipse
		Exec = /usr/bin/eclipse
		Icon = /opt/eclipse/cpp-neon/eclipse/icon.xpm
		Categories = Development;
def Arduino():
	for install:
		#za Debian le:
		sudo apt-get install git
	for config:
		git config --global user.name "davidrihtarsic"
		git config --global user.email "david.rihtarsic@gmail.com"
		git config --global core.editor="subl"
	for general_use:
		make new repository ... BlaBla_project (need to be on URL gitHub)
		make dir on your computer for that project 
		navigate to that dir
		:git init
		for editing:
			## na tem mestu spreminjaš FAJL...
			#:git add . #dodaj vse datoteke
			#:git commit -m "comment"
			:git commit -a -m "comment" #naredi vse naenkrat
			:git status # ni potreben a se vidi ce je potrebno kaj commitat
			:git diff 	#ni potrebno a pokaže razlike...
		for uploading:
			## kako dastvar na GitHub...
			# v spremenljivko "origin" spravimo URL projekta
			:git remote add origin https://github.com/davidrihtarsic/myZapiski.git
			:git push origin master #daš na GitHub +username +passWd
		for updating:
			## naprimer, da nekdo popravi kodo (recimo ti sam na GitHubu in na compu)
			## hočeš naložit...
		#heh nisem si zapisoval
def GitHub():

def w3m():
	for instalation :
		apt-get install w3m
	for frendlyUse:
		v ~/bashrc vpišeš:
		alias w3mm='w3m www.google.com'

