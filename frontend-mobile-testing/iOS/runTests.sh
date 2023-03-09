echo "Actual Directory: ${PWD}"
cwd=${PWD}

echo Removing old reports
rm -f $cwd/ExecutionReports

echo Initialize Mycar Execution
cd Mycar
behave -f allure_behave.formatter:AllureFormatter -o $cwd/ExecutionReports

echo Generating report of Mobile iOS Execution
allure serve ExecutionReports