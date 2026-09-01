Question 1. Choose one test from the provided suite and name it. In plain English, what does that test confirm about your site? Then name one thing your site could get wrong that this test would not catch.

Answer: One of the tests of the suite was test_page_shows_both_status_labels. This test confirms the text "Completed" and "In Progress" are atleast somewhere on the page. Something I actually encountered when running this test is it's exactness originally I had "In Progress" that test failed because it was supposed to say "In progress". Something that this test would not be able to catch is whether they are attached to the correct items such as is Completed attached to True or In progress attached to False. This could lead to your logic potentially being backwards where it shows the wrong text for the wrong tasks.

Question 2. You built three pages that share one navigation bar. If you added a fourth link to your navigation, how many files would you edit? How many would you have edited if you had not used base.html, and why?

Answer: In my case I would only have to edit one file which is base.html because that is where all of my links are held. This would change however if I didn't use base.html and I would have to edit every html page and any new ones that I add making this a very inneficient and time consuming process.
