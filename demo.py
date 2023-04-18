from utils.templatebase import TemplateInit

# home生成
home = TemplateInit()
home.render("index.txt",context={"title":"home测试1"})

# user模块生成
user = TemplateInit()
user.setdirPath("user")
user.render("index.txt",context={"title":"一层yser测试2"})


# user下的login模块生成
user.setdirPath("user/login")
user.render("login.txt",context={"content":"二层user测试3"})