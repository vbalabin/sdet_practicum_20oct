pytest --alluredir=allure-report/
echo "------------------------"
echo "Tests have been finished"
echo "------------------------"
pause
allure serve allure-report/