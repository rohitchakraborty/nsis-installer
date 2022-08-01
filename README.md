# nsis-installer
## Prerequisites
* Install [NSIS](https://nsis.sourceforge.io/Main_Page)
* Create virtual environment and install _requirement.txt_.
## Usage
* Open _installer.cfg_. This configures the installer.
* Uncomment Files and add the path to your project and any other tools.
* Activate virtual environment and run the following command:
```
pynsist installer.cfg --no-makensis
```
* This will create the _build_ folder with the _installer.nsi_ file inside _nsis_ folder.
* Replace that with the _installer.nsi_ inside _installer_ folder.
* Open NSIS application.
* Select _Compile NSIS scripts_.
* Select _load script_ and select _installer.nsi_ under _build_ folder.
* The exe file will be generated.