#codegeneration-allcode
## Code Generation Plugin Introduction
This code generation plugin is written using python [jinja module](https://github.com/pallets/jinja), which is very simple and flexible, and can be changed according to your needs

## how to use
1. Install python3.9\
2. pip install -U Jinja2\
3. git clone https://github.com/265525/codegeneration-allcode.git \
4. Run demo.py
## example
```
from utils. templatebase import TemplateInit
# home generation
home = TemplateInit()
home.render("index.txt",context={"title":"home test 1"})

# user module generation
user = TemplateInit()
user. setdirPath("user")
user.render("index.txt",context={"title":"One layer of yser test 2"})

# The login module under user is generated
user.setdirPath("user/login")
user.render("login.txt",context={"content":"Second-layer user test 3"})
```

## MIT License
Copyright (c) 2023 br66