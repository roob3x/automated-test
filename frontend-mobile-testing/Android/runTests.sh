echo "Actual Directory: ${PWD}"
cwd=${PWD}

echo Removing old reports
rm -f $cwd/ExecutionReports

echo Initialize Cliente Execution
cd Cliente
behave -f allure_behave.formatter:AllureFormatter -o $cwd/ExecutionReports

echo Generating report of Mobile Android Execution
allure serve ExecutionReports