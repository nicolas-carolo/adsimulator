# adsimulator:  A realistic random generator of Active Directory domains


Author: Nicolas Carolo <nicolascarolo.dev@gmail.com>

Copyright: © 2020, Nicolas Carolo.

Date: 2020-11-02

Version: 0.1.0


## PURPOSE
adsimulator is a realistic random generator of Active Directory environment that stores data into a Neo4j graph database. adsimulator is inspired to [DBCreator](https://github.com/BloodHoundAD/BloodHound-Tools), but it adds more features.

## INSTALLATION

### Linux
We can install adsimulator simply by doing:
```sh
git clone https://github.com/nicolas_carolo/adsimulator
cd adsimulator
./installer_linux.sh
pip install -r requirements.txt
python setup.py install
```

### macOS
We can install adsimulator simply by doing:
```sh
git clone https://github.com/nicolas_carolo/adsimulator
cd adsimulator
./installer_darwin.sh
pip install -r requirements.txt
python setup.py install
```


## USAGE

### Running
```
$ adsimulator
```

### Commands

- `dbconfig` - Set the credentials and URL for the database you're connecting too
- `connect` - Connects to the database using supplied credentials
- `setparams` - Import the settings JSON file containing the parameters for the graph generation
- `setdomain` - Set the domain name
- `cleardb` - Clears the database and sets the schema properly
- `generate` - Connects to the database, clears the DB, sets the schema, and generates random data
- `exit` - Exits the script


## COPYRIGHT

Copyright © 2020, Nicolas Carolo.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions, and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither the name of the author of this software nor the names of
   contributors to this software may be used to endorse or promote
   products derived from this software without specific prior written
   consent.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
