

Feature: Login valid
    Scenario: Valid login
        Given launch chrome
        When open urll
        And Enter "Admin" n "admin123"
        And Login button

        Then verify login

    Scenario Outline: Valid login
        Given launch chrome
        When open urll
        And Enter "<username>" n "<password>"
        And Login button

        Then verify login

        Examples:
            | username | password |
            | admin    | admin123 |
            | admin123 | admin    |
            | adminxyz | admin123 |


