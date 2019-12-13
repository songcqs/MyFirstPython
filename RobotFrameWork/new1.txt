*** Setting ***
Library    Selenium2Library


*** Test Cases ***
testCase
	open browser	http://www.baidu.com	chrome
	input text    id=kw    robot framework
	click button    id=su
	close browser