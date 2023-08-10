Feature:"Verifies book adding and deleteing 

    Scenario: Verify add book 
        Given the book details are present
        When we execute the Addbook API call
        Then book is successfully added