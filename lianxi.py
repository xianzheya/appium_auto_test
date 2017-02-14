# 1，启动Android
# 设备：
#
# // 启动
#
# // set
# up
# appium
#
# // File
# classpathRoot = new
# File(System.getProperty("user.dir"));
#
# // File
# appDir = new
# File(classpathRoot, "apps");
#
# // File
# app = new
# File(appDir, "ContactManager.apk");
#
# DesiredCapabilities
# capabilities = new
# DesiredCapabilities();
#
# capabilities.setCapability("device", "Android");
#
# // capabilities.setCapability(CapabilityType.BROWSER_NAME, "");
#
# capabilities.setCapability("deviceName", "xiaomi-mi_3-02214788"); // 小米
#
# // capabilities.setCapability("deviceName", "52c7c049"); // 三星
#
# // capabilities.setCapability("deviceName", "614ad249"); // 红米
#
# capabilities.setCapability("platformVersion", "4.4.4");
#
# capabilities.setCapability("platformName", "Android");
#
# // capabilities.setCapability("app", app.getAbsolutePath());
#
# capabilities.setCapability("appPackage", "com.tencent.mm");
#
# capabilities.setCapability("appActivity", "com.tencent.mm.ui.LauncherUI");
#
# capabilities.setCapability("unicodeKeyboard", "True");
#
# capabilities.setCapability("resetKeyboard", "True");
#
# driver = new
# AndroidDriver(new
# URL("http://127.0.0.1:4723/wd/hub"), capabilities);
#
#
#
#
#
# 启动IOS设备：
#
#
#
#
#
# DesiredCapabilities
# capabilities = new
# DesiredCapabilities();
#
# // capabilities.setCapability(CapabilityType.BROWSER_NAME, "ios");
#
# capabilities.setCapability(CapabilityType.VERSION, "8.1");
#
# capabilities.setCapability(CapabilityType.PLATFORM, "Mac");
#
# // capabilities.setCapability("device", "iPhone Simulator");
#
# // capabilities.setCapability("app", "safai");
#
# capabilities.setCapability("deviceName", "pohoto");
#
# capabilities.setCapability("platformName", "ios");
#
# driver = new
# RemoteWebDriver(new
# URL("http://0.0.0.0:4723/wd/hub"), capabilities);
#
#
#
# 注：Appium内还需要配置一些东西，UDID / BundleID / Force
# Driver
#
# 寻找元素超时时间：
#
# driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
#
# 打印整个页面的元素：System.out.print(driver.getPageSource());
#
# 获取当前时间并截图，命名：
#
# public
# static
# String
# getScreen()
# {
#
#     String
# fileRoute = "//liyu/testing/test/";
#
# SimpleDateFormat
# df = new
# SimpleDateFormat("yyyy-MM-dd-HH-mm");
#
# String
# picname = fileRoute + df.format(new
# Date()).toString() + ".png";
#
# // picname = picname.replaceAll(":", "-");
#
# // picname = picname.replaceAll(" ", "-");
#
# File
# screen = driver.getScreenshotAs(OutputType.FILE);
#
# System.out.println(picname);
#
# File
# screenFile = new
# File(picname);
#
# try {
#
# FileUtils.copyFile(screen, screenFile);
#
# String time=df.format(new Date()).toString();
#
# System.out.println("当前时间"+time);
#
# return time;
#
# } catch(IOException
# e) {
#
# e.printStackTrace();
#
# }
#
# return null;
#
# }
#
# 发送邮件：HTML / TXT（要把图片放到IIS路径拼接url）
#
#
#
#
#
# public
# void
# mail()
# {
#
# String
# value2 = "微信**系统: 本次**时间：" + getScreen();
#
# String
# Value = "<img src=\"http://172.17.6.134:88/test/" + getScreen() + ".png\">";
#
# System.out.print(Value);
#
# String
# smtpHost = "172.17.1.23";
#
# String
# from = "liyu@yiguo.com";
#
# String
# to = "liyu@yiguo.com";
#
# String
# subject = value2; // subject
# javamail自动转码
#
# StringBuffer
# theMessage = new
# StringBuffer();
#
# theMessage.append("<h2><font color=red>**截图乳腺：</font></h2>");
#
# theMessage.append("<hr>");
#
# theMessage.append(Value);
#
# try {
#
# Mail.sendMessage(smtpHost, from, to, subject, theMessage.toString());
#
# }
#
# catch(javax.mail.MessagingException
# exc) {
#
#     exc.printStackTrace();
#
# }
#
# catch(java.io.UnsupportedEncodingException
# exc) {
#
#     exc.printStackTrace();
#
# }
#
# }
#
# public
# static
# void
# sendMessage(String
# smtpHost, String
# from, String
# to, String
# subject, String
# messageText)throws
# MessagingException, java.io.UnsupportedEncodingException
#
# {
#
# // Step: Configure
# the
# mail
# session
#
# System.out.println("Configuring mail session for: " + smtpHost);
#
# java.util.Properties
# props = new
# java.util.Properties();
#
# props.setProperty("mail.smtp.auth", "true"); // 指定是否需要SMTP验证
#
# props.setProperty("mail.smtp.host", smtpHost); // 指定SMTP服务器
#
# props.put("mail.transport.protocol", "smtp");
#
# Session
# mailSession = Session.getDefaultInstance(props);
#
# mailSession.setDebug(true); // 是否在控制台显示debug信息
#
# // Step: Construct
# the
# message
#
# System.out.println("Constructing message -  from=" +
# from
#
# + "  to=" + to);
#
# InternetAddress
# fromAddress = new
# InternetAddress(
# from);
#
# InternetAddress
# toAddress = new
# InternetAddress(to);
#
# MimeMessage
# testMessage = new
# MimeMessage(mailSession);
#
# testMessage.setFrom(fromAddress);
#
# testMessage.addRecipient(javax.mail.Message.RecipientType.TO, toAddress);
#
# testMessage.setSentDate(new
# java.util.Date());
#
# testMessage.setSubject(MimeUtility.encodeText(subject, "gb2312", "B"));
#
# testMessage.setContent(messageText, "text/html;charset=gb2312");
#
# System.out.println("Message constructed");
#
# // Step: Now
# send
# the
# message
#
# Transport
# transport = mailSession.getTransport("smtp");
#
# transport.connect(smtpHost, "liyu@yiguo.com", "5201314");
#
# transport.sendMessage(testMessage, testMessage.getAllRecipients());
#
# transport.close();
#
# System.out.println("Message sent!");
#
# }
#
#
#
#
#
#
#
# APP内上滑：driver.swipe(250, 300, 250, 1400, 0);
#
# APP内下滑：     driver.swipe(250, 1400, 250, 300, 0);
#
# // driver.navigate().forward(); // 前进 \
#  \
#                                    // driver.navigate().back(); // 后退
#
# driver.navigate().refresh(); // 刷新
#
# String
# 字符串截取转成int：
#
# String
# getScreen = "2015-02-05-16-44";
#
# String
# Value = "2015-02-05-16-49";
#
# // int
# index = getScreen.substring(13, 1);
#
# String
# getScreen1 = getScreen.substring(14, 16);
#
# String
# Value2 = Value.substring(14, 16);
#
# System.out.print(getScreen1);
#
# System.out.print(Value2);
#
# Integer.parseInt(getScreen1);
#
# Integer.parseInt(Value2);
#
# int
# sum = Integer.parseInt(Value2) - Integer.parseInt(getScreen1);
#
# System.out.print(sum);
#
# 动作Action：
#
# / ** *
#
# * 切换WEB页面查找元素
#
#   * /
#
#   public
# static
# void
# switchtoWeb()
# {
#
# try {
#
# Set < String > contextNames = demotestcase.driver.getContextHandles();
#
# for (String contextName: contextNames) {
#
#                                        // 用于返回被测app是NATIVE_APP还是WEBVIEW，如果两者都有就是混合型App
#
# if (contextName.contains("WEBVIEW") | | contextName.contains("webview"))
# {
#
#     demotestcase.driver.context(contextName);
#
# System.out.println("跳转到web页 开始操作web页面");
#
# }
#
# }
#
# }catch(Exception
# e) {
#
#     e.printStackTrace();
#
# }
#
# }
#
# / ** *
#
# * 上滑1 / 4
# 屏幕
#
# * /
#
# public
# static
# void
# slideUP()
# {
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 2, y / 3 * 2, x / 2, y / 3 * 1, 0);
#
# }
#
# / ** *
#
# * 下滑1 / 4
# 屏幕
#
# * /
#
# public
# static
# void
# slideDown()
# {
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 2, y / 3 * 1, x / 2, y / 3 * 2, 0);
#
# }
#
# / ** *
#
# * 左滑1 / 2
# 屏幕
#
# * /
#
# public
# static
# void
# slideLeft()
# {
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 4 * 3, y / 2, x / 4 * 1, y / 2, 0);
#
# }
#
# / ** *
#
# * 右滑1 / 2
# 屏幕
#
# * /
#
# public
# static
# void
# slideRight()
# {
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 4 * 1, y / 2, x / 4 * 3, y / 2, 0);
#
# }
#
# / ** *
#
# * 特殊上滑
#
#   * @ param
# 传入从左到右宽度的百分比(1 - 99
# 之间)
#
# * /
#
# public
# static
# void
# slideUP(int
# i){
#
# Assert.assertFalse("上滑宽度传入错误", i <= 0 | | i >= 100);
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 10 * i, y / 3 * 2, x / 10 * i, y / 3 * 1, 0);
#
# }
#
# / ** *
#
# * 特殊下滑
#
#   * @ param
# 传入从左到右宽度的百分比(1 - 99
# 之间)
#
# * /
#
# public
# static
# void
# slideDown(int
# i){
#
# Assert.assertFalse("下滑宽度传入错误", i <= 0 | | i >= 100);
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 10 * i, y / 3 * 1, x / 10 * i, y / 3 * 2, 0);
#
# }
#
# / ** *
#
# * 特殊左滑
#
#   * @ param
# 传入从上到下宽度的百分比(1 - 99
# 之间)
#
# * /
#
# public
# static
# void
# slideLeft(int
# i){
#
# Assert.assertFalse("左滑宽度传入错误", i <= 0 | | i >= 100);
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 4 * 3, y / 10 * i, x / 4 * 2, y / 10 * i, 0);
#
# }
#
# / ** *
#
# * 特殊右滑
#
#   * @ param
# 传入从上到下宽度的百分比(1 - 99
# 之间)
#
# * /
#
# public
# static
# void
# slideRight(int
# i){
#
# Assert.assertFalse("左滑宽度传入错误", i <= 0 | | i >= 100);
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.swipe(x / 4 * 2, y / 10 * i, x / 4 * 3, y / 10 * i, 0);
#
# }
#
# / ** *
#
# * xpath根据content - desc查找元素
#
#                    * @ param
# view的类型
#
# * @ param
# content - desc
# 的内容
#
# * @
# return
#
# * /
#
# public
# static
# WebElement
# getViewbyXathwithcontentdesc(String
# view, String
# name){
#
# return demotestcase.driver.findElementByXPath("//" + view + "[contains(@content-desc,'" + name + "')]");
#
# }
#
# / ** *
#
# * xpath根据text查找元素
#
#   * @ param
# view的类型
#
# * @ param
# text的内容
#
# * @
# return
#
# * /
#
# public
# static
# WebElement
# getViewbyXathwithtext(String
# view, String
# name){
#
# return demotestcase.driver.findElementByXPath("//" + view + "[contains(@text,'" + name + "')]");
#
# }
#
# / ** *
#
# * 截图
# 文件名: 年月日时分秒
#
#      * /
#
#      public
# static
# String
# getScreen()
# {
#
# SimpleDateFormat
# df = new
# SimpleDateFormat("yyyy-MM-dd-HH-mm-ss");
#
# String
# picname = finalElement.phoneScreens + df.format(new
# Date()).toString() + ".png";
#
# // picname = picname.replaceAll(":", "-");
#
# // picname = picname.replaceAll(" ", "-");
#
# File
# screen = demotestcase.driver.getScreenshotAs(OutputType.FILE);
#
# System.out.println(picname);
#
# File
# screenFile = new
# File(picname);
#
# try {
#
# FileUtils.copyFile(screen, screenFile);
#
# } catch (IOException e) {
#
# e.printStackTrace();
#
# }
#
# return picname;
#
# }
#
# / ** *
#
# * 截图
# 文件名: 内容 - 年月日时分秒
#
#           * /
#
#           public
# static
# String
# getScreen(String
# name){
#
# SimpleDateFormat
# df = new
# SimpleDateFormat("yyyy-MM-dd-HH-mm-ss");
#
# String
# picname = finalElement.phoneScreens + name + df.format(new
# Date()).toString() + ".png";
#
# File
# screen = demotestcase.driver.getScreenshotAs(OutputType.FILE);
#
# System.out.println(picname);
#
# File
# screenFile = new
# File(picname);
#
# try {
#
# FileUtils.copyFile(screen, screenFile);
#
# } catch (IOException e) {
#
# e.printStackTrace();
#
# }
#
# return picname;
#
# }
#
# / ** *
#
# * 检查网络
#
#   * @
# return 是否正常
#
# * /
#
# public
# static
# boolean
# checkNet()
# {
#
#     String
# text = demotestcase.driver.getNetworkConnection().toString();
#
# if (text.contains("Data: true"))
#
# return true;
#
# else
#
# return false;
#
# }
#
# / ** *
#
# * 根据UIautomator底层方法得到对应desc的view
#
#   * @ param
# desc名
#
# * @
# return View
#
# * /
#
# public
# static
# WebElement
# getViewbyUidesc(String
# name){
#
# return demotestcase.driver.findElementByAndroidUIAutomator("new UiSelector().descriptionContains(\"" + name + "\")");
#
# }
#
# / ** *
#
# * 根据UIautomator底层方法得到对应text的view
#
#   * @ param
# text名
#
# * @
# return View
#
# * /
#
# public
# static
# WebElement
# getViewbyUitext(String
# name){
#
# return demotestcase.driver.findElementByAndroidUIAutomator("new UiSelector().textContains(\"" + name + "\")");
#
# }
#
# / ** *
#
# * 绝对坐标
# 传入长宽的像素点
#
# * @ param
# 宽度从左到右的像素点
#
# * @ param
# 长度从上到下的像素点
#
# * /
#
# public
# static
# void
# clickScreen(int
# i, int
# j){
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.tap(1, i, j, 200);
#
# }
#
# / ** *
#
# * 相对坐标
# 传入长宽的百分比
#
# * @ param
# 宽度从左到右的百分比
#
# * @ param
# 长度从上到下的百分比
#
# * /
#
# public
# static
# void
# clickScreen100(int
# i, int
# j){
#
# int
# x = demotestcase.driver.manage().window().getSize().width;
#
# int
# y = demotestcase.driver.manage().window().getSize().height;
#
# demotestcase.driver.tap(1, x * i / 100, y * j / 100, 200);
#
# }
#
# / ** *
#
# * log记录
#
#   * @ param
# 图片保存路径
#
# * @ param
# Exception参数
#
# * @ param
# AssertionError参数
#
# * @ param
# 测试用例名
#
# * /
#
# public
# static
# void
# getlog(String
# text, Exception
# error, AssertionError
# assertError, String
# testname){
#
# SimpleDateFormat
# df = new
# SimpleDateFormat("MM-dd-HH-mm");
#
# System.out.println("当前时间" + df.format(new
# Date()));
#
# String
# filename = finalElement.errorfile + testname + "-" + df.format(new
# Date()).toString() + ".txt";
#
# File
# file = new
# File(finalElement.errorfile);
#
# if (!file.exists())
#
# file.mkdirs();
#
# try {
#
# File f = new File(filename);
#
# if (!f.exists())
#
# f.createNewFile();
#
# FileWriter fw = new FileWriter(f, true);
#
# PrintWriter pw = new PrintWriter(fw);
#
# pw.append(testname+" 测试failed\r\n");
#
# pw.append("截图保存为:"+text+"\r\n");
#
# try{
#
# pw.append("eclipse报错为:\n"+error.toString()+"\r\n");
#
# error.printStackTrace(pw);
#
# } catch (Exception e){}
#
# try{
#
# pw.append("断言报错为:"+assertError.toString()+"\r\n");
#
# assertError.printStackTrace(pw);
#
# } catch (Exception e){}
#
# pw.flush();
#
# pw.close();
#
# file = new
# File(finalElement.errorlog);
#
# if (!file.exists())
#
# file.mkdirs();
#
# String
# cmd = "cmd /c \"adb logcat -d  *:E *:S |grep \"com.yiguo.app\" >" + finalElement.errorlog + testname + "-" + df.format(
#     new
# Date()).toString() + ".txt\"";
#
# // System.out.println(cmd);
#
# Runtime.getRuntime().exec(cmd);
#
# } catch(Exception
# e) {
#
# e.printStackTrace();
#
# }
#
# }
#
#
#
# 直接文本点击：
#
# driver.findElementByAndroidUIAutomator("new UiSelector().textContains(\"发现\")").click();
#
# driver.findElementByAndroidUIAutomator("new UiSelector().textContains(\"朋友圈\")").click();
#
# 访问远程共享文件夹bat
#
# net
# use \\192.168
# .100
# .170
# "5201314" / user: "office\yu.li"
#
# copy \\192.168
# .100
# .170\Builds\FanliApp_Android\4.3\4.3
# .1
# .4\FanliAndroid - release - fanli.apk
# D:\Apk\fanli.apk