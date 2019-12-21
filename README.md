
### Intro
This is Flask-React webapp for my personal workspace.

### Run the webapp
prerequisites:
`python3`, `git`, `npm`, `virtualenv`, `pip`

To download the repository:
```buildoutcfg
git clone https://github.com/zhengrui315/Mywebapp.git
```
or
```buildoutcfg
git clone git@github.com:zhengrui315/Mywebapp.git
```
if ssh key has been set up on github. 

To set up local environment:
```buildoutcfg
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
To start the wepapp:
```buildoutcfg
npm run dev-build
python -m flaskapp
```

### References:
- https://codeburst.io/creating-a-full-stack-web-application-with-python-npm-webpack-and-react-8925800503d9