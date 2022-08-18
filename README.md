# Service for checking in on my employer's website

...for Microsoft SharePoint

## Usage

You need:

* Python 3.9+
* Selenium
* Browser Google Chrome
* WebDriver for an installed browser

## Installation

### Web Browser (Google Chrome)

```bash
cd /tmp
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome*.deb
# fix dependencies
sudo apt -f -y install
```

### WebDriver for Google Chrome

```bash
# Find out the browser version
google-chrome --version
# Download the appropriate driver
cd /tmp
wget https://chromedriver.storage.googleapis.com/96.0.4664.45/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /var/local/
```

### Application

Clone git repository and create virtual environment:

```bash
git clone https://github.com/tarabrind/portal-register-selenium.git
python3 -m venv venv
# Install packets and copy configuration
pip install -r requirements.txt
cp config.template.py config.py
```

Edit `config.py` and add `starter.sh` to the scheduler to run on time.
