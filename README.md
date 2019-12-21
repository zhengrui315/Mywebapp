
### Intro
This is a skeleton Flask-React webapp. It can be used as a template for building your own webapp. Backend code can be written into `./flaskapp/` while React components can be added in `./static/src/`. 

### Run the webapp
prerequisites:
`python3`, `git`, `npm`, `virtualenv`, `pip` and some basic understanding of them.

**To download the repository:**
```buildoutcfg
git clone https://github.com/zhengrui315/Mywebapp.git
```
or
```buildoutcfg
git clone git@github.com:zhengrui315/Mywebapp.git
```
if ssh key has been set up on github. 

**To set up local environment:**
```buildoutcfg
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
for backend and 
```buildoutcfg
npm install
```
for frontend.

**To start the wepapp**

If not in virtual environment, enter by `source venv/bin/activate`, then
```buildoutcfg
./run.sh
```
the webapp can be accessed at [http://localhost:5001](http://localhost:5001). The port number can be set in `run.sh`. 

**To exit the virtual environment**
```buildoutcfg
deactivate
```


### How it works
Routing has been set up in `./flaskapp/routes.py` so that all urls go into frontend, which will be handled in `./static/src/App.js`. More routing options can be accommodated by adding `<Route />` accordingly. 

Some basic configuration of webpack has been set in `webpack.config.js` where the entry point is `./staic/src/index.js`. Webpack builds `./static/dist/index.js` which is injected into `./templates/index.html`.

### References:
- https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9