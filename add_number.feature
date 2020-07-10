Feature: Test Calculator Functionality

Scenario:Addition
 Given Calculator app is run
 When I input "2" and "3" to calculator
 Then I get result "5"

Scenario:Addition Negative
 Given Calculator app is run
 When I input "-2" and "3" to calculator
 Then I get result "1"